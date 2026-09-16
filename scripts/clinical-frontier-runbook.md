# The Clinical Frontier — Daily Runbook (HCITExperts Blog)

Procedure for the **daily "Clinical Frontier"** article on HCITExperts Blog
(hcitexpert.com). Each evening (19:00 IST) the routine reviews the latest
updates from the frontier AI companies and publishes **one** article on how a
recent frontier-model or AI-hardware update applies to a **specific healthcare
scenario**, written for an Indian health-IT audience.

Runs automatically via a scheduled cloud routine, but is written so a human can
run it identically.

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
- **Link out (dofollow):** every source announcement, and 1-3 contextual
  **dofollow links to yajur.ai** where genuinely relevant (e.g. the data
  lakehouse, Health Vault, or task-framework posts) to pass link equity.
  Do NOT set `canonical_url` — these are original HCITExperts articles.
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
