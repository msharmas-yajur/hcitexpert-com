---
title: "Anthropic's 2026 Usage Policy: The Human Oversight and Disclosure Rules That Now Apply to Clinical AI in India"
date: 2026-10-15 19:00:00 +0530
author: Manish Sharma
description: "The Clinical Frontier, Issue 028. Anthropic's updated Usage Policy, announced October 8 and effective November 12, 2026, explicitly covers uses that affect someone's health in its high-risk requirements. Qualified human review, mandatory AI disclosure to patients, and hardware safety controls are now Anthropic API terms. Indian health-IT vendors have 28 days to add these mechanisms."
keywords: "Anthropic usage policy 2026 India healthcare, clinical AI governance India, human oversight clinical AI India, AI patient disclosure DPDP India, CDSCO AI medical device India 2026, NHA PM-JAY AI compliance India, clinical AI regulation India 2026, AI high risk healthcare India"
image: /assets/images/logo.png
reading_time: "6 min read"
categories:
  - Healthcare Technology
  - AI/ML/DL
tags:
  - Anthropic
  - Claude
  - Clinical AI Governance
  - AI Policy
  - Human Oversight
  - DPDP Act
  - India Healthcare
  - NHA
  - PM-JAY
  - ABDM
mentions:
  - name: "Anthropic 2026 Usage Policy Update"
    description: "Anthropic's October 8, 2026 update to its Usage Policy, effective November 12, 2026. Rewrites the High-Risk Use Case Requirements section to cover uses affecting health, legal rights, finances, livelihood, or essential services, and adds hardware safety requirements for AI controlling physical equipment."
    url: "https://www.anthropic.com/news/2026-usage-policy-update"
  - name: "Anthropic Singapore Office Opening and MOU"
    description: "Anthropic opened its fifth Asia-Pacific office in Singapore on October 14, 2026, and signed an MOU with the Singapore Ministry of Digital Development and Information covering AI safety, model evaluation, skills development, and responsible AI adoption in public and private sectors."
    url: "https://www.anthropic.com/news/singapore-office-opening"
faq:
  - q: "What does Anthropic's 2026 Usage Policy require for healthcare AI deployments?"
    a: "The updated policy, effective November 12, 2026, covers any use that can affect someone's health. For such applications, the operator must ensure a qualified human can review and change the AI output before it affects the individual, and must notify the affected person that AI was used. Applications where Claude controls physical equipment that could cause injury must also have operator override capability and a safe state that the equipment holds if Claude disconnects."
  - q: "Who is the operator under Anthropic's policy and who carries the obligation?"
    a: "Under Anthropic's policy, the operator is the company or developer who builds a product on the Claude API. If an Indian health-IT vendor integrates Claude into a clinical decision support tool, diagnostic assistant, or patient communication system, that vendor is the operator and carries the obligation to implement human review and AI disclosure before its product reaches patients."
  - q: "How does Anthropic's AI disclosure requirement relate to India's DPDP Act?"
    a: "India's Digital Personal Data Protection Act (August 2023) classifies health data as sensitive personal data, requiring explicit consent and transparency in automated processing. Anthropic's obligation to notify affected individuals that AI was used in a health-affecting decision directly aligns with this transparency requirement. Satisfying the Anthropic policy notice also moves a vendor toward DPDP Act compliance on automated health-data processing."
  - q: "Does the human oversight requirement apply to Indian hospitals using Claude through a third-party product?"
    a: "The obligation rests with the operator, which is the vendor who built the product using the Claude API. Indian hospitals using a vendor product do not directly carry Anthropic's policy obligations, but they should verify with their vendors that human review and AI disclosure are in place. As DPDP Act enforcement matures, Indian hospitals may face direct obligations under Indian law regardless of which AI vendor their software uses."
---

> **The Clinical Frontier** · 15 October 2026 · Issue 028
> Anthropic's updated Usage Policy names health among the categories where a qualified human reviewer is now a terms-of-service requirement, not a best practice.

**In this issue**

- [Anthropic's 2026 Usage Policy](https://www.anthropic.com/news/2026-usage-policy-update), announced October 8 and effective November 12, explicitly covers "uses that can affect someone's health" in its rewritten High-Risk Use Case Requirements section.
- Three clinical AI requirements apply: a qualified human reviewer before output reaches the patient, mandatory AI disclosure to the affected individual, and hardware safety controls for AI-integrated physical equipment.
- India's DPDP Act transparency obligations and the country's emerging medical software regulatory landscape point in the same direction, creating a converging compliance floor.
- Indian health-IT vendors deploying Claude in clinical workflows have 28 days from today to audit their architecture and add the required mechanisms.

## The signal

On October 8, 2026, Anthropic published its [2026 Usage Policy update](https://www.anthropic.com/news/2026-usage-policy-update). The policy takes effect November 12. Most of the headline changes are about elections and influence operations, but two sections matter most for health-IT.

**The High-Risk Use Case Requirements section was rewritten.** It now specifies which applications it covers. The policy names "uses that can affect someone's health, legal rights, finances, livelihood, or access to essential services." For any such application, two requirements apply unconditionally:

- A qualified human must be able to review Claude's output and change it before it affects the individual.
- The affected individual must be told that AI was used.

**A new hardware safety section** was added. Where Claude is connected to physical equipment that takes autonomous actions and could cause injury, an additional two requirements apply:

- A qualified operator must be able to observe the equipment and stop it at any time.
- The equipment must hold a safe state if Claude loses connection.

These are not guidance or best practices. They are Anthropic API terms of service, enforceable through Anthropic's operator monitoring and audit processes.

## How it maps to clinical workflows

"Uses that can affect someone's health" covers a wide range of deployments that are already live or in pilot across Indian health systems:

**Clinical decision support and diagnostic assistance.** A tool that recommends a diagnosis, suggests a drug protocol, or flags a lab result as abnormal is affecting the patient's health. The human review requirement means a clinician must be able to see and override the AI output before it enters the clinical record or influences a care decision.

**Patient-facing communication tools.** A discharge summary generator, a post-visit care instruction bot, or a medication reminder system that uses AI to personalize the message is delivering health-affecting content. The AI disclosure requirement means the patient must know AI produced that content, whether through an in-app notice or a verbal disclosure from the clinician.

**Triage and prioritisation systems.** An AI tool that scores patient urgency for a helpline, scores a PM-JAY pre-authorisation, or ranks a referral queue affects health outcomes by changing who gets care first. This falls squarely under the human review requirement.

**AI-integrated clinical hardware.** Vendors who have integrated Claude or a Claude-based model into AI-guided infusion pump controllers, robotic surgical assistance systems, or AI-driven imaging platforms now have an explicit safe-state and override requirement in their API terms. "Safe state if Claude is disconnected" means the device must default to a known-safe configuration if the AI connection drops, not to its last AI-commanded state.

## The India-specific compliance landscape

Three frameworks are now pointing in the same direction for Indian health-IT vendors.

**Anthropic's Usage Policy (effective November 12, 2026).** Applies to every Indian vendor or hospital IT team that deploys Claude through the Anthropic API. The vendor is the operator and carries the obligation. This is not optional and does not depend on Indian law.

**India's Digital Personal Data Protection Act (August 2023).** India's DPDP Act classifies health data as sensitive personal data requiring explicit consent. It embeds transparency in automated data processing as a core principle. The Anthropic AI disclosure requirement directly overlaps with this: notifying a patient that AI was used in their health-affecting decision is both an Anthropic contractual obligation and a step toward DPDP Act compliance on automated health-data processing.

**India's medical device software regulatory landscape.** India's drug and medical device regulator, CDSCO, operates under the Medical Devices Rules, 2017, and has been developing software-as-medical-device guidance covering AI-enabled software, quality management systems, and post-market surveillance obligations. Internationally, regulators including the US FDA and the EU MDR require AI medical devices to document their algorithm change plans and demonstrate human oversight in their quality management systems. CDSCO's emerging framework is moving in the same direction. Indian vendors building AI diagnostic tools should be preparing their technical documentation to demonstrate human oversight, regardless of which AI API they use.

**NHA PM-JAY AI pilots.** The National Health Authority has been piloting AI tools in the PM-JAY claims and pre-authorisation workflow. Any Claude-based component in a PM-JAY adjudication chain, where AI output affects whether a claim is approved, denied, or pended, is directly covered by Anthropic's high-risk requirements: it affects a patient's "access to essential services." A qualified human reviewer step and a patient-visible AI notice are now required under the vendor's API contract.

## What Indian vendors should do in the next 28 days

The November 12 deadline is 28 days from today. For vendors already in production with Claude in clinical settings, the steps are concrete.

**Audit your workflows.** Map every point where Claude output enters a health-affecting decision. For each one, ask: does a qualified human review that output and can they change it before it reaches the patient or record? If not, that is the gap to close first.

**Add the AI disclosure.** Build a patient-visible notice into every clinical UI. One sentence is the minimum: "AI was used in preparing this information." Ensure the clinician knows to make a verbal disclosure when AI influenced a recommendation. Add it to the medical record as a structured field in your FHIR implementation.

**For AI-integrated hardware.** Document the override procedure. Test the safe-state mechanism on a disconnected Claude session. Confirm that a clinician at the bedside can physically halt the device without needing the AI to cooperate.

**Document the compliance.** Anthropic enforces through operator monitoring. India's DPDP enforcement framework, when fully operational, will look for documented processes. Build an internal compliance record now.

## The APAC governance signal

On October 14, six days after the policy update was published, Anthropic [opened its Singapore office and signed an MOU with the Singapore government](https://www.anthropic.com/news/singapore-office-opening). The MOU covers cooperation on AI safety, security, and model evaluation: technical exchanges with Singapore's AI safety and assurance bodies on evaluation frameworks, testing standards, and incident response.

Singapore is the second country after the US where Anthropic has a formal government-level safety partnership. The Indian government, through MEITY and the National Health Authority, should be in parallel dialogue with frontier AI vendors on healthcare-specific safety evaluation standards. India's ABDM stack is deploying AI in millions of patient records. Baking human oversight and AI disclosure into the vendor contracts for those deployments is the same requirement that Anthropic is now codifying in its API terms.

## The takeaway

Anthropic's November 12 policy effective date is both a compliance deadline and a design checkpoint. The "qualified human in the loop" requirement is not a bureaucratic overhead. It is the minimum viable safeguard for any AI that affects a patient's health, and it is now an API contract obligation for every vendor building on Claude.

Indian health-IT vendors who act on this in the next 28 days will be ahead of the Indian regulatory curve, not behind it. Those who do not will find themselves correcting their architecture under time pressure when DPDP enforcement tightens or a hospital customer asks for a compliance attestation.

The floor has been set. Build above it.

---

*The Clinical Frontier is a daily briefing from [HCITExperts](https://hcitexpert.com/) for India's health-IT community. Primary sources: [Anthropic 2026 Usage Policy Update](https://www.anthropic.com/news/2026-usage-policy-update) (Anthropic, 8 October 2026); [Anthropic Singapore Office Opening and MOU](https://www.anthropic.com/news/singapore-office-opening) (Anthropic, 14 October 2026). More tomorrow.*
