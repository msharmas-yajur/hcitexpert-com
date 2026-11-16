---
title: "Reading the Scan, Not Just the Text: Google's MKA Benchmark and NVIDIA's OpenShell, and What They Could Mean for Digitising Paper Medical Records in India"
date: 2026-11-16 18:24:13 +0530
author: Manish Sharma
description: "The Clinical Frontier, Issue 036. Google DeepMind's 10 November MKA benchmark tests agents on visually complex files, where Gemini 4 Carbon ranks second on quality in Google's report. NVIDIA's 10 November contribution of OpenShell to the CNCF adds an open runtime for governing agents. What this suggests for turning scanned and paper medical records into reviewed, source-linked data in Indian hospitals, and why neither announcement is a clinical result."
keywords: "scanned medical records AI, paper records digitisation India, multimodal AI agents healthcare, Multimodal Knowledge Agent benchmark, MKA benchmark Google DeepMind, Gemini 4 Carbon, NVIDIA OpenShell CNCF, AI agent governance hospital, FHIR DiagnosticReport presentedForm, FHIR Provenance, DocumentReference scanned report, DPDP Rules hospitals, legacy medical records, lab report PDF extraction, handwritten prescription AI"
image: /assets/images/logo.png
reading_time: "8 min read"
categories:
  - Healthcare Technology
  - AI/ML/DL
tags:
  - Medical Records
  - Multimodal AI
  - Document AI
  - Gemini
  - NVIDIA
  - AI Agents
  - AI Governance
  - FHIR
  - DPDP Act
  - Digitisation
mentions:
  - name: "Google: Introducing the Multimodal Knowledge Agent benchmark"
    description: "Google DeepMind's post of 10 November 2026, written with Artificial Analysis, introducing MKA, a 200-task benchmark of visually complex professional files across 10 verticals and 83 occupations, and reporting that Gemini 4 Carbon ranked second on quality among the models tested at about one sixth of the top model's average cost."
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/"
  - name: "Hugging Face: google/multimodal-knowledge-agent"
    description: "The public dataset card for MKA with 10 showcase tasks, their verticals and domains, and the task file structure."
    url: "https://huggingface.co/datasets/google/multimodal-knowledge-agent"
  - name: "Artificial Analysis: Multimodal Knowledge Agent (MKA) evaluation"
    description: "Artificial Analysis's page for its implementation of the MKA benchmark."
    url: "https://artificialanalysis.ai/evaluations/mka"
  - name: "NVIDIA Blog: NVIDIA Expands Open Source Commitment With OpenShell Contribution and New AI Infrastructure"
    description: "NVIDIA's post of 10 November 2026 on contributing OpenShell, an open source runtime for securing and governing autonomous agents, to the Cloud Native Computing Foundation, and contributing to the Google-led Agent Substrate project."
    url: "https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/"
  - name: "PIB: Government notifies DPDP Rules to empower citizens and protect privacy"
    description: "Press Information Bureau release of 14 November 2025 from the Ministry of Electronics and IT on the notification of the Digital Personal Data Protection Rules, 2025, including the 18 month phased compliance timeline and the rights of Data Principals."
    url: "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014"
  - name: "HL7 FHIR: DiagnosticReport"
    description: "HL7 FHIR resource for a set of discrete results and their context, with a presentedForm element that holds the entire report as issued."
    url: "https://hl7.org/fhir/diagnosticreport.html"
  - name: "HL7 FHIR: Provenance"
    description: "HL7 FHIR resource that tracks the activity that created, revised, deleted or signed a version of a resource, and the entities and agents involved."
    url: "https://hl7.org/fhir/provenance.html"
  - name: "HL7 FHIR: DocumentReference"
    description: "HL7 FHIR resource used to index a document, clinical note or other binary object to make it available to a healthcare system."
    url: "https://hl7.org/fhir/documentreference.html"
faq:
  - q: "What is Google's MKA benchmark?"
    a: "Per Google DeepMind's 10 November 2026 post, MKA (Multimodal Knowledge Agent) is a benchmark built with Artificial Analysis to evaluate how agents reason across visually complex files to solve real-world knowledge work tasks. It has a 200-task evaluation set made with domain experts across 10 verticals and 83 occupations. Each task is a multi-step project that Google says takes a seasoned professional three to eight hours."
  - q: "Does MKA test medical record reading?"
    a: "Not on the evidence of the public material. The ten showcase tasks on Hugging Face are labelled with verticals such as logistics, construction, engineering, science, business, finance, education, law and government, and software and data. Artificial Analysis describes the benchmark as covering project files such as architectural drawings, engineering schematics and clinical scans. The 200-task evaluation set is private, so the public tasks are the only ones outsiders can inspect. A hospital should test any model on its own scanned records."
  - q: "What did Google report for Gemini 4 Carbon on MKA?"
    a: "Google's post says Gemini 4 Carbon ranks second in quality among the models tested and completes tasks at 6x lower cost on average than the top-scoring model. These are Google's reported results from a benchmark run by Artificial Analysis, not a clinical evaluation."
  - q: "What is NVIDIA OpenShell?"
    a: "NVIDIA describes OpenShell as an open source runtime for securing and governing autonomous agents. NVIDIA's 10 November 2026 post says it applies deterministic controls to agent activity so teams can enforce policies as agents use tools, access inference services and execute workloads, and that NVIDIA is contributing it to the Cloud Native Computing Foundation as a Sandbox project. The post does not describe a healthcare use."
  - q: "Can AI safely digitise paper medical records on its own?"
    a: "Nothing in these announcements says so. A careful design keeps the original scan, stores each extracted value with a link to where it was read, and has a person confirm values that could change care, such as doses, units and decimal points. In FHIR terms a DiagnosticReport can hold the entire report as issued in presentedForm alongside discrete results, and a Provenance resource can record who or what produced a value."
  - q: "Which Indian rules matter when a hospital digitises old records with AI?"
    a: "According to the Press Information Bureau, India's DPDP Rules were notified in November 2025 with an 18 month phased compliance timeline. They require standalone, clear and simple consent notices that explain the specific purpose of use, and reinforce rights to access, correct, update or erase personal data, with a maximum of 90 days to respond. A hospital should take advice on how those apply to its own legacy records."
---

> **The Clinical Frontier** · 16 November 2026 · Issue 036
> A briefing on how the latest frontier AI models and hardware land in real healthcare workflows, written for India's health-IT community. No hype, just what changed and what to do about it.

**In this issue**

- On 10 November Google DeepMind introduced **MKA**, a benchmark of agents working through **visually complex files**, where Google reports **Gemini 4 Carbon** ranking second on quality.
- The same day NVIDIA said it is contributing **OpenShell**, an open runtime for **governing autonomous agents**, to the CNCF.
- Neither is a clinical result. Together they point at a very practical Indian problem: **decades of scanned and paper records** that have to be read as images, not just as text.
- We sketch a pattern that keeps the original scan, links every extracted value to its source, and puts a person in front of anything that could change care.

## What shipped

**MKA, a benchmark for visual work.** Google's [post of 10 November](https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/) introduces the Multimodal Knowledge Agent benchmark, built with Artificial Analysis. Its premise is that most knowledge work benchmarks can be solved with text alone, while everyday professional work is often visual.

- **The tasks.** A 200-task evaluation set made with domain experts across 10 verticals and 83 occupations. Google says each task is a multi-step project that takes a seasoned professional three to eight hours.
- **The grading.** Each task pairs a prompt and a bundle of multimodal files with an expert-written rubric of roughly 70 yes/no checks, weighted 75% on factual accuracy and 25% on visual design. An agentic autorater built on a non-Google model grades the deliverables, and Google says domain experts agreed with it 96% of the time.
- **The fairness setup.** Every model runs in the same open-source agent harness, Stirrup, with the same tools, sandbox and turn budget. Artificial Analysis keeps the 200 tasks private and Google released [10 public tasks](https://huggingface.co/datasets/google/multimodal-knowledge-agent) on Hugging Face.
- **The result Google highlights.** Models differed sharply in effort, using between 30 and 130 turns on average per task. Gemini 4 Carbon ranks second in quality among the models tested and completes tasks at 6x lower cost on average than the top-scoring model. These are Google's reported results.

**OpenShell, a seatbelt for agents.** NVIDIA's [post of 10 November](https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/), published around KubeCon, says it is contributing NVIDIA OpenShell, an open source runtime for securing and governing autonomous agents, to the Cloud Native Computing Foundation as a Sandbox project.

- **What it does.** NVIDIA says OpenShell applies deterministic controls to agent activity, so teams can enforce policies as agents use tools, access inference services and execute workloads, and connect their own compute, inference providers, credential storage and monitoring tools.
- **The companion project.** NVIDIA is also contributing to Agent Substrate, a Google-led open source framework for operating long-running agent workloads on Kubernetes, and says NVIDIA and Google are collaborating on an integration of the two.
- **The scale claim.** NVIDIA says hundreds of organisations have used OpenShell. The post describes no healthcare use.

## Why it matters: records are pictures

For a hospital with decades of paper, the oldest history may not be a database row at all. It may be a lab report printed with a layout, a stamped discharge summary, a handwritten prescription, a film jacket. Reading those means looking at the page: which number sits under which column, what a struck-out line means, where the unit is.

MKA matters here only as a signal about what is being measured. Google's pitch is that agents should be tested on files where the visual content carries the answer. That is the same property a scanned report has.

Be careful about what MKA is not. The ten public showcase tasks on Hugging Face are labelled with verticals such as logistics, construction, engineering, science, business, finance, education, law and government, and software and data, and none is labelled healthcare. [Artificial Analysis](https://artificialanalysis.ai/evaluations/mka) describes the benchmark as covering project files such as architectural drawings, engineering schematics and clinical scans, but the 200-task set is private, so nobody outside can check what the medical tasks look like. A benchmark score is not evidence that a model reads Indian lab reports correctly.

## For Indian hospitals: a pattern for scanned records

The following is our design proposal, not a product that either vendor describes.

1. **Keep the original.** Never replace the scan with extracted text. In FHIR, a [DiagnosticReport](https://hl7.org/fhir/diagnosticreport.html) has a presentedForm element for the entire report as issued, next to discrete results, and a [DocumentReference](https://hl7.org/fhir/documentreference.html) can index a document so it is available to a healthcare system. Which fits depends on your system's interface.
2. **Extract with receipts.** Each value the agent proposes (a haemoglobin result, a dose) should carry the page and the region it came from, so a reviewer sees the evidence next to the value. A [Provenance](https://hl7.org/fhir/provenance.html) resource is how FHIR tracks the activity that created or signed a version of a resource and the agents involved.
3. **Score risk, not just accuracy.** A benchmark averages many checks. In a record, a wrong decimal point or unit is not an average. Require a person to confirm values that could change a decision, and sample the rest.
4. **Fence the agent.** An agent that opens thousands of scans needs limits: which folders it can read, which tools it can call, which network it can reach, which inference endpoint it can use. That is the kind of policy control NVIDIA says OpenShell enforces, and a hospital could ask any agent platform the same question, whether open source or not. If you run the agent on your own cluster, ask how its policies are written, logged and reviewed.
5. **Test on your own paper.** Build a small, de-identified sample of your own scans, covering the worst ones: faded thermal prints, skewed phone photos, mixed English and local-language handwriting. Measure accuracy on that set before any pilot, and again after any model change.

## The Indian rulebook, briefly

India's DPDP Rules were [notified in November 2025](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014), and the Press Information Bureau describes an 18 month phased compliance timeline. Three points from that release bear on a digitisation project.

- **Consent notices.** Data Fiduciaries must issue standalone, clear and simple consent notices that explain the specific purpose of use. Using old records for a new purpose such as AI extraction is a question for your data protection lead.
- **Erase and correct.** Data Principals have rights to access, correct, update or erase their personal data, with a maximum of 90 days to respond. If extracted values live in several places, you need to be able to find and change them all. Provenance links help with that.
- **Breach notification.** Affected individuals must be told promptly, in plain language. A large pile of newly searchable scans is a bigger target than a filing room.

This is a summary of a press release, not legal advice.

## The takeaway

Neither announcement is about medicine. One is a benchmark that tries to measure whether agents can really look at the page. The other is an open way to put limits around what an agent may do. A hospital with decades of paper has a use for both ideas, and a reason to be sceptical of both until it has tested them on its own records. Start with a small, de-identified sample, keep the scan, link every value to its source, and let a clinician or a trained reviewer own the final entry.

---

*The Clinical Frontier is a daily briefing from [HCITExperts](https://hcitexpert.com/). Read the sources: [Google's MKA post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/) and [NVIDIA's OpenShell post](https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/). More tomorrow.*
