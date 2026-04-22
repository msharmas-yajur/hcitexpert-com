---
title: "Making HL7 #FHIR work for India by Kumar Satyam, @kr_satyam"
date: 2020-04-02 06:00:00 +0000
author: DigitalHealth Experts
excerpt: "FHIR profiles are layered in sense that national profiles adapt from base (core ) , states or regions adapt from national profiles and specialized domain or organizations further adapt the regional pr"
original_url: https://hcitexpert.com/2020/04/making-hl7-fhir-work-for-india-by-kumar-satyam-kr-satyam.html/
categories:
  - GUEST BLOG
  - INTEROPERABILITY
tags:
  - Featured
  - FHIR
  - Kumar Satyam
---

<!-- wp:image {"align":"center","id":5431,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://i0.wp.com/hcitexpert.com/wp-content/uploads/2020/03/Kumar-Satyam-Blogs-1.png?fit=845%2C423&amp;ssl=1" alt="Kumar Satyam FHIR for INDIA" class="wp-image-5431"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><em>"Can I see your blood test reports from last month"</em>&nbsp;- the doctor asked me.&nbsp;<em>"I have it on my mobile"</em>&nbsp;- I told him. I showed him the pdf report the lab had mail me on my email id.&nbsp;<em>"Do you have earlier reports?"</em>- he asked. I started searching my mailbox for previous reports but was unable to locate them. I asked him&nbsp;<em>"Sir, if I give you my hospital Id, can you fetch it from your system. some tests were done in another branch of your hospital"</em>. </p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>He took my hospital id , searched on his EMR and found my old records. Relieved I wondered&nbsp;<em>if I had my tests done in another hospital how would had I shown the reports</em>. This hospital has a centralized information management system connecting all the branches and an universal patient identifier. However the doctor was able to see all my tests and note of my encounters with other doctors in the hospital, which I felt was violation of my privacy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I used to go to a hospital when I lived in another part of the city, when I changed my residence I preferred a different hospital near to me. People are mobile, they move within cities and across cities for jobs, for better commute ,for better school for kids or for various other reasons. It is quite natural that preferred care facility a person chooses to go to for day to day care also changes as a result of relocation, this leads to broken medical history. There is no way for me to consolidate my electronic health record today. Lets us assume that hospitals do want to share patient records with each other for the better good of the patient, but limitations of their existing systems don't allow them to do so. Their existing infrastructure was designed to work well within the boundary of the enterprise.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://www.hl7.org/fhir/overview.html" target="_blank" rel="noreferrer noopener">HL7 FHIR (Fast Healthcare Interoperability Resources)</a>&nbsp;standard promises to enable these healthcare enterprises have mechanism to exchange data with third parties outside their corporate network cost effectively and efficiently. FHIR supports structured healthcare data exchange over standard web via&nbsp;<a href="https://github.com/basecamp/highrise-api" target="_blank" rel="noreferrer noopener">restful APIs</a>.Setting up a FHIR server can as simple as hosting a web server. No need to punch a hole in corporate IT firewall to open a custom port, no need for point to point vpn tunnel. In the Indian context, adopting FHIR makes a lot of sense. Following are some of the reasons why FHIR can be the go to healthcare data exchange standard for India.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><strong>FHIR Standard is free.</strong></li><li><strong>FHIR doesn't require specialized knowledge</strong>. FHIR makes use of several well-known web standards, the skills required to develop applications with FHIR are directly transferable from anyone working in website or web app development.</li><li><strong>Multiple opensource implementations available.</strong>&nbsp;Its vibrant community of developers , implementers and supporters can be tapped into for any support.</li><li><strong>Supports mobility.</strong>&nbsp;Strong focus on web technologies and implement-ability makes FHIR the standard for building Healthcare Apps for internet, cloud and mobile.</li><li><strong>Standard is flexible and adaptable</strong>. FHIR provides flexibility to extend and adapt it according to local needs.</li><li><strong>Standard is fairly stable</strong>&nbsp;and is being actively adopted across the world.</li><li>FHIR is listed as healthcare data exchange standard in&nbsp;<a href="https://mohfw.gov.in/newshighlights/final-report-national-digital-health-blueprint-ndhb" target="_blank" rel="noreferrer noopener">National Digital Health Blueprint (NDHB) 2019</a></li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>When implementing FHIR in your systems, it is important to keep in mind that two FHIR complaint systems may actually be not interoperable. The main reason for this is the inherent deliberate flexibility of the specification to allow it to be used in different diverse scenarios across the globe. To illustrate the flexibility let me tell that a blank patient&nbsp;<a href="https://www.hl7.org/fhir/resource.html" target="_blank" rel="noreferrer noopener">resource&nbsp;</a>with no elements is still a valid patient resource. Almost every element in the base FHIR specification is optional. Interoperablity will be guaranteed if both sender and receiver of the FHIR resource(s) agree on the content of the data and what operations are allowed on the resource(s).&nbsp;<a href="https://fhirblog.com/2014/03/26/fhir-profiles-an-overview/" target="_blank" rel="noreferrer noopener">FHIR profiling</a>&nbsp;is a way to build this consensus on content, operations &amp; search parameters supported. Two systems supporting a FHIR profile mean that they agree to the content rules specified in the profile and therefore they know what data to expect or send. In essence due its flexibility FHIR specification usually requires further adaptation to particular contexts of use. Typically, these adaptations specify:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Rules about which resource elements are or are not used, and what additional elements are added that are not part of the base specification</li><li>Rules about which API features are used, and how</li><li>Rules about which terminologies are used in particular elements</li><li>Descriptions of how the Resource elements and API features map to local requirements and/or implementations.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>As observed globally national FHIR initiatives typically start with Profiling at national level- Studying and adapting FHIR specification to meet the specific requirements of the country and targeted use cases. Creating a community , building human capital , enlisting support from key stakeholders , establishing tooling &amp; infrastructure for implementers also go in parallel. Profiling is a community activity, it typically involves following activities</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>Use Case selection,</p></blockquote>
<!-- /wp:quote -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>Definition of behaviors &amp; data models required,</p></blockquote>
<!-- /wp:quote -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>Mapping of resources &amp; creation of profiles,</p></blockquote>
<!-- /wp:quote -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>implementation in products,</p></blockquote>
<!-- /wp:quote -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>testing to validate &amp; refine as required, demonstrate maturity and then finally publish a stable version</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>National profiles are just the beginning, local regional &amp; specialized domains would require further adaptations to suit their specific needs and use cases. States may find a need to further adapt the National profiles to suit local regulations or uniqueness. Mental health &amp; Cardiology may need different set of data elements hence domain experts may choose to further adapt National or regional profiles. FHIR profiles are layered in sense that national profiles adapt from base (core ) , states or regions adapt from national profiles and specialized domain or organizations further adapt the regional profiles. The levels of layering depends on the context and the usecase.&nbsp;<a href="https://www.devdays.com/wp-content/uploads/2019/02/DD18-US-FHIR-Profiling-Overview-and-Introduction-Michel-Rutten-2018-06-19.pdf" target="_blank" rel="noreferrer noopener">Following picture</a>&nbsp;depicts the concept of layering. Given the diversity of Indian context, proliferation of profiles is very likely therefore a governance infrastructure is a must.</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://media-exp1.licdn.com/dms/image/C5112AQFL_dP7tIibcw/article-inline_image-shrink_1500_2232/0?e=1590624000&amp;v=beta&amp;t=PaGUfmadlz3KoiFdpUml6Iq6bJtgzFaxt5Jn4hbLy6o" alt="No alt text provided for this image"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>In the next article I will share the efforts underway to make FHIR work for India. The intent of this article is to get feedback and support from everyone as we embark on the journey of lighting the FHIR in India.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>This article was first published on Kumar Satyam's <a href="https://www.linkedin.com/pulse/making-hl7-fhir-work-india-kumar-satyam/" target="_blank" rel="noreferrer noopener">LinkedIn Pulse Blog</a>, its been published here with the author's permission</em></strong></p>
<!-- /wp:paragraph -->

<!-- wp:block {"ref":5638} /-->
