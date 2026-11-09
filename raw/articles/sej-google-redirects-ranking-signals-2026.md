# Google Explains How Redirects Affect Ranking Signals

Source: https://www.searchenginejournal.com/google-explains-how-redirects-affect-ranking-signals/595967/
Author: Roger Montti
Published: 2026-11-05
Fetched: 2026-11-09
Note: News write-up of a Google discussion between Gary Illyes and Cherry Prommawin (Google Search Central). Article text extracted from HTML. Sections headed "My Takeaway" are the SEJ author's opinion, not Google's.

---

Google explains how redirect choices affect ranking signals, canonicalization, and which URLs appear in Search.

Google’s Gary Illyes and Cherry Prommawin discussed how permanent and temporary redirects affect canonicalization and ranking signals. They explained that both can help Google recognize related URLs but that they also signal different intentions about which URL should represent the content in Search.

## 301 Versus 302

One of the first things they did was to set the table and explain the difference between a 301 and 302 redirect.

- A 301 redirect tells the crawler that a change in the URL is permanent and that the search index should be updated with the new URL.

- A 302 redirect tells a crawler that a URL change is temporary and that the old URL will eventually be restored.

## A Page Will Be Indexed Regardless Of Which Redirect Is Used

Google’s Cherry Prommawin started off the discussion by stating that regardless of what redirect is used, a web page is still going to be indexed by Google. She then affirmed that there are correct choices.

Prommawin explained:

“First of all, relax. No matter which redirect you choose, one of your pages will stay in search and be part of AI training.

There are technically correct choices, but getting it wrong is not the end of the world. Google will still index a page. It’s really just a matter of which URL will show up.”

She then asked:

“Does Google actually care if both numbers, 301, 302, successfully take user to the new page anyway? Aren’t they basically doing the same job?”

Google’s Gary Illyes responded:

“Well, yes and no. Google’s crawlers don’t care at all.”

## Deduplication

The conversation next turns to deduplication which is the part where Google groups together similar pages then chooses one page as the one to represent all of the other similar pages in the search index.

Illyes explained:

“But we have to talk about the real battlefield here, the deduplication process.”

Prommawin explained what that means:

“Ah, the digital family reunion. This is where we look at a room full of identical siblings and try to organize them into a single happy family.

…So in search deduplication, our system have to group all pages with similar main content together. That’s clustering.”

Prommawin added that both 301 and 302 will have an effect on clustering similar pages together. But that only the 301 redirect will have a canonicalization effect.

Gary continued the explanation:

…then our index has to select just one official URL to represent this entire flock in the search results. Basically, within a cluster, we choose one representative page.

The final selection process is called canonicalization.”

### My Takeaway:

Illyes and Prommawin said that Google has a system for dealing with content that is very similar. Rather than rank no pages from a site, Google will choose to rank one page in a process called deduplication and the page that’s chosen to be representative of all the similar pages is called the canonical.

Some SEOs have this idea called content cannibalization. It’s a concept that began in the early 2000s to explain why pages weren’t getting indexed. The idea is that a group of pages are so similar that Google is choosing not to rank any of them because all of the ranking signals are diluted across all of the URLs with similar content.

But content cannibalization contradicts what we know as a fact about how Google treats similar content in the real world. Google clusters them and then chooses one as the canonical and transfers all of the ranking signals to that one URL.

What SEOs call “cannibalization” is really some other problem like a lack of uniqueness, thin content, and all the other real reasons that cause Google to not index a web page.

## 301 Redirect Transfers Ranking Signals

The next thing they explained is that:

- 301 (permanent) redirect will transfer ranking signals from the old URL to the new URL.

- Google will not transfer ranking signals when it encounters a 302 (temporary) redirect.

With a 301 redirect the ranking signals from the old page/pages will transfer to the new URL which will then be the canonical.

Gary explained how the 301 redirect works:

“Google takes all the ranking signals of the old page and hands them to the new page.”

Then he explained why the 302 does not transfer ranking signals:

“Google assumes you are going back eventually, keeps the old URL in the search results, and basically ignores the new URL.”

So if you use a 302 redirect then the new URL will be “basically” ignored by Google.

## Google Explains When 307 And 308 Redirects Are More Appropriate

They next explained that 307 and 308 redirects serve the same kind of general temporary and permanent purposes as the 302 and 301 redirects. The difference is in how browsers handle submitted “post” data. Post is a reference to data that’s submitted from a web browser to a server using the HTTP POST method, such as when someone fills out a contact form and presses the “submit” button.

Illyes explained:

- “A 308 is the more modern version of a permanent 301.

- A 307 is the modern version of a temporary 302.

The only major difference is how they handle post data.

…Imagine our chicken is on your website on Black Friday and it just filled out a massive checkout form with its credit card and shipping details. It hits submit, but oh no, the site’s primary payment server is completely overloaded, so it triggers a quick failover redirect to the backup server.”

If a site uses a 302 redirect the data is lost. But if the site uses a 307 redirect the data is saved in the browser.

Illyes continued his explanation:

“But if you use a 307 redirect, it instructs the browser: Keep the data intact, keep the connection as a post request, and forward the exact same data to the backup payment processor.

The user just sees a brief loading wheel maybe, but the transaction goes through…”

## Google Recommends Server-Side Redirects Over JavaScript And Meta Refreshes

Lastly, Google recommends using server-side redirects like 301s and 302s rather than the old “meta refresh” or JavaScript redirects.

Illyes explained the reason why:

“A server-side HTTP redirect is a clean, instant instruction. JavaScript and meta refreshes force the browser to download the page, parse the code, wait for the script to execute, and then launch the user somewhere else.”

## Takeaways

The overall takeaway is that redirects are not just a way to forward visitors to another URL. They also communicate whether a move is permanent or temporary, influence Google’s canonicalization decisions, and can affect website functionality.

Google explained URL clustering and canonicalization, explaining that both 301 and 302 redirects work for clustering, but a permanent 301 is the recommended choice for identifying the canonical URL.

