---
title: "Anonymisation by Architecture: A Blueprint for Hospital Data Vaults That Cannot Leak Identity"
date: 2026-09-16 09:00:00 +0530
author: Manish Sharma
description: "A summary of Yajur Healthcare's concept paper on building a hospital health data vault where identity is structurally separated from clinical content, so re-identification is not blocked by a rule but is impossible by construction. Read the full whitepaper and try the interactive sandbox on yajur.ai."
keywords: "health data vault, hospital data anonymisation, de-identification healthcare, DPDP Act 2023 health data, ABDM health data management policy, MIMIC de-identification, SAIL Databank architecture, break-glass re-identification, pseudonymisation vs anonymisation, on-premise LLM healthcare, data sovereignty India, trusted research environment, Yajur Health Vault"
image: /assets/images/logo.png
canonical_url: https://yajur.ai/2026/09/16/the-yajur-health-vault-anonymisation-by-architecture.html
reading_time: "6 min read"
categories:
  - Healthcare Technology
  - Data Privacy
tags:
  - Data Privacy
  - De-identification
  - ABDM
  - DPDP
  - Health Data
  - Data Governance
  - Open Source
  - Clinical AI
  - Data Lakehouse
mentions:
  - name: "The Yajur Health Vault (full concept paper)"
    description: "The full whitepaper on anonymisation by architecture, published on yajur.ai"
    url: "https://yajur.ai/2026/09/16/the-yajur-health-vault-anonymisation-by-architecture.html"
  - name: "MIMIC-IV"
    description: "Intensive-care database from the MIT Laboratory for Computational Physiology"
    url: "https://physionet.org/content/mimiciv/"
  - name: "SAIL Databank"
    description: "Secure Anonymised Information Linkage Databank, Swansea University"
    url: "https://saildatabank.com/"
  - name: "Digital Personal Data Protection Act 2023"
    description: "India's data protection law"
    url: "https://www.meity.gov.in/"
faq:
  - q: "What does anonymisation by architecture mean?"
    a: "It is a design where a patient's identity is structurally separated from their clinical content, so re-identification is not blocked by a policy or a rule. It is impossible by construction. The identifying values are not in the clinical database, are not reachable from it, and cannot be derived from what is there. The full concept paper is on yajur.ai."
  - q: "How is this different from access control or removing names?"
    a: "Access control still keeps identity reachable to anyone who gets past the control, and removing names leaves indirect identifiers and reversible tokens behind. A vault splits identity from clinical data into physically separate stores with no join key, so even a full breach of the clinical store yields no identities."
  - q: "Is this approach compliant with India's DPDP Act and ABDM?"
    a: "The architecture is designed to align with the Digital Personal Data Protection Act 2023, ABDM's Health Data Management Policy, and international benchmarks such as HIPAA Safe Harbor and Expert Determination. Governance, not the algorithm alone, is the control. The full paper covers the legal analysis in detail."
---

> **This is a summary.** Yajur Healthcare has published the full concept paper, **[The Yajur Health Vault: Anonymisation by Architecture](https://yajur.ai/2026/09/16/the-yajur-health-vault-anonymisation-by-architecture.html)**, on yajur.ai, along with an interactive, fully client-side [sandbox](https://yajur.ai/sandbox/health-vault-anonymiser.html) that runs the whole pipeline in your browser on synthetic patients. This post distils the core idea; **[read the full whitepaper on yajur.ai](https://yajur.ai/2026/09/16/the-yajur-health-vault-anonymisation-by-architecture.html)** for the architecture, code, and legal analysis.

## The problem is not storage. It is permission.

You can build a hospital data lakehouse for the price of a mid-range car, with open-source tools and no licensing fees. The architecture works, and hospitals have built it. And then they stop.

They stop because the moment the lakehouse contains real patient records, a different set of questions arrives, and they are not engineering questions. Who is allowed to run a query? Can the analytics team see names? Can the billing vendor? If we want to try an AI model on discharge summaries, does that mean uploading two hundred thousand patients' clinical narratives to a company in another jurisdiction? These questions rarely have technical answers in most hospitals. They have organisational answers, which is to say they have none that survive contact with a serious auditor or a breach.

## The core idea, in one sentence

The full paper describes the layer that has to come next, and the idea behind it is a single sentence:

**A vault is not a place where the secret is kept. It is an architecture in which the secret is not present.**

The clinical data your analysts, dashboards, and models touch does not contain identity, not because a policy forbids looking, but because the identifying values are not in that database, are not reachable from it, and cannot be derived from what is. Re-identification remains possible for the few people whose job requires it, through a deliberate, authenticated, dual-authorised, time-boxed, and permanently audited path. For everyone else it is not restricted. It is absent.

This is deliberately not a new idea. Two systems have been doing versions of it for over a decade and have published how: **[MIMIC](https://physionet.org/content/mimiciv/)**, the intensive-care database from MIT, and the **[SAIL Databank](https://saildatabank.com/)** at Swansea University, which links health and social-care records for the population of Wales. Between them they have supported thousands of studies with no re-identification incident.

## What the design actually does

The [full whitepaper](https://yajur.ai/2026/09/16/the-yajur-health-vault-anonymisation-by-architecture.html) walks through the architecture in detail. The load-bearing decisions, in brief:

- **The split.** Identity and clinical content live in physically separate stores with no join path. A full breach of the clinical store yields no identities.
- **Random identifiers, never hashed.** A hash of a short, structured value like a hospital MRN is reversible by brute force in seconds. A random surrogate from a look-up table has no mathematical relationship to the original, so there is nothing to reverse.
- **No egress, made structural.** Inference runs locally or on-premise. There is no network path by which clinical data can leave the boundary to reach an external model or API. The claim is enforced by architecture, not by a policy document.
- **Break-glass re-identification.** When a clinician genuinely needs to re-identify a record, a governed, two-factor, fully logged process against the separately secured identity vault makes it possible, deliberate, and auditable, rather than routine.

## Why it is defensible

Governance, not the algorithm, is the control. The design is built to hold up under India's **Digital Personal Data Protection Act 2023**, **ABDM's Health Data Management Policy**, and international benchmarks such as HIPAA Safe Harbor and Expert Determination, the EU's 2025 anonymisation judgment, and the UK's direction. The paper is candid about what the approach does not do and what it costs, which is the section worth reading first.

## Read the full paper and try it yourself

This post is only a summary. For the complete architecture, the schema-level design, the code, the legal analysis, and the honest limitations:

**➡️ [Read the full whitepaper: The Yajur Health Vault, Anonymisation by Architecture](https://yajur.ai/2026/09/16/the-yajur-health-vault-anonymisation-by-architecture.html)**

**➡️ [Try the interactive sandbox](https://yajur.ai/sandbox/health-vault-anonymiser.html):** watch a synthetic patient record get anonymised, try to break it, then step through an authorised re-identification, all with real cryptography running in your browser.

*Both are published by [Yajur Healthcare](https://yajur.ai/), the medical data infrastructure company.*
