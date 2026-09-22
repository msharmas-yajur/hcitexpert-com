---
title: "Triage on the Line: GPT-Live-1 Telephony, Gemini 3.5 Transcribe, and India's 104 Health Helpline"
date: '2026-09-22 19:00:00 +0530'
author: Manish Sharma
description: "The Clinical Frontier, Issue 007. OpenAI launched GPT-Live-1 in the API on September 10, 2026, a full-duplex voice model with telephony support at five cents per minute. Google shipped Gemini 3.5 Transcribe in August, covering 85-plus languages with speaker diarisation. India already has the proof-of-concept: the 104 health helpline, which triages callers across multiple states over a regular phone call. Here is what these two releases mean for AI-assisted triage in a country where the phone line is the last mile of healthcare."
keywords: "voice triage AI India, GPT-Live-1 telephony API, Gemini 3.5 Transcribe languages, 104 health helpline India, AI triage India NHM, ASHA workers AI, virtual nursing India, DPDP Act voice recordings healthcare, multilingual health AI India, OpenAI voice API healthcare, NHM 104 helpline triage, India rural healthcare AI"
image: /assets/images/logo.png
reading_time: "6 min read"
categories:
  - Healthcare Technology
  - AI/ML/DL
tags:
  - Voice AI
  - Triage
  - Virtual Nursing
  - GPT-Live-1
  - Gemini Transcribe
  - 104 Helpline
  - ASHA Workers
  - DPDP Act
  - NHM
  - India Health IT
  - Multilingual AI
mentions:
  - name: "GPT-Live-1 in the API"
    description: "OpenAI launched GPT-Live-1 on September 10, 2026, bringing full-duplex voice conversations to the API with telephony support for phone calls. The model can listen and speak simultaneously, handle background noise, and delegate reasoning and tool calls to a backend model such as GPT-6 Astra or a third-party model. Pricing is five cents per minute, billed per second."
    url: "https://openai.com/index/introducing-gpt-live-1-in-the-api/"
  - name: "Gemini 3.5 Transcribe"
    description: "Google's speech-to-text model announced in August 2026, available in the Gemini API. Supports 85-plus languages with automatic language detection, speaker diarisation, code-switching support within sentences, and custom vocabulary of up to 1,000 domain-specific terms."
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/"
  - name: "Anthropic Life Sciences Verification Program"
    description: "Announced September 17, 2026. Gives verified life science teams access to Anthropic's Mythos, Opus, and Sonnet models with safeguards calibrated for biology-related tasks including clinical development and manufacturing, covering use cases currently restricted in generally available models."
    url: "https://www.anthropic.com/news/life-sciences-verification-program"
faq:
  - q: "What is GPT-Live-1 and why does its telephony support matter for healthcare?"
    a: "GPT-Live-1 is a full-duplex voice model that OpenAI released in the API on September 10, 2026. Full-duplex means it can listen and speak at the same time, the way people do on a natural phone call, rather than taking turns. The telephony support matters specifically because it enables developers to deploy voice agents on regular phone calls, not just smartphone apps. In healthcare, and especially in India, millions of people who cannot use an app or access a broadband connection can still receive a phone call. Deploying voice triage on a telephony infrastructure that already exists is a very different proposition from building an app and waiting for adoption."
  - q: "Is AI voice triage a medical diagnosis?"
    a: "No, and the distinction is not a technicality. A triage system classifies urgency (how quickly someone needs to see a clinician) rather than diagnosing a condition (what is wrong and what to do about it). India's existing 104 health helpline already demonstrates this model: it classifies callers into critical, serious, or stable categories and advises them on next steps. AI augmenting that classification is different from replacing the clinician who decides on treatment. Under India's Medical Device Rules 2017, software that makes a diagnostic or therapeutic claim for a specific disease is a regulated medical device and requires CDSCO clearance. Purpose-built, validated triage tools stay on the right side of that line; a general voice model reading symptoms and naming a diagnosis does not."
  - q: "What languages does GPT-Live-1 support for Indian healthcare deployments?"
    a: "OpenAI has stated that GPT-Live-1 is optimised for popular languages in ChatGPT but has not published a comprehensive language list as of the time of writing. Hindi is among the most spoken languages globally, but any health deployment targeting Hindi or other Indic languages should explicitly test language coverage and accuracy before going live. Gemini 3.5 Transcribe, which supports 85-plus languages with automatic detection and code-switching, can serve as the speech-to-text layer in an architecture where GPT-Live-1 handles the voice conversation and a multilingual transcription model handles the recognition layer. Confirming performance on the actual dialect and medical vocabulary of the target population is not optional."
  - q: "How does the DPDP Act 2023 apply to AI voice calls in healthcare?"
    a: "Voice calls that include health information are personal data under the Digital Personal Data Protection Act 2023. If the call is recorded for quality assurance, training, or audit, those recordings need a clear purpose, a legal basis for processing, and appropriate retention and deletion policies. Calls involving sensitive health information warrant additional care. The DPDP Act does not prohibit voice-based healthcare services, but it does require that data collection be deliberate, disclosed, and limited to what is needed. An AI triage system that records and stores conversations without explicit informed consent or a documented processing policy creates a compliance exposure, independent of how well the clinical logic works."
---

> **The Clinical Frontier** · 22 September 2026 · Issue 007
> A daily briefing on how frontier AI models and hardware land in real healthcare workflows, written for India's health-IT community. No hype, just what changed and what to do about it.

**In this issue**

- OpenAI released [GPT-Live-1](https://openai.com/index/introducing-gpt-live-1-in-the-api/) on September 10, 2026: a full-duplex voice model with telephony support at five cents per minute, billed per second, that delegates deeper reasoning to backend models like GPT-6 Astra.
- Google shipped [Gemini 3.5 Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) in August: 85-plus languages, automatic language detection, speaker diarisation, and code-switching within sentences.
- India already has the proof of concept at national scale: the 104 health helpline, which triages callers by phone across multiple states, classifying conditions as critical, serious, or stable.
- The opportunity is augmenting that triage throughput with voice AI. The guardrails are real: language coverage needs explicit testing for Indic dialects, triage is not diagnosis, and every recorded call is personal data under the DPDP Act 2023.

## What shipped

**[GPT-Live-1](https://openai.com/index/introducing-gpt-live-1-in-the-api/)** is OpenAI's first fully general voice model in the API. The important word in that sentence is telephony. Previous voice-in-the-API experiments required app-level integration; GPT-Live-1 explicitly supports deployment of full-duplex voice agents for phone calls. Full-duplex means both parties can speak and listen at the same time, the natural cadence of a phone call rather than the push-to-talk pattern of older voice assistants. The model handles background noise without breaking the conversation and without narrating every step it is taking, which matters enormously in noisy PHC waiting rooms and crowded ASHA camps.

The architecture is designed around delegation. GPT-Live-1 manages the voice interaction: tone, pace, conversational flow. When a question requires deeper reasoning or a tool call, it passes that sub-task to a backend text model, for instance GPT-6 Astra or any third-party model, then picks up the voice conversation again once the answer comes back. The pricing is five cents per minute, billed per second. Backend model usage is billed separately.

**[Gemini 3.5 Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/)** landed in public preview in the Gemini API in August. It is a speech-to-text model that auto-detects 85-plus languages, separates speakers through diarisation, and handles intra-sentence code-switching, the pattern common when a patient describes symptoms in Hindi and then reaches for an English medical term, without any manual configuration. Developers can bias recognition toward up to 1,000 domain-specific terms, covering the clinical vocabulary and drug names that standard consumer speech models miss.

These two releases are complementary. A voice triage architecture can route the speech layer through Gemini 3.5 Transcribe for multilingual recognition, pass the transcript to a reasoning model, then return the response through GPT-Live-1's voice output. Neither release was designed for healthcare; both describe the direction this infrastructure is heading.

## India already has the model: the 104 line

India does not need to invent voice-based health triage. It runs one.

The [104 health helpline](https://nhm.maharashtra.gov.in/en/scheme/health-advice-call-center-toll-free-104/), operated under the National Health Mission, provides non-emergency medical advice over a regular phone call. Callers are classified by urgency (critical, serious, or stable) and advised on whether to seek emergency care, visit a health facility, or manage at home with guidance. The 104 line is active across multiple states including Maharashtra, Assam, Odisha, Telangana, Tamil Nadu, and Rajasthan, among others.

The helpline works because the phone call is the right interface for where most Indians are. It requires no smartphone, no internet connection, no digital literacy. A person in a rural taluka with a two-year-old handset and intermittent network coverage can call 104 as easily as someone with a new flagship phone in Mumbai. The call agent does the language negotiation, the triage logic, and the documentation.

That call agent is also the bottleneck. After-hours coverage is limited by shift staffing. Scale is limited by the number of trained agents, not by demand. Language coverage depends on which languages a particular state helpline has trained its staff for. In states with many tribal or regional dialects, the gap between patient vocabulary and call agent fluency is real.

AI voice triage does not fix that by replacing the agent. It fixes it by changing what the agent handles and when. A voice model working the first level of the interaction, confirming the caller is not in an emergency, gathering symptoms in a structured way, and triaging clearly non-critical calls, frees the human agent for the ambiguous and urgent cases where clinical judgment is irreplaceable. At minimum, an AI-first layer extends effective after-hours coverage without proportionally expanding the staffing bill.

India's [roughly one million ASHA workers](https://nhm.gov.in/index1.php?lang=1&level=1&sublinkid=150&lid=226) form the last mile of the health system in villages and urban slums. ASHA workers already use phones for community health tracking and referral coordination. A voice decision-support layer that helps an ASHA worker assess urgency before referring a patient, running on a regular phone call, fits the infrastructure they already have rather than waiting for one they do not.

## The guardrails, stated plainly

Three constraints shape what is deployable versus what is a demo.

**1. Triage is not diagnosis.** A triage system classifies urgency; it does not diagnose a condition or prescribe a course of treatment. India's 104 helpline already demonstrates what that means in practice: it tells callers whether to go to the emergency room, the clinic, or stay home with advice. That is a different claim from naming a disease and recommending a drug. Under India's Medical Device Rules 2017, software making a diagnostic or therapeutic claim for a specific disease is a regulated medical device requiring CDSCO clearance. A voice tool that says "this sounds urgent, please visit a doctor today" is in a different regulatory position from one that says "you have bacterial pharyngitis and should take amoxicillin." Build for the first; do not slide toward the second.

**2. Language coverage is not guaranteed.** OpenAI states that GPT-Live-1 is optimised for popular languages in ChatGPT, but has not published a comprehensive list of supported languages as of September 2026. Hindi is among the most spoken languages in the world, and coverage is likely, but any health deployment targeting Hindi, Tamil, Telugu, Bengali, Marathi, or other Indic languages should test explicitly for the specific dialect, the clinical vocabulary, and the audio conditions of the target environment before going live. A voice model that mishears "pet dard" as a medication name is worse than no model. Gemini 3.5 Transcribe's 85-plus language coverage and custom vocabulary support make it a better-documented starting point for the recognition layer while GPT-Live-1 manages the conversation.

**3. Every recorded call is personal data.** Voice calls involving health symptoms are sensitive personal data under the [DPDP Act 2023](https://www.meity.gov.in/content/digital-personal-data-protection-act-2023). Recordings made for training, quality assurance, or compliance audit carry a processing purpose and a retention period that must be stated and enforced. Consent for recording, where not already covered by terms of service, should be explicit and audible to the caller. The DPDP Act does not prohibit voice-based health services; it requires that data collection be deliberate, disclosed, and minimal. An AI triage deployment built without a data governance policy is a liability exposure attached to a clinical tool.

## The takeaway

Two voice model releases in five weeks have changed what a phone call can do in a healthcare system. GPT-Live-1 turns the API into a telephony platform: a developer with a SIP trunk, five cents a minute, and a backend reasoning model can build a voice triage agent that answers calls around the clock, in any language the recognition layer supports. Gemini 3.5 Transcribe gives that agent 85-plus languages and speaker separation out of the box.

India already proved the model works at scale. The 104 helpline has been triaging callers by phone for years. The infrastructure is the phone network, which covers more of India than broadband ever will. The bottleneck is human capacity and shift-constrained operating hours, which is exactly what AI-first layers are designed to address.

The discipline is in the details: language coverage tested on actual dialects, triage logic validated against clinical protocols, data governance in place before a call is recorded, and a human clinician at the end of the escalation path when urgency is real. The capability is here early, and the 104 model is the architecture to build on. Phone-first, not app-first. Clinical guardrails from day one. That is how voice AI earns a place in the health system rather than around it.

---

*The Clinical Frontier is a daily briefing from [HCITExperts](https://hcitexpert.com/). More tomorrow.*
