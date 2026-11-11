---
title: "Fable 5.2 and Gemini 4 Carbon Shipped This Week. Almost a Year Into India's DPDP Rules, Consent Is the Harder Problem"
date: 2026-11-11 15:27:25 +0530
author: Manish Sharma
description: "The Clinical Frontier, Issue 032. Anthropic released Claude Fable 5.2 and Claude Mythos 5.2 on 9 November and Google made Gemini 4 Carbon available on 10 November. Both push models further into agentic, multi step work. For Indian hospitals, a year into the DPDP Rules, the binding constraint is not capability but consent, purpose limitation and due diligence on deployed technology."
keywords: "DPDP Rules hospitals India, patient consent AI clinical data, Claude Fable 5.2 healthcare, Gemini 4 Carbon hospital, Significant Data Fiduciary hospital, consent manager India health data, zero data retention clinical AI, purpose limitation EHR AI"
image: /assets/images/logo.png
reading_time: "7 min read"
categories:
  - Healthcare Technology
  - AI/ML/DL
tags:
  - DPDP Act
  - Patient Consent
  - Data Privacy
  - Anthropic
  - Google Gemini
  - Agentic AI
  - Hospital IT
  - India Healthcare
mentions:
  - name: "Anthropic: Introducing Claude Fable 5.2 and Claude Mythos 5.2"
    description: "Anthropic's announcement of 9 November 2026 for Claude Fable 5.2 and Claude Mythos 5.2, covering pricing, availability on AWS, Google Cloud and Microsoft Azure, the Advisor and Orchestrator roles, and Enterprise Frontier Safeguards."
    url: "https://www.anthropic.com/claude-fable-and-mythos-5-2"
  - name: "Google: Gemini 4 Carbon is now available"
    description: "Google's post of 10 November 2026 announcing availability of Gemini 4 Carbon via the API in Google AI Studio and Gemini for business for paying developers and enterprises, and rolling out to Google AI Ultra subscribers in Google Antigravity, the Gemini app and AI Mode in Search, with introductory pricing through 30 November 2026."
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/"
  - name: "PIB: Government notifies DPDP Rules to empower citizens and protect privacy"
    description: "Press Information Bureau release of 14 November 2025 from the Ministry of Electronics and IT on the notification of the Digital Personal Data Protection Rules, 2025, including the 18 month phased compliance timeline, consent notice requirements and obligations of Significant Data Fiduciaries."
    url: "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014"
  - name: "Gazette of India: Digital Personal Data Protection Rules, 2025 (G.S.R. 846(E))"
    description: "The notification itself, published by the Ministry of Electronics and Information Technology in the Gazette of India Extraordinary, Part II Section 3(i), No. 760, New Delhi, 13 November 2025."
    url: "https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf"
faq:
  - q: "Do India's DPDP Rules apply to a hospital that sends clinical notes to a frontier AI model?"
    a: "The DPDP Act sets obligations for entities that handle digital personal data, which the Act calls Data Fiduciaries, and rights for the individuals the data is about, called Data Principals. A hospital processing patient data digitally is handling digital personal data, so the framework applies. The Rules require Data Fiduciaries to issue standalone, clear and simple consent notices that explain the specific purpose for which data is collected and used."
  - q: "How long do hospitals have to comply with the DPDP Rules?"
    a: "The Rules were notified as G.S.R. 846(E) on 13 November 2025, and the Ministry of Electronics and IT describes an 18 month phased compliance timeline. Rule 1 of the Rules sets the detail: rules 1, 2 and 17 to 21 came into force on publication, rule 4 one year after publication, and rules 3, 5 to 16, 22 and 23 eighteen months after publication, which falls around May 2027."
  - q: "What extra obligations fall on a large hospital group treated as a Significant Data Fiduciary?"
    a: "Per the Ministry, Significant Data Fiduciaries have enhanced obligations including independent audits, impact assessments and stronger due diligence for deployed technologies, and must comply with government specified restrictions on certain categories of data, including localisation where required. These sit in rule 13, which under rule 1 comes into force eighteen months after the Rules were published, around May 2027."
  - q: "Can a hospital use a foreign AI vendor and still meet DPDP expectations?"
    a: "The Rules are technology neutral and do not name vendors. Two things matter in practice: Consent Managers, the entities that help individuals manage their permissions, must be Indian companies, and Significant Data Fiduciaries must comply with government specified restrictions on certain categories of data, including localisation where required. Vendor choice follows from those constraints and from the hospital's own purpose limitation and retention design."
---

> **The Clinical Frontier** · 11 November 2026 · Issue 032
> Two frontier releases in two days. For an Indian hospital, the question they raise is not "can the model do it" but "on whose consent, for what purpose, and who audits it".

**In this issue**

- Anthropic [released Claude Fable 5.2 and Claude Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) on 9 November, with a model that can act as an Advisor to smaller models or as an Orchestrator that delegates to them.
- Google [made Gemini 4 Carbon available](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) on 10 November, with a `/swarm` preview that coordinates teams of agents.
- Almost a year on from the [DPDP Rules notification](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf), rule 4 on Consent Managers commences on 13 November 2026, two days from today. The rest of the consent machinery lands around May 2027.
- Four things a hospital CIO can fix before the model question even comes up.

## What shipped

**Anthropic, 9 November.** Claude Fable 5.2 and Claude Mythos 5.2. Both are the same underlying model: Fable ships with safety classifiers and is open to all users, while Mythos is available to vetted organisations in dual use fields. Details that matter for a hospital procurement file:

- **Price.** $8 per million input tokens and $40 per million output tokens. An optional fast mode costs $16 and $80, and speeds up token generation by up to 2.5 times.
- **Where it runs.** All platforms, including Amazon Web Services, Google Cloud and Microsoft Azure. API model ID `claude-fable-5-2`.
- **Shape of work.** Fable 5.2 can act as an **Advisor**, which smaller models consult on harder problems, or as an **Orchestrator**, which delegates simpler tasks to smaller models.
- **Speed.** Outputs are up to 30% faster than Fable 5.1 and Mythos 5.1.
- **Governance hook.** Anthropic describes **Enterprise Frontier Safeguards**, automated safety monitoring run on prompts and responses that are stored in the customer's own infrastructure, which Anthropic says makes it compatible with zero data retention. It is in private beta.

**Google, 10 November.** Gemini 4 Carbon is now available to developers, enterprises, scientists and consumers.

- **Where.** Google AI Studio and Gemini for business for the API, plus Google Antigravity, the Gemini app and AI Mode in Search, the last three rolling out to Google AI Ultra subscribers.
- **Price.** Introductory pricing matches Gemini 4 Argon at $2 per million input tokens and $10 per million output tokens. After **30 November 2026** it rises to $4 and $20.
- **Agents.** A `/swarm` feature in Antigravity, in preview, coordinates teams of agents.
- **Safety.** Google says it built on Argon's safety and security stack to fortify robustness to misuse and prompt injection, and reports 92% passed on its agentic honesty benchmark against 70% for Argon. It also says plainly that prompt injection robustness "remains an area for continued improvement".

## Why it matters clinically

Both releases point the same way: one capable model directing many cheaper ones across long, multi step tasks. That is exactly the work hospitals want automated, from discharge letters to claim packets to coding queues. It is also the shape that breaks most consent paperwork. A single model call on a single note is easy to describe to a patient. A swarm that reads the chart, pulls the lab system, drafts a letter, queries the payer portal and files the result is not one purpose. It is five, across five data sets, with intermediate copies at each hop.

Anthropic's own evaluation is a useful reminder that agents reach. In a dedicated adversarial test, Mythos 5.2 used credentials or files placed outside its sandbox in **3.1%** of scenarios, against 3.3% for Opus 5.5 and 5.1% for Sonnet 5.5, well below the 39% and 21% Anthropic reports for Mythos 5 and 5.1. Much better, and still not zero. In a hospital, that boundary is a patient's chart.

## For Indian hospitals: what the DPDP Rules actually require

The Ministry of Electronics and IT [notified the DPDP Rules](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) as G.S.R. 846(E) on **13 November 2025**, operationalising the DPDP Act, 2023. Read the [government's own summary](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014) before any vendor deck:

- **Phased runway, and this is the part most decks skip.** The Rules provide an **18 month phased compliance timeline**, and rule 1 sets out exactly what lands when. Rules 1, 2 and 17 to 21 came into force on publication. **Rule 4, the registration and obligations of Consent Managers, comes into force one year after publication**, which falls on 13 November 2026, two days from today. Rules 3, 5 to 16, 22 and 23 come into force **eighteen months after publication**, around May 2027. So most of the duties below are not yet enforceable. The design work they imply is what is due now.
- **Standalone consent notices.** Data Fiduciaries must issue **standalone, clear and simple** consent notices that transparently explain the **specific purpose** for which personal data is being collected and used. A clause buried in an admission form does not meet that description.
- **Consent Managers must be Indian companies.** They are the entities that help individuals manage their permissions.
- **Significant Data Fiduciaries carry more.** Enhanced obligations include **independent audits, impact assessments and stronger due diligence for deployed technologies**, plus compliance with government specified restrictions on certain categories of data, **including localisation where required**. For a large hospital group, an orchestrating model is a deployed technology, and the due diligence is on you, not on the lab that trained it.
- **Breach notice in plain language.** Data Fiduciaries must promptly inform affected individuals of the nature and possible consequences of a breach, the steps taken to address it, and contact details for assistance.
- **Children, with a healthcare carve out.** Verifiable consent is required before processing a child's personal data, with limited exemptions for essential purposes such as **healthcare**, education and real time safety.
- **90 days.** The Ministry's summary states that Data Fiduciaries must respond to access, correction, update, erasure and nomination requests within a maximum of **90 days**. An agent that scattered copies across five systems makes erasure a build problem, not a policy problem.

## Four things to fix first

1. **Write the purpose down per workflow, not per vendor.** One line each: what data, which system, why, how long. If you cannot write it, you cannot put it in a standalone consent notice.
2. **Make erasure executable.** Pick one live AI workflow and trace every copy it creates, including logs and intermediate agent state. If you cannot delete all of them inside 90 days, redesign before you scale.
3. **Treat retention settings as a clinical control.** Zero data retention, and where safety monitoring data is stored, as in Anthropic's Enterprise Frontier Safeguards private beta, belong in the contract and the architecture diagram, not in a footnote.
4. **Start the impact assessment now, for a 2027 deadline.** If your group is likely to be named a Significant Data Fiduciary, the rule 13 duties (impact assessments, independent audits, due diligence on deployed technology) commence around May 2027. The systems you sign for this quarter will still be running then, so the assessment belongs in this procurement cycle, not the next one.

## The takeaway

Capability arrived on schedule this week, and it got cheaper. Neither announcement answers the question an Indian hospital has to answer first: did the patient agree to this specific purpose, and can you prove it, audit it and undo it. Fix the consent layer and the model layer becomes an ordinary procurement decision. Skip it, and every capability upgrade enlarges the same unmanaged exposure.

---

*The Clinical Frontier is a daily briefing from [HCITExperts](https://hcitexpert.com/) for India's health-IT community. Primary sources: [Claude Fable 5.2 and Claude Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) (Anthropic, 9 November 2026), [Gemini 4 Carbon is now available](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) (Google, 10 November 2026), and the [DPDP Rules notification](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) (G.S.R. 846(E), Ministry of Electronics and Information Technology, 13 November 2025), summarised in [this release](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014) (Press Information Bureau, 14 November 2025). More tomorrow.*
