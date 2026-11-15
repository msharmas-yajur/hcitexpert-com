#!/usr/bin/env python3
"""Candidate selection for "The Research Radar" (HCITExperts Blog).

Builds the ranked shortlist of recent arXiv preprints on digital health and
clinical AI. The ranking is deterministic and fully stated, so an edition can
describe its own method honestly.

Pipeline
  1. Pool: arXiv API, papers submitted in the last N days (default 14) in
     AI/ML/CV/NLP/HCI/signal-processing/stat categories whose abstract matches a
     health term, plus any paper matching "digital health" in any category.
  2. Pool (extra): Hugging Face daily papers for the same days, filtered by the
     same health terms (catches papers the arXiv query truncated).
  3. Scope filter: a paper must reach a minimum relevance score (default 3:
     several distinct health terms, title matches counting double), so one
     generic word such as "diagnostic" is not enough. Already-covered arXiv ids (ledger) are excluded.
  4. Rank:
       primary   Hugging Face upvotes, descending (papers featured on HF daily
                 papers)
       fallback  papers NOT featured on HF rank after them, ordered by a
                 keyword relevance score (distinct strong terms, title weighted),
                 then recency. Each row records its `rank_basis`, so the
                 article can say which papers were ranked by upvotes and which
                 by the fallback.
  5. Output: JSON (and optional markdown) with the top N plus a reserve for the
     maker to substitute from if a paper fails the read (out of scope, etc.).

The script only SELECTS. The maker must still read each abstract (or the full
text where the abstract is not enough) before writing a word about a paper.

Usage
  python3 scripts/research_radar.py --days 14 --top 10 --reserve 10 \
      --out /tmp/radar.json --md /tmp/radar.md
Standard library only. Be polite: arXiv asks for >= 3 s between API calls.
"""
import argparse
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (compatible; HCITExpertsResearchRadar/1.0)"
ARXIV_API = "http://export.arxiv.org/api/query"
HF_DAILY = "https://huggingface.co/api/daily_papers?date={date}"
LEDGER = "_data/research_radar_covered.yml"

CATEGORIES = [
    "cs.AI", "cs.CL", "cs.LG", "cs.CV", "cs.CY", "cs.HC", "cs.IR", "cs.MA",
    "eess.IV", "eess.SP", "stat.AP", "stat.ML", "q-bio.QM", "physics.med-ph",
]

# Terms used to build the arXiv query (broad; scope filter below is stricter).
QUERY_TERMS = [
    "clinical", "patient", "electronic health record", "healthcare",
    "digital health", "medical", "wearable", "radiology", "diagnosis",
]

# STRONG terms: a paper must match at least one in title or abstract to be in
# scope. Word-boundary regexes; matched case-insensitively.
STRONG_TERMS = [
    r"digital health", r"health ?care", r"clinical", r"clinician", r"patients?",
    r"electronic health records?", r"\behrs?\b", r"\bemrs?\b", r"medical",
    r"radiolog\w*", r"patholog\w*", r"diagnosis", r"diagnoses", r"wearables?", r"telemedicine",
    r"dermatolog\w*", r"ophthalm\w*", r"cardiolog\w*", r"psychiatr\w*", r"surg(?:ery|ical)",
    r"pharmac\w*", r"\becg\b", r"\beeg\b", r"biomedical", r"radiograph\w*",
    r"telehealth", r"\bfhir\b", r"hospital", r"physician", r"nurs(?:e|es|ing)",
    r"public health", r"epidemiolog\w*", r"mental health", r"oncolog\w*",
    r"cancer", r"drug discovery", r"genomic\w*", r"medical imaging",
    r"health records?", r"remote patient monitoring",
]
STRONG_RE = [re.compile(t, re.I) for t in STRONG_TERMS]

# --track phr: personal health records, patient-facing and mobile health apps.
# A paper must match at least one ANCHOR term (title or abstract) AND reach a
# general health relevance of at least 2, so a passing mention of "app" is not enough.
PHR_QUERY_TERMS = [
    "personal health record", "patient portal", "mobile health app", "health app",
    "mHealth", "patient-facing", "consumer health", "health data sharing",
    "patient-controlled", "digital health app",
]
PHR_ANCHOR_TERMS = [
    r"personal health records?", r"\bphrs?\b", r"patient portals?",
    r"mobile health app\w*", r"health apps?\b", r"\bmhealth\b", r"patient-facing",
    r"consumer health", r"health data sharing", r"patient-controlled",
    r"digital health apps?", r"health locker", r"patient-held",
    r"patient access to (?:their )?(?:health )?(?:records?|data)",
    r"smartphone app\w*", r"mobile app\w*",
]
PHR_ANCHOR_RE = [re.compile(t, re.I) for t in PHR_ANCHOR_TERMS]

# Geography annotation (near-term focus markets: India, Middle East, US). This only TAGS
# a paper with the settings its title or abstract names; it never changes the ranking.
GEO_PATTERNS = {
    "India": [r"\bIndia\b", r"\bIndian\b", r"\bABDM\b", r"\bABHA\b", r"\bAyushman\b"],
    "Middle East": [r"Saudi", r"\bUAE\b", r"United Arab Emirates", r"\bEmirates\b", r"\bQatar\b",
                    r"\bKuwait\b", r"\bOman\b", r"\bBahrain\b", r"\bGCC\b", r"\bGulf\b",
                    r"Middle East", r"\bArab(?:ic|ian)?\b"],
    "US": [r"United States", r"\bU\.S\.", r"\bUS\b", r"\bUSA\b", r"\bAmerican\b", r"\bMedicare\b",
           r"\bMedicaid\b", r"\bHIPAA\b"],
}
GEO_RE = {k: [re.compile(x) for x in v] for k, v in GEO_PATTERNS.items()}


def detect_geo(title, abstract):
    """Focus markets named in the title or abstract (case-sensitive acronyms)."""
    text = f"{title} {abstract}"
    return [k for k, rxs in GEO_RE.items() if any(rx.search(text) for rx in rxs)]


def http_get(url, retries=3, pause=3.0):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001 - report and retry
            last = e
            time.sleep(pause * (i + 1))
    raise RuntimeError(f"GET failed: {url}: {last}")


def norm(s):
    return re.sub(r"\s+", " ", html.unescape(s or "")).strip()


def bare_id(arxiv_id):
    """2611.15777v2 -> 2611.15777 ; old-style ids keep their slash."""
    return re.sub(r"v\d+$", "", arxiv_id.strip())


def relevance(title, abstract, track="main"):
    """Distinct strong terms matched; title matches count double. In the phr
    track, distinct anchor terms add double the weight on top."""
    score = 0
    for rx in STRONG_RE:
        if rx.search(title):
            score += 2
        elif rx.search(abstract):
            score += 1
    if track == "phr":
        for rx in PHR_ANCHOR_RE:
            if rx.search(title):
                score += 4
            elif rx.search(abstract):
                score += 2
    return score


def in_scope(title, abstract, min_relevance=3, track="main"):
    """A single generic word ("diagnostic", "clinical") is not enough: require
    several distinct health terms (title matches count double). The phr track also
    requires at least one PHR/app anchor term and a general health score of 2."""
    if track == "phr":
        text = f"{title} {abstract}"
        return (any(rx.search(text) for rx in PHR_ANCHOR_RE)
                and relevance(title, abstract, "main") >= 2)
    return relevance(title, abstract) >= min_relevance


def arxiv_pool(start, end, cap, track="main"):
    cats = " OR ".join(f"cat:{c}" for c in CATEGORIES)
    terms = " OR ".join(f'abs:"{t}"' for t in (PHR_QUERY_TERMS if track == "phr" else QUERY_TERMS))
    date = f"submittedDate:[{start:%Y%m%d}0000 TO {end:%Y%m%d}2359]"
    queries = [
        f"({cats}) AND ({terms}) AND {date}",
        (f'(abs:"personal health record" OR abs:"patient portal" OR abs:"mHealth") AND {date}'
         if track == "phr" else f'abs:"digital health" AND {date}'),  # any category
    ]
    out = {}
    for q in queries:
        got = 0
        while got < cap:
            params = urllib.parse.urlencode({
                "search_query": q, "start": got, "max_results": 100,
                "sortBy": "submittedDate", "sortOrder": "descending",
            })
            root = ET.fromstring(http_get(f"{ARXIV_API}?{params}"))
            ns = {"a": "http://www.w3.org/2005/Atom"}
            entries = root.findall("a:entry", ns)
            if not entries:
                break
            for e in entries:
                aid = bare_id(e.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1])
                authors = [norm(a.findtext("a:name", "", ns)) for a in e.findall("a:author", ns)]
                out.setdefault(aid, {
                    "id": aid,
                    "title": norm(e.findtext("a:title", "", ns)),
                    "abstract": norm(e.findtext("a:summary", "", ns)),
                    "authors": authors,
                    "published": e.findtext("a:published", "", ns)[:10],
                    "primary_category": (e.find("{http://arxiv.org/schemas/atom}primary_category") is not None
                                         and e.find("{http://arxiv.org/schemas/atom}primary_category").get("term")) or "",
                    "source": "arxiv",
                })
            got += len(entries)
            time.sleep(3.2)  # arXiv API etiquette
            if len(entries) < 100:
                break
    return out


def hf_feed(start, end):
    """All HF daily papers for each day in [start, end]: {arxiv_id: record}."""
    feed = {}
    day = start
    while day <= end:
        try:
            data = json.loads(http_get(HF_DAILY.format(date=f"{day:%Y-%m-%d}"), pause=1.0))
        except Exception as e:  # noqa: BLE001 - a missing day should not stop the run
            print(f"warn: HF daily feed {day}: {e}", file=sys.stderr)
            data = []
        for item in data:
            p = item.get("paper", {})
            pid = bare_id(p.get("id", ""))
            if not pid:
                continue
            rec = feed.get(pid)
            up = p.get("upvotes") or 0
            if rec is None or up > rec["upvotes"]:
                feed[pid] = {
                    "upvotes": up,
                    "title": norm(p.get("title") or item.get("title")),
                    "abstract": norm(p.get("summary") or item.get("summary")),
                    "published": (p.get("publishedAt") or "")[:10],
                    "github_stars": p.get("githubStars"),
                    "feed_date": f"{day:%Y-%m-%d}",
                }
        day += dt.timedelta(days=1)
        time.sleep(0.4)
    return feed


def covered_ids(path=LEDGER):
    try:
        text = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        return set()
    return {bare_id(m) for m in re.findall(r"arxiv\.org/abs/([^\s\"'>]+)", text)}


def build(days, top, reserve, cap, min_relevance=3, track="main", exclude=None):
    end = dt.date.today()
    start = end - dt.timedelta(days=days)
    pool = arxiv_pool(start, end, cap, track)
    hf = hf_feed(start, end)

    # HF-only additions (keeps papers the arXiv query may have truncated).
    for pid, h in hf.items():
        if pid not in pool and h["published"] and h["published"] >= f"{start:%Y-%m-%d}":
            pool[pid] = {"id": pid, "title": h["title"], "abstract": h["abstract"], "authors": [],
                         "published": h["published"], "primary_category": "", "source": "hf-daily"}

    skip = covered_ids() | set(exclude or [])
    rows = []
    for pid, p in pool.items():
        if pid in skip or not in_scope(p["title"], p["abstract"], min_relevance, track):
            continue
        h = hf.get(pid)
        rows.append({
            **p,
            "url": f"https://arxiv.org/abs/{pid}",
            "hf_upvotes": h["upvotes"] if h else None,
            "hf_github_stars": h["github_stars"] if h else None,
            "relevance": relevance(p["title"], p["abstract"], track),
            "geo": detect_geo(p["title"], p["abstract"]),
            "rank_basis": "hf_upvotes" if h else "keyword_relevance_fallback",
        })

    # primary: on HF (by upvotes desc); fallback: not on HF (relevance, recency)
    rows.sort(key=lambda r: (
        0 if r["hf_upvotes"] is not None else 1,
        -(r["hf_upvotes"] or 0),
        -r["relevance"],
        r["published"] and -int(r["published"].replace("-", "")),
    ))
    for i, r in enumerate(rows, 1):
        r["rank"] = i
    return {
        "as_of": f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%dT%H:%MZ}",
        "window": {"start": f"{start:%Y-%m-%d}", "end": f"{end:%Y-%m-%d}", "days": days},
        "track": track,
        "categories": CATEGORIES,
        "min_relevance": min_relevance,
        "pool_size_before_filters": len(pool),
        "in_scope_after_filters": len(rows),
        "ranked_by_hf_upvotes": sum(1 for r in rows if r["rank_basis"] == "hf_upvotes"),
        "criterion": ("Hugging Face daily-paper upvotes (descending); papers not featured on "
                      "Hugging Face rank after them by keyword relevance, then recency."),
        "top": rows[:top],
        "reserve": rows[top:top + reserve],
    }


def to_markdown(res):
    L = [f"# Research Radar candidates (as of {res['as_of']})", "",
         f"Window {res['window']['start']} to {res['window']['end']}; pool {res['pool_size_before_filters']}; "
         f"in scope {res['in_scope_after_filters']}; ranked by HF upvotes: {res['ranked_by_hf_upvotes']}.", "",
         f"Criterion: {res['criterion']}", ""]
    for label, rows in (("TOP", res["top"]), ("RESERVE", res["reserve"])):
        L.append(f"## {label}")
        for r in rows:
            up = "n/a" if r["hf_upvotes"] is None else r["hf_upvotes"]
            L += [f"### {r['rank']}. {r['title']}",
                  f"- {r['url']} | {r['published']} | HF upvotes: {up} | basis: {r['rank_basis']} | relevance: {r['relevance']}",
                  f"- Authors: {', '.join(r['authors'][:4])}{' et al.' if len(r['authors']) > 4 else ''}",
                  f"- Settings named (India / Middle East / US): {', '.join(r.get('geo') or []) or 'none stated in title or abstract'}",
                  f"- Abstract: {r['abstract']}", ""]
    return "\n".join(L)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--reserve", type=int, default=10)
    ap.add_argument("--cap", type=int, default=600, help="max arXiv results fetched per query")
    ap.add_argument("--min-relevance", type=int, default=3,
                    help="min distinct health terms (title match counts 2) to be in scope")
    ap.add_argument("--track", choices=["main", "phr"], default="main",
                    help="main = digital health and clinical AI; phr = personal health records and health apps")
    ap.add_argument("--exclude", default=None,
                    help="JSON file from another track; its top and reserve ids are never selected here")
    ap.add_argument("--out", default="research_radar.json")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()
    excl = []
    if a.exclude:
        prev = json.load(open(a.exclude, encoding="utf-8"))
        excl = [r["id"] for r in prev.get("top", []) + prev.get("reserve", [])]
    res = build(a.days, a.top, a.reserve, a.cap, a.min_relevance, a.track, excl)
    json.dump(res, open(a.out, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    if a.md:
        open(a.md, "w", encoding="utf-8").write(to_markdown(res))
    print(f"pool={res['pool_size_before_filters']} in_scope={res['in_scope_after_filters']} "
          f"hf_ranked={res['ranked_by_hf_upvotes']} -> {a.out}")
