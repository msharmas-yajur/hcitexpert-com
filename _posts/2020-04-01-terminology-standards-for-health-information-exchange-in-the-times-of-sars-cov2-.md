---
title: "Terminology Standards for Health Information Exchange in the times of SARS-Cov2 by Prof. Supten Sarbadhikari, @supten"
date: 2020-04-01 05:05:00 +0000
author: DigitalHealth Experts
original_url: https://hcitexpert.com/2020/04/terminology-standards-for-health-information-exchange-in-the-times-of-sars-cov2-by-prof-supten-sarbadhikari-supten.html/
categories:
  - EMR/EHR/HIMS
  - GUEST BLOG
  - SNOMED CT
tags:
  - Dr. Supten Sarbadhikari
---

<!-- wp:image {"align":"center","id":5508,"sizeSlug":"full"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://hcitexpert.com/wp-content/uploads/2020/03/Prof-Supten-Blogs.png" alt="" class="wp-image-5508"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>To provide better and cost effective patient care, one needs to exchange healthcare information. For this to happen seamlessly, there is a dire need of Standards that facilitate this interoperability.</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>A Standard denotes the ability of two or more systems or components to exchange information (structural or&nbsp;<strong><em>syntactic</em></strong>&nbsp;interoperability) and to (meaningfully) use the information that has been exchanged (functional or&nbsp;<em><strong>semantic</strong></em>&nbsp;interoperability).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The&nbsp;<strong>EHR Standards</strong>, 2<sup>nd</sup>&nbsp;edition, were notified by the&nbsp;Ministry of Health and Family Welfare, Government of India (MoHFW) in December 2016.<br>Subsequently, to give a boost to implementation of digital health in India, the&nbsp;<strong>National Digital Health Blueprint (NDHB)</strong>&nbsp;has been finally notified, and it also mentions a minimal set of standards to be used. It tries to define the standards required for ensuring interoperability within the National Digital Health Eco-system.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Also, now the&nbsp;<strong>Telemedicine Practice Guidelines</strong>&nbsp;have been notified by the MoHFW and NITI Aayog.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2><strong>Categories of Standards for exchange of Health Information</strong></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The broad categories for Standards mentioned in the NDHB are those for Consent, (Clinical) Content, Privacy and Security, Patient Safety and Data Quality. Currently for epidemiological purposes, all countries send reports to the WHO using the ICD classification system (current version is ICD-10, while ICD-11 has been formally released last year and will be applicable from January 2022). However, for getting better insights into the clinical data, SNOMED CT (a clinical terminology system) is the globally preferred standard and India has been a country member of SNOMED International since 2014. The basic differences of these two systems are summarized below.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><strong>ICD</strong>&nbsp;(International Statistical Classification of Diseases) codes, from the WHO, have limited scope and granularity, summarizes and aggregates data into broad categories (for epidemiological purposes), and are&nbsp;<strong>mono-hierarchical</strong>&nbsp;(Each code is grouped into a single grouping)<ul><li>No links to body sites or causes </li><li>Groups multiple clinical meanings&nbsp;&nbsp;together using a single code </li><li>Does not always represent sufficient detail for clinical purposes</li></ul></li></ul>
<!-- /wp:list -->

<!-- wp:list -->
<ul><li><strong>SNOMED CT</strong>&nbsp;is broader in scope, more granular, allows data to be grouped and aggregated in different ways (<strong>poly-hierarchical</strong>), and to be queried, basedon&nbsp;<strong>Relationships</strong>&nbsp;between the&nbsp;<strong>Concepts</strong>. Also, since it is inherently logical, developing Clinical Decision Support Systems (CDSS) is also relatively easier with SNOMED-CT enabled systems.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Presently mappings are available from to SNOMED CT to ICD-10 and its various adaptations. Therefore, if any system is SNOMED CT enabled, it is possible to report according to ICD-10 or 11 as may be the statutory requirement for epidemiological and public health purposes.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2><strong>Updating for SARS-Cov2</strong></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Now, with the world being gripped by a new Pandemic, the SDOs (Standards Development Organizations) have also geared up and come up with pertinent standards for this&nbsp;<em><strong>novel Corona virus</strong></em>&nbsp;or&nbsp;<strong><em>Covid-19</em></strong>&nbsp;(Corona virus Disease 2019) or&nbsp;<em><strong>SARS-Cov2 (Severe Acute Respiratory Syndrome Coronavirus-2)</strong></em>.&nbsp;The World Health Organization (WHO) has named the syndrome caused by this coronavirus “COVID-19”, and the International Committee on Taxonomy of Viruses (ICTV) has named the virus SARS-CoV-2.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The COVID-19 disease outbreak has been declared a public health emergency of international concern. The WHO has included it into the&nbsp;<strong>ICD</strong>&nbsp;system:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>An emergency ICD-10 code of ‘U07.1 COVID-19, virus identified’ is assigned to a disease diagnosis of COVID-19 confirmed by laboratory testing.</li><li>emergency ICD-10 code of ‘U07.2 COVID-19, virus not identified’ is assigned to a clinical or epidemiological diagnosis of COVID-19 where laboratory confirmation is inconclusive or not available.</li><li>Both U07.1 and U07.2 may be used for mortality coding as cause of death</li><li>In ICD-11, the code for the confirmed diagnosis of COVID-19 is RA01.0 and the code for the clinical diagnosis (suspected or probable) of COVID-19 is RA01.1.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>A more detailed breakup for ICD-10 is available at:&nbsp;<a href="https://www.who.int/classifications/icd/COVID-19-coding-icd10.pdf?ua=1">https://www.who.int/classifications/icd/COVID-19-coding-icd10.pdf?ua=1</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>SNOMED International has come out by placing the concept under the parent Human Coronavirus (Organism):&nbsp;Severe acute respiratory syndrome coronavirus 2 (organism) –&nbsp;SCTID: 840533007</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>840533007 | Severe acute respiratory syndrome coronavirus 2 (organism)| <em>en</em>&nbsp;&nbsp;&nbsp;Severe acute respiratory syndrome coronavirus 2 (organism)<br><em>en</em>&nbsp;&nbsp;&nbsp;2019-nCoV<br><em>en</em>&nbsp;&nbsp;&nbsp;Severe acute respiratory syndrome coronavirus 2<br><em>en</em>&nbsp;&nbsp;&nbsp;SARS-CoV-2<br><em>en</em>&nbsp;&nbsp;&nbsp;2019 novel coronavirus<br></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And, under Coronavirus infection (<strong>Disorder</strong>):&nbsp;Disease caused by severe acute respiratory syndrome coronavirus 2 (disorder) –&nbsp;<strong>SCTID: 840539006</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>840539006 | Disease caused by severe acute respiratory syndrome coronavirus 2 (disorder) |&nbsp;&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>en</em>&nbsp;&nbsp;&nbsp;Disease caused by severe acute respiratory syndrome coronavirus 2<br><em>en</em>&nbsp;&nbsp;&nbsp;COVID-19<br><em>en</em>&nbsp;&nbsp;&nbsp;Disease caused by 2019 novel coronavirus<br><em>en</em>&nbsp;&nbsp;&nbsp;Disease caused by 2019-nCoV<br><em>en</em>&nbsp;&nbsp;&nbsp;Disease caused by severe acute respiratory syndrome coronavirus 2 (disorder)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Regenstrief Institute that develops the LOINC codes, is developing Special Use codes in response to an urgent or emergent situation. These codes are based on the most up to date information available at the time of their creation. They have undergone the normal QA terminology process. LOINC supports their use in the unique situation that resulted in their rapid creation. However, be aware that downstream users may not be ready to handle prerelease codes until they are published in an official release. The emerging codes for Covid-19 are available at:&nbsp;<a href="https://loinc.org/sars-coronavirus-2/">https://loinc.org/sars-coronavirus-2/</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2><strong>Conclusion</strong></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The pandemic of SARS-Cov2 is evolving, and, so are the Standards related to the exchange of health information because of the disorder and / or organism. Once the situation stabilizes a bit, the unambiguity in the&nbsp;semantic&nbsp;exchange of such information will also become clear.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2><strong>References</strong></h2>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol><li>National Health Portal, Ministry of Health and Family Welfare, Government of India, EHR Standards.&nbsp;Available from:&nbsp;<a href="https://www.nhp.gov.in/ehr-standards-helpdesk_ms">https://www.nhp.gov.in/ehr-standards-helpdesk_ms</a></li><li>Ministry of Health and Family Welfare, Government of India,&nbsp;National Digital Health Blueprint, 2019, Available from:&nbsp;<a href="https://main.mohfw.gov.in/sites/default/files/Final%20NDHB%20report_0.pdf">https://main.mohfw.gov.in/sites/default/files/Final%20NDHB%20report_0.pdf</a>&nbsp;(A compressed version is available at:&nbsp;<a href="https://main.mohfw.gov.in/sites/default/files/Final%20Report%20-%20Lite%20Version.pdf">https://main.mohfw.gov.in/sites/default/files/Final%20Report%20-%20Lite%20Version.pdf</a>&nbsp;)</li><li>Ministry of Health and Family Welfare, Government of India,&nbsp;Telemedicine Practice Guidelines:&nbsp;<a href="https://www.mohfw.gov.in/pdf/Telemedicine.pdf">https://www.mohfw.gov.in/pdf/Telemedicine.pdf</a></li><li>Sarbadhikari SN, The Role of Standards for Digital Health and Health Information Management, JBCR, 2019, 6(1):1:&nbsp;<a href="https://jbcr.net.in/JBCR-VOL-6-issue-1-2019-20/current-issues-volume-VI-issue-1-1.html">https://jbcr.net.in/JBCR-VOL-6-issue-1-2019-20/current-issues-volume-VI-issue-1-1.html</a></li><li>Sarbadhikari SN, Digital Health in India - as envisaged by the National Health Policy (2017), Guest Editorial,&nbsp;<em>BLDE University Journal of Health Sciences</em>, 2019, 4: 1-6.</li><li>SNOMED International, SNOMED CT Basics:&nbsp;<a href="https://confluence.ihtsdotools.org/display/DOCSTART/4.+SNOMED+CT+Basics">https://confluence.ihtsdotools.org/display/DOCSTART/4.+SNOMED+CT+Basics</a></li><li>WHO, ICD-10:&nbsp;<a href="https://www.who.int/classifications/icd/covid19/en/">https://www.who.int/classifications/icd/covid19/en/</a></li><li>SNOMED International:&nbsp;<a href="http://www.snomed.org/news-and-events/articles/snomed-loinc-coronavirus-collaboration">http://www.snomed.org/news-and-events/articles/snomed-loinc-coronavirus-collaboration</a></li><li>SNOMED International:&nbsp;<a href="https://browser.ihtsdotools.org/">https://browser.ihtsdotools.org/</a></li><li>Regenstrief Institute, LOINC codes:&nbsp;<a href="https://loinc.org/prerelease/">https://loinc.org/prerelease/</a></li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong><em>This article was first published on <a href="http://supten.blogspot.com/2020/03/terminology-standards-for-health.html" target="_blank" rel="noreferrer noopener">Prof. Supten's Blog</a>, its been republished here with the Author's permission</em></strong></p>
<!-- /wp:paragraph -->

<!-- wp:block {"ref":5819} /-->
