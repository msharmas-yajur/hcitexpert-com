---
title: "Machine Sight: Gemini's Agentic Video, Multimodal Vision, and India's Radiology Backlog"
date: '2026-09-21 19:00:00 +0530'
author: Manish Sharma
description: "The Clinical Frontier, Issue 006. Google shipped agentic video understanding in Gemini on September 1, 2026, and Gemini 3.8 Flash, a multimodal model that reads image, video, and PDF, on September 2. Neither was built for medicine, yet both describe where machine vision is heading for a country with roughly one radiologist per 100,000 people. Here is what the imaging frontier means for India, and where the guardrails sit."
keywords: "medical imaging AI India, Gemini agentic video, Gemini 3.8 Flash multimodal, radiology AI India, radiologist shortage India, teleradiology AI India, AI chest X-ray TB screening India, CAD4TB qXR, DICOM de-identification, CDSCO software as a medical device, PC-PNDT ultrasound AI, DPDP Act imaging data, NTEP AI CAD"
image: /assets/images/logo.png
reading_time: "7 min read"
categories:
  - Healthcare Technology
  - AI/ML/DL
tags:
  - Medical Imaging
  - Radiology
  - Gemini
  - Multimodal AI
  - Agentic Video
  - Teleradiology
  - Tuberculosis Screening
  - CDSCO
  - PC-PNDT
  - DPDP Act
  - India Health IT
mentions:
  - name: "Agentic video understanding in Gemini"
    description: "Announced by Google on September 1, 2026. Pairs the model's reasoning with native video tools to dynamically search, scan, and inspect target video segments across frames, audio, and transcripts, cutting token use by up to 88 percent and improving accuracy by up to 7 percent over fixed-frame processing."
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/"
  - name: "Gemini 3.8 Flash"
    description: "Google's multimodal Flash-tier model announced September 2, 2026. Accepts text, image, video, audio, and PDF input with a one-million-token context window, at an introductory rate of 0.75 dollars per million input tokens through December 31, 2026."
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/"
faq:
  - q: "What is agentic video understanding in Gemini?"
    a: "Announced by Google on September 1, 2026, agentic video understanding lets Gemini scan a video dynamically rather than sampling it at a fixed frame rate. The model pairs its reasoning with native video tools to search, scan, and inspect specific segments across frames, audio, and transcripts, resampling interesting moments at a higher frame rate to inspect subtle artefacts. Google reports it cuts token consumption by up to 88 percent, lowers cost by up to 66 percent, and improves accuracy by up to 7 percent compared with static processing. Google did not market it as a medical product; the relevance to clinical video and imaging is an inference, not a claim by Google."
  - q: "Can a general model like Gemini 3.8 Flash read a medical scan?"
    a: "Gemini 3.8 Flash is multimodal and accepts image, video, and PDF input, so it can describe an image technically. That is not the same as being a cleared diagnostic device. Under India's Medical Device Rules, 2017, software intended to diagnose is a regulated medical device overseen by the CDSCO. A general-purpose model is best treated as a triage aid, a pre-read, or a second reader that flags studies for a radiologist, not as an autonomous diagnostician. Purpose-built, validated tools such as AI computer-aided detection for chest X-ray remain the clinically appropriate path where a diagnostic decision is at stake."
  - q: "How severe is India's radiologist shortage?"
    a: "India has roughly one radiologist per 100,000 people, against a United States ratio closer to one per 10,000. The Radiology and Imaging Association of India puts the active panel at approximately 20,000 to 22,000 radiologists for a population of about 1.4 billion, and most of them practise in Tier 1 metros while the majority of the population lives elsewhere. That mismatch is why teleradiology and AI triage are not conveniences in India but structural necessities for after-hours and rural imaging."
  - q: "What rules govern imaging AI in India?"
    a: "Three layers apply. Diagnostic software is regulated by the CDSCO under the Medical Device Rules, 2017. Ultrasound carries an additional constraint: the PC-PNDT Act regulates prenatal diagnostic imaging and prohibits its use to determine fetal sex, so any AI layered on obstetric ultrasound inherits those obligations. And imaging data is personal data under the DPDP Act, 2023, which matters because DICOM files embed patient identifiers in their metadata. De-identifying studies before they leave the hospital boundary is the architectural move that keeps all three layers manageable at once."
---

> **The Clinical Frontier** · 21 September 2026 · Issue 006
> A daily briefing on how frontier AI models and hardware land in real healthcare workflows, written for India's health-IT community. No hype, just what changed and what to do about it.

**In this issue**

- Google shipped [agentic video understanding in Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) on September 1, 2026, a model that scans video the way a specialist scrubs a study, slowing down on the moments that matter, and [Gemini 3.8 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) on September 2, a multimodal model that reads image, video, and PDF at a low price point.
- Neither was built for medicine. Yet both point at the same clinical bottleneck: India has roughly one radiologist per 100,000 people, and the imaging keeps arriving whether or not there is someone to read it.
- The opportunity is triage and pre-reading at volume. The guardrail is that a general model is not a cleared diagnostic device, and the honest deployment keeps de-identification, validation, and the human read all in the loop.

## What shipped

**[Agentic video understanding](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)** is the more interesting of the two. Instead of chopping a video into fixed one-frame-per-second slices, Gemini now, in Google's words, pairs "the model's core reasoning with native video tools to dynamically search, scan, and inspect target video segments across visual frames, audio, and transcripts." It runs an agentic loop that loads only the relevant part of a file, resamples interesting segments at a higher frame rate to catch subtle artefacts, and can do sub-second moment retrieval, long-form search across multi-hour footage, and action counting. Google reports up to 88 percent lower token use, up to 66 percent lower cost, and up to 7 percent higher accuracy than static processing.

Read that capability list again with a clinician's eye. Resampling a segment at higher frame rate to inspect a subtle artefact is what a sonographer does when something on the screen catches their attention. Searching a long recording for a precise moment is what reviewing an endoscopy or a cath-lab run looks like. Google made no medical claim, and I am not inventing one for them. The point is narrower and sturdier: the generic capability the labs are now shipping maps cleanly onto how imaging is actually read.

**[Gemini 3.8 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)**, a day later, is the delivery vehicle. It is multimodal across text, image, video, audio, and PDF, carries a one-million-token context window, and lists an introductory price of 0.75 dollars per million input tokens through the end of 2026. A model that can hold a full imaging report, prior studies, and the current scan in one context, at that cost, changes the economics of a pre-read.

## Why it matters: the read is the bottleneck, not the scan

India does not lack imaging machines. It lacks people to read what they produce. The [radiologist-to-population ratio sits near one per 100,000](https://medicalbuyer.co.in/indias-radiologist-to-patient-ratio-dismally-low-at-1100000/), roughly a tenth of the United States figure. The Radiology and Imaging Association of India counts an active panel of about 20,000 to 22,000 radiologists, and most of them work in metros while most patients do not live in one. This is why even large tertiary hospitals lean on [teleradiology for nights and weekends](https://www.thelancet.com/journals/lansea/article/PIIS2772-3682(23)00055-0/fulltext), and why the read, not the scan, is where the queue forms.

Machine vision does not fix that by replacing the radiologist. It fixes it by changing what reaches the radiologist and in what order. A multimodal model sitting in front of the worklist can do the unglamorous, high-value work: flag the study that looks urgent so it jumps the queue, draft a structured preliminary report the radiologist edits rather than types, check the current scan against the prior for interval change, and quietly hold back the studies that look normal for a lighter second pass. None of that is a diagnosis. All of it is throughput, and throughput is the thing India is short of.

The proof that narrow, validated imaging AI works at national scale already exists here. The WHO recommended AI computer-aided detection for tuberculosis screening on chest X-ray in 2021, setting a bar of at least 90 percent sensitivity and 70 percent specificity, and India's National TB Elimination Programme has [deployed CAD tools such as CAD4TB and qXR in the field](https://pmc.ncbi.nlm.nih.gov/articles/PMC10703224/), with studies from Indian screening programmes meeting or exceeding the WHO target. The lesson is not that a chatbot can read an X-ray. It is that a purpose-built, validated model, pointed at one question, has already earned a place in the national screening algorithm. The frontier multimodal models widen the surface of what that pattern can cover next.

## The guardrails, stated plainly

Three constraints separate a demo from a deployment, and none of them is optional.

1. **A general model is not a diagnostic device.** Under India's Medical Device Rules, 2017, software intended to diagnose is a regulated medical device overseen by the CDSCO. A frontier model reading a scan is a triage aid, a pre-read, or a second reader. The moment a tool makes a diagnostic claim, it enters a regulatory pathway, and validation on Indian imaging, not a benchmark score, is what clears it.
2. **Ultrasound carries an extra obligation.** The PC-PNDT Act regulates prenatal diagnostic imaging and prohibits its use to determine fetal sex. Any AI layered on obstetric ultrasound inherits that constraint by design, not as an afterthought.
3. **Imaging data is identifiable data.** DICOM files embed patient name, identifiers, and often the referring institution directly in the file metadata. Under the DPDP Act, 2023, that is personal data. Sending raw studies to a cloud model without stripping the identifiers first is a compliance exposure hiding inside a technical convenience. De-identify at the source, so what leaves the hospital boundary carries the pixels and not the patient. That is the same [anonymisation-by-architecture principle](https://yajur.ai/2026/09/16/the-yajur-health-vault-anonymisation-by-architecture.html) that applies to any clinical data leaving the building: solve it in the pipeline, not in a policy document.

## The takeaway

The imaging frontier moved twice in two days, and neither release mentioned medicine. That is the pattern worth internalising. The labs ship general capability, and healthcare inherits it a few months later, provided someone does the unglamorous work of validation, de-identification, and workflow fit in between. For India, where the scanners run faster than the radiologists can read, the near-term prize is not an AI that diagnoses. It is an AI that triages the worklist, drafts the pre-read, and catches the urgent study before it waits a night. Build that on de-identified data, keep the radiologist as the decision-maker, and reserve the diagnostic claim for tools that have earned it. The capability is here early. The discipline is what turns it into care.

---

*The Clinical Frontier is a daily briefing from [HCITExperts](https://hcitexpert.com/). More tomorrow.*
