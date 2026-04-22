---
title: "Explainable artificial intelligence in healthcare by Dr. Johnson Thomas, MD, FACE, @JohnsonThomasMD"
date: 2020-02-25 10:56:00 +0000
author: DigitalHealth Experts
original_url: https://hcitexpert.com/2020/02/explainable-artificial-intelligence-in-healthcare-by-dr-johnson-thomas-md.html/
categories:
  - AI/ML/DL
  - GUEST BLOG
tags:
  - Artificial Intelligence
  - Dr. Johnson Thomas
---

<!-- wp:image {"align":"center","id":5559,"sizeSlug":"full"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://hcitexpert.com/wp-content/uploads/2020/04/DrJohnson-Blogs.png" alt="" class="wp-image-5559"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Debates are raging on social media regarding explainable AI in healthcare. Geoffrey Hinton, one of the ‘godfathers of AI’ recently tweeted – “Suppose you have cancer and you have to choose between a black box AI surgeon that cannot explain how it works but has a 90% cure rate and a human surgeon with an 80% cure rate. </p>
<!-- /wp:paragraph -->

<!-- wp:more -->
<!--more-->
<!-- /wp:more -->

<!-- wp:paragraph -->
<p>Do you want the AI surgeon to be illegal?”. [JT1] As you can imagine twitterverse took sides. One camp argued that healthcare AI should be explainable and other camp argued that we should not sacrifice usefulness for explainability. &nbsp; There are different approaches to explainability. In linear models we could use the weight for each variable to determine how much it contributes to the prediction. In medical image classification we could use Eli5, LIME, and SHAP to explain the predictions. This adds another layer of computing complexity and in turns requires more computing resources and time. &nbsp; </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Why can’t we combine good accuracy and explainability in the same software? When faced with a clinical problem, we decided to combine the best of both worlds. More than 50 percent of women over the age of 50 have thyroid nodules. Because of increased use of imaging modalities, we are detecting more of these thyroid nodules. But, only about 5 to 10 percent of these nodules are cancerous. At present, the only way to identify whether there is cancer in these nodules are by invasive procedures like surgery and needle biopsy. We employed artificial intelligence to create a model that will help physicians to choose the right nodule for biopsy. In our study published in Thyroid journal[JT2] , we showed that by employing this model (AIBx), unnecessary biopsies could be reduced by more than 50 percent. The probability that a nodule is actually benign when the model predicts it to be benign, namely the negative predictive value of AIBx was 93.2 percent. &nbsp; AIBx&nbsp; finds similar images to the test image and displays those images along with their actual diagnosis. Physician reviews these similar images and the corresponding diagnosis to make the final decision. Our model was created to enhance the physician’s ability to choose the right nodules for biopsies rather than replace the physician. Every step of this process needs physician’s input and hence we used the term Physician in Loop (PIL). Latest version of AIBx also overlays heat maps over the test image to show areas of interest that resulted in the prediction. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>By combining image similarity and heat maps (class activation maps) we made it an explainable model. This in turn increases physician’s trust in the model. &nbsp; In conclusion, using an explainable artificial intelligence model helps to increase the trust in the model’s predictions. A physician refers a patient to a surgeon based on his or her trust in the surgeon. Similarly, AI algorithms that increase trust in their prediction will be preferentially used than black box algorithms, this is my answer to Geoffrey Hinton’s question. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For more information about our research, please visit <a href="https://www.thyroidbx.com/">https://www.thyroidbx.com/</a> &nbsp; </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To read our clinical research article in Thyroid journal, please visit <a href="https://www.liebertpub.com/doi/abs/10.1089/thy.2019.0752">https://www.liebertpub.com/doi/abs/10.1089/thy.2019.0752</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>References:</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>&nbsp;[JT1]<a href="https://twitter.com/geoffreyhinton/status/1230592238490615816">https://twitter.com/geoffreyhinton/status/1230592238490615816</a> &nbsp;[JT2]<a href="https://www.liebertpub.com/doi/abs/10.1089/thy.2019.0752">https://www.liebertpub.com/doi/abs/10.1089/thy.2019.0752</a></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>AUTHOR:</h2>
<!-- /wp:heading -->

<!-- wp:block {"ref":5851} /-->
