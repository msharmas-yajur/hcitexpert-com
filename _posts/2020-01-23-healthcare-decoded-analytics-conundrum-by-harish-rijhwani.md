---
title: "Healthcare Decoded – The #Analytics Conundrum by Harish Rijhwani, @Harish_Rijhwani"
date: 2020-01-23 08:08:00 +0000
author: DigitalHealth Experts
excerpt: "If we want to start using Analytics in India, one of the areas to focus on can be in the area of Diagnostic Analytics. We can leverage Transfer learning in this area as there are many pre-trained mode"
original_url: https://hcitexpert.com/2020/01/healthcare-decoded-analytics-conundrum-by-harish-rijhwani.html/
categories:
  - GUEST BLOG
tags:
  - "#DigitalHealth"
  - Artificial Intelligence
  - BIG DATA ANALYTICS
  - Harish Rijhwani
---

<!-- wp:image {"id":3209,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://hcitexpert.com/wp-content/uploads/2020/02/08f8a-harish2brijhwani2bblogs.png" alt="" class="wp-image-3209"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><em>If we want to start using Analytics in India, one of the areas to focus on can be in the area of Diagnostic Analytics. We can leverage Transfer learning in this area as there are many pre-trained models leveraged by others and available.</em>&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:heading -->
<h2>Introduction</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Abacus, one of the earliest form of Calculators, originated around 5000 years back. If we want to look at something, somewhat near to our timeline, we need to go to around 1890. In this year the Hollerith Tabulator was created, it is an Electromagnetic machine use to summarize information present on punch cards. Fifty years from here (the 1940s), Alan Turing created the Turing machine, first of its kind Analytics model to decode encrypted German Messages. From here on the world saw a growing need for computers. Fast forward to today’s day and age; we have reached the point where people have experimented with using DNA as a storage medium. DNA - Deoxyribonucleic Acid which stores the genetic instruction of the body. Oh, by the way, a DNA can store around 215 petabytes of information which is equivalent to 215 million gigabytes. Phew! That’s a huge number.&nbsp;<br><br><br>Over the past 120 years, Healthcare is one of the most unchartered territories when we consider Analytics. Organizations have focused on Supply Chain, Finance, Human Resources, and other domains. Compared to all these industries, Healthcare is in a stage of discovery. At some point in everyone’s life, one has been to a hospital. In my case I had gone to the US for a business trip in Feb 2006, and what do you know, I got chickenpox. I had to visit an “Urgent Care” where I waited around 20-30 minutes in the lobby before my turn came. Once my turn came, we went to the examination room where the nurse came and asked me some more questions. The nurse also had a form with her clipped on a writing pad. She asked me various questions around my lifestyle for example</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Do You Smoke?</li><li>Do You Drink?</li><li>Are you on any medication?</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><br>Along with this, she also took my vitals in terms of Blood pressure, height, weight, and temperature. She noted down all this information on a paper form. After all of this is when arrived the Physician. The physician looked at the information filled on the chart by the Nurse, then looked at the spots and said – "You have Chicken Pox." The Physician then gave me my prescription and also gave me a date for my next visit, which was around 4-5 days away. It was now time to leave, and I had to pay a bill of approx. $200/- out of my pocket, note that this did not include the bill for medications which I had to buy from a nearby pharmacy.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Looking Back</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Let us look back at some of the important aspects of the scenario depicted. If it came to your attention, the nurse was using a “Paper Chart,” this is the biggest challenge for the field of Business Intelligence and Analytics. Data in an electronic format is very much necessary for anyone to perform Analytics or create a simple Report depicting Insights viz. “No of Patients visiting the Hospital Daily.”&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><br>The second aspect, I had to wait for 20-30 minutes before the physician could see me. The scenario depicted was not an Emergency, but wait times are important and along with it the Patient Volume, which could be Monthly/Weekly/Daily/Hourly. One of the Largest US Based IDN’s (HCA hospitals) takes the help of large Electronic Billboards to keep people informed of the wait times.<br><br>The third aspect is the final bill amount which in this case, I had to pay out of pocket. In my case, I was on a Business Trip and had Insurance but did not have an Insurance Card. In other words, you can say it was not cashless insurance. In general, it would be important to know the approximate cost of treatment upfront.<br><br>One final aspect which does not come out that is unlike any other industry; the Healthcare Industry has multiple entities viz.<br></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Healthcare Provider – The Hospital / Care Provider, which can be a large hospital to a clinic.</li><li>Health Insurance Company&nbsp;</li><li>Pharmaceutical – Where the patients buy medications</li><li>Pharma and Life Sciences – These organizations focus on developing new medications</li><li>Medical Devices – These organizations develop Biomedical Devices viz. Glucometer</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Deep Dive</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Now that you have a basic idea about Healthcare and some of the touchpoints let us deep dive into more details around some possible scenarios of Analytics which can be done/achieved. These scenarios are not limited to just a Hospital/Care provider but would cover various entities. Let us divide the scenarios across the different types of Machine Learning Algorithms and see what we could do with each specific example.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>a. Regression</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Regression in its simplest format can solve very limited problems but is the basis for various other algorithms. In the case of healthcare, one can use Regression for some of the below examples.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Predicting Length of Stay(LOS):</strong> The Revenue for a hospital is directly proportional to the total number of patient visits/discharges. In 2018 my mother had to be admitted for treatment of Pneumonia, and we were not sure how long would it take to get a discharge. Discharge is one aspect, but there is a certain amount of time my mother had to spend in the ICU. The uncertainty around the duration causes a lot of stress, and this is not limited to me but impacts any individual. Regression can be used to calculate the Length of Stay, which can be beneficial to the hospital for planning and scheduling but also the Patients relatives. This length of stay can be broken down by predicting the number of days in ICU as well as in a ward/room before discharge. Assuming this is a supervised learning model, some of the data elements which would be needed to effectively predict/build an algorithm would be <em>Primary Diagnosis, Secondary Diagnosis, Comorbid Conditions, Admit Date, Discharge Date, Days in ICU, Severity of Illness, Prior Admission Details, Medications, Physician Specialty, Date of Birth, Lab Results.&nbsp;</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Reduce Patient Readmissions:</strong> Once we have predicted the length of stay, the next logical step would be to find out the possibility of the patient getting readmitted. Readmission is another key concern, and in countries like the US, if a patient gets readmitted within 30 days, there is a possibility of a penalty to the Hospital. The readmission could be due to various reasons viz. “Patient Refused to take therapy” or “Hospital Acquired Infection” to name a few. In this case, we would require similar information/data elements like for LOS. Also, one can consider the <em>geographical location of the patient </em>(Address/Zip Code). We could also leverage external databases related to <em>the weather</em>. E.g., Cases of Pneumonia increase when the weather suddenly changes from Hot and cold and vice versa.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Healthcare Cost Prediction:</strong> The Healthcare Cost referred to, can be the Total cost of treatment based on the diagnosis/treatment. By the way, when we talk about regression, we refer to predicting a numerical value, and in this case, one can also find the possible Insurance Premium a member would pay. In this case, as well, one would require data elements used in LOS and Readmissions. Along with this, one could also require <em>Hospital Address/Zip Code, the Cost of Treatment (Prior Years).</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Chronic Disease Prediction:</strong> At the beginning of the paper, we spoke about the Rise of Computers. In this day and age one cannot live without a Mobile phone (which is a powerful computer in itself). It was 2009, and I had gone to visit an Orthopedic Physician as I had got a stiff neck. The doctor came, asked me mover your neck to the right, left, up down and laterally. One question he asked me, <em>“What is your Profession?”</em> I said I work in the <em>IT Industry</em> (Software). To that, he promptly mentioned, <em>“Your profession is your problem.”</em> For anyone who works in the IT industry, there is a very high probability that a person will get some neck or back problem. By the way, when we look at the young population, kids today use mobiles from the age of 5 &amp; 6 and the probability of getting a similar problem will be pretty high. One can use Logistic Regression to predict the probability of such cases. The data required for such cases might not be so easy to gather since we require <em>Lifestyle details</em>. Things like <em>smoking and drinking</em> are captured during the Patient visit, but what one eats daily is not captured in any system unless the patient is using some system and many such patients are willing to share this data. have&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>b. Classification and Clustering</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The Banking Industry uses Analytics, especially in terms of Identifying Fraud. I will give a simple example which helps with the explanation. I assume you have Debit Card or a Credit Card and you have used the same. If you use your card 3-4 times in a span of 10 to 15 minutes, it is more than likely you will get a call from the Bank. The customer support executive will ask you if you have just used your card. The reason this happens is because the system has flagged the transaction as a possible fraudulent case. The basis for flagging the transaction could be basis the fact that historically you don’t have such a spending pattern. On similar lines, one can also leverage these algorithms to identify Fraudulent Claims. A very apt example which I can quote here is identifying cases which could be denied for Medical Necessity. To detail the same, let us say a Patient comes to the hospital complaining of chest pain. The physician checks the patient vitals, asks the nurse to do an ECG and other relevant tests if required. All the data looks normal, but still, the Physician asks the patient to stay in the hospital. The patient gets discharged after four days. In this case, one can understand the patient is kept under observation for one day, but more than that without any supporting information, there are very high chances of the claim getting denied. Other examples where a similar algorithm can be used is the Classification of diseases based on Medical data. One can identify patients with similar issues/symptoms and diagnosis.<br>Classification is used when we have labeled data, if not, then we use Clustering. So, in case we don’t have Labelled information related to Fraudulent old claims, we can use Clustering to identify similar claims.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>c. Natural Language Processing</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In the lifecycle of a patient, the hospital captures a lot of information. This information comes in the form of Physician notes, Nurse Notes, Lab &amp; Radiology Reports, and Discharge summary. All of this information together forms Clinical Documentation. This documentation, when in electronic format, can be used in a very powerful way, and we will talk about a couple of use cases. Before a new drug comes in the market, there are a lot of clinical trials which are done. To do clinical trials, one needs to identify and enroll patients for such trials. The process is manual and time-consuming. Identification of Trial Patients is where one can use Clinical Text Mining to mine the Clinical. One such tool is CLIX ENRICH from Clinithink. The second aspect where we can use Text Mining is to identify disease progression. Mining Clinical notes of similar patients, we can gather a lot of information. Clinical Notes mining is possible by leveraging the power of SNOMED-CT. If you are not aware, SNOMED is a collection of medical terms and it has 100,000 plus concepts. Using this and the logic of engrams, we can identify key terms in the Clinical notes. Example, if the note says “Patient comes to the Hospital complaining of Chest Pain,” using SNOMED API’s we can find out if the word “Chest Pain” is a finding, diagnosis or any other aspect. This logic can also be extended to Medical Coding and Hierarchical Condition Coding where Medical Coders have to identify Clinical Terms for billing purposes.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>d. Time Series Forecasting</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In any business, it is very important to identify the volume of customers expected each day. The same is true in case of a Hospital as well; here is where one can use Time Series Forecasting, to forecast the Hourly Patient Volume. This volume can be forecasted based on prior patient volumes for the past three to four years. In addition to this, one can also leverage seasonal factors like climate to identify the impact on patient volume. Based on the seasonal data, one can also go to the extent of identifying Patient Volume for a specific type of disease. For examples, Emergency Cases/Fractures cases increase during festivals like Janmashtami. On similar lines, burn cases increase during Diwali. All of this information, when tied together, can be used to forecast Patient Volume and accordingly, we can also calculate the Resourcing needs.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>e. Survival Analysis</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Survival Analysis is generally used for a time to event analysis. This technique is widely used in the manufacturing industry to calculate the warranty period of the product. In healthcare, we can use Survival analysis to calculate the Probability of Survival after the diagnosis of a Disease. As per the Analysis published by IHME, Global Burden of Disease, Cardiovascular Diseases, and Cancer are the Top two causes of deaths in 2017. Cancer has been the top four causes of death since 1990, and as per National Cancer Registry Programme (NCRP), more than 1300 Indians die every day due to cancer. If Cancer is identified at an early stage, the chances of survival increase. In this case, the data which we would require is quite varied; we have listed some of the data elements which can be considered. <em>Age, Gender, Genetic Information (Defects), Skin Type, Location (Geography), Lifestyle (Alcohol, Tobacco, Food), Type of Job/Work</em>. Using this information (Survival Analysis), the physician can decide the medication and diet plan for the patient. Small changes in the lifestyle of a patient can help increase the survival rate of the patient.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>f. Deep Learning</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Deep learning is a branch of machine learning which can be used to mimic the human brain. There are various Machine Learning Algorithms around Deep Learning, a couple of them being Artificial Neural Network (ANN) and Convolutional Neural Network (CNN).<br><strong>Diagnostic systems</strong> – Neural Networks can be used to detect heart problems; this can be done using ECG information as well as other details like Stress Test. Some of the prominent use cases here are to identify Metastatic Breast Cancer and Skin Cancer. A very common example where Convolutional Neural networks (CNN) are used is in Pneumonia detection. Stanford University has built a 121 Layer CNN to identify 14 different diagnosis just using X-Rays.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Biochemical analysis</strong> – Analyze urine and blood samples, as well as tracking glucose levels in people with diabetes, determining ion levels in fluids, and detecting various pathological conditions.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Drug development</strong> – Another key area is the development of drugs for various conditions – working by using large amounts of data to come to conclusions about treatment options.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>How can India Leverage Analytics?&nbsp;</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>One of the biggest challenges for India is the lack of data(electronic), more than that the means to capture data electronically. Many hospitals do not use any form of a HIS (Hospital Information System) or EHR (Electronic Health Record). If you want to do Analytics, you need data and that too a large amount. Even if we implement a HIS/EHR from tomorrow, we would have to wait for two years to do some decent Analytics. HIS/EHR is a long-term solution, but not something organizations can use immediately. For us to start leveraging the power of Analytics, we need to take the help of Transfer Learning. In simple terms, Transfer Learning is using the research done while solving one problem and applying the same while solving another but related problem. My team. &nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Each year lot of deaths happen due to Pneumonia, and the best diagnosis for the same is using a Chest X-Ray. A Chest X-Ray is the most common diagnosis used in any scenario. If we want to start using Analytics in India, one of the areas to focus on can be in the area of Diagnostic Analytics. We can leverage Transfer learning in this area as there are many pre-trained models leveraged by others and available. One example is leveraging ImageNet to identify Pneumonia in Chest X-rays. If one would want to build this from scratch one can even leverage datasets provided by National Institutes of Health (NIH) which has 100,000 Chest X-Rays. In recent times Stanford has released 224,000 Chest X-Rays which can be leveraged for building an improved model.<br>If you would like to understand more about Healthcare you can download my book <a href="https://amazon.in/dp/B07SLKYS29" target="_blank" rel="noreferrer noopener">“Healthcare Decoded – Begin Your Health IT Journey”</a>. &nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>References</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>1. Retrieved from&nbsp;<br><a href="https://www.icmr.nic.in/sites/default/files/Media_Report_IN_news.pdf">https://www.icmr.nic.in/sites/default/files/Media_Report_IN_news.pdf</a><br>2. Comparing Hospital ER Wait Times. (2011, May 2). Retrieved from <a href="https://www.nbcdfw.com/news/health/Hospitals-ER-Wait-Times-Online-on-Billboards-121120879.html">https://www.nbcdfw.com/news/health/Hospitals-ER-Wait-Times-Online-on-Billboards-121120879.html</a><br>3. Burden of Disease. (n.d.). Retrieved from <a href="https://ourworldindata.org/burden-of-disease">https://ourworldindata.org/burden-of-disease</a><br>4. Life Sciences 06/16 Copy. (n.d.). Retrieved from <a href="https://clinithink.com/clinical-trials/">https://clinithink.com/clinical-trials/</a><br>5. Neural Networks in Healthcare. (2017, April 6). Retrieved from <a href="https://royaljay.com/healthcare/neural-networks-in-healthcare/">https://royaljay.com/healthcare/neural-networks-in-healthcare/</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2><strong>Author </strong></h2>
<!-- /wp:heading -->

<!-- wp:block {"ref":5873} /-->

<!-- wp:coblocks/highlight -->
<p class="wp-block-coblocks-highlight"><mark class="wp-block-coblocks-highlight__content"><strong>Harish Rijhwani </strong>  <a rel="noreferrer noopener" href="https://www.amazon.in/dp/B07SLKYS29" target="_blank">Link to Book: Healthcare Decoded</a></mark></p>
<!-- /wp:coblocks/highlight -->
