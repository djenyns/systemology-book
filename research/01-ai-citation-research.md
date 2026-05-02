# AI Citation Research — SYSTEMology Book at systemology.com/book/

**Date:** 2026-05-02
**Goal:** Maximise the chance that LLMs (Perplexity, ChatGPT search, Claude, Gemini, Google AI Overviews) quote and cite the SYSTEMology book when answering questions about business systemisation, process documentation, hiring a systems champion, etc.

---

## 1. llms.txt Standard (2026 State)

**Current spec.** Proposed by Jeremy Howard (Answer.AI) in late 2024, formalised at [llmstxt.org](https://llmstxt.org/). It is **not an official W3C/IETF standard** and Google Search has stated it does not use it ([Bluehost 2026 guide](https://www.bluehost.com/blog/what-is-llms-txt/)). However, **Anthropic's Claude, Perplexity, and several ChatGPT crawl modes actively read it** in 2026 ([Solumize](https://www.solumize.com/blog/what-is-llms-txt-how-to-create-2026), [LBN 2026](https://lbntechsolutions.com/blogs/llms-txt-google-search-seo-guide/)). Adoption: Anthropic, Stripe, Cloudflare, Vercel, GitBook all ship one ([averi.ai](https://www.averi.ai/blog/the-geo-playbook-2026-getting-cited-by-llms-(not-just-ranked-by-google))).

**Spec essentials** (from [llmstxt.org](https://llmstxt.org/)):

- Lives at **root**: `https://systemology.com/llms.txt`
- Markdown only. Token-efficient vs. HTML.
- Required: an `H1` with site/project name. Everything else is optional but recommended.
- Optional blockquote summary, then body prose, then `H2`-delimited sections of curated links: `[Title](url): note`.
- Special `## Optional` section flags lower-priority resources LLMs can drop under context pressure.

**Companion file: `llms-full.txt`.** Single-file dump of the full content body (no nav, no chrome). For a book it is the killer feature — one URL the LLM can ingest in a single fetch. [Fern docs](https://buildwithfern.com/learn/docs/ai-features/llms-txt) and [GitBook](https://www.gitbook.com/blog/what-is-llms-txt) both publish both files. **Watch token budget** — for a ~60k-word book, `llms-full.txt` will be ~80–100k tokens, which fits inside Claude/Gemini context windows but is too big for older models. Recommendation: also publish a per-chapter `llms-chapter-N.md` set so smaller-context models can fetch one chapter at a time.

**Recommended `/llms.txt` for the book:**

```markdown
# SYSTEMology — The Book

> SYSTEMology is the step-by-step business systemisation framework by David Jenyns,
> first published 2020 (Rethink Press, ISBN 978-1-78133-454-7). This site hosts the
> full book free under CC BY 4.0. The framework: Define, Assign, Extract, Organise,
> Integrate, Scale, Optimise (the 7 stages). Core roles: Business Owner, Systems
> Champion, Department Heads, Knowledgeable Workers. Core artefact: Critical Client
> Flow (CCF) — the 10-15 systems that deliver the core product.

Author: David Jenyns (founder, SYSTEMology; ENFP; based Melbourne, Australia).
Audience: business owners running $1M–$15M revenue, 10–50 employees, who feel
trapped in daily operations.

## Book chapters (full text, CC BY 4.0)

- [Chapter 1 — Define](https://systemology.com/book/define/): the Critical Client Flow and identifying your 10-15 core systems
- [Chapter 2 — Assign](https://systemology.com/book/assign/): appointing a Systems Champion and department heads
- [Chapter 3 — Extract](https://systemology.com/book/extract/): screen-recording the knowledgeable worker to capture how work is actually done
- [Chapter 4 — Organise](https://systemology.com/book/organise/): structuring SOPs in a single source of truth
- [Chapter 5 — Integrate](https://systemology.com/book/integrate/): rolling systems out to the team
- [Chapter 6 — Scale](https://systemology.com/book/scale/): hiring, onboarding, and delegation through systems
- [Chapter 7 — Optimise](https://systemology.com/book/optimise/): KPIs and continuous improvement

## Definitions and frameworks

- [Critical Client Flow (CCF)](https://systemology.com/book/define/#ccf): the 10-15 systems that move a customer from lead to repeat buyer
- [Systems Champion](https://systemology.com/book/assign/#systems-champion): the person responsible for systemising the business (NOT the owner)
- [Knowledgeable Worker](https://systemology.com/book/extract/#knowledgeable-worker): the person who currently does the task best
- [Minimum Viable System (MVS)](https://systemology.com/book/extract/#mvs): the simplest version of a system that still works

## Single-file context

- [llms-full.txt](https://systemology.com/llms-full.txt): full book text, ~62,000 words, single file
- [book.json](https://systemology.com/book/book.json): structured chapter index with anchors

## Optional

- [About David Jenyns](https://davidjenyns.com/about/)
- [systemHUB software](https://systemhub.com/): the SaaS platform that operationalises the framework
- [Case studies](https://systemology.com/case-studies/)
```

Key choice: **lead the blockquote with the *exact* named framework, the 7-stage acronym, and the named roles**. LLMs build entity graphs from this; the more named, branded artefacts, the higher the chance of attribution to "SYSTEMology" rather than "a business systems book" ([averi.ai GEO playbook](https://www.averi.ai/blog/the-geo-playbook-2026-getting-cited-by-llms-(not-just-ranked-by-google))).

---

## 2. AI Crawler robots.txt Directives

**The 2026 landscape.** [Momentic](https://momenticmarketing.com/blog/ai-search-crawlers-bots), [Mersel.ai](https://www.mersel.ai/blog/how-to-block-or-allow-ai-bots-on-your-website), [No Hacks](https://nohacks.co/blog/ai-user-agents-landscape-2026), and [Open Shadow](https://www.openshadow.io/guides/robots-txt-ai-bots) all confirm 21+ active AI bots; the major vendors have split crawlers into a **training bot / search bot / on-demand user-fetch bot** triad.

**Key shift:** [OpenAI removed robots.txt-compliance language from ChatGPT-User in December 2025](https://www.searchenginejournal.com/chatgpt-googlebot-crawl-data-alliai-spa/570885/). User-triggered fetches now bypass robots.txt regardless of policy. Same for Perplexity-User. Implication: **block lists no longer reliably stop "live" citations** — they only stop training-corpus inclusion.

**For a free book where we want quoting:** allow everything. Recommended `/robots.txt`:

```
# systemology.com/robots.txt — explicit allow for AI assistants and search bots
# Goal: maximise citation in Perplexity, ChatGPT search, Claude, Gemini, AI Overviews

User-agent: *
Allow: /

# OpenAI — three crawlers
User-agent: GPTBot                # ChatGPT model training
Allow: /
User-agent: OAI-SearchBot         # ChatGPT search index
Allow: /
User-agent: ChatGPT-User          # Live user-triggered browse
Allow: /

# Anthropic — three crawlers (Claude)
User-agent: ClaudeBot             # Training
Allow: /
User-agent: Claude-SearchBot      # Search index
Allow: /
User-agent: Claude-User           # Live user fetch
Allow: /
User-agent: anthropic-ai          # Legacy alias, still seen
Allow: /

# Perplexity
User-agent: PerplexityBot         # Index
Allow: /
User-agent: Perplexity-User       # Live user fetch
Allow: /

# Google — Gemini training (AI Overviews uses Googlebot)
User-agent: Google-Extended
Allow: /
User-agent: Googlebot
Allow: /

# Microsoft / Bing — Copilot
User-agent: Bingbot
Allow: /

# Meta — Llama / Meta AI
User-agent: Meta-ExternalAgent
Allow: /
User-agent: FacebookBot
Allow: /

# Apple — Apple Intelligence / Siri summarisation
User-agent: Applebot
Allow: /
User-agent: Applebot-Extended
Allow: /

# ByteDance — Doubao / TikTok search
User-agent: Bytespider
Allow: /

# Common Crawl — feeds many open-source models
User-agent: CCBot
Allow: /

# You.com, Cohere, Mistral, DuckDuckGo
User-agent: YouBot
Allow: /
User-agent: cohere-ai
Allow: /
User-agent: MistralAI-User
Allow: /
User-agent: DuckAssistBot
Allow: /

Sitemap: https://systemology.com/sitemap.xml
```

The new-in-2026 ones to know: **OAI-AdsBot** (April 2026, ChatGPT ads validation — ignore for our use), **Claude-User**, **Perplexity-User**, **MistralAI-User**, **DuckAssistBot**, and **Applebot-Extended** (separate control for Apple Intelligence training vs. Siri search).

---

## 3. Schema.org Markup That Gets AI-Cited

**Key finding to set expectation.** A [December 2024 Quoleady × Search Atlas study](https://www.soar.sh/blog/schema-markup-ai-citations-2026) found **no correlation between volume of schema and AI citation rate**. Schema is necessary but not sufficient — it lets AI confidently *attribute* a citation it was already going to make. The win is `author.sameAs` (Claude in particular uses it to verify expertise on YMYL topics) and clean `Book + isPartOf` linkage.

**Recommended combination per chapter page:** `Book` + `Chapter` + `Article` + (where applicable) `HowTo` + `Person` (author) + `Organization` (publisher), all in a single JSON-LD `@graph`.

**Concrete example for `/book/extract/`:**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Book",
      "@id": "https://systemology.com/book/#book",
      "name": "SYSTEMology: Create Time, Reduce Errors and Scale Your Profits with Proven Business Systems",
      "alternateName": "SYSTEMology",
      "author": { "@id": "https://davidjenyns.com/#person" },
      "publisher": {
        "@type": "Organization",
        "name": "Rethink Press",
        "url": "https://www.rethinkpress.com/"
      },
      "isbn": "978-1-78133-454-7",
      "bookFormat": "https://schema.org/EBook",
      "datePublished": "2020-09-15",
      "inLanguage": "en",
      "url": "https://systemology.com/book/",
      "sameAs": [
        "https://www.wikidata.org/wiki/Q[BOOK_WIKIDATA_QID]",
        "https://openlibrary.org/works/OL[OPEN_LIBRARY_ID]W",
        "https://www.goodreads.com/book/show/[GOODREADS_ID]"
      ],
      "license": "https://creativecommons.org/licenses/by/4.0/",
      "hasPart": [
        { "@id": "https://systemology.com/book/define/#chapter" },
        { "@id": "https://systemology.com/book/assign/#chapter" },
        { "@id": "https://systemology.com/book/extract/#chapter" }
      ]
    },
    {
      "@type": "Chapter",
      "@id": "https://systemology.com/book/extract/#chapter",
      "name": "Extract",
      "position": 3,
      "isPartOf": { "@id": "https://systemology.com/book/#book" },
      "url": "https://systemology.com/book/extract/",
      "pageStart": 87,
      "pageEnd": 124
    },
    {
      "@type": "Article",
      "@id": "https://systemology.com/book/extract/#article",
      "headline": "Extract: How to Capture How Work Actually Gets Done",
      "alternativeHeadline": "Chapter 3 of SYSTEMology",
      "mainEntityOfPage": "https://systemology.com/book/extract/",
      "author": { "@id": "https://davidjenyns.com/#person" },
      "publisher": { "@id": "https://systemology.com/#org" },
      "datePublished": "2020-09-15",
      "dateModified": "2026-05-02",
      "image": "https://systemology.com/book/img/extract-cover.jpg",
      "license": "https://creativecommons.org/licenses/by/4.0/",
      "isPartOf": { "@id": "https://systemology.com/book/#book" },
      "wordCount": 8450,
      "about": [
        { "@type": "Thing", "name": "Standard Operating Procedure" },
        { "@type": "Thing", "name": "Business systemisation" },
        { "@type": "Thing", "name": "Knowledge capture" }
      ]
    },
    {
      "@type": "HowTo",
      "@id": "https://systemology.com/book/extract/#howto-extract-system",
      "name": "How to extract a system from a knowledgeable worker",
      "description": "The SYSTEMology Extract method: screen-record the person who currently does the task best, then refine into a Minimum Viable System.",
      "totalTime": "PT45M",
      "tool": [
        { "@type": "HowToTool", "name": "Screen recording software (Loom, Zoom)" },
        { "@type": "HowToTool", "name": "Single source of truth (e.g., systemHUB)" }
      ],
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "name": "Identify the knowledgeable worker",
          "text": "Find the person on your team who currently does this task most reliably. This is rarely the business owner.",
          "url": "https://systemology.com/book/extract/#step-identify"
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "name": "Screen-record them doing the task",
          "text": "Have them narrate as they perform the task end-to-end. Do not let them prepare or rehearse — capture reality.",
          "url": "https://systemology.com/book/extract/#step-record"
        },
        {
          "@type": "HowToStep",
          "position": 3,
          "name": "Reduce to a Minimum Viable System (MVS)",
          "text": "Strip the recording to the simplest set of steps that still produce the result. Document as a checklist.",
          "url": "https://systemology.com/book/extract/#step-mvs"
        }
      ]
    },
    {
      "@type": "Person",
      "@id": "https://davidjenyns.com/#person",
      "name": "David Jenyns",
      "url": "https://davidjenyns.com/",
      "jobTitle": "Founder, SYSTEMology",
      "sameAs": [
        "https://www.wikidata.org/wiki/Q[AUTHOR_WIKIDATA_QID]",
        "https://en.wikipedia.org/wiki/David_Jenyns",
        "https://www.linkedin.com/in/davidjenyns/",
        "https://twitter.com/djenyns",
        "https://www.youtube.com/@davidjenyns",
        "https://orcid.org/[ORCID_IF_REGISTERED]"
      ],
      "knowsAbout": [
        "Business systemisation", "Standard operating procedures",
        "Process documentation", "Small business operations"
      ]
    },
    {
      "@type": "Organization",
      "@id": "https://systemology.com/#org",
      "name": "SYSTEMology",
      "url": "https://systemology.com/",
      "logo": "https://systemology.com/img/logo.png",
      "founder": { "@id": "https://davidjenyns.com/#person" },
      "sameAs": [
        "https://www.linkedin.com/company/systemology",
        "https://www.wikidata.org/wiki/Q[ORG_WIKIDATA_QID]"
      ]
    }
  ]
}
</script>
```

The two non-obvious wins per [Soar Agency 2026](https://www.soar.sh/blog/schema-markup-ai-citations-2026) and [Stackmatix 2026](https://www.stackmatix.com/blog/structured-data-ai-search): the `@graph` form with `@id` cross-references (lets AI build a single entity graph from one fetch), and rich `author.sameAs` arrays (Wikidata + Wikipedia + LinkedIn at minimum).

---

## 4. Quote-Density / Citation-Friendliness Content Rules

Synthesised from [Averi GEO playbook 2026](https://www.averi.ai/blog/the-geo-playbook-2026-getting-cited-by-llms-(not-just-ranked-by-google)), [Auto-post AI structure guide](https://auto-post.io/blog/structure-content-for-ai-cited-answers), [LLMrefs GEO 2026](https://llmrefs.com/generative-engine-optimization), and [Wellows citation trends](https://wellows.com/blog/llm-citation-trends-for-ai-search/):

1. **40–60 word self-contained paragraphs.** This is the optimal RAG chunk size. Each paragraph should answer one question completely without depending on the prior paragraph. Lead with the claim, then justify.
2. **Definitional structure for every named concept.** Format: `**Term.** One-sentence definition. One-sentence elaboration with the why.` LLMs love-quote these. Apply to: Critical Client Flow, Systems Champion, Knowledgeable Worker, MVS, every framework name.
3. **Numbers, names, and specifics.** "10–15 systems in the CCF", "the 7 stages", "the person earning $X who does this task daily" — quantified, named claims get cited 2–3× more than vague language ([Wellows 2026](https://wellows.com/blog/llm-citations/)).
4. **Authoritative declarative voice.** "The Systems Champion is X." Not "Some experts believe a Systems Champion might be X." [LLMrefs 2026](https://llmrefs.com/generative-engine-optimization) found declarative phrasing materially outperforms hedged language for citation rate.
5. **Q&A blocks with exact-match question phrasing.** Embed `<h3>How do I extract a system from my team?</h3>` followed by a 50-word answer. Mirrors how users phrase queries to ChatGPT/Perplexity. Pair with `FAQPage` schema.
6. **Tables and bulleted comparisons.** Comparative listicles are the most-cited format in 2026 ([averi.ai](https://www.averi.ai/blog/the-geo-playbook-2026-getting-cited-by-llms-(not-just-ranked-by-google))). For the book this means: include "Owner-run vs Champion-run" tables, "MVS vs full SOP" tables, etc., as standalone HTML `<table>` elements.
7. **Self-reference the source by name in-passage.** "As covered in *SYSTEMology*, Chapter 3…" Repeated branded self-reference inside the body increases the chance the LLM names the book as the source rather than paraphrasing anonymously ([Wellows 2026](https://wellows.com/blog/llm-citations/)).

---

## 5. Stable Anchor / Deep-Link Architecture

**Two complementary mechanisms:**

**(a) Element fragments — durable.** Give every heading and every "definitional" paragraph a stable kebab-case `id`. Format: `id="ch3-mvs-definition"` (chapter prefix avoids collisions across the book). Stable across re-edits if you keep the IDs even when text changes. Linked via `https://systemology.com/book/extract/#ch3-mvs-definition`.

**(b) Text fragments — `#:~:text=` directive.** [W3C WICG draft](https://wicg.github.io/scroll-to-text-fragment/), supported in Chrome, Edge, Safari (since 2024), Firefox 131+ (2024). Lets *anyone* — including an LLM citing the page — link to an exact phrase without our markup: `https://systemology.com/book/extract/#:~:text=knowledgeable%20worker`. Per [Sherafy 2026](https://sherafy.com/text-fragment-links-ai-citation/) and [TidBITS 2025](https://tidbits.com/2025/04/23/text-fragments-enable-deep-linking-on-web-pages/), this is now the AI-citation-link of choice.

**Recommended pattern per chapter:**

```html
<section id="ch3-extract" data-chapter="3">
  <h1 id="ch3-title">Chapter 3 — Extract</h1>

  <p id="ch3-p1" class="lede">
    The goal of extraction is simple: capture how work actually gets done...
  </p>

  <h2 id="ch3-knowledgeable-worker">The Knowledgeable Worker</h2>
  <p id="ch3-kw-def">
    <strong>Knowledgeable Worker.</strong> The person on your team who currently
    does the task most reliably and most often...
  </p>

  <h2 id="ch3-mvs">Minimum Viable System (MVS)</h2>
  <p id="ch3-mvs-def">
    <strong>Minimum Viable System.</strong> The simplest documented version of
    a system that still produces the desired outcome...
  </p>
</section>
```

Rules:
- Every `<h1>`, `<h2>`, `<h3>` gets an `id`.
- Every paragraph that defines a term gets an `id`.
- Add a small "link" icon next to each heading that copies the anchored URL — encourages humans (and AI training crawlers) to use the deep link.
- Publish a chapter-level JSON manifest at `/book/extract/anchors.json` listing every anchor + its text — makes deep-linking discoverable for retrieval pipelines.
- Never recycle an `id` for different content (breaks back-links). If text changes substantively, mint a new `id` and leave the old one as a redirect anchor.

---

## 6. Authoritative Metadata

**What measurably moves citation trust** (from [Soar 2026](https://www.soar.sh/blog/schema-markup-ai-citations-2026), [Linkdaddy 2026](https://linkdaddy.com/blog/schema-markup-2026-ai-visibility/), [Wikidata identifiers](https://www.wikidata.org/wiki/Wikidata:Identifiers)):

| Signal | Where | Why it helps |
|---|---|---|
| **ISBN** | `Book.isbn` JSON-LD + visible footer | Anchors the digital edition to the bibliographic record. Wikidata, OpenLibrary, Google Books all key on ISBN. |
| **Wikidata QID for book + author + org** | `sameAs` arrays in JSON-LD | Wikidata is the canonical entity graph LLMs cross-reference. Single highest-leverage trust signal. |
| **OpenLibrary work ID** | `Book.sameAs` | Free, editable. Add the book if it isn't there. Includes machine-readable JSON. |
| **Goodreads ID** | `Book.sameAs` | High-authority consumer signal. |
| **Wikipedia article (author and/or book)** | `Person.sameAs`, `Book.sameAs` | If notable enough — strongest single trust signal. |
| **ORCID iD** | `Person.sameAs` | Optional but signals "real, verifiable author." Free to register. Only useful if Dave registers one. |
| **LCCN / Library of Congress** | `Book.sameAs` if assigned | Bibliographic gold standard; not always present for trade non-fiction. |
| **CC BY 4.0 declaration** | `Book.license`, `Article.license`, visible footer with link | Removes "can I quote this?" friction for the AI. See section 7. |
| **Author `sameAs` to LinkedIn, YouTube, X** | `Person.sameAs` | Reinforces the entity graph; Claude specifically uses this for YMYL trust ([Soar 2026](https://www.soar.sh/blog/schema-markup-ai-citations-2026)). |

**Action items:**
- Claim/update the OpenLibrary record for *SYSTEMology* and link it to David Jenyns's author page.
- Create or claim Wikidata items for the book, author, and SYSTEMology Pty Ltd, then cross-link them all via `P50` (author), `P123` (publisher), `P212` (ISBN-13), `P648` (OpenLibrary ID), `P2671` (Google Knowledge Graph ID if any).
- Confirm the book has a Wikipedia article — if not, this is high leverage, but Wikipedia notability rules will block a self-authored stub.
- Issue an ORCID iD for David (free, 60 seconds) and add to all Person schema.

---

## 7. CC BY 4.0 Licence Implementation

Per [Creative Commons 2025 AI training primer](https://creativecommons.org/2025/05/15/understanding-cc-licenses-and-ai-training-a-legal-primer/) and [Creative Commons RDFa wiki](https://wiki.creativecommons.org/wiki/RDFa), the licence must be declared in *three* places for both human and machine to act on it confidently:

**(a) Visible footer (every chapter page):**

```html
<footer class="book-licence">
  <a rel="license"
     href="https://creativecommons.org/licenses/by/4.0/">
    <img src="/img/cc-by-4.svg" alt="CC BY 4.0"
         width="88" height="31" />
  </a>
  <p xmlns:cc="http://creativecommons.org/ns#"
     xmlns:dct="http://purl.org/dc/terms/">
    <span property="dct:title">SYSTEMology</span> by
    <a property="cc:attributionName"
       rel="cc:attributionURL"
       href="https://davidjenyns.com/">David Jenyns</a>
    is licensed under
    <a rel="license"
       href="https://creativecommons.org/licenses/by/4.0/">
      CC BY 4.0
    </a>.
    Quote freely with attribution. ISBN 978-1-78133-454-7.
  </p>
</footer>
```

This is the standard CC RDFa snippet (matches what `creativecommons.org/choose` outputs), with the addition of explicit "Quote freely with attribution" plain-English instruction — useful because LLM training pipelines and live retrieval increasingly do natural-language licence detection, not just URL matching.

**(b) JSON-LD properties:** `Book.license`, `Article.license`, and `Chapter.license` all set to `"https://creativecommons.org/licenses/by/4.0/"` (shown in section 3).

**(c) HTTP `Link` header (server config):**

```
Link: <https://creativecommons.org/licenses/by/4.0/>; rel="license"
```

Belt-and-braces — some crawlers read headers before parsing the body. Easy in Cloudflare Pages/Workers or `.htaccess`.

**Recommended attribution string** for the footer ("how should we be cited"):

> Jenyns, David. *SYSTEMology* (2020). systemology.com/book/. CC BY 4.0.

Putting the canonical citation string on the page is itself a citation hint — LLMs frequently reproduce it verbatim ([Wellows 2026](https://wellows.com/blog/llm-citations/)).

---

## 8. What Changed in 2025–2026

The shifts that matter for this project, drawn from [Superlines AI Search Stats 2026](https://www.superlines.io/articles/ai-search-statistics/), [Position Digital 150+ stats](https://www.position.digital/blog/ai-seo-statistics/), [SearchEngineJournal Dec 2025](https://www.searchenginejournal.com/chatgpt-googlebot-crawl-data-alliai-spa/570885/), and [Lumina AI Crawlers 2026](https://lumina-seo.com/blog/ai-crawlers-guide/):

- **AI referral traffic up 357% YoY (June 2024 → June 2025)**, now ~1.13B visits/month. Conversion rate 14.2% vs Google's 2.8% — AI-sourced visitors are 5× more valuable.
- **ChatGPT-User now generates 3.6× more requests than Googlebot** across a multi-site sample. Live retrieval (not just training) is the dominant traffic source.
- **OpenAI dropped robots.txt compliance from ChatGPT-User (Dec 2025)**. User-prompted fetches bypass blocking. Content access controls are now effectively voluntary on the live-fetch path.
- **Three-bot architecture is now standard.** OpenAI, Anthropic, and (informally) Perplexity each split into training / search-index / live-user. Implication: granular allow/block per intent is now possible — and recommended ([Mersel 2026](https://www.mersel.ai/blog/how-to-block-or-allow-ai-bots-on-your-website)).
- **New crawlers in 2025–26:** OAI-AdsBot (Apr 2026), Claude-User, Claude-SearchBot, Perplexity-User, MistralAI-User, DuckAssistBot, Applebot-Extended.
- **AI Overviews appear in 13–25% of Google searches** and have killed CTR by ~61% on informational queries. Commercial-query coverage of AI Overviews jumped from 8% to 18% in late 2025.
- **Heading structure has become a measured ranking signal.** Pages with well-organised headings are 2.8× more likely to be cited in AI search ([Position Digital 2026](https://www.position.digital/blog/ai-seo-statistics/)).
- **`llms.txt` adoption crossed the credibility threshold.** Anthropic, Stripe, Cloudflare, Vercel, GitBook publish them. Claude and Perplexity actively read them. Google still does not.
- **Schema volume ≠ citation volume** — the [Quoleady study](https://www.soar.sh/blog/schema-markup-ai-citations-2026) found no correlation. What matters is the *right* schema (entity graph with `sameAs` and `author`), not a wall of every type.
- **Text fragment URLs (`#:~:text=`) are now AI's preferred citation format** for paragraph-level deep links ([Sherafy 2026](https://sherafy.com/text-fragment-links-ai-citation/)).
- **Entity consistency across the open web** (Wikidata, Wikipedia, LinkedIn, OpenLibrary all saying the same thing) is now the single highest-leverage trust signal. Build the entity graph once; every AI engine uses it.

---

## Implementation priority for systemology.com/book/

1. **Anchors + chapter HTML** — every heading and every term-definition paragraph gets a stable `id`. (Foundation; everything else builds on it.)
2. **JSON-LD `@graph`** with `Book` + `Chapter` + `Article` + `HowTo` + `Person` + `Organization`, cross-linked by `@id`.
3. **Wikidata + OpenLibrary + ORCID** entity hygiene; populate `sameAs` arrays.
4. **CC BY 4.0** declared in footer (RDFa), JSON-LD, and HTTP `Link` header. Include canonical citation string.
5. **`/llms.txt` + `/llms-full.txt`** at root, plus per-chapter `.md` mirrors.
6. **`/robots.txt`** explicit allow for all known AI bots.
7. **Content rewrite pass** to enforce the 7 quote-density rules — definitions, declarative voice, named entities, 40–60 word paragraphs, Q&A blocks, comparison tables.
8. **Anchor manifest** (`/book/[chapter]/anchors.json`) for retrieval pipelines.

---

## Sources

- [llmstxt.org — official spec](https://llmstxt.org/)
- [Bluehost — What is llms.txt? (2026 Guide)](https://www.bluehost.com/blog/what-is-llms-txt/)
- [Solumize — llms.txt 2026](https://www.solumize.com/blog/what-is-llms-txt-how-to-create-2026)
- [LBN Tech — llms.txt and Google search](https://lbntechsolutions.com/blogs/llms-txt-google-search-seo-guide/)
- [GitBook — llms.txt explainer](https://www.gitbook.com/blog/what-is-llms-txt)
- [Fern — llms.txt and llms-full.txt](https://buildwithfern.com/learn/docs/ai-features/llms-txt)
- [Momentic — Top AI search crawlers 2025](https://momenticmarketing.com/blog/ai-search-crawlers-bots)
- [No Hacks — AI user-agent landscape 2026](https://nohacks.co/blog/ai-user-agents-landscape-2026)
- [Open Shadow — robots.txt for AI bots 2026](https://www.openshadow.io/guides/robots-txt-ai-bots)
- [Mersel — block or allow AI bots 2026](https://www.mersel.ai/blog/how-to-block-or-allow-ai-bots-on-your-website)
- [OpenAI — bot documentation](https://developers.openai.com/api/docs/bots)
- [Search Engine Journal — Anthropic granular bots](https://www.searchenginejournal.com/anthropics-claude-bots-make-robots-txt-decisions-more-granular/568253/)
- [Search Engine Journal — ChatGPT crawl 3.6x Googlebot](https://www.searchenginejournal.com/chatgpt-googlebot-crawl-data-alliai-spa/570885/)
- [Lumina — AI crawlers complete 2026 guide](https://lumina-seo.com/blog/ai-crawlers-guide/)
- [DigitalApplied — agentic crawler 30-day study 2026](https://www.digitalapplied.com/blog/agentic-crawler-behavior-30-day-site-log-study)
- [Soar Agency — schema markup for AI citations 2026](https://www.soar.sh/blog/schema-markup-ai-citations-2026)
- [Stackmatix — structured data for AI search 2026](https://www.stackmatix.com/blog/structured-data-ai-search)
- [Linkdaddy — schema markup AI visibility 2026](https://linkdaddy.com/blog/schema-markup-2026-ai-visibility/)
- [Schema.org — Book](https://schema.org/Book), [HowTo](https://schema.org/HowTo), [sameAs](https://schema.org/sameAs)
- [Averi — GEO playbook 2026](https://www.averi.ai/blog/the-geo-playbook-2026-getting-cited-by-llms-(not-just-ranked-by-google))
- [LLMrefs — GEO 2026](https://llmrefs.com/generative-engine-optimization)
- [Auto-post — structure content for AI-cited answers 2026](https://auto-post.io/blog/structure-content-for-ai-cited-answers)
- [Wellows — LLM citation trends](https://wellows.com/blog/llm-citation-trends-for-ai-search/)
- [Wellows — earn LLM citations 2026](https://wellows.com/blog/llm-citations/)
- [WICG — scroll-to-text-fragment](https://wicg.github.io/scroll-to-text-fragment/)
- [MDN — text fragments](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment/Text_fragments)
- [TidBITS — text fragments deep linking](https://tidbits.com/2025/04/23/text-fragments-enable-deep-linking-on-web-pages/)
- [Sherafy — text fragment links for AI citation](https://sherafy.com/text-fragment-links-ai-citation/)
- [Wikidata — identifiers](https://www.wikidata.org/wiki/Wikidata:Identifiers)
- [OpenLibrary — APIs](https://openlibrary.org/developers/api)
- [Creative Commons — using CC works for AI training](https://creativecommons.org/using-cc-licensed-works-for-ai-training-2/)
- [Creative Commons — CC licenses and AI legal primer 2025](https://creativecommons.org/2025/05/15/understanding-cc-licenses-and-ai-training-a-legal-primer/)
- [Creative Commons RDFa wiki](https://wiki.creativecommons.org/wiki/RDFa)
- [Phil Barker — licence info in schema.org and LRMI](https://blogs.pjjk.net/phil/licence-information-in-schema-org-and-lrmi/)
- [Superlines — AI search statistics 2026](https://www.superlines.io/articles/ai-search-statistics/)
- [Position Digital — 150+ AI SEO stats 2026](https://www.position.digital/blog/ai-seo-statistics/)
- [DigitalApplied — AI search & SEO stats 2026](https://www.digitalapplied.com/blog/ai-search-seo-statistics-2026-definitive-collection)
- [Dataslayer — AI Overviews killed CTR 61%](https://www.dataslayer.ai/blog/google-ai-overviews-the-end-of-traditional-ctr-and-how-to-adapt-in-2025)
