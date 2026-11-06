Source: https://dejan.ai/blog/google-store-alt-text/
Author: Dan Petrovic (DEJAN AI)
Published: 2026-10-31
Retrieved: 2026-11-06

# We rewrote the alt text on Google Store's Pixel Watch 5 page. Its images went from a 30% to an 84% match.


![We rewrote the alt text on Google Store's Pixel Watch 5 page. Its images went from a 30% to an 84% match.](/media/header/posts/google-store-alt-text-6fe42b30.png)


# We rewrote the alt text on Google Store's Pixel Watch 5 page. Its images went from a 30% to an 84% match.

![](https://lh3.googleusercontent.com/a/ACg8ocIzPbX1yzNoZGisEyNHQT2qdNnPceJVlyoTQ1N2MGmg9fO-sR1t3A=s96-c)

Google Store's Pixel Watch 5 page has 109 images. 47 had no alt text and menu images carried labels like "Browse all offers". After a page scan in Image Optimizer, the average match between alt text and image rose from 30% to 84%.

![](/media/images/misc/arrow-marker-left.svg)

Google Store's Pixel Watch 5 page has 109 images. 47 of them had no alt text, and the menu images carried labels such as "Phones" and "Browse all offers". We ran the page through Image Optimizer's page scan in DEJAN App . Across the 95 images we report on, the average match between each image and its alt text rose from 30% to 84%. The page's main content images went from 2% to 93%.

![Dumbbell chart of average alt text match on the Google Store Pixel Watch 5 page: all 95 images from 30% to 84%, main content images from 2% to 93%, images that had alt text from 58% to 78%](/media/images/posts/google-store-alt-page-alignment.png)

The full scan is public: Google Store page scan , with every image, its old and new alt text and both scores.


## What the page had

- 109 images: 63 in the page's main content and 46 in the site menu.

- 47 images with no alt text, 45 of them in the main content: product photos, watch faces, health and sleep screens.

- Menu images whose alt text is the menu label, such as "Phones", "Laptops" and "Browse all offers".

- Placeholder alt text: "Aria Label 2" on 8 images, and "Image 1 Desktop" and "Image 1 Mobile" on 3 each.

- One portrait of Stephen Curry whose alt text describes a different image: "A Pixel phone shows that it has detected a pair of Pixel Buds and asks the user if they want to connect."

Of the 48 images with real alt text, 30 scored under 60%.


## How the scan works

![Diagram of a page scan: a page URL, every image with its alt text, sorted into main content and menus or icons, fixed by filling gaps, Quick Fix or deep optimization, scored before and after, and the better text accepted](/media/images/posts/google-store-alt-page-mode-diagram.png)

The scan fetches the whole page and lists every image with its alt text and where it sits. One AI call sorts the images into the ones the page is about and the rest (menus, icons, badges), and writes alt text for images that have none. Each image then gets one of three fixes:

- Fill: new alt text for images that have none.

- Quick Fix: one rewrite using the image, the page and the current alt text.

- Deep optimization: ten rewrites, each scored against the image, keeping the best.

We deep-optimized the 61 main content images and used Quick Fix on the 46 menu images. Two decorative images were marked to keep an empty alt.

The score is the match between an image and its alt text as Google's multimodal embedding model sees it: the model places both in the same vector space, and the closer they sit, the higher the score. Image and text pairs rarely go above a cosine similarity of 0.60, so the tool shows 0.60 as 100%. Product, model and brand names in the original alt text are kept as written.


## One image, step by step

The store's alt text for this image describes "a macro shot of two Pixel Watch Two-Tone Leather Bands". The image is a collage of people wearing them. That text scores 43%. The first rewrite describes the collage and scores 77%. Each later rewrite sees the image and every earlier version with its score, keeps what raised the score and drops what lowered it. Step 10 won with 87.4%, 0.1 points above step 7.

![Line chart of one deep optimization run on the Pixel Watch Two-Tone Leather Bands collage: the original alt text scores 43%, the first rewrite 77%, later rewrites move between 78% and 87%, and step 10 is the finalist at 87.4%](/media/images/posts/google-store-alt-run-walkthrough.png)

Step

Match

Alt text

Original

43.0%

A macro shot of two Pixel Watch Two-Tone Leather Bands. One is in Porcelain color; the other is in Bay color.

1

76.9%

Athletic people wearing Pixel Watch Two-Tone Leather Bands, including a woman in red sportswear outdoors and a man stretching in sunlight.

2

80.7%

Fitness models wearing smartwatch bands outdoors: woman in red athletic wear, man stretching, and woman in green skirt with Pixel Watch Two-Tone Leather Bands.

3

84.0%

Collage of active people wearing Pixel Watch Two-Tone Leather Bands: woman in red crop top, man stretching, and wrist with pink strap.

4

82.0%

Collage of athletic models wearing Pixel Watch Two-Tone Leather Bands, featuring a woman in bright red activewear and a man stretching outdoors.

5

77.7%

Three panel collage of athletic people wearing Pixel Watch Two-Tone Leather Bands: woman in red, man stretching, and wrist with pink strap.

6

84.7%

Collage of active people wearing Pixel Watch Two-Tone Leather Bands: woman in red, man stretching in sunglasses, and wrist with bright pink strap.

7

87.3%

Collage of active people wearing Pixel Watch Two-Tone Leather Bands: woman in red activewear, man stretching in sunglasses, and wrist with pink strap.

8

84.0%

Collage of people wearing Pixel Watch Two-Tone Leather Bands: athletic woman in red activewear, man stretching wearing sunglasses, and wrist with pink strap.

9

86.9%

Collage of active people wearing Pixel Watch Two-Tone Leather Bands: woman in red activewear, man stretching in sunglasses, and a wrist with pink band.

10

87.4%

Collage of active people wearing Pixel Watch Two-Tone Leather Bands: athletic woman in red activewear, man stretching in sunglasses, and wrist with pink strap.

Full run: Pixel Watch Two-Tone Leather Bands .


## Results

![Chart of all 95 images on the page, each with its match before and after: 47 images without alt text rise from 0% to between 73% and 100%, and 48 images with alt text rise from between 28% and 80% to between 61% and 88%](/media/images/posts/google-store-alt-per-image.png)

Before

After

Average match, all 95 images (no alt text = 0%)

30%

84%

Main content images (47)

2%

93%

Images that had alt text (48)

58%

78%

Images with alt text under 60%

30

0

Images with no alt text

47

2 (decorative)

No image scored lower after the rewrite.

We report on 95 of the 109 images. On the 14 images with placeholder alt text, the rewriter kept the placeholder words, because it is told to keep names from the original alt text, so we left those images out.


## Examples

The menu image the store labels "Browse all offers":

![Google Store menu image of a coral Pixel phone and Pixel Buds Pro: alt text Browse all offers at 55% match, Quick Fix alt text describing the phone and earbuds case at 81%](/media/images/posts/google-store-alt-ex-browse-offers.png)

The menu image labelled "Phones":

![Google Store menu image of a rose pink Pixel phone: alt text Phones at 60% match, Quick Fix alt text describing the rear view of the phone at 75%](/media/images/posts/google-store-alt-ex-phones.png)

A health notification image with no alt text:

![Pixel Watch health alert card with no alt text at 0%, deep optimized alt text describing the irregular rhythm notification at 100% match](/media/images/posts/google-store-alt-ex-health-alert.png)

A Pixel Watch 5 with a Stephen Curry strap, also with no alt text:

![Back of a Google Pixel Watch 5 with a woven Stephen Curry LockIn strap: no alt text at 0%, deep optimized alt text at 100% match](/media/images/posts/google-store-alt-ex-lockin-strap.png)


## Try it

The page scan is in DEJAN App , under Content Optimizer, Image, Page. A single image can be optimized for free with the public Image Optimizer . Our first look at the method walks through one Fitbit Air image step by step.