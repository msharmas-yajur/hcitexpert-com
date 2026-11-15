# The Research Radar: Alternate-Day Runbook (HCITExperts Blog)

Procedure for **The Research Radar**, the alternate-day edition that reviews the
**ten highest-ranked recent arXiv preprints on digital health and clinical AI**
for an Indian health-IT audience. It alternates with **The Clinical Frontier**
(`scripts/clinical-frontier-runbook.md`); the two share the same maker-checker
gate, house style and publishing mechanics. Only the sourcing, article shape and
claim checks differ, and they are set out here.

## Step 0: which edition runs today?

1. `git checkout main && git pull --rebase origin main`.
2. If a file `_posts/<today IST>-*.md` already exists, or today is in either
   ledger's `covered` or `held`, **stop**: today is done.
3. Find the most recent entry across `_data/clinical_frontier_covered.yml` and
   `_data/research_radar_covered.yml` (latest `date`; a `held` day does not
   count). If it is a **Clinical Frontier**, today is a **Research Radar**; if it
   is a **Research Radar**, today is a **Clinical Frontier** (follow the Frontier
   runbook instead). Frontier entries carry no `series` marker; every entry in
   `clinical_frontier_covered.yml` is a Frontier.
   If the two ledgers share the latest date (a double-edition day), the Radar
   counts as the later edition, so the next day is a Frontier.
4. Radar issue number = (entries in `research_radar_covered.yml` `covered`) + 1,
   zero-padded to 3 digits.

## Step 1: build the shortlist (deterministic, do not hand-pick)

```bash
python3 scripts/research_radar.py --days 14 --top 10 --reserve 10 \
    --out /tmp/radar.json --md /tmp/radar.md
```

The script pools arXiv preprints submitted in the last 14 days (AI, ML, vision,
NLP, HCI, signal processing, statistics and medical-physics categories, plus any
paper matching "digital health"), adds Hugging Face daily papers for the same
days, drops out-of-scope and already-covered papers, and ranks:

- **Primary:** Hugging Face daily-paper **upvotes**, descending.
- **Fallback:** papers **not featured on Hugging Face** rank after those, by
  keyword relevance (distinct health terms; title matches count double), then
  recency. Each row records its `rank_basis`.

**Be honest about the criterion.** Hugging Face features few health papers, so in
practice most of the ten will usually be ranked by the fallback. The edition must
state how many of the ten were ranked by upvotes and how many by the fallback
(`ranked_by_hf_upvotes` in the JSON), and the `as_of` time of the upvote counts.
Never describe a fallback-ranked paper as "most upvoted" or imply popularity.

If the script fails (arXiv or Hugging Face unreachable), retry once; if it still
fails, record the day in `held` with the reason. Do not substitute a hand-picked
list.

### Track 2: personal health records (PHR) spotlight, papers

Every Radar edition includes a PHR spotlight (see Article format). Its three papers
come from a second run of the same script:

```bash
python3 scripts/research_radar.py --track phr --days 90 --top 3 --reserve 10 \
    --exclude /tmp/radar.json --out /tmp/radar_phr.json --md /tmp/radar_phr.md
```

- **Window is 90 days, not 14.** Very few preprints a fortnight mention personal
  health records or health apps (a 15-day window returned 0 or 1 per search phrase).
  The article must state the window.
- **Scope:** a paper needs at least one PHR or health-app anchor term (for example
  "personal health record", "patient portal", "mobile health app", "mHealth",
  "patient-facing") **and** a general health relevance of at least 2.
- `--exclude` keeps papers already on the Track 1 shortlist (top and reserve) out of
  the spotlight. Ranking is the same rule as Track 1 (Hugging Face upvotes first,
  keyword relevance for papers not featured there); expect all three to be
  fallback-ranked, and say so.
- If fewer than three papers are in scope, show what exists and say so. Never pad.

## Step 2: read every paper (MAKER)

Take the `top` ten. For **each** paper:

1. Read the **abstract** in full at `https://arxiv.org/abs/<id>`. Read the
   **full text** (`https://arxiv.org/pdf/<id>`) before stating anything the
   abstract does not say: a number, a dataset, a limitation, a comparison. If the
   full text cannot be read, say only what the abstract says.
2. **Substitute from `reserve`** (next in rank order) if a paper is out of scope
   on reading (not actually about health or clinical use), withdrawn, a duplicate
   of another entry, or has an abstract too thin to describe honestly. Record each
   substitution in the ledger `skipped` list with the reason, and say in the
   article's method note how many candidates were skipped on reading.
3. Never choose or drop a paper because you like or dislike it. The criterion
   is the criterion.
4. Read the arXiv `comment` and `journal_ref` fields for **every** paper (Track 1
   and Track 2). They can show acceptance at a venue; say so, and never write that
   a paper is not peer reviewed unless the record says so (say "the arXiv record
   gives no peer-review status" instead).

Apply the same reading rules to the three Track 2 papers.

## Step 3: research the PHR apps (MAKER)

The spotlight also covers **three live PHR apps**. This is a researched section,
held to the same primary-source rule as the Frontier.

**Selection rule (state it in the article, never call it a ranking):** PHR or
health-record apps from **different health-system contexts** (for example a consumer
platform, a national health service, a national digital public good), each with a
**recent update or announcement on the operator's or government's own pages in the
current year**. We cannot verify app-store rankings or download counts, so the
section is **not** a "top" or "trending" list and must never be worded as one.

- **Find candidates** with WebSearch, then **fetch the operator's or government's own
  pages** and read them. Search-result summaries and news write-ups are leads, not
  sources. If the primary page cannot be fetched, the app cannot be featured.
- Describe an app **only** from those pages: what it is, the capabilities **as the
  operator describes them**, and scale figures **attributed** ("PIB says",
  "Google says"). Dates and version numbers must match the page. Distinguish what
  has **shipped** (release notes, launch posts) from what is **planned** (policy
  documents), and label the latter.
- **Never claim to have tested an app.** The article says "we have not tested them".
- **Rotation:** do not repeat a featured app in the next three Radar issues unless
  it has a new announcement; vary the regions. Record the three apps and their
  source URLs in the ledger.
- Add one **"Our reading"** line per app and a short "across the three" list, all
  labelled as editorial. Each synthesis line must be literally true of every app or
  paper it names (see the pre-flight checklist).

## Maker pre-flight (do this before sending any draft to a checker)

Every checker round on Issue 001 failed on the maker's own synthesis sentences, not
on facts. Before the gate, read every "In this issue" bullet, "Patterns" or "across
the three" bullet, takeaway, FAQ answer and the description, and check each for:

1. A claim about **more than one** paper or app: is it literally true of **each**
   one named?
2. Words the sources do not literally support ("efficiency", "edge", "benchmark",
   "peer reviewed", "validated", "trend", "keep", "most", "popular", "trending").
3. **Timing words** ("this week", "recently") against each source's real date.
4. A vendor or government claim stated as fact instead of attributed.
5. Absence claims ("the abstract gives no figures", "the release notes do not
   mention X"): confirm against the **whole** source before writing them, or drop them.
6. Rewrite generalisations as strictly attributable statements ("NPCBench
   reports...", "PIB says...") and drop counts and trends.

## Article format

Front matter as in the Frontier runbook, with these differences:

```yaml
description: "The Research Radar, Issue NNN. <1-2 sentences: the window, the criterion, and the headline themes>"
tags: [ ... , Research Radar, arXiv, Preprints, ... ]
mentions:          # one entry per paper (all 13) and one per app source: {name, description (authors, arXiv id, date), url}
```

Body, as a newsletter (no dashes anywhere, see the Frontier runbook). **Order matters:**
the issue leads with the content and puts the methodology **at the end**, so readers
can review how it was made after they have read it.

1. Masthead: `> **The Research Radar** · <Day Month Year> · Issue NNN`, plus the
   one-line tagline.
2. **In this issue**: 2 to 4 bullets (the themes, not a list of titles).
3. **Preprint notice** (always included, near the top): "These are arXiv preprints.
   They have not necessarily been peer reviewed, and results may change. We report
   what the authors state in their abstracts. None of this is clinical guidance."
4. **The ten papers**, numbered by shortlist rank. If a candidate was skipped on
   reading, the numbers start above 1: add one line under the heading saying why and
   pointing to the process section. Each entry has: title linked to
   `arxiv.org/abs/<id>`; authors (first three, then "et al."); submitted date;
   `Rank basis:` Hugging Face upvotes (count) **or** "not featured on Hugging Face,
   ranked by keyword relevance"; then three short lines:
   **What it does** (from the paper), **What it reports** (only what the abstract
   or full text states, attributed to the authors), **Caveat** (a limitation the
   paper states, or "preprint, not peer reviewed"). After each entry, optionally
   one line headed **Why it could matter in India**, clearly labelled as our
   reading, never as a claim about the paper.
5. **Patterns across the ten**: 2 to 3 bullets, each strictly attributable.
6. **Personal health records spotlight**: a one-paragraph intro; **three preprints**
   on PHRs and health apps (same entry template as step 4, with the Track 2 rank
   basis); **three PHR apps in the wild** (for each: context, sources linked,
   what it is, capabilities as the operator describes them or what has shipped vs
   what is planned, and an "Our reading" line); and a short "across the three apps
   and three papers (our reading)" list.
7. **Takeaway.**
8. **How this issue was made** (always last before the sign-off). Begin with the
   italic **process version line** (see Process version history). Then:
   - *Track 1, the ten papers:* window, pool size, how many in scope, the criterion,
     the upvote vs fallback split and the `as_of` time, and how many candidates were
     skipped on reading and why.
   - *Track 2, the PHR spotlight:* the 90 day window, pool, in scope, that papers on
     the Track 1 shortlist were excluded, the ranking basis and `as_of`; and the app
     selection rule (not a ranking; contexts; sources; rotation).
   - *Checking:* the independent reviewer (separate agent, sees only the draft and
     the written procedure, re-derives claims from primary sources, approves or
     lists fixes, extra rounds need the human editor); what is and is not read
     (abstracts only unless said; apps not tested); "our reading" is opinion; an AI
     reviewer can miss errors.
   - Any **new concept or process added to the Radar** gets its own bullet or
     sub-heading here, so readers can see how the Radar is made as it evolves.
9. Sign-off linking back to HCITExperts, as in the Frontier.

**Updating a published issue.** Only when the owner asks. Keep the `date`, add a
one-line blockquote near the top: `> **Updated <date>.** <what changed>`, say whether
the rest is unchanged, and re-run the checker gate on the updated text.

About 1,200 to 1,800 words for the ten papers' part; the spotlight and process section add to that (Issue 001 v2 is about 5,000 words in total, and a shorter template is on the backlog). Prefer tight bullets over paragraphs. No
claim of clinical validation, regulatory approval or deployment unless the paper
says so, and then attributed to the authors.

## Checker procedure (fresh subagent, same independence rules as the Frontier)

Give the checker **only** the draft path, this runbook and the Frontier runbook's
"Checker procedure". Do **not** pass the maker's notes or the `radar.json`
conclusions about what each paper says. The checker may be given `radar.json`
only to verify the method note's numbers. Use a new checker for every pass, up
to 3, with the same revise-and-recheck and hold rules as the Frontier.

In addition to the Frontier checks, the checker must:

1. **Per paper:** open `arxiv.org/abs/<id>` and confirm the title, authors,
   submitted date and arXiv id. Confirm every statement under "What it does" and
   "What it reports" against the abstract (or full text where the draft cites it).
   Numbers must match exactly. Mark UNSUPPORTED any claim the paper does not make,
   and WRONG any that it contradicts.
2. **Overreach:** flag any sentence that presents a preprint result as established,
   validated, deployed, approved or peer reviewed, or that attributes a conclusion
   to the paper that is really the editor's.
3. **Method note:** confirm the window, the criterion, the counts and the "ranked
   by upvotes vs fallback" split match `radar.json`, and that no fallback-ranked
   paper is described as popular or most upvoted.
4. **Upvotes:** re-fetch `https://huggingface.co/api/daily_papers?date=<D>` for the
   paper's feed day (or `https://huggingface.co/api/papers/<id>`) and confirm the
   stated count. Counts only rise, so a re-fetch equal to or higher than the stated
   count passes; a lower count is WRONG.
5. **Preprint notice** present, and "Why it could matter in India" lines labelled
   as the editor's reading.
6. Every outbound link returns 200 (GET if HEAD fails) and points where the text
   says.
7. **Apps:** for each PHR app, fetch the operator's or government's own page and
   confirm every capability, date, version number and figure against it. Mark
   UNSUPPORTED any feature not on the page, and flag anything planned that is
   written as shipped. Confirm no sentence calls the apps ranked, top, trending or
   popular, that scale figures are attributed, and that the article says the apps
   were not tested.
8. **Track 2:** confirm the PHR papers as in checks 1, 2 and 4, the stated window,
   pool and in-scope numbers against `radar_phr.json`, and that no paper is called
   "not peer reviewed" unless the record says so (check `comment` and `journal_ref`).
9. **Process section:** confirm "How this issue was made" matches this runbook and
   the ledger (tracks, windows, counts, selection rule, rotation rule, checking
   description, process version line) and makes no claim about the process that is
   not true.
10. **Synthesis sentences:** check every "In this issue", "Patterns", "across the
    three" and takeaway line word by word against the sources (see Maker pre-flight).

## Process version history

The article's process section opens with a version line. **Bump the version, add a
row here, and say what changed in the article** whenever the way the Radar is made
changes (a new track, a new rule, a new check).

| Version | Date | What changed |
|---|---|---|
| 1 | 2026-11-15 | Ten papers (Track 1). Method note at the top of the issue. |
| 2 | 2026-11-15 | Method note moved to the end as "How this issue was made". Track 2 added: personal health records spotlight (three papers from a 90 day shortlist plus three PHR apps researched from primary sources). Maker pre-flight and extra checker items added. |

Backlog (not yet in the process): a biomedical-agents track (see `CLAUDE.md`).

## Publish and ledger

Identical to the Frontier's Publish step (set the front matter `date` to the
current IST time immediately before committing; push; verify the live URL and
feed). Append the entry to `_data/research_radar_covered.yml` in the same commit,
with the shape documented at the top of that file (including `phr_papers`, `phr_apps` and the process `version`). A held day goes in `held`.

## Guardrails

- One article per day across both series. Never repeat an arXiv id in the ledger.
- Never fabricate or round a result; quote the paper's own numbers.
- A preprint is not evidence of clinical effectiveness. Say so.
- No em or en dashes. Never force-push or edit earlier posts.
