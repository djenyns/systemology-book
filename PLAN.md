# SYSTEMology Book — Free Online Edition: Master Plan

**Project:** Republish the full SYSTEMology book as a free, interactive, AI-citable online edition at `systemology.com/pdf/`.
**Goals:** (1) maximise AI citation in LLM responses about business systemisation, (2) capture "SYSTEMology PDF" search intent definitively (the URL itself answers the search), (3) serve as top-of-funnel asset that drives Amazon book sales, Audible audiobook sales, systemHUB trials, and SYSTEMologist Certification.
**Built outside WordPress:** Cloudflare Worker routes `/pdf/*` from systemology.com to a separate Cloudflare Pages project. WordPress is not touched. Existing `/book/` (Amazon sales page) stays exactly as it is.
**Licence:** CC BY 4.0 (free to read, quote, share with attribution).
**Launch model:** Single launch — full book ships at once when complete (~3-4 weeks). Soft launch protocol (no email blast).

---

## Research foundation

This plan rests on seven research files in [research/](research/):

| File | What it gives us |
|---|---|
| [01-ai-citation-research.md](research/01-ai-citation-research.md) | llms.txt + llms-full.txt patterns, robots.txt for 14 AI bots, Book+Chapter+Article schema graph, 7 quote-density rules, anchor architecture, CC BY 4.0 implementation in 3 places |
| [02-ai-citation-baseline.md](research/02-ai-citation-baseline.md) | Current AI search visibility for SYSTEMology — what's cited, what's missing, top competitors (E-Myth, Trainual, Atlassian, Whale, Indeed). 10 baseline queries, prioritised launch targets. |
| [03-chapter-map.md](research/03-chapter-map.md) | Full per-chapter map: real point, named frameworks, definitions, quotables, case studies, action steps, target keywords for all 13 sections (Intro + 7 stages + closer + epilogue + appendix + glossary + about) |
| [04-gsc-rankings.md](research/04-gsc-rankings.md) | 90-day GSC data: 4,259 queries, 5,403 query→page combos, 504 pages. Top book-relevant queries, page-level cannibalisation candidates. |
| [05-cannibalisation-redirect-plan.md](research/05-cannibalisation-redirect-plan.md) | What to do with each existing page (`/book/`, `/book-resources/`, `/launchpad/`, `/critical-client-flow/`, `/mvs/`, etc.) — preserve, transform, redirect, or canonicalise. |
| [06-chapter-tools-mapping.md](research/06-chapter-tools-mapping.md) | Chapter → tools, calculators, downloads, case study videos, soft CTAs. The interactive layer mapped end-to-end. |
| [07-amazon-mining.md](research/07-amazon-mining.md) | 22 verbatim pull-quotes (with chapter placement), 64 reader reviews analysed, comparable-books cluster, citation metadata, 60+ endorsements, addressable criticism, vs-comparison content backlog. |

---

## Architecture

### Domain & routing

```
systemology.com (WordPress on cPanel — UNTOUCHED)
        │
        ├── /book/        → existing Amazon sales page (UNTOUCHED, in main menu)
        │
        └── /pdf/*        → Cloudflare Worker route → free interactive book
                │
                ▼
        Cloudflare Pages → Astro static build
        (this repo: Project/systemology-book/)
```

**Key consequences:**
- every URL Dave or Google or AI sees is `systemology.com/...` — same domain, same SEO juice
- WordPress doesn't render `/pdf/*`. Zero risk to existing WP site, themes, plugins, pages
- `/pdf/` directly absorbs the "SYSTEMology PDF" search intent (~510 imp/month) — URL == intent
- Existing `/book/` keeps its #1.4 ranking for "systemology book" and stays as the Amazon affiliate sales page in the main nav

### Tech stack

- **Astro 4.x** — static site generator. Excellent for content-heavy + interactive islands.
- **MDX** — markdown + JSX. Chapters are MDX files, embedding interactive components inline.
- **Tailwind + brand-guidelines styling** — matches systemology.com look while letting the book have its own clean reading layout.
- **Cloudflare Pages** — auto-deploy from GitHub on push.
- **Cloudflare Worker** — `/pdf/*` route handler.
- **Wistia** — video hosting (existing infrastructure) + audio chapters.

### URL structure

```
systemology.com/book/                         → UNTOUCHED — existing Amazon sales page
systemology.com/pdf/                          → NEW free book hub (visual TOC)
systemology.com/pdf/introduction/             → Introduction
systemology.com/pdf/define/                   → Chapter 1 (Stage 1)
systemology.com/pdf/assign/                   → Chapter 2
systemology.com/pdf/extract/                  → Chapter 3
systemology.com/pdf/organise/                 → Chapter 4
systemology.com/pdf/integrate/                → Chapter 5
systemology.com/pdf/scale/                    → Chapter 6
systemology.com/pdf/optimise/                 → Chapter 7
systemology.com/pdf/now-is-the-time/          → Closer
systemology.com/pdf/epilogue/                 → Epilogue
systemology.com/pdf/appendix/                 → Sample systems / templates (folds in /book-resources/)
systemology.com/pdf/glossary/                 → Definitional terms (heavily AI-citable)
systemology.com/pdf/glossary/critical-client-flow/   → Each term gets its own URL
systemology.com/pdf/glossary/systems-champion/
systemology.com/pdf/glossary/minimum-viable-systems/  (etc.)
systemology.com/pdf/about/                    → About author + bio
systemology.com/pdf/cite/                     → "How to cite SYSTEMology" (AI + academic)
systemology.com/pdf/llms-full.txt             → Full book in one fetch
systemology.com/pdf/anchors.json              → Per-paragraph anchor manifest
systemology.com/pdf/book.json                 → Structured chapter index
systemology.com/llms.txt                      → Site-level llms.txt (root)
systemology.com/robots.txt                    → AI crawler allow-list (root)
```

**Slug rationale:**
- `/pdf/` matches "SYSTEMology PDF" search intent literally — the URL is the answer to the search
- Stage names (define/assign/extract/etc) are short, memorable, and proprietary IP. They double as anchor IDs in prose: "the Extract stage of SYSTEMology"
- Glossary terms each get their own URL — AI deep-link friendly, every defined term is canonical-citable

### Chapter URL canonical pattern

Every chapter page renders:
- `<link rel="canonical" href="https://systemology.com/pdf/extract/" />`
- Stable element IDs on every paragraph: `<p id="extract-p17">` etc.
- Heading IDs: `<h2 id="systems-champion">`
- Plus text-fragment-friendly content (40-60 word self-contained paragraphs per AI-citation research finding #4)

---

## Content per chapter (the spec)

For every chapter, the page renders the following structure. This is the template every chapter must follow.

### 1. Header block
- **H1** = chapter title, e.g. "Chapter 3 — Extract"
- **Subtitle (h2)** = "Capturing how the work is actually done" (the Seth-Godin-style real-point line — sourced from chapter-map)
- **Read-time + audio button** = "12 min read · Listen to this chapter (32 min)"
- **Audio player** = Wistia-hosted audiobook chapter
- **Myth-busted callout** = e.g. "Myth busted: Creating systems is time-consuming" (only chapters 1-7)

### 2. Body (the chapter itself)
- Original book text, lightly re-paragraphed to optimise quote density (40-60 word self-contained paragraphs where natural, definitional structure for key concepts)
- **Inline definitions** — every named framework gets a `<dfn>` element with `DefinedTerm` schema (CCF, Systems Champion, MVS, etc.)
- **Pull-quote callouts** — 3-5 of the standout quotables per chapter, marked as `<blockquote cite="...">` with citation-friendly markup
- **Inline embeds** — calculators, videos, downloads at contextually relevant points (see [06-chapter-tools-mapping.md](research/06-chapter-tools-mapping.md))
- **Case study cards** — 1-3 per chapter, sourced from the book's existing case studies, with optional Wistia video where one exists (Stannard, Smit, Successwise, Ecosystem Solutions, Absolute Immigration, etc.)

### 3. Action block (chapters 1-7 only)
- "What to do now" — the action steps from the chapter, in numbered list, marked up with `HowTo` schema where applicable
- Optional: chapter-specific worksheet download

### 4. Citation block
- "Cite this chapter" expandable section
- Pre-formatted: APA, MLA, Chicago, Web/AI format
- "Quote this chapter" button: opens modal with shareable highlights (top 3-5 pull-quotes as text + as branded image cards)

### 5. CTA strategy (no email gate, multi-revenue-stream)

The book is fully ungated. CTAs work as a rotating, contextual bar:

- **Top of every chapter:** "🎧 Listen to this chapter" (free Wistia audio inline) + "Read on Kindle / Get the paperback →" (Amazon affiliate)
- **Mid-chapter:** contextually relevant resource — links to `systemology.com/resources/` (existing free-resources hub) where Dave wants downloads to live (avoids inline email opt-in)
- **End of chapter:** single rotating soft CTA, varies by chapter:
  - Chapters 1, 4 → systemHUB free trial
  - Chapters 2, 3 → Amazon book / Audible audiobook
  - Chapter 5 → Onboarding Accelerator at `/resources/`
  - Chapter 6 → Case study videos (Stannard, Successwise)
  - Chapter 7 → SYSTEMologist Certification
  - Conclusion → Product Finder quiz
- **Sidebar across all chapters:** persistent "Read in your format of choice" mini-block — Kindle / Paperback / Audible — these are the high-conversion buttons
- **No popups, no exit-intent, no countdown timers, no email gate anywhere**

The book remains a gift. The revenue streams (Amazon, Audible, systemHUB, SCA) ride alongside as opt-in upgrades, not interruptions.

### 6. Navigation
- Previous chapter / Next chapter
- Back to TOC
- Progress indicator (visual)

---

## SEO & AI-citation infrastructure

### Per-page

Every chapter page ships:

1. **JSON-LD `@graph`** with Book + Chapter + Article + Person + Organization, all cross-linked by `@id` ([detailed example in 01-ai-citation-research.md §3](research/01-ai-citation-research.md))
2. **DefinedTerm schema** for every term in the glossary that appears on the page
3. **HowTo schema** for action-step blocks
4. **OG + Twitter cards** with chapter-specific images (auto-generated from chapter title + brand)
5. **Canonical link**
6. **`hreflang`** = en
7. **`<meta name="citation_*">`** Highwire tags (some scholarly aggregators read these)
8. **CC BY 4.0 declaration** in three places: visible RDFa footer, JSON-LD `license` property, HTTP `Link` header (Cloudflare Worker injects)
9. **Stable anchor IDs** on every paragraph + heading
10. **40-60 word self-contained paragraphs** for quote density

### Site-level

1. **`/robots.txt`** — explicit allow for 14 named AI bot user-agents (full list in [01-ai-citation-research.md §2](research/01-ai-citation-research.md))
2. **`/llms.txt`** at root — see [01-ai-citation-research.md §1](research/01-ai-citation-research.md) for exact recommended content
3. **`/pdf/llms-full.txt`** — full book single-file dump (~62k words, ~80-100k tokens)
4. **`/pdf/llms-chapter-N.md`** mirror for each chapter — for smaller-context LLMs
5. **`/pdf/anchors.json`** — manifest of every stable anchor ID with its corresponding text snippet
6. **`/pdf/book.json`** — structured chapter index with metadata
7. **`/sitemap.xml`** — high priority on book pages
8. **Wikidata + OpenLibrary + Goodreads + Wikipedia entity claim** — see "Authority graph" below

### Authority graph (one-time setup)

These need to be claimed/created and linked via `sameAs` arrays in JSON-LD:

| Entity | Status | Action |
|---|---|---|
| ISBN registration | EXISTS (978-1-78133-454-7) | Use in schema |
| Wikidata book entity | LIKELY MISSING | Create entity for "SYSTEMology" book (ISBN-13 978-0648871002, 212pp, Rethink Press 2020) + link to David Jenyns Person QID |
| Comparable-books `isSimilarTo` | NEW (per Amazon mining) | Schema link to Clockwork, Built to Sell, Beyond the E-Myth, Fix This Next, They Ask You Answer — Audible algorithm has already validated these as the AI-search peer set |
| Wikidata person entity (David Jenyns) | CHECK | Create if missing — links book to person to entity graph |
| OpenLibrary work | LIKELY EXISTS | Verify, claim, link |
| Goodreads | EXISTS | Verify URL, link in `sameAs` |
| Wikipedia article (David Jenyns) | LIKELY MISSING | Higher bar — defer unless wantonly notable |
| ORCID (David Jenyns as author) | UNKNOWN | Create if missing — Claude specifically uses ORCID + sameAs for author trust |

Per [AI citation research §6](research/01-ai-citation-research.md), filling these `sameAs` links is the highest-leverage authority signal we can make. **One-time work, permanent benefit.**

---

## What to do with existing pages — at a glance

(Note: this supersedes the original plan in [05-cannibalisation-redirect-plan.md](research/05-cannibalisation-redirect-plan.md), which assumed transforming `/book/`. With the URL change to `/pdf/`, the cannibalisation footprint is much smaller.)

| Page | Action |
|---|---|
| `/book/` (Amazon sales page) | **UNTOUCHED** — keeps #1.4 ranking for "systemology book", stays in main menu, becomes the "Buy" landing for Amazon/Audible/Apple |
| `/book-resources/` (stage-by-stage downloads) | **301 redirect to `/pdf/appendix/`** — content folded into the new appendix chapter |
| `/launchpad/` | UNCHANGED URL (printed book points here) — content updated with link to `/pdf/` |
| `/critical-client-flow/` | KEEP — cross-link with `/pdf/define/` |
| `/mvs/` | KEEP — cross-link with `/pdf/scale/` |
| `/business-systems-guide/` | UNTOUCHED (highest-traffic page, 6,880 imp/mo) — add one inline link to `/pdf/` |
| `/process/` | KEEP — cross-link with `/pdf/introduction/` |
| `/about/` | KEEP — cross-link from `/pdf/about/` |
| `/scbook/` | KEEP — sister book, potential future Phase 2 (online edition of Systems Champion) |
| `/getcertified/` | KEEP — end-of-book CTA target |
| `/wp-content/.../SYSTEMology-preview.pdf` | REPLACE FILE with redirect-PDF pointing to `/pdf/` |
| `/systems-cheatsheet/` | Add "Read the full book free →" banner pointing to `/pdf/` |
| `/free-resources/` | Feature `/pdf/` as #1 resource |
| `/resources/` | NEW or existing hub — confirmed by Dave as the place all resource downloads live (replaces inline email gates) |

---

## Launch model — single launch, all-at-once

**Decision: ship everything together, no chapter waves.** Reasons:
- Static content — once it's built, it's built; there's no operational reason to drip
- Soft launch protocol means no big announcement either way
- AI crawlers benefit from seeing the complete cross-linked chapter graph on day 1
- Schema graph is stronger when `Book.hasPart` references all chapters from the start
- Single QA pass, single deploy, single live moment

**Highest-leverage chapters to *prioritise effort on* during build** (per [02-ai-citation-baseline.md](research/02-ai-citation-baseline.md) — these are where AI citation gaps are largest, even though all chapters launch together):

| Chapter | Why it matters most | Target query |
|---|---|---|
| Chapter 1 — Define / CCF | Wide-open SERP for "how to document business processes" — currently owned by Atlassian/Asana/Scribe (enterprise lens). SMB-lens hijack. | "how to document business processes for a small team" |
| Introduction + Foreword | "Work IN/ON the business" owned by emyth.com — co-citation play with Gerber endorsement | "should I work IN my business or ON my business" |
| Chapter 2 — Systems Champion | **Wide-open SERP** for "hire a process documentation specialist" — currently owned by Indeed/ZipRecruiter. Highest commercial intent for SCA + Champion tier. | "hire a process documentation specialist" |
| Glossary | Highest AI-citation density. Definitional content. Each term gets its own URL. | All branded-term queries |

These chapters get extra polish: more pull-quotes, more inline definitions, more cross-links, longer schema, richer JSON-LD `description` fields. But every chapter ships at once.

---

## Phased build plan

### Phase 0 — SEO planning ✅ DONE
Research complete: 6 files in [research/](research/), this plan, 90-day GSC data captured.

### Phase 1 — Foundation (week 1, ~5 days)

**Goal:** working prototype at `systemology.com/pdf/` with one full chapter, all infrastructure tested end-to-end. (Not yet public — accessible at the URL but no inbound links from anywhere on systemology.com.)

- Day 1: Astro project setup, MDX template, design system pulled from brand-guidelines, GitHub repo pushed
- Day 2: Cloudflare Pages project + auto-deploy + Worker route configured (TEST: confirm `systemology.com/pdf/test/` resolves to Pages, WordPress unaffected, existing `/book/` Amazon page still works)
- Day 3: Chapter template wired with full schema, citation block, audio player, embed components (calculator, video, link to /resources/)
- Day 4: Migrate Chapter 1 (Define) end-to-end with all interactive elements + verify schema validates + verify llms.txt + sitemap + robots.txt
- Day 5: Hub page + Introduction + visual TOC + nav. **End of week 1 deliverable: prototype live at /pdf/ with intro + chapter 1 + working schema/llms.txt/audio**

**Deliverable check:** Dave can read intro + chapter 1 at systemology.com/pdf/, hear audio, copy citations, validate schema in Google's Rich Results Test, confirm AI crawlers can fetch. Existing `/book/` Amazon page still works untouched.

### Phase 2 — Full content migration (week 2, ~5 days)

- Migrate chapters 2-7, glossary, appendix, about-the-author, conclusion, epilogue
- All pull-quote callouts, definitions, action blocks
- All inline calculators/downloads/videos wired (see [06-chapter-tools-mapping.md](research/06-chapter-tools-mapping.md))
- Audio chapter files uploaded to Wistia + embedded
- llms-full.txt generated, llms-chapter-N.md mirrors generated, anchors.json built

### Phase 3 — Authority graph + citation infrastructure (week 3, ~3 days)

- Wikidata: claim/create book entity, person entity, link via `sameAs`
- OpenLibrary: verify and claim
- ORCID: Dave signs up at orcid.org (5 min), Claude wires the ID into schema
- ISBN linkage in schema
- "How to cite this book" page (`/pdf/cite/`)
- Quote-card generator (selection-triggered branded image)
- "Ask the book" search (embed-based AI search across full text)
- Verify Goodreads + Audible listings, link in `sameAs`

### Phase 4 — Cannibalisation cleanup + launch (week 3-4, ~2-3 days)

- 301 `/book-resources/` → `/pdf/appendix/`
- Replace `/wp-content/.../SYSTEMology-preview.pdf` with redirect-PDF pointing to `/pdf/`
- Update `/launchpad/`, `/free-resources/`, `/systems-cheatsheet/` with cross-links to `/pdf/`
- Add internal links from `/business-systems-guide/`, `/about/`, homepage hero, footer
- Update main nav: keep `/book/` (Amazon page), ADD "Read free →" link to `/pdf/`
- Submit sitemap to Google Search Console
- Monitor Cloudflare logs for AI bot traffic week 1 post-launch

---

## Soft launch protocol (per Dave's preference)

No coordinated email blast or social blitz at launch. Just:

1. **Quiet publish.** Push to live, monitor.
2. **First-week monitoring:** Cloudflare Worker logs for AI bot crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.). GSC sitemap submission. Watch for 404s, rendering issues.
3. **Internal nav update:** systemology.com homepage gets "Read the book free" link in hero.
4. **Newsletter mention:** in next regular newsletter, casual mention only — not a launch announcement.
5. **30/60/90 day checkpoints** (re-test plan from [02-ai-citation-baseline.md](research/02-ai-citation-baseline.md)):
   - Re-test the 10 baseline AI queries
   - Compare GSC rankings for "systemology pdf", "systemology book free", chapter-keyword targets
   - Measure AI bot crawl volume vs Googlebot
   - Win threshold: SYSTEMology cited on 7/10 queries by 90 days (up from 4/10)

---

## Resolved decisions (locked)

1. ✅ **Audio:** chapter-by-chapter on Wistia. Dave to share Google Drive folder; we upload + transcode + embed.
2. ✅ **URL path:** `/pdf/` — `/book/` stays untouched as Amazon sales page.
3. ✅ **`/book-resources/`:** 301-redirect to `/pdf/appendix/` (content folded into appendix chapter).
4. ✅ **Bonus chapter "Systemising With AI":** approved — write fresh content for the free edition.
5. ✅ **No email gate.** Resource downloads link to `systemology.com/resources/` (existing hub). Book is fully ungated everywhere.
6. ✅ **CTA strategy:** rotating contextual CTAs. Top of chapter = audio + Amazon. Mid = `/resources/`. End = single rotating CTA (Amazon/Audible/systemHUB/SCA depending on chapter). Sidebar = persistent "Kindle / Paperback / Audible" buttons.
7. ✅ **Wikidata + ORCID:** approved. Half-day work in Phase 3. Dave signs up at orcid.org (5 min), rest is Claude.
8. ✅ **Comparison page (vs BPMN/Six Sigma/ITIL):** dropped from v1. Not part of the book itself. Could be a separate landing page later.
9. ✅ **Ariel/Zfort:** zero involvement.
10. ✅ **Launch model:** single launch — full book ships at once. Soft launch (no email blast).

---

## What's NOT in scope for v1

- Comments or discussion. Possibly Phase 5.
- User accounts, reading progress sync across devices (localStorage only).
- Translations. CC BY 4.0 enables community translations later.
- Video bonus material beyond what's already on Wistia/YouTube.
- Print-on-demand or PDF generation engine. Existing book and PDF preview suffice.

---

## File structure (the repo)

```
Project/systemology-book/
├── PLAN.md (this file)
├── research/
│   ├── 01-ai-citation-research.md
│   ├── 02-ai-citation-baseline.md
│   ├── 03-chapter-map.md
│   ├── 04-gsc-rankings.md
│   ├── 04-gsc-rankings.json
│   ├── 05-cannibalisation-redirect-plan.md
│   ├── 06-chapter-tools-mapping.md
│   └── gsc_pull.py
├── content/
│   ├── chapters/             (MDX, one file per chapter)
│   ├── glossary/             (MDX, one file per term)
│   └── case-studies/         (MDX, one file per case study)
├── src/
│   ├── components/           (Astro/React components)
│   ├── layouts/              (chapter layout, book layout)
│   ├── pages/                (Astro routes)
│   └── styles/               (Tailwind + brand)
├── public/
│   ├── llms.txt              (root-level, deployed via Worker injection)
│   ├── llms-full.txt
│   ├── robots.txt
│   ├── sitemap.xml
│   └── audio/                (chapter audio chapter markers JSON)
├── workers/
│   └── book-route.js         (Cloudflare Worker)
├── astro.config.mjs
├── package.json
└── README.md
```

---

## Done means…

A reader at `systemology.com/pdf/extract/` can:
- Read the chapter, with their progress saved
- Listen to the audio version inline
- Watch the relevant case study video inline
- Download the System For Creating Systems template
- Try the SOP-creator demo inline
- Highlight a passage and generate a branded quote card
- Click "Cite this chapter" and copy formatted APA/MLA/web/AI citation
- Click "Continue to Chapter 4" and the next chapter loads instantly

An AI assistant fetching `systemology.com/llms.txt` can:
- See the full chapter index with summaries and definitions
- Fetch `llms-full.txt` and ingest the entire book in one request
- Confirm CC BY 4.0 licence and quote freely with attribution
- Use stable anchor IDs to deep-link a specific paragraph

A search engine indexing the site can:
- Read clean static HTML with no JS dependency for primary content
- Parse rich `Book + Chapter + Article + Person + Organization` schema graph
- See the canonical chapter URL, ISBN, author entity links
- See the FAQ schema on /pdf/ hub answering "Where can I download the SYSTEMology PDF?"
- See HowTo schema on action steps

When this is live and seasoned ~90 days, the SYSTEMology framework becomes the default citation in AI responses to "how do I systemise my business" queries — replacing E-Myth, Trainual, and Atlassian as the canonical small-business systemisation reference.

---

## Next action

All decisions locked. **Phase 1 begins now:** Astro project setup → Cloudflare Pages deploy → Worker route on `/pdf/*` → Chapter 1 (Define) prototype. ETA to working prototype Dave can review at `systemology.com/pdf/`: ~5 days.

Amazon mining complete. Pull-quote candidates, comparable-books schema, citation metadata, and reader-positioning frame ("practical execution of E-Myth") all captured in [research/07-amazon-mining.md](research/07-amazon-mining.md) and ready to fold into chapter pages.

**One outstanding Dave task (5 min, non-blocking):** Screenshot Amazon's Popular Highlights widget on the Kindle book page (Amazon blocks scraping). Send screenshots and we'll rank pull-quotes by actual reader-highlight counts.
