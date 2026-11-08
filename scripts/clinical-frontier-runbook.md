# The Clinical Frontier: Daily Runbook (HCITExperts Blog)

Procedure for the **daily "Clinical Frontier"** article on HCITExperts Blog
(hcitexpert.com). Each afternoon the routine reviews the latest updates from the
frontier AI labs and publishes **one** article on how a recent frontier-model or
AI-hardware update applies to a **specific healthcare scenario**, written for an
Indian health-IT audience.

**Schedule.** The cloud routine starts at **15:00 IST** (09:30 UTC). Research,
writing and checking take 30 to 60 minutes, so the article goes live at about
**16:00 IST**. Publishing is direct to the live site (push to `main`); there is
no human approval gate. The maker-checker process below is the gate.

Runs automatically via a scheduled cloud routine, but is written so a human can
run it identically.

## Step 0: guards (before any research)

1. `git checkout main && git pull --rebase origin main`.
2. If a file `_posts/<today IST>-*.md` already exists, or today's date is already
   in `covered` or `held`, **stop**: today is done. Report "already published".
3. Issue number = (number of entries in `covered`) + 1, zero-padded to 3 digits.
   Held days do not take an issue number.

## Editorial process: maker-checker (MANDATORY, fully automated)

Every article passes through two roles. **Nothing is published until an
independent checker returns APPROVED.**

**Phase 1, MAKER (the main run).** Research and write the article to its
`_posts/` file. Do NOT commit or push yet.

**Phase 2, CHECKER (a separate subagent, fresh context).** The maker launches
the checker with the Agent tool. The checker must be independent of the maker:

- Give it **only**: the path of the draft file and the path of this runbook
  (section "Checker procedure"). Do **not** pass the maker's research notes,
  search results, reasoning, or any summary of what the maker believes is true.
  The checker re-derives everything from the sources itself.
- Use a **new** checker subagent for every pass, so no pass inherits the
  previous one's conclusions.
- The checker does not edit the file. It returns a report: the claim table and
  a verdict.

### Checker procedure

1. Build a **claim inventory**: every factual assertion in the draft, including
   front matter (`description`, `mentions`, `faq`): dates, names, numbers, model
   capabilities, architectures, quotes, "X launched Y", "supports Z", Indian
   regulatory statements (ABDM, NHCX, PM-JAY, DPDP, CDSCO, ICMR).
2. For **each** claim, fetch the cited source and confirm the source actually
   says it. A **primary source is required** for any claim about a model, its
   architecture, capabilities, launch date, or numbers: the company's own site
   (anthropic.com, openai.com, blog.google, deepmind.google, research.google,
   microsoft.com/ai, ai.meta.com, nvidia.com, nvidianews.nvidia.com, groq.com,
   cursor.com). For Indian regulation, the primary source is the government or
   regulator site (abdm.gov.in, nha.gov.in, meity.gov.in, cdsco.gov.in, icmr.gov.in,
   egazette.gov.in). Secondary sites may add colour but may NOT be the sole
   support for a technical, regulatory or numeric claim.
3. Mark each claim **VERIFIED**, **UNSUPPORTED** (source does not say it),
   **WRONG** (source says otherwise), or **NO PRIMARY SOURCE**. Watch for:
   invented architectures the vendor never described; capability claims that
   are technically wrong (a text-only model "transcribing audio"); false
   deployment claims ("weights available on-premises" for an API-only model);
   wrong venues or dates; precise numbers that trace only to a secondary site;
   regulation described as in force when it is draft or proposed.
4. Check every outbound link returns 200 (`curl -sIL -o /dev/null -w '%{http_code}'`,
   with a browser user agent if a site blocks curl) and points where the text says.
5. Check style: no em dashes or en dashes anywhere; masthead, issue number and
   date are right; front matter is valid YAML.
6. Verdict: **APPROVED** only when every remaining claim is VERIFIED and every
   link resolves. Otherwise **CHANGES REQUIRED**, listing each failing claim
   and the fix (delete, or rewrite to what the source says).

**Revise-and-recheck loop.** On CHANGES REQUIRED, the maker revises the draft
(delete or correct each listed claim; never argue a claim back in without a
primary source) and launches a **new** checker. Up to 3 checker passes.

**Hold rule.** If the third pass is still not APPROVED, **do not publish**.
Either switch to a different, fully verifiable angle and restart at Phase 1
once, or publish nothing and record the day in `held` (see Ledger). A missing
day is acceptable; a false claim is not.

Only an **APPROVED** draft proceeds to Publish.

## Sourcing rule

Lead with genuine, verifiable updates. Prefer the company's own announcement
over any re-write of it. Trace every figure, name, and date to the primary
source, and cite that primary source in the article. Never fabricate a
benchmark, architecture, quote, or number.

## Tracked sources (get the latest updates each run)

Primary labs (check every run):

| Lab | Primary index | Fallback |
|-----|---------------|----------|
| Anthropic | https://www.anthropic.com/news | WebSearch `site:anthropic.com` |
| OpenAI | https://openai.com/news/ (often 403s) | WebSearch `openai.com` recent announcements |
| Google (Gemini, DeepMind, Research, Health) | https://blog.google/products/gemini/ · https://deepmind.google/discover/blog/ · https://research.google/blog/ · https://blog.google/technology/health/ | WebSearch |
| Microsoft AI | https://microsoft.ai/news/ · https://www.microsoft.com/en-us/research/blog/ | WebSearch `Microsoft AI health announcement` |
| Meta AI | https://ai.meta.com/blog/ | WebSearch |
| NVIDIA | https://blogs.nvidia.com/ (+ healthcare) · https://nvidianews.nvidia.com/ | WebSearch `NVIDIA healthcare AI announcement` (the blog healthcare category URL 404s) |

Secondary (use when they carry a clear healthcare angle):

| Company | Primary index |
|---------|---------------|
| Groq | https://groq.com/blog/ · https://groq.com/newsroom/ |
| Cursor | https://www.cursor.com/blog · https://www.cursor.com/changelog |

Focus on the **last 7 days**. Prefer items not already cited in `covered.sources`.

## What it does each run

1. **Guards** (Step 0).
2. **Gather updates.** For each primary lab, pull recent notable items (title,
   URL, date, 1-2 line description). Use the WebSearch fallback where a fetch is
   blocked or empty.
3. **Pick the day's angle.** Read `_data/clinical_frontier_covered.yml`. Choose
   a healthcare scenario (`angle`) that is NOT already in `covered`; start from
   the "Fresh angles" list in that file and extend it freely with new kebab-case
   angles. Prefer an angle that a **fresh** update maps onto naturally (a new
   vision model to radiology or dermatology; new inference hardware to on-prem
   hospital inference; an agentic release to EHR or claims workflows). If the
   week is quiet, write an evergreen scenario piece grounded in already-announced
   capabilities. **Never invent an announcement.**
4. **Write the article** (MAKER; format below), about 800 to 1,200 words of
   body, healthcare-first.
5. **Check it** (CHECKER subagent; loop as above).
6. **Publish** (below), then verify.
7. **Report** (below).

## Style: publish as a NEWSLETTER, with no dashes

**Newsletter format.** Every edition reads as a scannable briefing, not a long
essay. Use `_posts/2026-09-16-on-premise-inference-hospital-firewall-*` as the
reference:
- Open with a **masthead** blockquote naming the series, the date, and the issue
  number, plus a one-line tagline. Example:
  `> **The Clinical Frontier** · <Day Month Year> · Issue NNN`.
- Follow with an **"In this issue"** TL;DR of 2 to 4 bullets.
- Use short, bold-headed sections ("What shipped", "Why it matters", "For Indian
  hospitals", "The takeaway") and tight bullets. Prefer 1 to 3 sentence blurbs
  over long paragraphs.
- Close with a consistent **sign-off** line and the call to action (read the
  source, next issue).

**No dashes as punctuation (hard rule).** Never use em dashes (—) or en dashes
(–) anywhere, including the title, headers, and front matter. Use commas,
colons, parentheses, or periods. For number ranges write "30 to 40 minutes" or
"5-10" with a hyphen.

## Article format (match HCITExperts house style)

Front matter:

```yaml
---
title: "<healthcare-scenario-led title naming the model/update>"
date: <YYYY-MM-DD HH:MM:SS> +0530      # the ACTUAL IST time at commit, see Publish
author: Manish Sharma
description: "The Clinical Frontier, Issue NNN. <1-2 sentences, healthcare framing, includes model names>"
keywords: "<clinical + model + India/ABDM/DPDP terms>"
image: /assets/images/logo.png
reading_time: "<N> min read"
categories:
  - Healthcare Technology
  - AI/ML/DL
tags: [ ... clinical + model tags ... ]
mentions:            # each source model/update as {name, description, url}
  - name: "..."
    description: "..."
    url: "https://..."
faq:                 # 2-4 Q&A for AEO
  - q: "..."
    a: "..."
---
```

Body guidance:
- **Lead with the update**, then pivot fast to the **clinical scenario**: what
  changes for a hospital, clinician, registry, payer, or patient in India.
- Be **specific and technical** where it helps (model sizes, context windows,
  on-prem/quantisation, latency, cost), and ground claims in the **linked
  source**.
- Connect to the **Indian context** where relevant: ABDM, FHIR, NHCX, PM-JAY,
  DPDP Act, on-prem/data-residency, Indic languages.
- **Link out (dofollow):** link every source announcement you cite. Do NOT force
  a link to our own properties. At most one genuinely relevant self-reference
  (a yajur.ai post or another HCITExperts post) per article, often none. Do NOT
  set `canonical_url`.
- Include a short FAQ block (front matter `faq`) for answer engines.

## Publish (auto-deploy pipeline)

HCITExperts deploys on push to `main` (GitHub Actions to GitHub Pages).

**Date stamp rule.** Jekyll does not build posts dated in the future, and the
site only rebuilds on a push. So the front matter `date` must be **no later
than the moment of the push**. Immediately before committing, set it to the
current IST time: `TZ=Asia/Kolkata date '+%Y-%m-%d %H:%M:%S +0530'`.

```bash
git checkout main && git pull --rebase origin main
# set front matter date to the current IST time (rule above)
git add _posts/<file>.md _data/clinical_frontier_covered.yml
git commit -m "post: Clinical Frontier <YYYY-MM-DD> - <angle>"
git push origin main            # auto-deploys
```

Append the ledger entry (below) in the same commit.

**Verify.** Wait for the deploy (poll every 60 seconds, up to 10 minutes) until
`curl -s -o /dev/null -w '%{http_code}' https://hcitexpert.com/<yyyy>/<mm>/<dd>/<slug>/`
returns 200, then confirm the post is in `https://hcitexpert.com/feed.xml`.
If it never returns 200, check the latest GitHub Actions run and report the
error; do not force-push or rewrite history.

## Ledger

`_data/clinical_frontier_covered.yml`:

- **Published:** append to `covered` one entry with `date`, `slug`, `angle`,
  `models`, `sources` (every URL referenced).
- **Held:** append to `held` one entry with `date` and `reason` (for example
  "held: could not verify <claim> after 3 checker passes"). Commit and push it
  alone with message `ledger: Clinical Frontier <YYYY-MM-DD> held`.

## Report (end of every run)

End the run with a short summary, in this form:

- **Published:** Issue NNN, title, live URL, angle, checker passes used, claims
  removed or corrected by the checker.
- **Held:** reason, and the angle tried.
- **Failed:** the step that failed and the error.

## Guardrails

- One article per day. Never repeat an `angle` already in the ledger.
- Never fabricate an announcement, benchmark, or figure; link every claim.
- No em or en dashes.
- Keep it genuinely useful to a health-IT reader, not a press-release rewrite.
- Never force-push, rewrite history, or edit earlier posts. Only add the day's
  post and the ledger entry.
- If publish fails, stop and report the error rather than forcing it.
