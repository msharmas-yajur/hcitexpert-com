---
title: "#FHIR Important Concepts, Terms and Definitions by Manish Sharma, @msharmas"
date: 2020-05-15 09:25:00 +0000
author: Manish Sharma
excerpt: The purpose of this article is to get the reader to understand the difference between the earlier versions of HL7 interoperability standards and then present the important concepts that will help you 
original_url: https://hcitexpert.com/2020/05/fhir-important-concepts-terms-and-definitions-by-manish-sharma.html/
categories:
  - INTEROPERABILITY
tags:
  - "#NCII"
  - Featured
  - FHIR
---

<!-- wp:image {"align":"center","id":5318,"sizeSlug":"full"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://hcitexpert.com/wp-content/uploads/2020/03/Blogs-by-Manish.png" alt="" class="wp-image-5318"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>FHIR is the latest interoperability standard based on a RESTful API architecture published by <a rel="noreferrer noopener" aria-label="HL7 (opens in a new tab)" href="https://www.hl7.org/" target="_blank">HL7</a>. HL7 has been working for over 25 years in publishing standards for Healthcare data interoperability. The move from the earlier HL7's 2.x standards evolved to the Development of the RIM v3 and then to FHIR, has now allowed a paradigm shift to leverage web standards. The purpose of this article is to get the reader to understand the difference between the earlier versions of HL7 interoperability standards and then present the important concepts that will help you to understand FHIR concepts, terms and definitions. </p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading {"level":3} -->
<h3>How is data exchange different using web APIs and FHIR compared to traditional HL7 interfaces? (<a rel="noreferrer noopener" href="https://healthstandards.com/blog/2017/07/11/will-fhir-apis-change-interop-views/" target="_blank">Ref1</a>)</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Dave Shaver, “<strong><em>The interoperability standards we have today are focused on exchanging transactions at certain points of the care lifecycle</em></strong>. In HL7 version 2 that’s focused on patient care, including myriad activities such as administrative tasks, admission, discharge, orders, or results availability. Clinical administrative data is being moved at a certain point in time during the lifecycle of the data. <strong><em>This means it’s difficult to ask questions about that data, except when it has reached that exact point in its life cycle</em></strong>. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>FHIR</strong>, on the other hand, <strong><em>For the first time is going to be a standard  that will allow applications to query the source of truth for data when they need it, not just when it reaches a specific point in its lifecycle</em></strong>. HL7 v2 and CDA documents rely on a push-model of data exchange. <strong><em>FHIR, on the other hand, is more of a pull-model</em></strong>.”</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Before we get into the details of FHIR, we need to understand what is <strong>RESTful API Architecture</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>REST</strong> full form is <strong>REpresentational State Transfer</strong> and <strong>API</strong> stands for <strong>Application Program Interface</strong>. The term representational state transfer was introduced and defined in 2000 by Roy Fielding in his doctoral dissertation (<a rel="noreferrer noopener" href="https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm" target="_blank">ref2</a>). <em><strong>REST is a software architectural style that defines the set of rules and constraints to be used for creating web services between applications, to allow requesting systems to access and manipulate web resources by using a uniform and predefined set of rules.</strong></em> Interaction in REST based systems happen through Internet’s Hypertext Transfer Protocol (HTTP). Web services which follow the REST architectural style are known as RESTful web services.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":5140,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://hcitexpert.com/wp-content/uploads/2020/03/1_tmvBCo4fCH-ms7X8tsOPQg.jpeg" alt="" class="wp-image-5140"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>FHIR</strong> stands for, <strong>Fast Healthcare Interoperability Resources</strong>. In the early days of the development of the FHIR standard, </p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>it<em> was called <strong>Resources for Health in 2011</strong> by Grahame Grieve. </em>A Reading of the <a rel="noreferrer noopener" href="http://www.healthintersections.com.au/?p=502" target="_blank">FHIR Genesis blog by Grahame Grieve</a>, is a must to understand the how the transition from HL7 2.x to FHIR happened and most importantly, why. He also highlights the move from RIM v3 to Resources for Health (RfH as it was called then).</li><li><em><strong>In Feb 2014 FHIR</strong> was released by HL7 as a "Draft Standard for Trial Use" (DSTU), Release 1, version DSTU 1 (v0.0.82). </em></li><li><em><strong>In December 2014</strong>, a broad cross-section of stakeholders committed to the Argonaut Project, in the US. </em></li><li><em>FHIR Release 3 was published <strong>in March 2017</strong>, as the first STU (Standards for Trial Use) release. </em></li><li><em>FHIR Release 4.0.1 was published </em><strong><em>on October 30, </em>2019</strong> (<a rel="noreferrer noopener" aria-label="Wiki (opens in a new tab)" href="https://en.wikipedia.org/wiki/Fast_Healthcare_Interoperability_Resources" target="_blank">Wiki</a>)</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>In a change from the earlier event driven model of Interoperability, which relied on exchange of messages during patient registration, admission, ordering, and other similar events, FHIR solutions are built primarily from a set of two modular components called "<strong>Resources</strong>" &amp; <strong>"APIs</strong>". (<a rel="noreferrer noopener" href="https://www.hl7.org/fhir/summary.html" target="_blank">ref3</a>)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Resources</strong>: A resource is an entity that: (source: <a rel="noreferrer noopener" href="https://www.hl7.org/fhir/summary.html" target="_blank">ref3</a>)</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>has <strong><em>a known identity (a URL)</em></strong> by which it can be addressed</li><li>identifies itself as <strong><em>one of the types of resource</em></strong> defined in this specification</li><li>contains a<strong><em> set of structured data</em></strong> items as described by the definition of the resource type</li><li>has an <strong><em>identified version</em></strong> that changes if the contents of the resource change</li><li>Resource instances are represented as either&nbsp;<a href="https://www.hl7.org/fhir/xml.html">XML</a>,&nbsp;<a href="https://www.hl7.org/fhir/json.html">JSON</a>&nbsp;or&nbsp;<a href="https://www.hl7.org/fhir/rdf.html">RDF</a>&nbsp;and <strong><em>there are currently 145 different</em></strong>&nbsp;<a href="https://www.hl7.org/fhir/resourcelist.html">resource types defined</a>&nbsp;in the FHIR specification.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>APIs – a collection of well-defined interfaces</strong> (<a rel="noreferrer noopener" href="https://www.hl7.org/fhir/summary.html" target="_blank">ref3</a>) for interoperating between two applications. Although not required, the FHIR specification targets RESTful interfaces for API implementation</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If one were to view the healthcare data in its entirety, we will be able to understand that there's a need to share healthcare data by the way of a more manageable sub-domain or smaller chunks of data, at the same time ensuring we are able to maintain the integrity and consistency in the way the resources interact with each other and while maintaining the context between these pieces of information. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And based on this concept, there are projects live today that are DOMAIN driven, argonaut for clinical data, CARIN for consumer directed approach, DaVinci for payors, BlueButton for observational reports, etc, look up more projects here (<a rel="noreferrer noopener" aria-label="ref3.1 (opens in a new tab)" href="https://wiki.hl7.org/National_FHIR_Projects" target="_blank">ref3.1</a>)</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6118,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://hcitexpert.com/wp-content/uploads/2020/05/FHIR-By-Domain-1.jpeg" alt="" class="wp-image-6118"/></figure>
<!-- /wp:image -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>"<strong><em>Think of Resources as paper "forms" reflecting different types of clinical and administrative information that can be captured and shared</em></strong>. [10]</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Therefore, each form has a category, like administrative, clinical, financial, etc. For each patient, one or many of these categories of information can be recorded. For instance, one form template for the clinical category would be recorded for allergies, another one for prescriptions, or in the administrative category, about the physician for the encounter, or the encounter information itself that is stored in various FHIR repositories.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>FHIR repositories can be an EHR , a pharmacy systems, a hospital information systems (HIS), etc. Some systems, such as a patient health record (e.g., Apple's Health App), may expose FHIR interfaces even though they don't actually store any patient or administrative information themselves. Each Resource defines a small amount of highly-focused data. [10]</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>"<strong><em>A single resource doesn't say very much, but a collection of Resources taken together creates a useful clinical record</em></strong>. Information systems map the actions that a user takes (look up patient records, make a note in their history, etc.) to operations on the relevant resources." Source: (<a rel="noreferrer noopener" href="https://build.fhir.org/overview-clinical.html" target="_blank">Ref4</a>). The<strong><em> Resources</em> <em>in FHIR</em> </strong>are categorised as the <strong><em>FHIR Composition Framework</em></strong></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":5147,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://hcitexpert.com/wp-content/uploads/2020/03/framework-2.png" alt="" class="wp-image-5147"/><figcaption>Source: FHIR Overview - Architects, HL7, <a href="http://hl7.org/fhir/overview-arch.html" target="_blank" rel="noreferrer noopener">Link</a> </figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Descriptions of the layers in the FHIR Composition framework: (<a rel="noreferrer noopener" aria-label="ref: Architects Overview (opens in a new tab)" href="https://www.hl7.org/fhir/overview-arch.html" target="_blank">source: Architects Overview</a>)</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><li><strong>Foundation Resources</strong>: Foundation resources are the most rudimentary, foundational resources. They are often used for infrastructural tasks. Although not prohibited, they are not always referenced by other resources.</li><li><strong>Base Resources</strong>: Layer two consists of base resources. These are often the leaf nodes of a resource graph. In other words, they are often referenced by other resources, but don't typically reference other resources themselves. These resources are typically the most commonly used, and therefore require the highest degree of consistency and architectural rigor. Governance is greatest for resources in layers one and two.</li><li><strong>Clinical Resources</strong>: Layer 3 includes the resources that are clinical in nature but are also very common across many use cases. This includes resources for clinical observations, clinical treatment, care provision, and medications. These resources can be used by themselves, but typically build on the resources in layer two. For example, an observation resource will reference the patient resource from layer two. These resources are also frequently contextualized when they are referenced by resources in layers three, four and five.</li><li><strong>Financial Resources</strong>: Layer four is dedicated to financial resources. Logically, financial resources build on clinical and base resources. For example, a billing resource will reference clinical events and activities as well as base resources like a patient.</li><li><strong>Specialized Resources</strong>: In layer five, we find more specialized resources for less common use cases. These resources almost always reference resources in lower layers. Given that FHIR places priority on satisfying the most common use cases, there are fewer resources in this layer.</li><li><strong>Resource Contextualization</strong>: Layer 6 does not contain resources. However, it does extend the composition framework made up by the first five layers of resources. Layer 6 includes profiles and graphs. Profiles are used to extend, constrain, or otherwise contextualize resources for a given purpose. Graphs are compositions of resources, or webs of resource, that contain attributes of their own.</li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Let's take for discussion the <strong>Patient Resource</strong> and review the definition provided in the standard. Each Resource has the following details: </p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><li>Scope &amp; Usage</li><li>References to other Resources</li><li>Resource Content defines the structure<ol><li>Name of the Data Element (Patient Name, Active, Patient Telecom, Gender, etc)</li><li>Flags: A set of information about the element that impacts how implementers handle them.</li><li>Cardinality Rule: Cardinality: the lower and upper bounds on how many times this element is allowed to appear in the resource</li><li>Type</li><li>Description and Constraints defined for each Resource Content</li></ol></li><li>Examples with narratives</li><li>Detailed Descriptions of the Elements in a Resource</li><li>Mappings to other standards</li><li>Profiles and Extentions (definitions below)</li><li>More Information about <strong><em>Resource Formats</em></strong> can be viewed <a rel="noreferrer noopener" aria-label="here (opens in a new tab)" href="http://hl7.org/fhir/formats.html#table" target="_blank">here</a></li></ol>
<!-- /wp:list -->

<!-- wp:image {"id":5183,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://hcitexpert.com/wp-content/uploads/2020/03/Screenshot-2020-03-20-at-2.12.51-PM.png" alt="" class="wp-image-5183"/><figcaption>a Resource UML diagram that summarizes the content graphically</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Extensibility:</strong> as explained earlier about there being a domain driven effort in defining the FHIR resources, FHIR takes into consideration such a  need by defining "Extentions" as well as enforcing constraints. For example, a "prescription" resource might have extension elements added to support tracking of restricted medications while also constraining the codes that can be used to communicate types of drugs to a particular national standard. Another example of extensibility is the Patient Consent for Record sharing, (<a rel="noreferrer noopener" aria-label="ref (opens in a new tab)" href="http://build.fhir.org/extensibility-examples.html" target="_blank">ref5</a>). The <strong><em>Patient Resource</em></strong> doesn't in itself contain the information about patient consent to sharing information. But a PHR vendor could extend the Patient Resource, to maintain a record of this agreement/ consent. (<a rel="noreferrer noopener" aria-label="ref: extensibility examples (opens in a new tab)" href="http://build.fhir.org/extensibility-examples.html" target="_blank">ref: extensibility examples</a>)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Source: <a href="https://www.hl7.org/fhir/overview-clinical.html">https://www.hl7.org/fhir/overview-clinical.html</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Profiles:</strong> To keep the number of base resources reasonable, some of them are fairly broad. For example, <em><strong>the&nbsp;<a href="https://www.hl7.org/fhir/observation.html">Observation</a>&nbsp;resource is used for vital signs, lab results, psychological assessments and a variety of other things</strong></em>. To support setting rules for more narrow areas (e.g. "<em>What should I send if I want to share a blood pressure?</em>"), <strong><em>FHIR allows the creation of Profiles</em></strong> to allow for different types of detailed clinical information to be captured and shared in particular setting (country, state, organisation etc). A Profile is, therefore, a set of constraints on a resource represented as a structure definition with kind = constraint. <strong><em>For example, create a profile for how the patient phone number, a data element in the Patient Resource, should be captured and displayed, another example is the patient blood pressure</em></strong> (<a rel="noreferrer noopener" aria-label="ref (opens in a new tab)" href="http://build.fhir.org/profiling-examples.html" target="_blank">ref, Profiling Examples</a>)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Narrative: </strong>FHIR resources support sharing not only discrete data for computation, but also a human-readable view so that the humans on each end of a healthcare information exchange can still get a full picture of what's going on. Narrative is expected to exist for most resource instances, although it can be omitted in a few limited circumstances. In some cases, the narrative will be generated from discrete information. In other cases, the <strong><em>narrative might be free-form text commentary entered directly by a practitioner, such as referral letters, pathology reports, etc.</em></strong> Certain parts of the narrative content could also later be exposed as discrete data. [source: 10]</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>FHIR has a set of <strong>INTERFACES</strong> [10] using which the information is exchanged between different systems. There are four primary mechanisms of exchange supported by FHIR, via a </p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>A. <strong>REST</strong> interface, </li><li>B. by exchanging <strong>Documents</strong>, </li><li>C. by sending and receiving <strong>Messages</strong> </li><li>D. and by exposing and invoking <strong>Services</strong>.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>A. REST: </strong>For manipulation of resources, FHIR provides a&nbsp;<a href="https://www.hl7.org/fhir/http.html">REST API</a>&nbsp;with a rich but simple set of interactions:(<a rel="noreferrer noopener" aria-label="Ref8 (opens in a new tab)" href="https://www.hl7.org/fhir/overview-dev.html" target="_blank">Ref6</a>)</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":5152,"sizeSlug":"full"} -->
<figure class="wp-block-image size-full"><img src="https://hcitexpert.com/wp-content/uploads/2020/03/restful-api-hc.png" alt="" class="wp-image-5152"/><figcaption>Example of FHIR REST interface</figcaption></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>Some examples of REST Interfaces for manipulation of Resources, along with the URLs</h3>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol><li><em><strong>create</strong></em>: Add a new patient, when a new patient registers at the hospital for a visit, with a new patient id. <em><a href="https://www.hl7.org/fhir/http.html#create">Create</a>&nbsp;= POST https://example.com/path/{resourceType}</em></li><li><em><strong>read</strong></em>: Get a copy of the current medications list, for a particular patient. <em><a href="https://www.hl7.org/fhir/http.html#read">Read</a>&nbsp;= GET https://example.com/path/{resourceType}/{id}</em></li><li><em><strong>update</strong></em>: a patient's appointment information, due to the change in the appointment date and time, as requested by the patient. <em><a href="https://www.hl7.org/fhir/http.html#update">Update</a>&nbsp;= PUT https://example.com/path/{resourceType}/{id}</em></li><li><em><strong>delete</strong></em>: Mark a Medication as inactive because its no longer part of the National Drug Formulary. <em><a href="https://www.hl7.org/fhir/http.html#delete">Delete</a>&nbsp;= DELETE https://example.com/path/{resourceType}/{id}</em></li><li><em><strong>search</strong></em>: Have the clerk search through the list of all the patients for one(s) that meet a set of search criteria, age range between 40 to 45 and Location ="Bangalore" and return the results of those patients that meet this criteria. <em><a href="https://www.hl7.org/fhir/http.html#search">Search</a>&nbsp;= GET https://example.com/path/{resourceType}?search parameters</em>...</li><li><em><strong>history</strong></em>: is when the user wants to view the list of past encounters for a patient. <em><a href="https://www.hl7.org/fhir/http.html#history">History</a>&nbsp;= GET https://example.com/path/{resourceType}/{id}/_history</em></li><li><em><strong>transaction</strong></em>: is equivalent to asking the doctor or the nurse to record a visit summary or a discharge note for a patient. <em><a href="https://www.hl7.org/fhir/http.html#transaction">Transaction</a>&nbsp;= POST https://example.com/path/&nbsp;(POST a transaction bundle to the system)</em></li><li><em><strong>operation</strong></em>: Ask the clerk to perform an action or procedure on papers from one or more of the folders - for example, averaging numbers across patients, producing a summary record, or perform a complex search just by ticking a box on a requisition saying "do that one". <em><a href="https://www.hl7.org/fhir/operations.html">Operation</a>&nbsp;= GET https://example.com/path/{resourceType}/{id}/${opname}</em></li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>B. Documents [10]</strong> are a "frozen" view of information that can be reliably retrieved even years in the future. <strong><em>Examples of document-like things in healthcare include discharge summaries and lab reports.</em></strong> Two systems or two FHIR servers could connect with each other to just exchange documents for a particular patient.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>C. Message [10] </strong>is a set of information sent from one system to another, typically triggered by an event in the sender system. <em><strong>For example, a patient being admitted, a lab test being ordered, a drug being administered</strong></em>. A message might request that a lab order be fulfilled or notify a system that two patient records have been merged or that a patient has been transferred from one bed to another. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>D. Services [10]</strong> can be thought of as a small sticky note. Services are likely to be used for things like decision support. E.g. "<em>Is there a problem with prescribing medication X for patient Y?</em>" or "<em>What's the recommended care plan for a patient with conditions A, B and C?</em>"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>FHIR from a System Architects perspective</em></strong>, (<a rel="noreferrer noopener" href="http://hl7.org/fhir/overview-arch.html" target="_blank">Source:Ref7</a>) In the healthcare domain, we have a core set of common business objects including things like “a patient”, “a procedure”, “an observation”, “an order”, etc. (see&nbsp;<a href="http://hl7.org/fhir/resourcelist.html">a list of defined resources</a>). The FHIR specification provides a framework for defining these healthcare business objects (“resources”), for relating them together, for implementing them in a computable form, and for sharing them across well-defined interfaces. The <strong><em>FHIR framework contains a verifiable and testable syntax, a set of rules and constraints, methods and interface signatures for “FHIR-aware” APIs, and specifications for the implementation of a server capable of requesting and delivering FHIR business objects</em></strong></p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>A FHIR REST server is any software that implements the FHIR APIs and uses FHIR resources to exchange data</p></blockquote>
<!-- /wp:quote -->

<!-- wp:image {"id":5150,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://i2.wp.com/hcitexpert.com/wp-content/uploads/2020/03/arch-uml3.png?fit=845%2C600&amp;ssl=1" alt="" class="wp-image-5150"/><figcaption>Source: FHIR Overview - Architects, <a href="https://www.hl7.org/fhir/overview-arch.html" target="_blank" rel="noreferrer noopener" aria-label="link (opens in a new tab)">link</a></figcaption></figure>
<!-- /wp:image -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p><strong><em>HL7 suggested list of documents to review when trying to understand the FHIR standards for the first time</em></strong><br>See the&nbsp;<a href="http://hl7.org/fhir/summary.html">executive summary</a>, the&nbsp;<a href="http://hl7.org/fhir/overview-dev.html">developer's introduction</a>,&nbsp;<a href="http://hl7.org/fhir/overview-clinical.html">clinical introduction</a>, or&nbsp;<a href="http://hl7.org/fhir/overview-arch.html">architect's introduction</a>, and then the FHIR&nbsp;<a href="http://hl7.org/fhir/overview.html">overview / roadmap</a>&nbsp;&amp;&nbsp;<a href="http://hl7.org/fhir/versions.html">Timelines</a></p></blockquote>
<!-- /wp:quote -->

<!-- wp:heading {"level":3} -->
<h3>Why FHIR is better? (Source: <a rel="noreferrer noopener" href="https://www.hl7.org/fhir/summary.html" target="_blank">Ref8</a>)</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>A <em><strong>strong focus on implementation</strong></em>: fast and easy to implement (multiple developers have had simple interfaces working in a single day)</li><li>Multiple implementation libraries, <em><strong>many examples available to kick-start development</strong></em></li><li><strong><em>Specification is free for use</em></strong> with no restrictions</li><li><em><strong>Interoperability out-of-the-box</strong></em>: base resources can be used as is, but can also be adapted as needed - which happens a lot - for local requirements using Profiles, Extensions, Terminologies and more</li><li><strong><em>Evolutionary development path from HL7 Version 2 and CDA</em></strong>: standards can co-exist and leverage each other</li><li><strong><em>Strong foundation in Web standards</em></strong>: XML, JSON, HTTP, OAuth, etc.</li><li><em><strong>Support for RESTful architectures</strong></em>, seamless exchange of information using messages or documents, and service-based architectures</li><li><em><strong>Concise and easily understood</strong></em> specifications</li><li>A <strong><em>human-readable serialization</em></strong> format for ease of use by developers</li><li><em><strong>Ontology-based analysis</strong></em> with formal mapping for correctness (under development)</li><li>A central challenge for healthcare standards is how to handle the wide variability caused by diverse healthcare processes. FHIR solves this challenge by defining a <em><strong>simple framework for extending the existing resources and describing their use with Profiles</strong></em>. All systems can read all resources, but applications can add more control and meaning using profiles. Many healthcare contexts require extensive local agreements</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Currrent Landscape</h2>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol><li>There are many companies and big tech that have already adopted the FHIR Standards in a big way. For instance, <a rel="noreferrer noopener" aria-label="Apple has integrated the FHIR (opens in a new tab)" href="https://developer.apple.com/documentation/healthkit/samples/accessing_health_records" target="_blank">Apple has integrated the FHIR</a> standards into the iphone Health App in a way that the patient information from her multiple visits across multiple healthcare organisation are pulled into the users iphone and shown to her as and when required. <strong>Apple</strong> has even ensured that no health data is stored on the users phone/ device. </li><li><strong>Google</strong> has also published the <a rel="noreferrer noopener" aria-label="CloudHealthcare APIs (opens in a new tab)" href="https://cloud.google.com/healthcare/docs/concepts/fhir" target="_blank">CloudHealthcare APIs</a> based on the FHIR R4 standard.</li><li><a rel="noreferrer noopener" aria-label="Microsoft Azure has expanded the API for FHIR (opens in a new tab)" href="https://hitinfrastructure.com/news/microsoft-azure-expands-api-for-fhir-to-fuel-interoperability" target="_blank"><strong>Microsoft Azure</strong> has expanded the API for FHIR</a> to fuel interoperability in Healthcare </li><li>And here's a HL7Wiki article, Companies interested in or using FHIR, <a rel="noreferrer noopener" href="https://wiki.hl7.org/Organizations_interested_in_FHIR" target="_blank">link</a></li><li>The MOHFW, India has recently published the National Digital Health Blueprint, which mentions the use of FHIR as an interoperability standard. It identifies 8 FHIR Resources as a starting point.</li><li>In a book published by the NitiAayog, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="https://niti.gov.in/sites/default/files/2019-11/NitiAayogBook_compressed.pdf" target="_blank">link</a>, <strong>Building a 21st Century Health System for India</strong>, the Chapter 5 of the document highlights the evolving Healthcare Technology framework. FHIR is mentioned as the foundational standard for semantic interoperability between systems.</li><li>eObjects framework and information can be found here, <a rel="noreferrer noopener" href="http://www.openbodhik.in/?m=1" target="_blank">link</a></li><li>Also read the Blog by Dr. Pankaj Gupta, on some new and interesting concepts around interoperability in India <a rel="noreferrer noopener" href="https://hcitexpert.com/2020/04/health-systems-for-a-new-india-eobjects-building-blocks-by-dr-pankaj-gupta-pankajguptadr.html/" target="_blank">link</a></li><li>Based on various updates from the Govt. Of India and across the Healthcare Industry in India, you can also join and follow the work being done at the <a href="https://hcitexpert.com/2020/01/the-national-collaborative-initiative-for-interoperability-by-aniruddha-nene-ncii.html/">National Collaborative Initiative For Interoperability</a></li></ol>
<!-- /wp:list -->

<!-- wp:image {"id":5237,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://i1.wp.com/hcitexpert.com/wp-content/uploads/2020/03/NDHB_FHIR_Resources.jpeg?fit=845%2C595&amp;ssl=1" alt="" class="wp-image-5237"/><figcaption>Source: The NDHB Document by MoHFW, India</figcaption></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Usecase Scenarios for FHIR</h2>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol><li>Personal Health Records</li><li>Document Exchange</li><li>Decision Support Systems</li><li>Federated Health Records (ref: NDHB, India)</li><li>Usecases from Argonaut Project: [source: 16]<ol><li><em><strong>Patient &nbsp;uses </strong>&nbsp;provider-approved &nbsp;<strong>web &nbsp;application</strong> &nbsp;to &nbsp;access &nbsp;health &nbsp;data</em></li><li><em><strong>Patient &nbsp;uses</strong> &nbsp;provider-­approved &nbsp;<strong>mobile &nbsp;app</strong> &nbsp;to &nbsp;access &nbsp;health &nbsp;data</em></li><li><em><strong>Clinician &nbsp;uses</strong> &nbsp;provider­-approved &nbsp;<strong>web &nbsp;application</strong> &nbsp;to &nbsp;access &nbsp;health &nbsp;data</em></li><li><em><strong>Clinician &nbsp;uses </strong>&nbsp;provider­-approved &nbsp;<strong>mobile &nbsp;app </strong>&nbsp;to &nbsp;access &nbsp;health &nbsp;data</em></li><li><em>(future) Clinician &nbsp;in &nbsp;organization &nbsp;A &nbsp;uses &nbsp;EHR &nbsp;A &nbsp;to &nbsp;access &nbsp;patient &nbsp;data &nbsp;in &nbsp;EHR &nbsp;B, &nbsp;operated &nbsp;by&nbsp;organization &nbsp;B</em></li></ol></li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Review the details of these usecases defined in the <a href="http://build.fhir.org/usecases.html" target="_blank" rel="noreferrer noopener" aria-label="Ref: Usecases (opens in a new tab)">Ref: Usecases</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Suggested Readings</h2>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol><li>Rest API talk by Leonard Richardson: <a rel="noreferrer noopener" href="https://www.crummy.com/writing/speaking/2008-QCon/act3.html" target="_blank">link</a></li><li>Richardson Maturity Model, talks about the principle elements of a REST approach with a healthcare example thats worth reviewing, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="https://martinfowler.com/articles/richardsonMaturityModel.html" target="_blank">link</a></li><li>Book: Rest in Practice, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="https://www.amazon.com/gp/product/0596805829?ie=UTF8&amp;tag=martinfowlerc-20&amp;linkCode=as2&amp;camp=1789&amp;creative=9325&amp;creativeASIN=0596805829" target="_blank">link</a></li><li>RESTful API wiki, <a rel="noreferrer noopener" href="https://en.m.wikipedia.org/wiki/Representational_state_transfer" target="_blank">link</a></li><li>Mastering REST Architecture — REST Architecture Details, <a rel="noreferrer noopener" href="https://medium.com/@ahmetozlu93/mastering-rest-architecture-rest-architecture-details-e47ec659f6bc" target="_blank">link</a></li><li>HBR, The untapped potential of Healthcare APIs <a rel="noreferrer noopener" href="https://hbr.org/2015/12/the-untapped-potential-of-health-care-apis" target="_blank">link</a></li><li>Will web APIs and HL7 FHIR change our views on data interoperability?, HealthStandards, David Shavers presentation <a rel="noreferrer noopener" href="https://healthstandards.com/blog/2017/07/11/will-fhir-apis-change-interop-views/" target="_blank">Link</a></li><li>HL7 FHIR, r4 Home page <a rel="noreferrer noopener" href="http://hl7.org/fhir/" target="_blank">Link</a></li><li>HL7, Getting Started with FHIR, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="http://build.fhir.org/modules.html" target="_blank">link</a></li><li>HL7, Clinical Overview, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="https://www.hl7.org/fhir/overview-clinical.html" target="_blank">link</a></li><li>HL7, Blogs on FHIR, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="https://confluence.hl7.org/display/FHIR/Blogs" target="_blank">link</a></li><li>HL7, FHIR Product Brief, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="https://www.hl7.org/implement/standards/product_brief.cfm?product_id=491" target="_blank">link</a></li><li>HL7, FHIR for C-Suite, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="http://www.hl7.org/documentcenter/public/standards/FHIR/FHIR%20for%20the%20C-Suite.4Sep19.pdf" target="_blank">link</a></li><li>HL7Wiki, Companies interested in or using FHIR, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="https://wiki.hl7.org/Organizations_interested_in_FHIR" target="_blank">link</a></li><li>HL7Wiki, National FHIR Projects, <a rel="noreferrer noopener" aria-label="link (opens in a new tab)" href="https://wiki.hl7.org/National_FHIR_Projects" target="_blank">link</a></li><li>HL7, Argonaut Project, <a href="https://argonautwiki.hl7.org/Implementation_Guide#Use_Cases" target="_blank" rel="noreferrer noopener" aria-label="link (opens in a new tab)">link</a></li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><em>This article is also quite similar to the concepts of FHIR, I have reviewed the literature on FHIR and tried to collate excerpts from various sources (mentioned next to the relevant excerpt as a <strong>source</strong> or reference(<strong>ref</strong>)) that will help the reader understand the fundamental definitions of FHIR. It's a FHIR Reference Document of sorts, containing information pulled together from various sources of information.</em></p>
<!-- /wp:paragraph -->

<!-- wp:coblocks/highlight -->
<p class="wp-block-coblocks-highlight"><mark class="wp-block-coblocks-highlight__content">Stay tuned for the HL7 India CONNECTATHON happening in june. <br><br>A big thanks to <a href="https://hcitexpert.com/tag/kumar-satyam/">Kumar Satyam</a></mark></p>
<!-- /wp:coblocks/highlight -->

<!-- wp:block {"ref":6100} /-->
