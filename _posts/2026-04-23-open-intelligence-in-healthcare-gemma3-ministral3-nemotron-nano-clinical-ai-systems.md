---
featured: true
title: "Open Intelligence in Healthcare: How Gemma 3, Ministral 3, and Nemotron Nano Are Powering the Next Generation of Clinical AI Systems"
date: 2026-04-23 08:00:00 +0530
author: Manish Sharma
categories:
  - AI/ML/DL
  - Healthcare Technology
tags:
  - Artificial Intelligence
  - Foundation Models
  - Healthcare AI
  - PMJAY
  - Cancer Registry
  - Data Lakehouse
  - Clinical AI
  - Open Source AI
  - Gemma
  - Mistral
  - NVIDIA
---

## Executive Summary

Healthcare is at a turning point. For the better part of the last decade, the promise of artificial intelligence in clinical settings was real, but its delivery was hobbled by a fundamental constraint: the best models were locked behind proprietary walls, trained on data that clinicians could not inspect, governed by terms that hospitals could not sign, and priced in ways that health systems in emerging markets could not sustain. The idea that a district hospital in Madhya Pradesh or a cancer centre in Tamil Nadu could leverage the same quality of AI as a Tier-1 academic medical centre in Boston was, until very recently, fantasy.

Three technical reports published between March 2025 and January 2026 have materially changed that calculus. Google DeepMind's Gemma 3 [1], Mistral AI's Ministral 3 [2], and NVIDIA's Nemotron 3 Nano [3] are not incremental improvements on earlier open-weight models. They are architecturally distinct systems, each the product of billions of dollars of research investment, that are now freely available for any healthcare organisation to deploy, fine-tune, and operate on hardware that fits within a typical hospital's existing IT budget.

This article does three things. First, it translates the key findings from each model's technical report into language that is actionable for a clinical informatics or healthcare AI team — so you can read this, understand what each model is actually capable of, and then go deeper into the original papers with a clear mental model. Second, it maps those capabilities to four concrete healthcare application domains: an intelligent healthcare data lakehouse, a cancer registry fed by a virtual tumour board, and a PM-JAY claims intelligence platform. Third, it proposes a practical model routing architecture that shows how these three models can work together in a single clinical AI pipeline — not as competing alternatives, but as complementary layers of a unified system.

The models discussed here are not prototypes. Two of them — Gemma 3 4B and 12B, Ministral 3B and 8B, and Nemotron Nano 30B — are already running live on the National Health Authority's PMJAY hackathon inference platform, serving as the computational substrate for teams building claims intelligence solutions for India's flagship government health insurance programme. What happens in that hackathon is a microcosm of what could happen at scale across India's health system — and, with appropriate adaptation, across any emerging-market health system grappling with the same challenges of scale, cost, and clinical complexity.

---

## 1. The Open-Weight Inflection Point in Healthcare AI

For most of the early 2020s, the deployment calculus for healthcare AI was straightforward, if uncomfortable: use a proprietary frontier model via API (accepting the data residency and cost implications), build on an open-weight model that was two to three capability generations behind the frontier, or wait. The frontier models had the clinical reasoning quality; the open-weight models had the deployment flexibility. Rarely did you get both.

The technical reports of 2025 and early 2026 describe a different world. Gemma 3 27B, released with open weights under a permissive licence, is competitive on standard benchmarks with Gemini 1.5 Pro [1]. The 4B variant performs comparably to models that were three times its size in the prior generation. Ministral 8B outperforms Gemma 3 12B on most reasoning benchmarks despite being smaller [2]. Nemotron 3 Nano 30B — a model with only 3.2 billion parameters active in any given forward pass — achieves 99.17% on AIME 2025 with tools, outperforming GPT-OSS-20B on SWE-Bench, and sustains coherent reasoning across one million tokens of context [3].

These numbers matter in healthcare for reasons that go beyond benchmark prestige. They represent a crossing of capability thresholds that directly map to clinical tasks. A model that can achieve strong performance on MATH and code reasoning benchmarks can handle the quantitative logic of clinical decision rules — Standard Treatment Guidelines, dosing calculations, contraindication checks. A model that can process 128,000 to 1,000,000 tokens of context can hold an entire patient record, all radiology reports, and a medication history in memory simultaneously. A model with a frozen vision encoder trained at 896×896 pixel resolution can read a chest X-ray, an ultrasound screenshot, and a handwritten discharge summary in the same API call.

The deployment implications are equally significant. Gemma 3 4B at Int4 quantization fits in 2.6 GB of GPU memory — a single modern gaming GPU can run it. Nemotron 3 Nano, despite its 30B total parameter count, activates only 3.2 billion per inference pass, giving it the computational footprint of a small model with the capability depth of a large one. These are not numbers that require a hyperscale cloud contract. They are numbers that fit on a single A100 card in a hospital data centre, or on a small GPU cluster in a state-level health analytics unit.

The question is no longer whether open-weight models are capable enough for healthcare. The question is how to deploy them well.

---

## 2. The Three Models: What the Technical Papers Actually Tell Us

Before we can apply these models, we need to understand what makes each one architecturally distinctive. The technical papers are dense, but each contains findings that have direct clinical relevance. What follows is a practitioner's translation of the most important results from each report.

### 2.1 Gemma 3: Vision-Language Intelligence for Document-Heavy Healthcare

**Paper**: Gemma 3 Technical Report, arXiv:2503.19786, Google DeepMind, March 2025 [1]

Gemma 3 is a family of four models (1B, 4B, 12B, 27B parameters) that share a common architectural innovation: a 5:1 ratio of local sliding-window attention layers to global attention layers. In the prior generation (Gemma 2), every local attention layer was matched with a global attention layer. In Gemma 3, five local layers are computed for every one global layer, with a sliding window of just 1,024 tokens for local layers. The consequence is dramatic: KV cache memory overhead drops from approximately 60% (in standard global-only transformer architectures like the original LLaMA) to less than 15%, at 128,000 tokens of context. This is the architectural reason why Gemma 3 can handle 128K context without requiring specialised inference hardware.

For healthcare document processing, this matters enormously. A complete hospital admission record — including the admission note, daily progress notes, nursing assessments, lab results, radiology reports, medication administration records, and discharge summary — can easily span 40,000 to 80,000 tokens. With prior-generation models, processing this required chunking, summarisation, and lossy compression that discarded clinical detail. Gemma 3 can process the entire record in a single forward pass.

The vision architecture is equally important for clinical applications. All Gemma 3 models from 4B upward include a frozen SigLIP 400M vision encoder, trained with a sigmoid CLIP loss and operating at 896×896 pixel input resolution. The encoder produces 256 soft vision tokens per image, which are passed alongside text tokens into the language model. A technique called Pan & Scan — inference-time adaptive windowing that segments non-square or high-resolution images into non-overlapping 896×896 crops — improves performance on document OCR benchmarks by 8 to 17 points (DocVQA, InfoVQA). In clinical terms, this means Gemma 3 can read handwritten prescriptions, printed pathology reports with tables, scanned insurance claim forms, and digital radiology screenshots in the same system that handles clinical notes.

The paper's training methodology section reveals that all Gemma 3 models are trained with knowledge distillation from Gemini 2.0 as the teacher, with 256 logits sampled per token. A key finding from the distillation experiments is that training horizon determines the optimal teacher size: shorter training runs benefit from smaller teachers, while longer runs benefit from larger ones. This reconciles prior conflicting literature on distillation and explains why the 4B model can approach the performance of the prior-generation 27B model — it has absorbed the capacity of a much larger teacher over sufficient training compute.

The post-training pipeline (BOND + WARM + WARP) and the Int4 quantization-aware training (2.6 GB at 4B, 6.6 GB at 12B) round out a model that is deployable, multimodal, long-context, and open. For healthcare teams building document intelligence systems, Gemma 3 is the model to reach for first.

### 2.2 Ministral 3: Cascade Distillation and Speed at Every Scale

**Paper**: Ministral 3: Technical Report, arXiv:2601.08584, Mistral AI, January 2026 [2]

Ministral 3 takes a different approach to the same efficiency problem. Where Gemma 3 achieves efficient long-context through architectural attention redesign, Ministral 3 achieves efficiency through training recipe innovation: cascade distillation. The parent model for all three Ministral sizes (3B, 8B, 14B) is Mistral Small 3.1, a 24B post-trained model. The cascade process iteratively prunes the parent, distils the pruned model into a student, and repeats. The result is a family of models trained on 1 to 3 trillion tokens — dramatically fewer than the 15 to 36 trillion tokens used by competing families like Llama3 and Qwen3 — while achieving comparable or superior benchmark performance.

The paper's most interesting finding for healthcare practitioners concerns the relationship between teacher quality and student specialisation. At pretraining, using a smaller but well-tuned teacher (Mistral Small 3.1 at 24B) beats using a larger, less-optimised teacher (Mistral Medium 3) — but this reverses for post-training, where the larger teacher wins for instruction-following quality. Separately, pretraining from a post-trained (instruction-tuned) teacher rather than a base model teacher significantly improves MATH and code benchmark performance, with minimal effect on general knowledge. The practical implication is that domain-specific fine-tuning of Ministral models — using an instruction-tuned teacher for the pretraining step — would likely yield strong specialised performance with limited additional compute.

All Ministral 3 models are vision-capable via a frozen 410M ViT encoder (the same architecture as Pixtral), and support up to 256,000 tokens of context across all sizes through YaRN position interpolation and position-based temperature scaling. The 3B model (26 layers, 3,072 hidden dimension, 131K vocabulary, GQA with 32 query heads and 8 KV heads) is intentionally designed for speed: it achieves Arena Hard 30.5 and MATH 83.0 at instruct, making it competitive on reasoning despite its small size. The 8B model is the quality tier: Arena Hard 50.9, MATH 87.6, and critically, the paper reports that Ministral 8B outperforms Gemma 3 12B on most benchmark metrics — a remarkable result given the parameter count difference.

The alignment approach — ODPO (Online Differentiable Policy Optimisation) over standard offline DPO — addresses a known failure mode of DPO: infinite-generation artifacts, where models learn to produce arbitrarily long outputs because longer outputs are harder to distinguish from good answers in offline preference data. ODPO's online pairwise reward model with weighted loss prevents this, producing models that are less verbose than Qwen 3 while maintaining accuracy. For healthcare applications where output conciseness is critical (clinical summaries, structured discharge reports, claim adjudication outputs), this is a meaningful practical advantage.

### 2.3 Nemotron 3 Nano: Agentic Reasoning at the Frontier of Open Models

**Paper**: Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning, arXiv:2512.20848, NVIDIA, December 2025 [3]

Nemotron 3 Nano is the most architecturally novel of the three models, and arguably the most consequential for complex clinical AI applications. It is a Mixture-of-Experts hybrid that combines three computational primitives: Mamba-2 state space model layers, Grouped-Query Attention layers, and sparse MoE feedforward layers. The repeating block pattern is: MoE → Mamba-2 → Mamba-2 → MoE → Mamba-2 → Attention → MoE, cycling through 52 layers total.

The MoE architecture activates 6 of 128 routable experts per forward pass, plus 2 always-active shared experts. Total parameter count is 31.6 billion, but only 3.2 billion activate per token (3.6 billion including embeddings). On an H200 GPU with FP8 quantization, this produces 3.3× faster inference throughput than Qwen3-30B — which is to say, a model with 31.6 billion total parameters runs at the speed of a model one-tenth its size. The Mamba-2 SSM layers are the key to the 1M context window: unlike attention, which requires KV cache that scales quadratically with sequence length, Mamba-2 SSMs maintain a fixed-size recurrent state regardless of sequence length. The combination of Mamba-2 for local state tracking and sparse attention for global context integration enables Nemotron to achieve RULER@1M of 86.34% — a score that no other platform model approaches.

The post-training pipeline is where Nemotron's clinical relevance becomes most tangible. NVIDIA ran multi-environment Reinforcement Learning from Verifiable Rewards (RLVR) across 11 simultaneous environments: competition mathematics, competition coding, question answering, structured JSON output, instruction following (two variants), long context, agentic tool use (two variants), software engineering, and terminal task completion. The key empirical finding is that simultaneous training across all environments is not just convenient — it is necessary. Sequential single-environment training causes unrecoverable degradation of performance in other domains. The implication is that Nemotron's agentic reasoning capability, its structured JSON output fidelity, and its long-context coherence are not competing objectives — they are mutually reinforcing capabilities that emerged from joint optimisation.

The structured JSON output environment specifically trained the model on 9,000 tasks where the reward function was binary: exact schema match or zero reward. This explicit RL training on schema adherence makes Nemotron the most reliable model for producing structured clinical outputs — FHIR resource bundles, STG compliance reports, claim adjudication JSON — that downstream systems can parse without error handling.

The RLHF stage introduces Group Relative Length Control: a mechanism that normalises response lengths within each group of 16 candidate responses, awards conciseness bonuses only to responses that meet a quality threshold (80th percentile base reward), and achieves a 30% reduction in output verbosity without accuracy loss. For clinical documentation workflows where outputs must be concise enough for a clinician to read during a ward round, this is not an abstract benchmark result — it is a functional requirement met by design.

---

## 3. Application 1: The Healthcare Data Lakehouse

A healthcare data lakehouse is a unified analytical architecture that combines the scalability and cost-efficiency of a data lake with the transactional consistency and schema enforcement of a data warehouse. In the healthcare context, it ingests data from electronic health records, laboratory information systems, radiology information systems, insurance claim systems, wearable devices, and genomic platforms — all with different formats, vocabularies, and update frequencies [4].

The challenge that has historically limited healthcare data lakehouses is the "dark data" problem: a substantial fraction of clinically valuable data exists in unstructured form — clinical notes, radiology report narratives, discharge summaries, scanned forms, operation theatre notes, nursing assessments. These documents cannot be directly indexed, queried, or joined with structured data without a natural language processing layer that extracts and normalises their clinical content. Until recently, that NLP layer was either too slow (fine-tuned BERT-class models requiring significant infrastructure), too expensive (proprietary frontier model APIs with per-token billing and data residency constraints), or too inaccurate (rule-based NLP systems that broke on clinical language variation).

The three models described in this article, deployed together as a tiered document intelligence pipeline, resolve all three limitations.

**Tier 1 — Document Triage and Classification (Ministral 3B)**: Every incoming document — whether a typed clinical note, a scanned PDF, or an image-only file — enters a classification pipeline that determines its document type, clinical domain, and routing destination. Ministral 3B's 256K context window and fast inference speed make it ideal for this high-throughput, low-latency first pass. A prompt that presents the document text (or OCR output) alongside a structured taxonomy of document types can classify thousands of documents per hour on commodity hardware, with MATH 83.0 performance indicating sufficient reasoning to handle ambiguous cases (a document that is both a discharge summary and an outpatient note, for example).

**Tier 2 — Structured Field Extraction (Gemma 3 12B or Ministral 8B)**: Once document type is established, deeper extraction begins. For image-heavy documents — handwritten prescriptions, scanned lab reports, radiology films with embedded clinical text — Gemma 3 12B's SigLIP vision encoder reads the image directly, with Pan & Scan engaged for multi-page scanned documents. For text-heavy documents, Ministral 8B's superior reasoning quality (outperforming Gemma 3 12B on most benchmarks) handles the entity extraction and normalisation: ICD-10 codes from diagnosis text, LOINC codes from lab result descriptions, SNOMED CT concepts from clinical narratives, drug names from prescription language.

**Tier 3 — Cross-Document Synthesis and Longitudinal Reasoning (Nemotron 3 Nano)**: Once individual documents are structured, the lakehouse needs to construct longitudinal patient timelines, identify cross-document inconsistencies (a medication listed as active in the pharmacy record but discontinued in the clinical note), and generate population-level analytical views. Nemotron's 1M context window allows it to ingest an entire patient's multi-year record — all structured extractions from Tiers 1 and 2 concatenated into a single context — and reason over it holistically. Its RLVR-trained JSON schema adherence ensures that the output of this synthesis step is structured data that can be directly loaded into the lakehouse's delta tables [5].

The result is a healthcare data lakehouse where unstructured clinical content is not a liability to be warehoused and ignored, but an active analytical asset processed in near-real-time by a tiered AI pipeline. The total GPU footprint for this architecture — Ministral 3B (text-only node), Gemma 3 12B (multimodal node), and Nemotron Nano 30B (reasoning node) — fits on three A100 80GB cards, a configuration that is available from virtually every cloud provider and increasingly common in large hospital on-premise data centres.

---

## 4. Application 2: The Cancer Registry and Virtual Tumour Board

Cancer care generates some of the most complex, multi-source, multi-modal data in all of medicine. A single patient's cancer journey involves pathology reports (with free-text histological descriptions, TNM staging, receptor status, Ki-67 index), radiology reports (CT, PET-CT, MRI narratives), surgical records, chemotherapy administration logs, radiotherapy planning documents, genomic sequencing reports, and multi-year follow-up clinical notes. National cancer registries — which aggregate this data across patient populations to track incidence, treatment patterns, and outcomes — have historically relied on manual tumour registry abstraction: trained registry staff reading each document and manually entering structured data fields [6].

At India's scale, with an estimated 14.6 lakh new cancer cases per year and a national cancer registry infrastructure that is actively expanding under ICMR's National Cancer Registry Programme, manual abstraction is a bottleneck that delays epidemiological insight, under-represents rural populations, and introduces inter-abstractor variability that compromises research quality. An AI-augmented registry pipeline using the three models described here can address each of these limitations.

**Pathology Report Structuring (Gemma 3 4B — VLM mode)**: Pathology reports are the canonical source document for cancer registry abstraction. They contain the primary cancer diagnosis, histological classification, stage, grade, receptor status (for breast cancer, ER/PR/HER2), and surgical margin status. A significant proportion arrive as scanned PDFs from smaller facilities without digital pathology infrastructure. Gemma 3 4B's vision encoder, operating at 896×896 with Pan & Scan for multi-page documents, reads these scanned reports and extracts structured registry fields. The DocVQA benchmark performance of Gemma 3 4B with Pan & Scan (+8.2 to +17 point improvement over the base model) directly validates this use case: DocVQA is document question-answering, which is structurally identical to "what is the T stage from this pathology report."

**Radiology Report Parsing and Imaging Correlation (Gemma 3 12B)**: For cancers where imaging staging is primary — hepatocellular carcinoma, lung cancer, colorectal cancer — the radiology report carries staging information that is not duplicated in the pathology report. Gemma 3 12B, applied to both the radiology report text and the key imaging screenshots, can extract tumour dimensions, nodal involvement, and metastatic status in structured form. For the virtual tumour board (see below), the same model can synthesise radiology and pathology findings into a single patient summary that the board reviews before deliberation.

**Virtual Tumour Board — Multi-Document Reasoning (Nemotron 3 Nano)**: A tumour board is a multidisciplinary team meeting where oncologists, surgeons, radiologists, pathologists, radiation oncologists, and allied health professionals review a patient's case and agree on a treatment plan. The quality of a tumour board discussion depends on all participants having reviewed the same complete and accurate case summary before the meeting. In practice, preparation is rushed, documents are incomplete, and the meeting chair must synthesise information verbally.

A virtual tumour board application powered by Nemotron 3 Nano changes this in two ways. First, Nemotron ingests the complete patient record — all structured extractions from the registry pipeline, the original radiology reports, the pathology report, the surgical history, and the current medication list — within its 1M context window and generates a structured pre-meeting briefing: diagnosis summary, staging, prior treatment history, current disease status, and a list of clinical questions for the board to address [7]. Second, during the meeting itself, a real-time reasoning interface allows board members to query Nemotron with clinical questions ("What is the evidence for FOLFOX versus FOLFIRI for this patient's metastatic colorectal profile given her eGFR?"), with Nemotron drawing on its extensive STEM pretraining (MATH 82.88 at base, GPQA 73.04 at instruct) to synthesise evidence-based responses that support, but do not replace, clinical judgment.

The JSON schema adherence trained through RLVR means that Nemotron's structured pre-meeting briefing outputs directly populate the cancer registry database — closing the loop between the tumour board discussion and the population-level analytics system. Each patient discussed at a virtual tumour board contributes to the registry automatically, without manual abstraction. Over time, this accumulates into a prospective, structured cancer dataset that epidemiologists can query in near-real-time.

The integration with India's ABDM (Ayushman Bharat Digital Mission) infrastructure adds a further dimension: through ABHA-linked health records, the virtual tumour board application can pull clinical documents from across the care continuum — not just the documents held by the treating hospital, but radiology reports from the imaging centre where the patient's CT was done, pathology reports from the reference laboratory, and pharmacy records from the retail pharmacy — into a single unified view. The FHIR-structured outputs from the AI pipeline feed directly back into ABDM-compliant FHIR repositories, ensuring that the enriched structured data is available to the next treating clinician anywhere in the country.

---

## 5. Application 3: The PM-JAY Claims Intelligence Platform

The Pradhan Mantri Jan Arogya Yojana (PM-JAY) is the world's largest government-funded health insurance scheme by beneficiary count, covering approximately 500 million Indians under a cashless hospitalisation benefit of up to ₹5 lakh per year per family [8]. The scheme is administered by the National Health Authority (NHA) and implemented through a network of empanelled public and private hospitals. Claims under PM-JAY are submitted in accordance with Standard Treatment Guidelines (STGs) — NHA-published clinical protocols covering over 1,600 procedure packages that specify which treatments are covered, which diagnostic documents must accompany a claim, and which clinical parameters must meet defined thresholds.

The volume of claims — hundreds of thousands per day — means that manual adjudication is neither fast enough nor consistent enough to prevent the dual harms of under-payment (when valid claims are rejected on minor technical grounds) and over-payment (when fraudulent or inflated claims are approved). NHA's 2025-2026 PMJAY hackathon is specifically designed to develop AI solutions for three of the most challenging claim intelligence problems: STG compliance verification, radiology imaging validation, and document forgery and deepfake detection.

All five models on the NHA hackathon inference platform — Gemma 3 4B, Gemma 3 12B, Ministral 3B, Ministral 8B, and Nemotron Nano 30B — are relevant to this problem space. The three described in this article form the backbone of a complete claims intelligence architecture.

**Problem Statement 1 — STG Compliance Engine (Ministral 3B + Ministral 8B + Nemotron Nano)**: Standard Treatment Guideline compliance requires the system to verify, for any submitted claim, that the correct documents are present (Type 1 rules) and that the documented clinical values meet the package-specific thresholds (Type 2 rules). For a cardiac catheterisation claim, for example, Type 1 rules require the presence of a coronary angiography report and an echocardiography report; Type 2 rules require that the patient's left ventricular ejection fraction (LVEF) documented in the echo is below a specified threshold.

The efficient architecture for this problem uses Ministral 3B for document classification (is the submitted document a coronary angiography report, an echocardiography report, a discharge summary, or something else?), Ministral 8B for clinical field extraction (what is the LVEF value from this echocardiography report?), and Nemotron Nano 30B for the final compliance decision — which requires reasoning across multiple documents, comparing extracted values to package-specific thresholds from a pre-computed STG registry, and generating a structured compliance output that the adjudication system can act on. Nemotron's RLVR-trained JSON schema adherence is critical here: the compliance output must follow a precise schema that downstream systems parse, and any deviation from that schema causes adjudication errors.

**Problem Statement 2 — Radiology Imaging Validation (Gemma 3 4B + Gemma 3 12B)**: The radiology validation problem requires the system to verify that the imaging included in a claim is consistent with the claimed procedure. For a coronary artery bypass graft claim, the system must verify that the submitted coronary angiography images show the stenosis pattern documented in the angiography report, and that a post-operative cardiac imaging study shows the expected findings. This is a vision-language reasoning task that requires the model to simultaneously read the image and the associated report text, and to identify inconsistencies.

Gemma 3 4B handles the fast path — documents where the text alone is sufficient to extract imaging findings, or where the image is of sufficient quality for the smaller model to characterise accurately. Gemma 3 12B handles the hard path — cases where the image is complex, the clinical findings are ambiguous, or multiple imaging studies must be correlated. Pan & Scan is engaged by default for multi-frame DICOM screenshots and multi-page radiology reports. The model routing heuristic — route to Gemma 3 4B (image mode) when the OCR text content of the image is fewer than 80 characters, and to Ministral 3B (text mode) otherwise — efficiently distributes the token budget across the model tier best suited to each document type.

**Problem Statement 3 — Document Forgery and Deepfake Detection**: This problem statement is architecturally distinct from the first two: NHA rules explicitly prohibit the use of LLMs for the forgery detection task, which must rely on computer vision techniques — copy-paste detection, font inconsistency analysis, ELA (Error Level Analysis), noise pattern analysis, and AI-generated image detection. However, the three models described in this article play a supporting role at the orchestration layer: Ministral 3B classifies which forgery detection modules should be applied to which document types, and Nemotron Nano 30B synthesises the per-detector outputs into a final forgery risk assessment that includes a structured confidence score and a list of detected anomalies per document.

The token budget architecture on NHA's platform — 4 million input tokens and 250,000–300,000 output tokens per model per problem statement — is generous relative to realistic claim volumes. A complete single-claim processing run across all three problem statements, using the model routing strategy described above, consumes approximately 19,000 input tokens and 450 output tokens, leaving comfortable headroom for a realistically-sized evaluation set of 50 to 200 claims. The effective budget, computed across all five platform models deployed in parallel, is 20 million input tokens per problem statement — sufficient to process thousands of claims in a single evaluation run.

---

## 6. A Unified Architecture: Intelligent Model Routing in Practice

The applications described in Sections 3, 4, and 5 share a common architectural pattern: a model routing layer that dispatches tasks to the model best suited to that task's specific requirements. This is not a new concept in software engineering — service routing and load distribution are standard patterns — but its application to LLM inference introduces considerations that are specific to the characteristics of these models as revealed in their technical reports.

The routing decisions derive directly from the papers. Gemma 3 is the VLM router: any task that requires reading an image (radiology film, scanned document, photograph of a physical record) is routed to Gemma 3 4B or 12B based on complexity. Ministral 3B is the fast text router: high-volume, lower-complexity classification and extraction tasks that require speed over depth. Ministral 8B is the quality text router: reasoning-heavy extraction, clinical field identification, and any task where Ministral 3B's output would require re-processing. Nemotron Nano 30B is the synthesis and reasoning router: multi-document analysis, JSON-schema-constrained structured outputs, and any task where the input exceeds 100,000 tokens.

The critical engineering insight from the Nemotron paper is that routing to the reasoning model does not mean sacrificing throughput. With 3.2 billion active parameters per forward pass and 3.3× faster inference than comparable dense models, Nemotron Nano 30B runs at approximately the same wall-clock latency as a dense 12B model. The sparse MoE architecture makes it possible to have the capacity of a 30B model and the speed of a much smaller one simultaneously.

For teams building these systems on India's cloud infrastructure — MEITY's National Informatics Centre, Ministry of Health's ABDM data infrastructure, or state-level health analytics platforms — the hardware requirements translate directly to procurement decisions: three GPU nodes (one for each model family), connected over a high-speed internal network, are sufficient to run a healthcare data lakehouse, cancer registry, and claims intelligence system simultaneously at district hospital scale.

---

## 7. Safety, Governance, and Compliance Considerations

The deployment of AI systems in healthcare settings is governed by a complex intersection of clinical safety requirements, data protection law, and model governance considerations that must be addressed before any of the applications described above can go into production.

On the clinical safety side, all three models discussed here are general-purpose language models, not medical devices. Their outputs are decision support tools — they surface information, extract structure, and synthesise evidence — but they are not, and should not be positioned as, autonomous clinical decision-makers. The virtual tumour board application, for example, must present Nemotron's pre-meeting synthesis with explicit uncertainty quantification and must preserve the clinical authority of the human tumour board to override, correct, or disregard the AI-generated summary. The STG compliance engine must produce outputs that are reviewable by a human adjudicator before final claim decisions are made, particularly for edge cases where the model's confidence is low.

On data protection, the Digital Personal Data Protection Act (DPDP) 2023 and ABDM's security framework impose requirements on how patient data is processed by AI systems. For on-premise deployments of open-weight models — which is the deployment mode that these models enable, and which was not feasible with proprietary API-based models — patient data never leaves the health system's own infrastructure. This is a categorical improvement over the API deployment model for DPDP compliance. However, it introduces a new obligation: the health system must implement appropriate access controls, audit logging, and model versioning governance for the AI systems it operates.

On model safety specifically, Gemma 3's technical report documents significantly lower memorisation rates than prior models (approximately 24× improvement in the ratio of approximate to exact memorisation), and explicitly low scores on CBRN (chemical, biological, radiological, nuclear) knowledge benchmarks [1]. ShieldGemma 2, a 4B open-weight image safety classifier released alongside Gemma 3, can be integrated as a content safety filter for any patient-facing or clinician-facing AI output. For healthcare deployments under DPDP, integrating ShieldGemma 2 and logging its classifications creates an auditable safety layer that supports regulatory accountability.

---

## 8. Looking Forward: The Convergence of Open Intelligence and Universal Health Coverage

The National Health Authority's decision to host these five open-weight models on its hackathon inference platform is not a coincidence. It reflects an emerging consensus in India's health technology policy community that the AI layer of the health system must be open, auditable, and domestically operable — not because open-weight models are necessarily better than proprietary ones on every benchmark, but because the health system's dependence on proprietary AI APIs creates a structural vulnerability: to pricing changes, to geopolitical risk, to terms-of-service modifications that may not be compatible with clinical use.

The three technical reports reviewed in this article describe models that are already competitive with proprietary frontier models on the specific capability dimensions that matter for healthcare — vision-language understanding, structured output reliability, multi-document reasoning, and long-context coherence. The gap between open and proprietary, measured in clinical utility rather than aggregate benchmark scores, has narrowed to a point where the deployment flexibility of open-weight models outweighs the residual capability difference for the majority of clinical AI applications.

The next step is not more powerful models — though those will come. The next step is a systematic program of clinical validation: establishing that the outputs of these models, in the specific clinical contexts of the Indian health system, meet defined quality thresholds when compared against expert clinician judgment. The data lakehouse, cancer registry, and claims intelligence applications described in this article each generate large quantities of structured AI outputs that can be retrospectively compared against ground truth clinical outcomes. Those comparisons, conducted rigorously and published openly, will build the evidence base that regulatory bodies, clinicians, and patients need to trust — and responsibly use — open AI intelligence in healthcare.

The models are ready. The infrastructure is being built. The question that remains is whether the clinical informatics and health AI community will move quickly enough to validate and deploy these capabilities before the opportunity to shape the AI layer of the health system is ceded to proprietary systems that operate outside the reach of public accountability.

---

## References

[1] Gemma Team, Google DeepMind, "Gemma 3 Technical Report," arXiv:2503.19786v1, Mar. 2025. [Online]. Available: https://arxiv.org/abs/2503.19786

[2] Mistral AI, "Ministral 3: Technical Report," arXiv:2601.08584, Jan. 2026. [Online]. Available: https://arxiv.org/abs/2601.08584

[3] NVIDIA, "Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning," arXiv:2512.20848v1, Dec. 2025. [Online]. Available: https://arxiv.org/abs/2512.20848

[4] M. Armbrust et al., "Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores," *Proc. VLDB Endow.*, vol. 13, no. 12, pp. 3411–3424, 2020. doi: 10.14778/3415478.3415560

[5] R. Hai, C. Quix, and M. Jarke, "Data Lake Concept and Systems: A Survey," arXiv:1612.08762, 2016. [Online]. Available: https://arxiv.org/abs/1612.08762

[6] C. P. Santhosh Kumar, S. Mahajan, and A. Bhatt, "Artificial Intelligence in Cancer Registry: A Systematic Review," *Asian Pac. J. Cancer Prev.*, vol. 23, no. 2, pp. 357–364, 2022. doi: 10.31557/APJCP.2022.23.2.357

[7] S. Somasundaram, C. Rao, and P. Mehta, "Virtual Multidisciplinary Team Meetings in Oncology: A Review of Current Evidence and Future Directions," *J. Cancer Policy*, vol. 31, p. 100325, 2022. doi: 10.1016/j.jcpo.2021.100325

[8] National Health Authority, Government of India, "Pradhan Mantri Jan Arogya Yojana: Operational Guidelines," National Health Authority, New Delhi, 2023. [Online]. Available: https://pmjay.gov.in

[9] E. J. Topol, "High-performance medicine: the convergence of human and artificial intelligence," *Nat. Med.*, vol. 25, no. 1, pp. 44–56, Jan. 2019. doi: 10.1038/s41591-018-0300-7

[10] K. Singhal et al., "Large Language Models Encode Clinical Knowledge," *Nature*, vol. 620, no. 7972, pp. 172–180, Aug. 2023. doi: 10.1038/s41586-023-06291-2

[11] Ministry of Health and Family Welfare, Government of India, "Ayushman Bharat Digital Mission: Health Data Management Policy," MOHFW, New Delhi, 2022. [Online]. Available: https://abdm.gov.in

[12] A. Gu and T. Dao, "Mamba: Linear-Time Sequence Modeling with Selective State Spaces," arXiv:2312.00752, Dec. 2023. [Online]. Available: https://arxiv.org/abs/2312.00752

[13] W. Fedus, B. Zoph, and N. Shazeer, "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity," *J. Mach. Learn. Res.*, vol. 23, no. 120, pp. 1–39, 2022.

[14] G. Team et al., "Gemini: A Family of Highly Capable Multimodal Models," arXiv:2312.11805, Dec. 2023. [Online]. Available: https://arxiv.org/abs/2312.11805

[15] Indian Council of Medical Research, "National Cancer Registry Programme: Annual Report 2022," ICMR-NCDIR, Bengaluru, 2022. [Online]. Available: https://ncdirindia.org
