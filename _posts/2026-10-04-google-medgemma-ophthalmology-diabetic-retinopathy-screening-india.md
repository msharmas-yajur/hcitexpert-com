---
title: "MedGemma 1.5 and Diabetic Retinopathy Screening: A Path to District-Level Eye Care for India"
date: 2026-10-04 19:00:00 +0530
author: Manish Sharma
description: "The Clinical Frontier, Issue 018. Google's open MedGemma 1.5 model interprets retinal fundus images and can be fine-tuned to detect diabetic retinopathy on a smartphone. With more than 90 million adults with diabetes in India and about 1 in 5 showing some degree of DR, an AI-assisted district screening program is now technically and financially feasible."
keywords: "diabetic retinopathy screening India, MedGemma 1.5, Google medical AI, ophthalmology AI India, MedASR, retinal fundus AI, ABDM eye care, diabetes India AI screening, Visilant, DPDP Act healthcare AI"
image: /assets/images/logo.png
reading_time: "7 min read"
categories:
  - Healthcare Technology
  - AI/ML/DL
tags:
  - MedGemma
  - Ophthalmology
  - Diabetic Retinopathy
  - Google
  - Medical Imaging
  - India Healthcare
  - Screening
  - ABDM
  - DPDP
  - Visilant
mentions:
  - name: "MedGemma 1.5"
    description: "Google's open vision-language foundation model for medical imaging, supporting ophthalmology, radiology, and histopathology, released January 2026"
    url: "https://developers.google.com/health-ai-developer-foundations/medgemma/model-card"
  - name: "MedASR"
    description: "Google's speech-to-text model trained on medical language for accurate clinical dictation, released alongside MedGemma 1.5"
    url: "https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/"
  - name: "Visilant"
    description: "Startup that fine-tuned MedGemma 1.5 4B on 200,000 eye images to build a smartphone-based eye care screening system for India"
    url: "https://developers.google.com/health-ai-developer-foundations/showcase/visilant"
faq:
  - q: "What is MedGemma 1.5 and can Indian hospitals use it?"
    a: "MedGemma 1.5 is Google's open collection of medical vision-language foundation models, released January 2026, available on Google Cloud Vertex AI and HuggingFace for research and commercial use. The 4B multimodal version can be fine-tuned on a hospital's own de-identified retinal dataset without sending patient data to an external server, making it compatible with India's DPDP Act 2023 data-residency requirements."
  - q: "Can MedGemma detect diabetic retinopathy?"
    a: "MedGemma 1.5 is designed and trained for ophthalmology image interpretation, including diabetic retinopathy detection, as one of its key image classification applications. Production accuracy depends on the fine-tuning dataset and clinical grading protocol, but the foundation model pretraining significantly reduces the labelled data needed compared to training from scratch."
  - q: "Why does diabetic retinopathy screening matter so urgently for India?"
    a: "India has more than 90 million adults with diabetes, the second-largest diabetic population globally after China (IDF Diabetes Atlas). Approximately 1 in 5 has some degree of DR, and 1 in 10 has the vision-threatening form requiring urgent treatment. India's ophthalmology workforce cannot deliver annual fundus screening at that scale without AI assistance."
  - q: "What does MedASR add to a DR screening workflow?"
    a: "MedASR transcribes medical speech more accurately than general-purpose models, enabling a screener or doctor to dictate a grading note or referral decision immediately after reviewing the fundus image. This eliminates manual typing at the point of screening and lets the encounter be logged to an ABDM-linked health record in real time."
---

> **The Clinical Frontier** · 4 October 2026 · Issue 018
> How frontier AI and open models land in real clinical workflows, for India's health-IT community.

**In this issue**

- Google's **MedGemma 1.5** (released January 2026) is an open medical vision-language model that supports ophthalmology, CT, MRI, and histopathology, available commercially on Vertex AI.
- A startup called **Visilant** has already fine-tuned it on 200,000 eye images to build a smartphone screening system for eye care access in India.
- For India's more than 90 million adults with diabetes, about 1 in 5 carrying some degree of diabetic retinopathy, this stack is the practical foundation for district-level screening at a cost the public health system can actually reach.

## The signal

Google released **[MedGemma 1.5](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card)** on 13 January 2026 as an update to its open collection of medical vision-language foundation models. The 4B multimodal version expanded support for three-dimensional imaging (CT and MRI volumes), whole-slide histopathology images, longitudinal chest X-ray comparisons, and ophthalmology, training on an extended collection of retinal fundus images. The model is available for research and commercial use on [Google Cloud Vertex AI](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/medgemma) and HuggingFace (google/medgemma-1.5-4b-it).

Alongside it, Google released **[MedASR](https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/)**, a speech-to-text model trained specifically for medical language. On Google's internal benchmarks, MedASR produces significantly fewer transcription errors than a general-purpose speech recognition model on medical dictation, where a wrong drug name or dosage carries clinical weight.

Both models are described in the **[MedGemma 1.5 blog post](https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/)** from Google Research.

## One India example already shipping

[**Visilant**](https://developers.google.com/health-ai-developer-foundations/showcase/visilant), a startup focused on expanding eye care access in India, fine-tuned MedGemma 1.5 4B on a specialised dataset of 200,000 eye images and domain-specific knowledge. The result is a smartphone-based screening system that can detect conditions affecting visual health, expanding eye care access across India.

Visilant's work is documented in Google's own [Health AI Developer Foundations showcase](https://developers.google.com/health-ai-developer-foundations/showcase/visilant). It is not a research paper. It is a working product built on an open Google model, already oriented toward India's access gap.

## How it actually works

**MedGemma 1.5** is a collection of three model variants: 4B multimodal, 27B text-only, and 27B multimodal. All multimodal versions use a SigLIP image encoder trained on de-identified medical data. For ophthalmology, the model is trained for image classification tasks including diabetic retinopathy detection.

A team building a DR screening app does not train from zero. They:
1. Start from MedGemma 1.5 4B multimodal weights, which already encode retinal anatomy from the expanded ophthalmology training dataset.
2. Fine-tune on a locally held, de-identified dataset of graded fundus images, with significantly less data than building a model from scratch.
3. Deploy the fine-tuned model on a local server or edge device, with no dependency on an external API.

**MedASR** runs separately as a speech model, accepting medical dictation and returning accurate transcripts for clinical notes, referral letters, and encounter records.

## Why India needs this, now

India has more than **90 million adults living with diabetes**, the second-largest diabetic population globally after China (IDF Diabetes Atlas). The International Diabetes Federation estimates that approximately **1 in 5 people with diabetes in India has some degree of diabetic retinopathy**, and **1 in 10 has the vision-threatening form** that requires laser photocoagulation or intravitreal injection to prevent blindness.

That is a population requiring annual fundus screening. The clinical standard is one screening encounter per year for every diabetic. India's ophthalmology workforce, concentrated in tier-one cities and medical colleges, cannot reach that volume in rural districts and peri-urban primary health centres without AI-assisted grading.

Today, many DR screening camps work like this: images are captured, sent to a grader in a city, and results returned days later. The patient who needed an urgent referral is long gone, back to their village, and the delay costs them their vision. An on-device AI model that grades the image at the moment of capture collapses that latency to zero.

## The DPDP and data-residency fit

Under India's **Digital Personal Data Protection Act 2023**, clinical images are personal data. Sending a fundus image to an external cloud API for grading is an act of data transfer that requires a valid legal basis, consent in a prescribed form, and potentially a data processing agreement with the cloud provider. On-device or on-premise inference sidesteps all of that: the image never leaves the health facility.

MedGemma's open weights mean the fine-tuned model can run entirely inside the screening device or a local server at the primary health centre, with zero data egress. This is not just a nice property. For NHM-funded screening programs and state health departments, it is the difference between a legally simple deployment and a programme that needs a lawyer before it can start.

## An ABDM-linked screening workflow

A practical district-level AI-assisted DR screening camp:

1. **Capture.** An ophthalmic assistant attaches a smartphone fundus adaptor and photographs both fundus images.
2. **Instant grade.** The on-device fine-tuned MedGemma model grades DR severity at the point of capture: no DR, mild, moderate, severe, or proliferative.
3. **Dictated note.** MedASR transcribes the screener's spoken summary directly into the patient encounter record.
4. **Referral routing.** Mild grades receive a printed recall slip for next year. Severe or proliferative grades trigger an immediate referral to the nearest vitreoretinal service, logged in the health record.
5. **Registry linkage.** All encounters, grades, and referrals are written to the patient's ABHA-linked health record, building a longitudinal DR registry for district health planning and NHA monitoring.

No cloud call. No data leaving the district. No waiting for a grader in a city.

## The takeaway

MedGemma 1.5 is not a finished product. It is an open foundation model with a clear primary source from Google and a verified India deployment example from Visilant. What it means for public health in India:

- The **model pretraining is already done** and given away. The hard compute and data cost has been paid by Google.
- **Fine-tuning on local data is feasible** for a district hospital network or NIN programme, with significantly less labelled data than training a model from scratch.
- **Deployment behind the firewall is the architecture**, not a constraint. DPDP compliance is built in.
- **MedASR reduces workflow friction** at the point of screening, which is usually the bottleneck in camp-based settings.

The screening gap in India is real and large. The model infrastructure to close it now exists, is free to use, and has already been deployed by an India-focused startup. The remaining work is building the fine-tuning datasets, the integration with ABDM health records, and the camp logistics to reach the 1 in 5 diabetics who do not yet know they have retinopathy.

---

*The Clinical Frontier is a daily briefing from [HCITExperts](https://hcitexpert.com/) for India's health-IT community. Primary sources: [MedGemma 1.5 model card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card), [MedGemma 1.5 and MedASR announcement](https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/), [Visilant India showcase](https://developers.google.com/health-ai-developer-foundations/showcase/visilant), [IDF Diabetes Atlas 2024](https://diabetesatlas.org/). More tomorrow.*
