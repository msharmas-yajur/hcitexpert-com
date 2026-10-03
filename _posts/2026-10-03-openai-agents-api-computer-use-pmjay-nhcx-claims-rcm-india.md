---
title: "OpenAI Agents API Gains Computer Use: Automating PM-JAY Claims on NHCX for Indian Hospitals"
date: '2026-10-03 19:00:00 +0530'
author: Manish Sharma
description: "The Clinical Frontier, Issue 017. OpenAI announced GPT-6.1 Sol and computer use in the Agents API at DevDay 2026. For India's PM-JAY ecosystem, this means agents that can navigate NHCX portals, submit pre-authorisation forms, and chase claim status without custom integrations, at one-fifth the cost of GPT-6 Astra."
keywords: "PM-JAY claims automation India, NHCX AI claims processing, OpenAI Agents API computer use India, GPT-6.1 Sol healthcare India, AI prior authorisation PM-JAY, NHCX portal automation India, health insurance claims AI India, revenue cycle management AI India, ABDM claims exchange, TPA claims processing AI India"
image: /assets/images/logo.png
reading_time: "6 min read"
categories:
  - Healthcare Technology
  - AI/ML/DL
tags:
  - GPT-6.1 Sol
  - OpenAI
  - PM-JAY
  - NHCX
  - Claims Processing
  - Revenue Cycle Management
  - Agents API
  - Computer Use
  - India Health IT
  - Healthcare AI
mentions:
  - name: "GPT-6.1 Sol"
    description: "OpenAI's model announced at DevDay 2026. Delivers near-GPT-6 Astra performance on agentic coding, computer use, and professional work at one-fifth of Astra's standard token prices. Standard pricing: $2 per million input tokens, $10 per million output tokens."
    url: "https://openai.com/index/introducing-gpt-6-1-sol/"
  - name: "Agents API with Computer Use (OpenAI DevDay 2026)"
    description: "Computer use added to OpenAI's Agents API at DevDay 2026, enabling agents to complete tasks in an OpenAI-hosted browser and operate software through its UI. Agents API is now in public beta."
    url: "https://openai.com/index/devday-2026-recap/"
  - name: "Claude Frontier Academy"
    description: "Anthropic's $100 million commitment to train 10,000 Frontier Deployed Engineers by end of 2027, following a medical-residency model with a 12-week hands-on deployment at partner organisations."
    url: "https://www.anthropic.com/news/claude-frontier-academy"
  - name: "PM-JAY (Pradhan Mantri Jan Arogya Yojana)"
    description: "India's government-funded health insurance scheme, implemented by the National Health Authority. Covers over 100 million families for cashless treatment at empanelled hospitals."
    url: "https://nha.gov.in/PM-JAY"
faq:
  - q: "What is computer use in the OpenAI Agents API, and how does it differ from a standard API integration?"
    a: "Computer use in the Agents API lets an AI agent operate software through its user interface rather than through a dedicated API. The agent navigates to a website in a hosted browser, fills in forms, clicks buttons, and reads responses, exactly as a human operator would. For NHCX claims workflows, this matters because the portal handles pre-authorisation submission and status tracking through a web interface. A computer-use agent can work that portal without requiring a custom EDI or HL7 integration."
  - q: "How does PM-JAY pre-authorisation work, and where does AI help most?"
    a: "Under PM-JAY, a beneficiary seeks cashless treatment at an empanelled hospital. The hospital submits a pre-authorisation request to the insurer or TPA via NHCX. If approved, treatment proceeds and the hospital raises a final claim after discharge. Each step requires structured data entry, document attachment, and manual follow-up on denials. AI agents with computer use can automate the pre-auth submission, monitor status, flag missing documents, and draft appeal letters, cutting the time a billing team spends per claim."
  - q: "Is GPT-6.1 Sol affordable for a mid-size Indian hospital running PM-JAY claims?"
    a: "At $2 per million input tokens, processing a 2,000-token PM-JAY pre-authorisation packet costs $0.004 per claim in input. Output at $10 per million tokens adds $0.005 for a 500-token form response. Total model cost: roughly $0.009 per claim, or under 1 rupee at current exchange rates, well within the administrative margin for a cashless scheme. A hospital doing 200 cashless pre-authorisations a day spends under $2 in total model costs."
  - q: "What is the Anthropic Frontier Academy and why does it matter for health-IT teams?"
    a: "The Claude Frontier Academy is Anthropic's $100 million commitment, announced October 2, 2026, to train 10,000 Frontier Deployed Engineers (FDEs) by end of 2027. It follows a medical-residency model: multi-day classroom training followed by a 12-week residency where the engineer implements a live Claude project at their own organisation. Healthcare partners in the first cohorts include Novo Nordisk. For Indian health-IT teams, the significance is that structured AI-deployment training, not just model access, is now a product offered by the frontier labs."
---

> **The Clinical Frontier** · 3 October 2026 · Issue 017
>
> *Agents that click buttons: computer use arrives in the OpenAI Agents API just as India's PM-JAY claims portal begs for automation.*

## In this issue

- OpenAI unveiled [GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/) at DevDay 2026: near-Astra reasoning at one-fifth of Astra's standard token prices.
- OpenAI added computer use to the [Agents API](https://openai.com/index/devday-2026-recap/), now in public beta, letting agents operate any web interface like a human operator would.
- Anthropic announced the [Claude Frontier Academy](https://www.anthropic.com/news/claude-frontier-academy): a $100 million, 10,000-engineer training programme that follows a medical-residency model.
- Why the PM-JAY and NHCX claims pipeline is the first Indian healthcare workflow that can realistically benefit from computer-use agents.

---

## The signal

At DevDay 2026, OpenAI announced [GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/), a major upgrade to GPT-6 Sol. The model delivers near-GPT-6 Astra performance on agentic coding, computer use, and professional work at one-fifth of Astra's standard input and output token prices. Standard API pricing is $2 per million input tokens and $10 per million output tokens.

Alongside the new model, OpenAI added computer use to the [Agents API](https://openai.com/index/devday-2026-recap/), now in public beta. Computer use lets an agent complete tasks inside an OpenAI-hosted browser: navigating websites, filling forms, clicking buttons, and reading results, without requiring the target service to expose a dedicated API endpoint.

One day earlier, Anthropic [announced the Claude Frontier Academy](https://www.anthropic.com/news/claude-frontier-academy): a $100 million commitment to train 10,000 Frontier Deployed Engineers (FDEs) by end of 2027, using a medical-residency model with a 12-week hands-on deployment period.

---

## How computer use works

A conventional AI integration requires the target service to expose a clean REST or HL7 endpoint. Most hospital billing teams never get that from insurers or TPAs.

Computer use flips this. The Agents API provisions a hosted browser, and the model navigates the target portal autonomously. For a PM-JAY claims workflow, the agent can:

- Log in to NHCX with the hospital's stored credentials.
- Fill the structured pre-authorisation form from the patient's admission data in the HIS.
- Attach supporting documents: investigation reports, consultant notes, diagnosis summary.
- Submit, then read the response: approval, query, or denial code.
- Flag only genuine clinical queries to the billing supervisor.

The model doing all of this is GPT-6.1 Sol at $2 per million input tokens. A typical 2,000-token pre-auth packet costs $0.004 in model input. A hospital processing 200 cashless claims a day spends under $2 in total model costs, under 1 rupee per claim at current exchange rates.

---

## Why Indian hospitals need this now

[PM-JAY](https://nha.gov.in/PM-JAY), implemented by the National Health Authority, covers over 100 million families for cashless treatment at empanelled hospitals. Every cashless admission requires a pre-authorisation request submitted via NHCX to the insurer or TPA, followed by a final claim after discharge.

The process is manual at every step. Billing staff navigate a portal, enter structured patient and diagnosis data, attach scanned documents, wait for a response, and then chase queries or appeal denials. A single denied claim can require multiple re-submissions, each entered by hand. For a secondary hospital with a small billing team, PM-JAY claims management is a full-time burden that grows with bed capacity.

Three capabilities now align for the first time:

**Near-Astra reasoning at one-fifth the price.** GPT-6.1 Sol at $2 per million input tokens brings high-quality agentic decision-making within reach of mid-market hospitals. Extracting the right ICD-10 codes and diagnosis narrative from an admission note to populate a pre-auth form is exactly the kind of professional work where this model excels.

**Browser-native portal operation.** Computer use in the Agents API removes the need for custom NHCX integration code. The agent works the portal the same way a billing clerk does. When NHCX adds a new field or changes a form layout, you update the agent's prompt, not a fragile scraping script.

**Structured deployment know-how.** Anthropic's Frontier Academy, with Deloitte, McKinsey, and Accenture among the founding cohort organisations, signals that the consulting ecosystem building health-IT AI systems now has a formal AI-deployment certification track. Partners active in Indian health-system engagements will carry this capability across.

---

## What this does not solve

Computer use is not a complete claims automation solution on its own.

**Clinical review stays human.** The pre-auth form requires ICD codes, clinical severity, and treatment justification. The agent reads from HIS data; a clinician must verify those inputs are correct before submission. The workflow is agent-assisted, not agent-only.

**DPDP Act compliance.** Every NHCX submission carries patient health data. Under India's Digital Personal Data Protection Act 2023, the hospital is the data fiduciary. Any automated agent workflow must log what was submitted, maintain an audit trail, and operate within ABDM's consent framework.

**Portal changes break agents.** NHCX and insurer portals update without notice. A production deployment needs a monitoring layer, and a human oversight loop for the times the agent encounters an unexpected form state.

---

## The Frontier Academy thread

The [Claude Frontier Academy](https://www.anthropic.com/news/claude-frontier-academy) deserves a separate note because of its structure. Anthropic built it on the medical-residency model: multi-day classroom training with Anthropic engineers, covering use-case selection through security review, followed by a 12-week period where the FDE leads a live Claude project at their own organisation, supported by Anthropic staff throughout.

The credential is earned through demonstrated deployment, not a written test. First cohorts run in San Francisco, New York, and London, with partner organisations including Accenture, Bain, Capgemini, Deloitte, McKinsey, Morgan Stanley, and Novo Nordisk. The stated goal is 10,000 certified FDEs by end of 2027.

For Indian health-IT teams, the near-term relevance is structural rather than direct: initial cohorts do not include Indian health systems. But Accenture, Deloitte, and McKinsey are all founding cohort members and are active in Indian health-system engagements. An organisation working with any of them on AI-assisted claims or prior-authorisation workflows can now ask whether an FDE is on the team. That is a new, specific question to ask.

---

## The takeaway

Computer use in the Agents API is not a healthcare-specific announcement. It is a general-purpose capability that lands on a very specific healthcare problem: the portal-first, form-heavy architecture of India's PM-JAY claims pipeline. GPT-6.1 Sol at one-fifth of Astra's price makes the unit economics of per-claim AI assistance clear and positive.

The hospitals that move first will reduce billing-staff overhead per PM-JAY claim and shorten the gap between admission and payment. The technology is in public beta today. The talent infrastructure to deploy it is being built through programmes like the Frontier Academy. The remaining variable is whether Indian health-IT teams treat this as a pilot-eligible workflow in the next quarter.

---

*That is all for Issue 017. Primary sources: [Introducing GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/), [DevDay 2026 recap](https://openai.com/index/devday-2026-recap/), [Claude Frontier Academy](https://www.anthropic.com/news/claude-frontier-academy), [PM-JAY](https://nha.gov.in/PM-JAY). Next edition tomorrow.*
