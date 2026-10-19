# GitHub Search Engine Optimization (SEO): how to rank your repository in GitHub search

Source: https://www.markepear.dev/blog/github-search-engine-optimization
Author: Jakub Czakon (CMO at a dev tool startup; dev marketing advisor)
Published: 2024-07-03 (per meta description; article screenshots/observations appear to date from ~March 2022)
Type: practitioner blog (Developer Markepear)
Retrieved: 2026-10-19

Note: the original embeds live GitHub search result screenshots for each example query; images not downloaded.

GitHub search engine optimization (GitHub SEO) or optimizing your project repo for the GitHub search engine is easier than you think.

Really. Or certainly was easier than I thought it would be.

We have recently revamped our Readme.md hoping to get more traffic from people searching for product-related keywords on GitHub and not much changed.

That got me thinking.

If Readme.md is not an important ranking factor then what is?

It turns out that you can push your project to the top **by tweaking the About and Topics sections of your GiHub repository.**

Obviously, your project needs to be a real thing with code, commits, stars, and watchers. But keeping all of those things “as they are” and optimizing About and Topics you can make your project rank on GitHub search.

Yep, crazy, made me question everything as well :)

In this article I will talk about:

- GitHub search ranking factors
- How to optimize your repository for GitHub search

Let’s get to it!

## GitHub search engine: what are the ranking factors?

I always thought ranking on GitHub is some combination of stars, and Readme.md text. Perhaps a bit of good old page rank.

In an older discussion on Quora people claimed it was by Watchers or Forks.

The reality seems to be a mix of that plus some completely different things.

From my recent research, the GitHub search ranking factors in no particular order are:

- Name
- About
- Topics
- Stars
- Watchers
- Forks

Let’s just type in **“data visualization python”** and see the results.

https://github.com/search?q=data+visualization+python

GitHub even shows us what it is looking at by highlighting those things in there.

Ok, so explain this.

Why is bokeh with 16k stars and 3.9k forks below seaborn with only 9k stars and 1.6k forks?

Or why **"Data-Visualization"** repo with 328 stars is below **"data-visualization"** repo with 667 stars?

I know it feels weird but **my bet is on the About and Topics sections**. And you can change those and see better results in almost real-time.

Not saying that Watchers, Forks, or stars are not important. They are, but you cannot directly impact those numbers anyway. And for the repository Name, most of the time you already have it set.

Let’s talk about optimizing all of those ranking factors for GitHub search.

## How to optimize repo for GitHub search engine (SEO)?

To optimize rankings for your GitHub repo you need to take care of:

- Name
- About
- Topics
- Stars, Watchers, and Forks (via traffic, Readme.md, and just having a project that is useful to people :) )

We’ll talk about how to do that now.

## Optimizing repository Name

Whether your repository name includes a keyword or a variation of it is a big factor in search ranking.

For example, let’s type in **“deep learning python”**

https://github.com/search?q=deep+learning+python&type=Repositories

**“deep-learning-with-python-notebooks” **ranks first, in front of the most popular python deep learning framework **“keras” **with 4x stars.

Or a **“DeepLearningPython” **repo with only 2.2k stars ranks way higher than one of the most popular deep learning libraries **“fastai” **with 22k stars.

The only reasonable explanation IMHO is the Name of the repository.

So if you can put your core keywords in the repository name try and do that.

## Optimizing the About section

If you take anything from this article it is this.

**Include your core keywords and not much else in the About section.**

Let’s check a competitive keyword **“monitoring”**:

https://github.com/search?q=monitoring&type=Repositories

The search term, or variations of it (’monitor’), are in the About. It is absolutely crucial to include your keywords there.

But how come **“cgm-remote-monitor”** end up higher than **“prometheus” **that has 20x GitHub stars?

I think one of the ranking factors is the **percentage of search terms in all words from the About** section.

To prevent stuffing all possible keywords in the About section, GitHub search has a simple mechanism to figure out how essential to the project the search term is.

Taking the **“cgm-remote-monitor”** example, the About has only 3 words “nighscout web monitor” and **“prometheus”** has 8.

By the same token, you could explain **“prometheus” **ranking higher than **“netdata”.**

And it makes a lot of sense to do it this way.

You, as the project author, have to figure out what keywords are core to your project and put them in the About secion. You need to figure out what is important and what isn't.

Now, **should you just put a list of keywords** and nothing else?

Not really, it should be readable.

Assuming you come up in the GitHub search results **you also want people to go to your repo.**

So make the description pop.

For example, typing in **“javascript testing”** I got:

https://github.com/search?q=testing+javascript&type=Repositories

As we talked about before, putting keywords in the name made a repo with best practices outrank **“facebook/jest”,** but the interesting part is the **use of emojis in the description**.

It catches attention. I think using three emojis is probably too much but adding one, especially something that contrasts with the blue colors of GitHub is a great idea.

You can find a full list of GitHub emojis here. Just remember that the word count of the emoji counts to the word count of the About section (and to the % of search terms in the About).

Other than that I think it is just important for the description to be:

- short not to overstuff keywords
- convincing that your repo is about what I am searching
- somewhat different from other search results

## Optimizing Topics

While GitHub is looking for keywords and variations of a keyword in the Name and About sections, **with Topics it is an exact match of the search keyword**.

For example, you put **“orchestration data science”** and get:

https://github.com/search?q=orchestration+data+science&type=Repositories

But if you go **“orchestration data-science”** you get:

https://github.com/search?q=orchestration+data-science&type=Repositories

The difference is that for the second query **“data-science” **was in the Topics.

And do you know anyone who searches for **“orchestration data-science”**?

I don’t.

Topics with multiple words get a "-" between them so if you are optimizing for search, **use single words in the Topics**.

Another thing is that you can only use 20 Topics per repository so it is important to choose them wisely. If you already have certain keywords in the About or Name you should probably drop them from your Topics.

Think about **Topics not only as something that extends your About, but makes the search more specific.** Sometimes you can show up as almost the only repository for some specific search.

For example, say we wanted to find those orchestration tools for keras models and type **“orchestration keras”:**

https://github.com/search?q=orchestration+keras&type=Repositories

There are only 4 results and basically, only Polyaxon makes sense. Even though it is not the only orchestration framework that works with Keras. It is just the only one that has it listed in the Topics.

## Getting more Stars, Watchers, and Forks

While those things definitely play an important role in ranking on GitHub search you cannot really affect them directly. You need to get more people interested and actively using your project and hope they will star, fork, or watch it.

#### **Get people to see your repository page**

You need to get as many people as possible to see your project.

To do that you can use all the typical promotion channels like:

- Reddit
- Twitter
- Medium
- Slack communities

I am not going to get into this here as promoting projects is another subject entirely. You can read this guide if interested.

#### **Help people understand what you are doing and get inspired to try it**

This is where a good Readme.md comes into play.

Readme.md is a landing page of your project so make sure it answers questions and looks good.

The main **questions it should answer are**:

- What does this project do?
- How do I get started?
- What libraries/frameworks/languages it supports?
- How to install it?

By **looking good** I mean:

- have a **visual** or GIF that shows the results you can get with the project
- have some nice c**ode examples**, preferably things I can copy-paste
- have **tags** for languages, frameworks, Twitter accounts, the website page (if you have it), and things like that.

There is obviously more to it but this should get you started. If you want to dive deeper, some good resources on optimizing Readme.md and promoting a GitHub project I found are:

- How we got our 2-year-old repo trending on GitHub in just 48 hours
- How I got 1,000 stars on my GitHub Project, and the lessons learned along the way
- How to get up to 3500+ GitHub stars in one week

#### **Get people to use and benefit from your tool or project**

Ok, throughout this article, I sort of assumed that your project is valuable to some people. If not then you probably have bigger problems to solve than optimizing your GitHub search rankings.

But say use your tool or project and like it. You should try and get them to spread the word or at least drop you a GitHub star.

A cool tactic I saw, is a hello bar at the top of docs or website.

https://docsearch.algolia.com/

Sometimes people just need a little nudge. I think a hello bar with a basic ask has this tasteful balance.

If Algolia who is known for one of the best developer experience out there does it I think we are safe to assume it is not too pushy.

In case you were interested in some other cool tactics Algolia uses in developer marketing you can check out this article.

## What is next?

If you remember one thing from this article it is this: get your About and Topics optimized for rankings. If you can choose an optimized Name as well, awesome!

Once you have people flowing to your repo, optimize the Readme.md to get more people to understand and use your project and later star, watch and fork your repo.

Ok, now go and optimize your GitHub project!

Hey, I am Jakub Czakon. CMO at a dev tool startup and a dev marketing advisor.‍
