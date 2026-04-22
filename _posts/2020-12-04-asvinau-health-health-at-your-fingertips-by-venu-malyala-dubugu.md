---
title: "aśvinau health - health at your fingertips by Venu Malyala, @dubugu"
date: 2020-12-04 08:54:00 +0000
author: DigitalHealth Experts
original_url: https://hcitexpert.com/2020/12/asvinau-health-health-at-your-fingertips-by-venu-malyala-dubugu.html/
categories:
  - "#DIGITALHEALTH"
  - GUEST BLOG
  - Startup Showcase
tags:
  - Featured
---

<!-- wp:image {"id":7461,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://hcitexpert.com/wp-content/uploads/2020/12/Blog-by-Venu-Malyala-1024x512.png" alt="" class="wp-image-7461"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>EDIT - As of 28th Nov 2020, NDHM issued a clarification that HealthID will be made an OpenIDC as envisioned below. The below was written prior to that</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>India's National Digital Health Mission (NDHM) is great opportunity to adopt a truly digital health platform. A pandemic staring at us and with the evolution of policy, standards &amp; technology, a vibrant developer community, a workforce that can be trained, upskilled to deliver the digital services the timing has never been this urgent !</strong></p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>India witnessed massive success of digital payments in Unified Payments Interface (UPI) and has embarked developing a similar model for healthcare. However, fitting healthcare in UPI paradigm comes with its own challenges. In this article I list some of them. Let me know what you think</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1) UPI doesn't provision the user with a bank account. It provides a virtual id that links to the bank account. The custodian of the account is the bank. In NDHM there is a no such account. A new entity in Health Locker is needed, with an app as its user interface</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>2) In UPI once an asset is transferred, the ownership is changed. In NDHM even if an asset (read Personal health record - PHR) is shared, the ownership doesn't change. Therefore to safeguard privacy &amp; security, the asset should never leave the custody of the Health Locker. A recipient granted access&nbsp;<strong>must</strong>&nbsp;login into the PHR with their digitalID to view the shared assets. Even this is complex. The problem is the heterogeneity of the data. Not all users can be allowed to view all data. Expecting a patient to know the role of the recipient and share accordingly, is too naive. We are not talking selective sharing yet. UPI never had these issues</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>3) Assuming there will be multitude of lockers, the recipients may have to maintain as many logins, if not more, and is unmanageable. Therefore it is important to have one Digital HealthID with scopes, contexts properly attached to it, and proper audit/trail. UPI never had this problem. A lot of innovation is happening in this area, but the one I like &amp; think that can work is a&nbsp;<a href="https://www.ietf.org/" target="_blank" rel="noreferrer noopener">ieft.org</a>&nbsp;protocol called&nbsp;<a href="https://datatracker.ietf.org/wg/gnap/documents/" target="_blank" rel="noreferrer noopener">Grant Negotiation Access Protocol (GNAP)</a>, proposed by Justin Ritcher. The most I like about GNAP is this :</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://media-exp1.licdn.com/dms/image/C5612AQGO8DGXAENfqA/article-inline_image-shrink_1500_2232/0/1606267866259?e=1612396800&amp;v=beta&amp;t=pZ5LpwvT_adSJRmJt3jiBWq1fyvfFbGF2-y-SwJRRTA" alt="No alt text provided for this image"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Snip from a FHIR meetup youtube video. GNAP extends where OAUTH2.0 stops. As Justin Ritcher says :</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>To provide granular access, we must know what the grains are</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>This somehow is seen by some as digging a mountain out of mole hill. The argument begins by stating,&nbsp;<strong><em>"today we have none what is being stated, if it isn't a problem today, how would it be, later ?"</em></strong>&nbsp;The short and straight answer to any such arguments past, present, future would be :</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>Ease of Access</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Understanding this is not simple, often one needs to think like a bad actor and there are various scenarios, that we mayn't foresee all of them. But it is enough to say this can be a difference between life &amp; death and anything in-between. I can play scenarios, relate things from past, or even provide a&nbsp;<a href="https://en.wikipedia.org/wiki/List_of_genres" target="_blank" rel="noreferrer noopener">multi-genre</a>&nbsp;script that involves melodrama, romance, horror, comedy to really simplify it and explain. But that's not the intent of this article</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>4) A Patient will expect to consume services like book appointments, order medicines, purchase insurance using their Digital healthID. UPI it was never the case</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>5) All of this is not to be confused with Health Information Exchanges (HIE/HIX). We still need it to exchange data between Insurers (payors), Providers, states, registries, regulators and so on..</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>6) Once this is sorted out we can figure out, the semantic interoperability, managing consents (app/SMS/IVRS), terminology, archival, selective sharing and so on</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>7) We, at Appiarise, are working on a modern day healthcare app&nbsp;<strong>aśvinau health</strong>&nbsp;that is modeled on the above thought process. We plan to launch it in phase wise manner starting off with appointments, tele-consultation, roles based access control (RBAC), calendar &amp; scheduling, health records. It is expected to be launched soon</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here is a quick demo of the app  </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://www.youtube.com/watch?v=G9ZBVof9vdo&amp;feature=emb_title" target="_blank" rel="noreferrer noopener">aśvinau health iSPIRT healthathon - YouTube</a></p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>As it is often said.. solve the identity, the rest will fall in place</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>P.S :</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1) Removal of jargons and generalizing is simple terms is deliberate. Views expressed are individual</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>2) Let me know if you want to try out the app</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>3) Let me know instead, you are interested in the muti-genre script I mentioned above. It comes with a price tag, I am not known for faster delivery times, and I wrote "zero" such scripts before :-)\</p>
<!-- /wp:paragraph -->

<!-- wp:coblocks/author {"imgId":7462} -->
<div class="wp-block-coblocks-author"><figure class="wp-block-coblocks-author__avatar"><img class="wp-block-coblocks-author__avatar-img" src="https://hcitexpert.com/wp-content/uploads/2020/12/Venu_malyala.jpg" alt="Venu Malyala"/></figure><div class="wp-block-coblocks-author__content"><span class="wp-block-coblocks-author__name">Venu Malyala</span><p class="wp-block-coblocks-author__biography">I am an IT architect &amp; developer. I believe in IT enabling solutions for humanity. I founded Appiarise an IT Solutions company in April 2019. I am a HL7 India technical committee membe</p><!-- wp:button {"placeholder":"Author link…"} -->
<div class="wp-block-button"><a class="wp-block-button__link" href="https://www.linkedin.com/in/dubugu/" target="_blank" rel="noreferrer noopener">LinkedIn</a></div>
<!-- /wp:button --></div></div>
<!-- /wp:coblocks/author -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->
