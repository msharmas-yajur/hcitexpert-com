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

## Article format

Front matter as in the Frontier runbook, with these differences:

```yaml
description: "The Research Radar, Issue NNN. <1-2 sentences: the window, the criterion, and the headline themes>"
tags: [ ... , Research Radar, arXiv, Preprints, ... ]
mentions:          # one entry per paper: {name: "<paper title>", description: "<authors, arXiv id, date>", url: "https://arxiv.org/abs/<id>"}
```

Body, as a newsletter (no dashes anywhere, see the Frontier runbook):

- Masthead: `> **The Research Radar** · <Day Month Year> · Issue NNN`, plus the
  one-line tagline.
- **In this issue**: 2 to 4 bullets (the themes, not a list of titles).
- **How these ten were chosen** (always included): window dates, pool size, how
  many in scope, the criterion, how many were ranked by Hugging Face upvotes vs
  the keyword fallback, the `as_of` time for upvote counts, and how many
  candidates were skipped on reading.
- **Preprint notice** (always included): "These are arXiv preprints. They have
  not necessarily been peer reviewed, and results may change. None of this is
  clinical guidance."
- **The ten papers**, numbered in rank order. Each entry has: title linked to
  `arxiv.org/abs/<id>`; authors (first three, then "et al."); submitted date;
  `Rank basis:` Hugging Face upvotes (count, as of date) **or** "not featured on
  Hugging Face, ranked by keyword relevance"; then three short lines:
  **What it does** (from the paper), **What it reports** (only what the abstract
  or full text states, attributed to the authors), **Caveat** (a limitation the
  paper states, or "preprint, not peer reviewed").
  After each entry, optionally one line headed **Why it could matter in India**,
  clearly labelled as our reading, never as a claim about the paper.
- **Patterns across the ten**: 2 to 3 bullets on what the set shows together.
- **Takeaway** and the sign-off linking back to HCITExperts, as in the Frontier.

About 1,200 to 1,800 words of body. Prefer tight bullets over paragraphs. No
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

## Publish and ledger

Identical to the Frontier's Publish step (set the front matter `date` to the
current IST time immediately before committing; push; verify the live URL and
feed). Append the entry to `_data/research_radar_covered.yml` in the same commit,
with the shape documented at the top of that file. A held day goes in `held`.

## Guardrails

- One article per day across both series. Never repeat an arXiv id in the ledger.
- Never fabricate or round a result; quote the paper's own numbers.
- A preprint is not evidence of clinical effectiveness. Say so.
- No em or en dashes. Never force-push or edit earlier posts.
