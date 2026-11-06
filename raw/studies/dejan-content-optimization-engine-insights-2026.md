Source: https://dejan.ai/blog/coe/
Author: Dan Petrovic (DEJAN AI)
Published: 2026-07-08
Retrieved: 2026-11-06

# Content Optimization Engine Insights by DEJAN AI


![Content Optimization Engine Insights by DEJAN AI](/media/header/posts/coe-4707de15.png)


# Content Optimization Engine Insights by DEJAN AI

![](https://lh3.googleusercontent.com/a/ACg8ocIzPbX1yzNoZGisEyNHQT2qdNnPceJVlyoTQ1N2MGmg9fO-sR1t3A=s96-c)

We spent 2.71 Billion tokens teaching a machine to reverse-engineer how AI search ranks pages. What it found overturns the usual SEO playbook: structure and intent beat every credential you've been told to add, and the engine that proved it reached #1 in 1,554 of 2,246 runs.

![](/media/images/misc/arrow-marker-left.svg)

In AI search, users don't interact with the traditional search results anymore. The good old 'ten blue links' is now considered the raw data and is supplied as grounding context.

We went from this:

(#1) The 9 Best Running Shoes for Beginners runnersworld.com Tested picks for new runners, ranked by cushioning and fit.

(#2) Best Beginner Running Shoes (2026) nytimes.com/wirecutter Our favourite after 40 hours of testing and 50 miles per shoe.

(#3) How to Choose Your First Running Shoes brooksrunning.com A beginner's guide to cushioning, support, and fit.

To this:

For a first pair, most guides point to the (#1) Brooks Ghost as the safest all-rounder, thanks to its soft, forgiving cushioning. The (#3) Hoka Clifton is the other favourite if you want the most padding underfoot, while the (#3) ASICS Gel-Nimbus earns a mention for stability on longer first runs.

Between the search engine and the user is a language model which now acts as both a filter and a re-ranker. This opinionated mega-influencer decides what brand, product or service to recommend and in which order.

The question on every SEO's mind is, how do we influence the influencer?


### Here's how we do it.

Our algorithmic content optimization framework forms a set of testable hypotheses about why a page sits where it does, rewrites the page one careful edit at a time, asks an AI ranker to re-judge it against its real competitors, and keeps only the changes that genuinely move it up. In plain terms, it is a tireless scientist whose entire job is content optimization: propose, test, discard, repeat, until the page wins or the evidence runs out.

We let it run. A lot. Across 2,249 experiments on 113 properties it chewed through 2.71 Billion tokens of reading and writing, and in the process it produced something rare in our field: a large, controlled body of evidence about what an AI ranker actually rewards. This article is what that evidence says.


## The scale of it

Every figure below is a total from real optimization runs on real client pages.

To put the ranking effort in perspective: the engine re-ranked every edit around five times and took the middle result, so a single fluke could never be mistaken for a real gain. That discipline is why there were nearly 56,000 ranking passes sitting on top of only 10,548 edits.


## How it works

Every experiment follows the same loop, and it mirrors how a careful person would reason if they had infinite patience.

- Read the field. The engine pulls the page and the competitors currently winning for the query, and asks a ranker to place the page in that field as a baseline.

- Form hypotheses. It writes a handful of testable claims about why the page ranks where it does, each with a calibrated, measured prior on how likely it is to matter.

- Make one change. It picks the most promising untested idea and expresses it as a single, concrete edit to the page or its grounding snippet , changing one thing so the effect is attributable.

- Re-rank and learn. The ranker re-judges the edited version against the same competitors. If the page moved up, the idea earns belief; if not, it loses belief. The winning version carries forward, and the loop repeats.

It stops when the page reaches the top, when it runs out of budget, or when the evidence on every remaining idea has settled. The result is a documented trail of what helped, what hurt, and what did nothing.


## What the machine learned

Here is the finding that should make anyone in this industry sit up. When we group every tested idea into the family it belongs to and measure how often each family produced a genuine rank improvement, the winners are not the things the SEO industry tells you to add.

Idea family

What it covers

Win rate

Framing

How the page is angled: a list, a definition, a how-to

31.4%

Alignment

Matching the query's actual words and intent

26.2%

Architecture

Structure: the opening line, sentence length, formatting

25.4%

Style

Voice, register, readability

25.2%

Substance

Facts, named entities, numbers, definitions

25.1%

Proof

Credentials: awards, expert endorsements, citations

15.4%

Proof came last, at roughly half the win rate of everything else. The single most effective levers were about how a page is framed and how well it speaks to the query. The least effective levers were exactly the trust signals that dominate optimization advice.

Zoom into individual tactics and the gap gets starker. These were the strongest and weakest single ideas across the whole program.

Strongest levers

Win rate

Weakest levers

Win rate

"Best of" / top-N list framing

38.4%

Awards and certifications

13.1%

"What is" / definition framing

36.7%

Expert endorsements

14.8%

Clear category definitions

33.3%

Scale signals (user counts, volumes)

15.6%

Short, concise sentences

33.1%

Statistics and study citations

18.2%

How-to / step-by-step framing

30.9%

.gov / .edu citations

18.9%

Matching the query's intent

27.7%

Adding more raw numbers

20.7%

The plain reading: an AI ranker choosing between two comparable pages is swayed far more by how clearly a page is framed and matched to the question than by how decorated it is with credentials. Awards, expert names, and citation badges are worth having for the humans who read your page, but they are close to the bottom of the list of things that tip an AI ranker in your favour.


## The engine argued itself out of most of its own ideas

One more number is worth dwelling on, because it is the opposite of how optimization is usually sold. Of every hypothesis the engine tested, it revised its belief downward 5,911 times and upward only 1,440 times . The machine spent most of its energy disproving plausible-sounding ideas. That is the whole point of testing: most confident advice does not survive contact with evidence, and a system that only ever finds reasons to agree with itself is not measuring anything.


## Did it actually move pages?

Yes, and here is the full accounting. Not every edit is a winner, because that is what real experimentation looks like.

- The engine drove a page to the number one position in 1,554 of 2,246 runs , about 69% of the time.

- Across the program, pages climbed a combined 6,092 positions from where they started to their best result, averaging 2.74 positions gained per experiment .

- 2,695 individual edits improved a page's position, roughly one in four of every edit tried. A winning edit lifted the page 2.31 places on average, and the single biggest jump was 10 places from one change.

- Underneath that, the raw churn: edits added up to 6,215 positions of upward movement against 3,788 of downward movement, a net gain of 2,427 places after the losing experiments are subtracted.

Three out of four edits either held steady or slipped. That miss rate is the method working as designed. The value is in cheaply finding the one edit in four that works, and never shipping the three that do not.


## Where all the tokens went

The 2.71 billion figure is not spread evenly, and the shape of it tells you something about the problem. Judging content is far more expensive than writing it. The ranking step alone consumed about 83% of all tokens , because every ranking pass re-reads the entire competitive field, every rival page alongside the one being edited, on each cycle. Writing the edits was comparatively cheap.

The same story shows up between the two modes the engine runs in. Optimising a full page rather than a short grounding snippet accounted for just under a third of all experiments but 91% of all tokens , because ranking whole pages against whole pages, over and over, is where the real work lives. Knowing this is what lets us aim the heavy machinery only where it earns its keep.


## But here's the 'it depends' element.

On the left are the top positive and negative rank factors specific to Gemini alongside the number of times they've increased or decreased the brand's rank during our testing.

Look at the top two most impactful rank factors. They're also at the top of the negative rank factor list. Not as strong (+1701, +1101 vs -81, -80) but still the message is clear. Something which can move your brands odds in your favour for one query or competitive set can do the exact opposite in a different setting.

This means that while we can rely on our rank factors as a general rule, every proposed content edit must be thoroughly tested on its own.

![A slope chart connects positive ranking gains on the left to corresponding negative losses on the right.](/media/images/posts/coe-3.png)

Here's how the above rank factors group by rank factor class.

![A slope chart compares positive and negative ranking categories, showing alignment as the top gain and architecture as the top loss.](/media/images/posts/coe.png)


## What this means for you

The comforting takeaway is that the biggest levers are the ones you can actually pull. How a page is framed, how directly it answers the query, how cleanly it is structured: these are all in your hands, and they are exactly what the evidence says move an AI ranker. The credential signals that are hardest to manufacture turn out to matter least to the machine, even as they remain worth having for the people who read you.

One caveat, stated plainly: this measures what shifts an AI ranker's preference between competing pages in a controlled setting, across four leading models. It is not a claim about every live search system, and it is not a substitute for building genuine authority over time. It is 2.71 billion tokens of tested evidence pointing in one clear direction. Most of what passes for optimization advice has never been tested at all. This has.

Content Optimizer is part of the AI-visibility platform built by DEJAN AI . Related reading: Grounding Snippets and In AI SEO, #10 is the new #1 .