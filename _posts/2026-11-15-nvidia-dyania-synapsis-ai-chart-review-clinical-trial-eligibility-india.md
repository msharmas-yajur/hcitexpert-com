---
title: "A Clinical Reasoning Engine Inside the Hospital Firewall: What NVIDIA's Dyania Health Story Suggests for Chart Review and Trial Matching in India"
date: 2026-11-15 14:36:57 +0530
author: Manish Sharma
description: "The Clinical Frontier, Issue 035. NVIDIA's 13 November post describes Dyania Health's Synapsis AI, a clinical reasoning engine that reads whole patient records on hospital-owned GPU servers, and a Cleveland Clinic study of more than 7,800 valve replacement patients. What this suggests for chart review, trial eligibility and registry work in Indian hospitals."
keywords: "clinical chart review AI, clinical trial eligibility matching, Dyania Health Synapsis AI, NVIDIA NeMo TensorRT-LLM healthcare, on-premise clinical AI India, free text medical records, clinical registry abstraction, DPDP Rules hospitals, Cleveland Clinic aortic valve replacement AI, hospital firewall inference"
image: /assets/images/logo.png
reading_time: "6 min read"
categories:
  - Healthcare Technology
  - AI/ML/DL
tags:
  - Chart Review
  - Clinical Trials
  - On-Premise AI
  - NVIDIA
  - Dyania Health
  - Clinical Reasoning
  - DPDP Act
  - ABDM
mentions:
  - name: "NVIDIA Blog: How AI Is Helping Care Teams Get Patients the Right Care, Sooner"
    description: "NVIDIA's post of 13 November 2026 describing how health systems and startups use AI across healthcare, including Dyania Health's Synapsis AI clinical reasoning engine, which runs on NVIDIA-accelerated computing inside a health system's own firewall, and a Cleveland Clinic study of more than 7,800 aortic valve replacement patients."
    url: "https://blogs.nvidia.com/blog/how-ai-is-helping-care-teams/"
  - name: "PIB: Government notifies DPDP Rules to empower citizens and protect privacy"
    description: "Press Information Bureau release of 14 November 2025 from the Ministry of Electronics and IT on the notification of the Digital Personal Data Protection Rules, 2025, including the 18 month phased compliance timeline."
    url: "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014"
faq:
  - q: "What is Dyania Health's Synapsis AI?"
    a: "According to NVIDIA's 13 November 2026 post, Synapsis AI is a clinical reasoning engine from New Jersey based Dyania Health. It works across the notes, reports and lab results in a patient's record, connects findings that may be years apart, and returns clinical signals that are each traceable to their source in the record. Clinicians review the evidence and make every decision."
  - q: "Does the patient data leave the hospital when Synapsis AI is used?"
    a: "NVIDIA's post says Synapsis AI runs on NVIDIA-accelerated computing inside a health system's own firewall, that the entire health system's records can be processed onsite, and that patient data is never shared and never leaves the hospital. That is NVIDIA's description of the deployment model, so any hospital evaluating a similar tool should confirm it in its own architecture review."
  - q: "What did the Cleveland Clinic study show?"
    a: "NVIDIA reports that Cleveland Clinic used Synapsis AI to support a study of more than 7,800 aortic valve replacement patients between 2005 and 2021. The system reasoned across each patient's record, including echocardiograms added in the years after surgery, to build a predictive model of valve deterioration and reintervention risk at three, five and ten years. NVIDIA says the chart review across the cohort would have taken clinicians years to do by hand."
  - q: "Why does this matter for Indian hospitals?"
    a: "Wherever a hospital's history sits in free text notes, reports and discharge summaries, the same pattern of on-premise, evidence-linked chart reasoning could apply to trial eligibility screening, care-gap closure and registry abstraction. Because India's DPDP Rules were notified in November 2025 with an 18 month phased timeline, keeping that processing inside the hospital boundary is also the simplest design to defend."
---

> **The Clinical Frontier** · 15 November 2026 · Issue 035
> A briefing on how the latest frontier AI models and hardware land in real healthcare workflows, written for India's health-IT community. No hype, just what changed and what to do about it.

**In this issue**

- NVIDIA's 13 November post profiles **Dyania Health's Synapsis AI**, a clinical reasoning engine that reads a patient's whole record and runs **inside the hospital's own firewall**.
- A **Cleveland Clinic** study of more than 7,800 valve replacement patients shows what changes when chart review stops being a manual, years-long task.
- For Indian hospitals, the interesting part is the pattern: **on-premise, evidence-linked reading of free text**, applied to trial screening, care gaps and registries.

## What shipped

NVIDIA's [post of 13 November](https://blogs.nvidia.com/blog/how-ai-is-helping-care-teams/) is a roundup of how health systems and startups are using AI, with the same framing throughout: clinicians stay at the centre, reviewing AI outputs and guiding decisions, while NVIDIA technology provides the compute. Its Dyania Health section is the one worth reading closely.

- **The product.** Dyania, a New Jersey based clinical AI company, built **Synapsis AI**, which NVIDIA describes as a clinical reasoning engine. It works across every note, report and lab result in a patient's record and connects findings that may be years apart, to answer clinical questions the way a specialist reviewing the chart would.
- **The output.** A set of clinical signals, each traceable to its source in the record, that tells care teams which patients need attention and why. NVIDIA is explicit that it is an assistive tool: a clinician must still confirm and act on what it surfaces.
- **The deployment.** NVIDIA says Synapsis AI runs on NVIDIA-accelerated computing inside a health system's own firewall. The post says a health system's entire patient records can be processed onsite, and that patient data is never shared and never leaves the hospital.
- **The stack.** Dyania builds and trains its models with NVIDIA NeMo open libraries, then optimises them with NVIDIA TensorRT and TensorRT-LLM to run faster and more efficiently on the hospital's own GPU servers.

## The evidence: 7,800 patients and a ten year question

NVIDIA reports that Cleveland Clinic used Synapsis AI to support a study of more than 7,800 aortic valve replacement patients between 2005 and 2021. The system reasoned across each patient's record, including every echocardiogram added in the years after surgery, and built a predictive model of **valve deterioration and reintervention risk at three, five and ten years**. By NVIDIA's account, the chart review across the full cohort would have taken clinicians years to complete by hand.

Dr. Lars Svensson, chief of the Heart, Vascular & Thoracic Institute at Cleveland Clinic, is quoted in the post: "Using technology to bring together and analyze information that can help us predict the duration of implanted heart valves is a promising step towards enhanced outcomes and more personalized care for patients."

Two cautions belong next to that. This is a vendor-reported case study in a roundup, not a peer reviewed result, and the post does not give accuracy figures for the predictive model. Treat it as evidence of a workable pattern, not of a validated clinical tool.

NVIDIA also notes where the same approach could go: identifying patients eligible for clinical trials, closing care gaps in cardiology and oncology, and populating clinical registries.

## Why it matters: the answer is usually already in the chart

Much of what a hospital knows about a patient is not in a structured field. It is in physicians' notes, operative reports, imaging and pathology reads and discharge summaries. Questions such as "who meets these eligibility criteria" or "who has missed a follow-up scan" are really chart-reading questions, and today they are answered by people reading charts, slowly, for a few patients at a time.

The Dyania example is a reminder of three design choices that make that task tractable:

- **Read the whole record, not a summary of it.** Findings that matter are often separated by years, which is exactly where a keyword search fails.
- **Every signal links back to its source.** A reviewer can check the evidence in seconds, which is what keeps the clinician, not the model, accountable.
- **The model goes to the data.** As NVIDIA describes it, running on hospital-owned GPU servers means the record never has to travel to be read.

## For Indian hospitals: where this pattern could apply

The following is our reading of the pattern, not a claim about Dyania's availability or fit in India.

1. **Trial eligibility screening.** If your site participates in studies, a first pass that surfaces candidate patients with the supporting passages from their notes could shorten the screening queue. A coordinator still confirms eligibility against the protocol.
2. **Care-gap and follow-up lists.** Chronic and post-procedure follow-up often depends on a result or an instruction buried in a discharge summary. Evidence-linked flags are easier to act on than a bare risk score.
3. **Registry abstraction.** Registry teams spend their time turning free text into coded fields. An assistive reader that proposes values with source passages, for a human to accept or reject, fits that workflow.
4. **Keep the boundary in the design.** India's DPDP Rules were [notified on 14 November 2025](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014) with an 18 month phased compliance timeline. Whatever tool you evaluate, the simplest posture to defend is the one where patient records are read inside your own boundary, and where you can show an auditor exactly what left it, which ideally is nothing.

Before you pilot anything like this, ask four questions: Where does inference run? What is logged, and where? How does a reviewer see the source behind each flag? And who signs off on the output before it changes care?

## The takeaway

The headline in NVIDIA's post is a case study, not a new model, but it points at a useful shift. The valuable clinical AI task for many hospitals is not generating text, it is **reading what the hospital already wrote, carefully and with receipts**, on infrastructure the hospital controls. If your record is mostly free text, that is a pilot worth scoping with a clinician, a data protection lead and your IT team at the same table.

---

*The Clinical Frontier is a daily briefing from [HCITExperts](https://hcitexpert.com/). Read the source: [How AI Is Helping Care Teams Get Patients the Right Care, Sooner](https://blogs.nvidia.com/blog/how-ai-is-helping-care-teams/). More tomorrow.*
