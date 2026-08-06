# Publishers and Developers - FAQ (OpenAI Help Center)

Source: https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
Publisher: OpenAI (Help Center)
Status: living document — "Updated 7 days ago" as of capture (≈ 2026-07-30)
Captured: 2026-08-06 (via in-app browser; WebFetch returned 403)

---

## Publisher FAQs

### How can I get my website to appear in ChatGPT search results in the browser?

Any public website can appear in ChatGPT search. To help ensure content
can be discovered, surfaced, cited, and linked:

- For content to be included in summaries and snippets in ChatGPT, make
  sure you aren't blocking **OAI-SearchBot**. Update robots.txt if
  necessary to ensure OAI-SearchBot has access.
- Note: if OpenAI obtains the URL of a *disallowed* page from a
  third-party search provider or by crawling other pages, and has signals
  the page is relevant to a user's query, it may surface **just the link
  and page title in ChatGPT Atlas**.
- To prevent this, use the **noindex meta tag**. For the crawler to read
  the meta tag, it must be allowed to crawl the page.
- Publishers who allow OAI-SearchBot can track referral traffic from
  ChatGPT via analytics (e.g. Google Analytics). ChatGPT automatically
  includes **`utm_source=chatgpt.com`** in referral URLs.

### Does ChatGPT Atlas train on my web page content?

- Publishers should **disallow the GPTBot user-agent** from sites/pages
  they wish to exclude from potential training. OpenAI respects this signal
  for content acquired via users' interactions in Atlas.
- Note: if users opt in to training, webpages that opt out of GPTBot will
  not be trained on.

## Developer FAQs

### What can I do to improve my website performance with ChatGPT agent in Atlas?

- **Making your website more accessible helps ChatGPT Agent in Atlas
  understand it better.**
- ChatGPT Atlas uses **ARIA tags — the same labels and roles that support
  screen readers — to interpret page structure and interactive elements.**
- To improve compatibility, follow **WAI-ARIA best practices**: add
  descriptive roles, labels, and states to interactive elements like
  buttons, menus, and forms. This helps ChatGPT recognize what each element
  does and interact with the site more accurately.

### How do apps built with the Apps SDK work in Atlas?

- Apps in ChatGPT work in Atlas the same way they work in ChatGPT on the
  web; naming an available app in a message (e.g. "Spotify, make a
  playlist…") can surface the app. First use prompts a connect step.
- Recommend testing apps within the Chat sidebar to ensure they work at
  smaller widths. Deeper Atlas integrations are being worked on.

---

## Notable for the wiki

- First-party confirmation of OpenAI's three user agents by function:
  **OAI-SearchBot** (ChatGPT search indexing/citation), **GPTBot**
  (training; opt out to exclude), **ChatGPT-User / ChatGPT Agent** (live
  user-triggered fetch/agent action in Atlas).
- First-party confirmation that **ChatGPT Atlas's agent reads ARIA/the
  accessibility tree** to understand and operate pages.
- Clarifies the robots.txt-vs-noindex distinction for ChatGPT: blocking
  OAI-SearchBot doesn't guarantee the link/title won't surface; noindex
  does (but the page must be crawlable for the tag to be read).
