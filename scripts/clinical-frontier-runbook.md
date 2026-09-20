# The Clinical Frontier — Daily Runbook (HCITExperts Blog)

Procedure for the **daily "Clinical Frontier"** article on HCITExperts Blog
(hcitexpert.com). Each evening (19:00 IST) the routine reviews the latest
updates from the frontier AI companies and publishes **one** article on how a
recent frontier-model or AI-hardware update applies to a **specific healthcare
scenario**, written for an Indian health-IT audience.

Runs automatically via a scheduled cloud routine, but is written so a human can
run it identically.

## Editorial process: maker-checker (MANDATORY, fully automated)

Every article passes through two phases in the same run. **Nothing is published until the checker validates it.**

**Phase 1, MAKER.** Research and write the article to a file. Do NOT commit or push yet.

**Phase 2, CHECKER (adversarial fact-check).** Put the maker's draft aside and re-verify it with fresh, skeptical eyes:
1. Build a **claim inventory**: list every factual assertion in the draft (dates, names, numbers, model capabilities, architectures, quotes, "X launched Y", "supports Z").
2. For **each** claim, re-fetch the cited source and confirm the source actually says it. A **primary source is required** for any claim about a model, its architecture, its capabilities, launch dates, or numbers: the company's own site (anthropic.com, openai.com, blog.google/deepmind.google, groq.com, cursor.com, nvidia.com/nvidianews). Secondary aggregators (news sites, blog re-writes, AI-content sites) may add colour but may NOT be the sole support for a technical or numeric claim.
3. **Delete or rewrite** every claim that the primary source does not support. Watch specifically for: invented technical architectures (e.g. "cascade of model A + model B") that the vendor never described; capability claims that are technically wrong (e.g. a text-only model "transcribing audio"); false deployment claims (e.g. "model weights available on-premises" when the vendor is API-only); wrong venues/dates; and precise numbers that trace only to a non-primary source.
4. Verify every outbound link returns 200 (curl) and points where the text claims.
5. Produce a one-line verdict: **APPROVED** only when every remaining claim is verified against a primary source.

**Revise-and-recheck loop.** If the checker finds problems, revise the draft and run the checker again. Up to 3 passes.

**Hold rule.** If, after revision, a compelling hook still cannot be verified, **do not publish it**. Either switch to a different, fully-verifiable angle, or, as a last resort, publish nothing that day and log "held: could not verify" rather than shipping an unverified article. A missing day is acceptable; a false claim is not.

Only an **APPROVED** draft proceeds to Publish.

## Sourcing rule

Lead with genuine, verifiable updates. Prefer the company's own announcement over any re-write of it. Trace every figure, name, and date to the primary source, and cite that primary source in the article. Never fabricate a benchmark, architecture, quote, or number.

## Tracked sources (get the latest updates each run)

| Company | Primary index | Fallback |
|---------|---------------|----------|
| Anthropic | https://www.anthropic.com/news | — |
| OpenAI | https://openai.com/news/ (often 403s) | WebSearch `openai.com` recent announcements |
| Google (Gemini / DeepMind) | https://blog.google/products/gemini/ · https://deepmind.google/discover/blog/ | WebSearch |
| Groq | https://groq.com/blog/ · https://groq.com/newsroom/ | WebSearch |
| Cursor | https://www.cursor.com/blog · https://www.cursor.com/changelog | WebSearch |
| NVIDIA | https://blogs.nvidia.com/ (+ healthcare) · https://nvidianews.nvidia.com/ | WebSearch `NVIDIA healthcare AI announcement` (the blog healthcare category URL 404s) |

## What it does each run

1. **Gather updates.** For each company, pull recent notable items (title, URL,
   date, 1-2 line description). Use the WebSearch fallback where a fetch is
   blocked/empty (OpenAI, NVIDIA routinely need this).
2. **Pick the day's angle.** Read `_data/clinical_frontier_covered.yml`. Choose a
   healthcare scenario (`angle`) that is NOT already in `covered` — see the
   rotation list in that file. Prefer an angle that a **fresh** update maps onto
   naturally (e.g. a new vision model → radiology; new inference hardware →
   on-prem hospital inference; a new agentic/coding release → EHR agentic
   workflows). If there is genuinely fresh news, lead with it; if the day is
   quiet, write an evergreen scenario piece grounded in already-announced
   capabilities — **never invent an announcement**.
3. **Write the article** (see format below), ~800-1200 words, healthcare-first.
4. **Publish** via push to `main` (auto-deploys), then verify 200.
5. **Append** one entry to `covered` with `date`, `slug`, `angle`, `models`,
   and `sources` (the URLs referenced).

## Style: publish as a NEWSLETTER, with no dashes

**Newsletter format.** Every edition reads as a scannable briefing, not a long essay. Use the published template at `_posts/2026-09-16-on-premise-inference-hospital-firewall-*` as the reference:
- Open with a **masthead** blockquote naming the series, the date, and the issue number, plus a one-line tagline. Example: `> **The Clinical Frontier** · <Day Month Year> · Issue NNN`.
- Follow with an **"In this issue"** TL;DR of 2 to 4 bullets.
- Use short, bold-headed sections ("What shipped", "Why it matters", "For Indian hospitals", "The takeaway") and tight bullets. Prefer 1 to 3 sentence blurbs over long paragraphs. Keep it skimmable.
- Close with a consistent **sign-off** line and the call to action (read the source, the yajur.ai posts, next issue).

**No dashes as punctuation (hard rule).** Never use em dashes (—) or en dashes (–) anywhere, including the title, headers, and front matter. Use commas, colons, parentheses, or periods. For number ranges write "30 to 40 minutes" or "5-10" with a hyphen.

## Article format (match HCITExperts house style)

Front matter (mirror recent posts, e.g. `_posts/2026-04-23-open-intelligence-*`):

```yaml
---
title: "<healthcare-scenario-led title naming the model/update>"
date: <YYYY-MM-DD> 19:00:00 +0530
author: Manish Sharma
description: "<1-2 sentences, healthcare framing, includes model names>"
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
  source**. Trace every figure to a source; never fabricate benchmarks or news.
- Connect to the **Indian context** where relevant: ABDM, FHIR, NHCX, PM-JAY,
  DPDP Act, on-prem/data-residency, Indic languages.
- **Link out (dofollow):** always link every source announcement you cite. These
  are market-trend briefings that inform readers first, so do NOT force a link to
  our own properties. Reference a yajur.ai post (Health Vault, data lakehouse,
  task framework) or another HCITExperts post ONLY when it is genuinely and
  directly relevant to the point being made, at most one such self-reference per
  article, and often none. Never insert a self-link as a routine call to action.
  Do NOT set `canonical_url`, these are original HCITExperts articles.
- Include a short FAQ block (front matter `faq`) for answer engines.
- **NO em dashes (—) or en dashes (–).** Use commas, colons, or periods. This is
  a hard style rule for this series.

## Publish (auto-deploy pipeline)

HCITExperts deploys on push to `main` (GitHub Actions -> GitHub Pages).

```bash
git checkout main && git pull --rebase origin main
git add _posts/<file>.md _data/clinical_frontier_covered.yml
git commit -m "post: Clinical Frontier <date> — <angle>"
git push origin main            # auto-deploys
```

Verify: `curl -s -o /dev/null -w '%{http_code}' https://hcitexpert.com/<yyyy>/<mm>/<dd>/<slug>/` returns 200 (allow a few minutes), and the post appears on the homepage and in feed.xml.

## Guardrails

- One article per day. Never repeat an `angle` already in the ledger.
- Never fabricate an announcement, benchmark, or figure; link every claim.
- No em/en dashes.
- Keep it genuinely useful to a health-IT reader, not a press-release rewrite.
- If publish fails, stop and report the error rather than forcing it.
