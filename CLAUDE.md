# HCITExperts Blog: Publisher Memory

This file is the working memory for any Claude session acting as the **publisher** of
the HCITExperts Blog (hcitexpert.com, Jekyll on GitHub Pages). It exists so that a new
session can pick up exactly where a previous one stopped, for example after a crash.
Read it fully before doing anything. When you finish a session's work, update the
"State" and "Change log" sections so the next session inherits your context.

Everything here is about process and state. It holds no secrets, and none should be added.

---

## 1. Quick start: what do I do today?

1. `git checkout main && git pull --rebase origin main` (a sandbox session restricted to a
   feature branch: see section 8).
2. Read the two runbooks, which are the source of truth for each edition:
   - `scripts/clinical-frontier-runbook.md` (**The Clinical Frontier**)
   - `scripts/research-radar-runbook.md` (**The Research Radar**)
3. Decide which edition runs, using **Step 0** of either runbook. In short:
   - If a `_posts/<today IST>-*.md` file or a ledger entry for today already exists, today
     is done unless the owner explicitly asks for a second edition.
   - Otherwise take the most recent entry across `_data/clinical_frontier_covered.yml` and
     `_data/research_radar_covered.yml`. If it is a **Frontier**, today is a **Radar**.
     If it is a **Radar**, today is a **Frontier**.
   - Tie-break: if both ledgers share the latest date (a double-edition day), the Radar
     counts as the later edition, so the next day is a Frontier.
4. Follow that edition's runbook end to end, including the maker-checker gate. **Nothing
   is published until an independent checker returns APPROVED.**

## 2. Repo map

| Path | What it is |
|---|---|
| `_posts/` | All posts. File name `YYYY-MM-DD-slug.md`. |
| `_data/clinical_frontier_covered.yml` | Frontier ledger: one entry per published Frontier (angle, models, sources). `held:` lists skipped days. |
| `_data/research_radar_covered.yml` | Radar ledger: window, pool counts, the ten papers with rank basis, skipped candidates. Separate issue numbers. |
| `scripts/clinical-frontier-runbook.md` | Frontier procedure, house style, checker procedure, publish steps. |
| `scripts/research-radar-runbook.md` | Radar procedure, article format, paper-level checker procedure. |
| `scripts/research_radar.py` | Deterministic Radar shortlist builder (stdlib only). `--track main` (default, the ten papers) and `--track phr` (personal health records and health apps), `--exclude <json>` to keep one track's papers out of another. |
| `.github/workflows/jekyll.yml` | Deploys on **push to `main`**. A merge to `main` publishes. |
| `DESIGN.md` | Visual design reference for the site (not editorial guidance). |

Other posts exist that are not part of either edition (for example the owner-written
"Building the Caladrius PHR with agents" series, front matter `series:`). Do not edit
earlier posts. See section 7 for that series.

## 3. The two editions

**The Clinical Frontier** (issue numbers = Frontier ledger count + 1): a newsletter on how a
fresh frontier-lab or AI-hardware update applies to one healthcare scenario, for an Indian
health-IT audience. Sources are primary lab announcements. One `angle` (scenario) per
issue, never repeated (it is the ledger key).

**The Research Radar** (alternate days, its own issue numbers = Radar ledger count + 1):
a review of the ten highest-ranked recent arXiv preprints on digital health and clinical
AI, plus a **personal health records (PHR) spotlight in every edition**: three PHR and
health-app preprints and three live PHR apps researched from primary sources. The
shortlists are produced by a script, not hand-picked. The **methodology goes at the end
of the article** ("How this issue was made", opening with a process version line), so
readers can review how it was made; any new concept or process added to the Radar gets
its own entry there. Process version history lives in the Radar runbook.

Shared rules (full detail in the runbooks):
- **No em dashes or en dashes anywhere**, including title and front matter. Ranges are
  "30 to 40" or "5-10".
- Newsletter format: masthead blockquote with series, date, issue number; "In this issue"
  bullets; short bold-headed sections; consistent sign-off. Front matter fields as in the
  runbook (`description`, `keywords`, `reading_time`, `mentions`, `faq`, `image`).
- Set the front matter `date` to the **current IST time immediately before the push**
  (`TZ=Asia/Kolkata date '+%Y-%m-%d %H:%M:%S +0530'`). Jekyll skips future-dated posts.
- Append the ledger entry in the **same commit** as the post.
- Verify after deploy: the post URL returns 200 and appears in `https://hcitexpert.com/feed.xml`.

## 4. Research Radar: how the shortlist works

`python3 scripts/research_radar.py --days 14 --top 10 --reserve 10 --out <json> --md <md>`

1. **Pool:** arXiv API, last N days, 14 categories (cs.AI/CL/LG/CV/CY/HC/IR/MA, eess.IV/SP,
   stat.AP/ML, q-bio.QM, physics.med-ph) whose abstract matches a health term, plus any
   category for "digital health". Plus Hugging Face daily papers for the same days.
2. **Scope filter:** a paper needs a minimum **relevance score of 3** (distinct health
   terms; a title match counts double). This was added after the first dry run: a single
   generic word ("diagnostic", "triage", "clinical" mentioned once) let off-topic ML
   papers through and, ranked by upvotes, they took the top slots. Do not lower it
   without re-checking the top ten by eye.
3. **Rank:** primary = Hugging Face upvotes (descending). Papers **not featured on
   Hugging Face** rank after those, by keyword relevance, then recency. Each row records
   its `rank_basis`.
4. **Be honest about the criterion.** Hugging Face features few health papers (Issue 001:
   7 of 194 in scope; counts of 1 to 10 upvotes), so most of the ten are usually ranked by
   the fallback. The article must state the split and the `as_of` time, and must never
   call a fallback-ranked paper "popular" or "most upvoted".
5. **Reading step:** read every abstract (full text before saying anything the abstract
   does not). Substitute from the `reserve` if a paper is out of scope on reading; record
   it under `skipped` in the ledger and say so in the method note. Also read the arXiv
   `comment` field: it can show acceptance at a venue (Issue 001 had two such papers).

**Track 2 (PHR spotlight).** `--track phr --days 90 --top 3 --reserve 10 --exclude <track 1 json>`.
The window is 90 days because very few preprints a fortnight mention PHRs or health apps
(a 15-day window returned 0 or 1 per phrase). A paper needs a PHR/health-app anchor term
and a general health score of 2. In Issue 001 all nine in-scope papers were fallback-ranked
(none on Hugging Face), and the article says so. The runbook (Steps 1 and 3) also sets the
rules for **researching the three apps**: different health-system contexts, a recent update
or announcement on the operator's or government's **own pages**, described only from them,
shipped vs planned kept apart, figures attributed, **never a "top" or "trending" ranking
and never a claim to have tested an app**, no repeat of a featured app within three Radar
issues unless there is a new announcement.

Known issue: `covered_ids()` excludes **every** arXiv id found anywhere in the ledger,
including `skipped` entries, so a skipped paper can never be selected again, even by a
different track. See the backlog (section 6).

## 5. The maker-checker gate, and the lessons from Issue 001

The checker is a **fresh subagent** given only the draft path and the runbooks (never the
maker's notes or conclusions). It re-derives each claim from the primary source, marks it
VERIFIED / UNSUPPORTED / WRONG / NO PRIMARY SOURCE, and returns APPROVED or CHANGES
REQUIRED. Up to 3 passes, a new checker each time. If pass 3 is not APPROVED: do not
publish. You may restart Phase 1 once; otherwise record the day in `held`.

What actually went wrong (use this as a pre-flight list *before* sending a draft to a checker):

1. **Paper and source content was almost never the problem.** Titles, authors, dates and
   numbers verified on every pass. **The maker's own synthesis sentences were the problem**:
   "In this issue" bullets, "Patterns" bullets, takeaways, FAQ answers, the description.
2. Each pass found a different sentence that turned one paper's result into a trend or a
   field-wide claim ("benchmarks keep finding...", "models are getting smaller, faster and
   more clinician-evaluated", "two papers focus on efficiency", "most have not been peer
   reviewed", "whole care pathways remain hard"). Fixing one word at a time did not
   converge. What worked: **rewrite synthesis lines as strictly attributable statements**
   ("NPCBench reports...", "the Mixed Signals authors say...") and drop counts and
   generalisations.
3. Before sending to a checker, check every synthesis sentence for: (a) a claim about more
   than one paper, is it true of *each* paper named? (b) words like "efficiency", "edge",
   "benchmark", "peer reviewed", "validated", "trend", "keep", "most" that the abstracts do
   not literally support; (c) timing words ("this week") against each source's real date;
   (d) a vendor claim stated as fact instead of attributed ("NVIDIA says...").
4. Absence claims ("the abstract gives no figures", "no accuracy figures") are accepted
   only if the checker confirms the abstract really omits it.
5. The Frontier gate caught real errors too: Claude answers in writing by default (not
   aloud); Google's note-taker notifies participants (it does not ask their permission);
   Anthropic's "not available to HIPAA-ready configurations" must not be rewritten as
   "not for patient data".
6. **Issue 001 exceeded the pass limit.** Three passes plus the one restart (six checkers)
   all returned CHANGES REQUIRED; the owner then explicitly authorised one further pass,
   which approved the text. The published text is exactly the approved text (optional
   checker notes were not applied afterwards, because any edit after approval means the
   shipped text is not the approved text). Never extend the pass limit on your own
   authority; ask the owner.
7. Length: the Radar body ran about 2,300 words against the runbook's 1,200 to 1,800
   target. The checker treats length as advisory. Consider tightening the entry template.

## 6. State and backlog (as of 2026-11-15)

**Published today (both live, verified 200 and in the feed):**
- Clinical Frontier Issue 035, angle `chart-review-and-clinical-meeting-capture-india`
  (NVIDIA / Dyania Health Synapsis AI; Claude Meetings; Google Meet "Take notes for me";
  a proposed capture, draft, clinician attestation, EHR commit pattern using FHIR
  Composition and DocumentReference). Frontier ledger: 35 entries, none held.
- Research Radar Issue 001, window 1 to 15 Nov 2026, pool 665, in scope 194, six of ten
  ranked by upvotes and four by fallback, one candidate skipped on reading. Radar ledger:
  1 entry, none held.
- **Issue 001 was then updated to Radar process version 2** (at the owner's request): the
  method note moved to the end ("How this issue was made") and a PHR spotlight was added
  (papers 2610.41437, 2610.23851, 2610.31467; apps **Google Health app, NHS App, Aarogya
  Setu 2.0**, so those three apps are not repeated in Radar Issues 002 to 004 unless they
  have a new announcement). The update goes live only when its PR is merged.

**Next edition due:** a **Clinical Frontier, Issue 036** (the last entry is a double-edition
day, and the tie-break makes the Radar the latest). The next Radar will be Issue 002.

**Backlog (not yet done; owner has seen these):**
1. **Biomedical research agents track.** The owner wants these topics considered for the
   Radar in future. Recommended design: a **separate track**, not a wider main scope
   (AI-for-science papers draw more Hugging Face upvotes than clinical papers and would
   crowd out the clinical ten; the skipped Issue 001 paper had 10 upvotes vs 4 for the next
   clinical one). Add `--track biomedical-agents` to `research_radar.py` with its own term
   list, a short labelled section (about 3 papers) in the Radar, ranked separately.
   **Fix first:** make the covered-id exclusion per track so skipped papers (for example
   arXiv:2611.01527, the biomedical-agents audit) remain eligible for that track.
   Awaiting the owner's go-ahead.
2. **OpenAI sources for the Frontier.** The owner wants OpenAI's Meetings plugin, team
   features and any healthcare releases covered from primary sources. `openai.com/index/*`
   and `help.openai.com/*` return 403 to every fetch method available (see section 9).
   Leads that load: the OpenAI RSS feed and the OpenAI Developer Community DevDay thread
   (a community summary, not a primary page: it lists ChatGPT Space, Teams and Team Tasks,
   ChatGPT in Slack and Microsoft Teams, and a Meetings plugin in beta on macOS for Pro and
   Business). Use only with explicit attribution, or ask the owner to paste the OpenAI page
   text. Search results also mention "Health in ChatGPT" (July) and an Epic EHR integration
   for ChatGPT for Healthcare (September); unverified.
3. **Checker process improvements (LLM-as-judge):** deterministic checks (dashes, YAML,
   links, ledger, dates) as scripts, not model passes; a rubric with a required verbatim
   quote per claim and an explicit "unverifiable" verdict; extra rubric items for synthesis
   sentences, timing words, Indian regulatory claims needing a government primary source,
   and clinical or patient-data advice; use a judge from a different model family than the
   maker where possible (same-family judges tend to go easy); a small gold set of past
   drafts with seeded errors to measure catch rate (the real errors in section 5 are
   candidates); a periodic human spot check on clinical claims.
4. **Scheduled routine:** the daily cloud routine (15:00 IST) was not inspected in the
   session that built the Radar. Confirm its prompt follows the runbooks. If it hard-codes
   the Frontier steps, it needs one line to follow the Step 0 alternation.
5. **Maker pre-flight** is now in the Radar runbook ("Maker pre-flight"). Add the same
   checklist to the Frontier runbook's maker step.
6. **Radar length.** Issue 001 v2 is about 5,000 words in total. A shorter per-entry
   template (or fewer lines per paper) is on the backlog.
7. **PHR apps for later editions** (candidates only; each needs a fetched primary page
   before it can be featured): Apple Health (Apple newsroom), Australia's My Health
   Record, Epic MyChart, Microsoft's Copilot Health, Health in ChatGPT (OpenAI's own
   pages are blocked here), other national apps. The owner asked for the spotlight "on a
   daily basis": the Radar runs on alternate days, so it appears in every Radar edition.
   If the owner wants a PHR item every day, that is a separate daily item and needs a
   decision.

## 7. Other content you may be asked about

- **"Building the Caladrius PHR with agents"** series (owner-written, front matter
  `series: building-the-caladrius-phr-with-agents`). Day 0 is published (2026-11-14) and
  ends "Next, Day 1 (29 October): the app stops talking to a mock and starts talking to
  ABDM." **No Day 1 source material exists in this repository or the sandbox.** Do not
  write Day 1 from imagination: ask the owner for the build log, plans or notes.
- Sister repository `yajur-ai` (yajur.ai) has its own `CLAUDE.md` and posts. It is a
  separate site; do not mix its ledgers or branches with this one.

## 8. Git and publishing rules

- The site deploys on **push to `main`** (`.github/workflows/jekyll.yml`); a merge publishes.
- The scheduled cloud routine publishes by pushing to `main` per the Frontier runbook.
- An interactive or sandbox session may be restricted to a feature branch (check the
  session's instructions). In that case: commit on that branch, push it, open a PR, and
  **merge only when the owner asks**. Merging is outward-facing and deploys.
- After a PR from that branch merges, restart the branch from the latest `main` before more
  work (a force-with-lease push is acceptable when the remote branch holds only merged
  history).
- Never force-push or rewrite history on `main`; never edit earlier posts; only add the
  day's post, its ledger entry and runbook or script changes.
- Never skip or weaken the checker gate to meet a deadline. A missing day is acceptable;
  a false claim is not. Record held days in the ledger `held:` list and push that alone.
- GitHub comments and PR bodies you author end with the attribution footer your session
  instructions require.

## 9. Environment notes: what a sandbox session can reach

Observed on 2026-11-15; these change, so re-test before relying on them.

| Works | Blocked or unreliable |
|---|---|
| arXiv API (`export.arxiv.org`, id_list and search) | `openai.com/index/*`, `help.openai.com/*` (403) |
| Hugging Face API (`/api/daily_papers?date=`, `/api/papers/<id>`) | `dyaniahealth.com` (403) |
| `blogs.nvidia.com`, `blog.google`, `research.google`, `claude.com/blog`, `anthropic.com/news` | `ctri.nic.in`, `cdsco.gov.in` (unreachable) |
| `pib.gov.in` press releases and `static.pib.gov.in` PDFs (GET works; HEAD returns 401) | `microsoft.com/en-us/research/blog` (403) |
| `nhs.uk` (NHS App release notes), `gov.uk` press releases | |
| `hl7.org/fhir`, `meity.gov.in` | `deepmind.google` blog index returned binary/unusable content |
| `openai.com/news/rss.xml`, `community.openai.com` | |
| `hcitexpert.com` and its `feed.xml` | |

Consequences: Indian regulatory claims must rest on a reachable government primary source
(PIB works; CTRI and CDSCO do not, so do not make trial-regulation claims); a checker that
cannot fetch a source must say "unverifiable", never pass it. Some servers refuse HEAD:
retry with GET before counting a link as broken.

## 10. Change log

| Date | What changed |
|---|---|
| 2026-11-15 | **Clinical Frontier Issue 035** published (PR #6). **Research Radar** built and Issue 001 published (PR #7): `scripts/research_radar.py`, `scripts/research-radar-runbook.md`, `_data/research_radar_covered.yml`, Step 0 alternation and tie-break in both runbooks. Scope filter tightened after a dry run (min relevance 3). Issue 001 needed more checker passes than the runbook allows; the owner authorised one extra pass. This `CLAUDE.md` created as the publisher memory. |
| 2026-11-15 (later) | **Radar process version 2**: PHR spotlight added (`--track phr`, app research rules, three papers and three apps in Issue 001), methodology moved to the end of the article as an extensible "How this issue was made" section, process version history, maker pre-flight and extra checker items added to the runbook, ledger gained `version`, `phr_*` fields. Issue 001 updated accordingly. |
