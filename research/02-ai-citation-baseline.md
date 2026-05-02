# AI Citation Baseline — Pre-Book-Launch Snapshot

**Date:** 2026-05-02
**Purpose:** Baseline of how AI search engines currently surface SYSTEMology content **before** systemology.com/book/ launches the full free interactive book. Re-test 30/60/90 days post-launch to measure lift.

## Engines Tested

| Engine | Method | Result |
|---|---|---|
| Google (organic + AI Overview proxy) | WebSearch tool | **Tested** — full data |
| Perplexity | WebFetch on /search?q= | Blocked (403, anti-bot) |
| Bing / Copilot | WebFetch on bing.com | Blocked (geo-served junk results) |
| DuckDuckGo | WebFetch | Blocked (no body returned) |
| You.com | WebFetch | Blocked (header only) |
| Phind | WebFetch | Blocked (403) |
| Google direct | WebFetch on google.com/search | Blocked (CAPTCHA wall) |

**Honest caveat:** The major LLM-powered engines (Perplexity, ChatGPT Search, Copilot, You.com) all block automated fetches. The WebSearch tool returns Google-equivalent organic results, which are **the corpus those engines retrieve from**. So while I can't see the synthesised AI answer, I can see whether SYSTEMology surfaces in the retrieval set the AI is choosing from — which is the upstream signal that matters most for citation strategy.

---

## Query-by-Query Findings

### 1. "What is SYSTEMology" — **OWNED**
- **Top sources:** systemology.com (#1), Target, Amazon, Audible, Apple Books, Instagram (@systemhub), execleadercoach.com (book review), thinkingbusinessblog.com (book review), systemhub.com.
- **SYSTEMology / Jenyns appears:** Yes — every result.
- **Quality:** AI summary correctly named the 7-step framework (Define, Assign, Extract, Organise, Integrate, Scale, Optimise), credited Jenyns, and mentioned systemHUB.
- **Competing authorities:** None. This is a branded query and SYSTEMology owns it.

### 2. "How do I systemise my small business" — **PARTIALLY VISIBLE**
- **Top sources:** ventureharbour.com, **systemhub.com (#2)**, businessgrowthmadeeasy.com, yoursmallbusinesscoach.com.au, usewhale.io, trainual.com, businessignites.com, Medium (Moe Nawaz), saasbpm.com, moenawaz.com.
- **SYSTEMology / Jenyns appears:** Indirect — systemhub.com guide is cited, but no mention of the book or the 7-step framework by name.
- **Quality:** Generic step-by-step (identify → document → automate → pilot → buy-in → refine). No CCF, no "Critical Client Flow," no "Systems Champion."
- **Competing authorities:** Whale (EOS-flavoured), Trainual, Venture Harbour, Moe Nawaz "Business Systemisation®" (registered trademark — direct positioning competitor).

### 3. "What is a Critical Client Flow" — **OWNED**
- **Top sources:** systemology.com (#1, #3, #6, #10), systemhub.com (#2), hellosocialavenue.com (uses CCF in marketing post), 3× YouTube videos featuring David, Agency Management Institute (Drew McLellan ran a SYSTEMology workshop).
- **SYSTEMology / Jenyns appears:** Yes — dominates the SERP.
- **Quality:** AI synthesised the definition correctly ("one-page map of 7-12 essential steps to attract, convert, and serve clients").
- **Competing authorities:** None — this is SYSTEMology-coined terminology and competitors haven't adopted it.

### 4. "How to document business processes for a small team" — **INVISIBLE**
- **Top sources:** docuflows.com, atlassian.com, oconomowoc.org (chamber of commerce), asana.com, scribe.com, guidejar.com, heflo.com, supademo.com, quickbase.com, magichow.co.
- **SYSTEMology / Jenyns appears:** **No.** Zero citations.
- **Quality:** Generic best-practice answer (single source of truth, video screencasts, quarterly review, team contribution).
- **Competing authorities:** Atlassian (Confluence), Asana, Scribe, Trainual-adjacent SaaS tools. **The "how-to-document" SERP is owned by tooling vendors, not methodology books.**

### 5. "What is a Systems Champion in business" — **OWNED**
- **Top sources:** systemology.com (#1, #4, #5, #8, #10), Amazon (Systems Champion book), Barnes & Noble, shortcuttowisdom.com (book summary), estimaterocket.com (uses the term), champion-business-solutions.com (unrelated ERP company).
- **SYSTEMology / Jenyns appears:** Yes — overwhelmingly. Five of ten URLs are systemology.com.
- **Quality:** Correctly framed the role as "right-hand to the owner," responsible for extraction and rollout, sweet spot 5–30 staff.
- **Competing authorities:** None — "Systems Champion" is SYSTEMology-coined terminology that David has successfully owned.

### 6. "Should I work IN my business or ON my business" — **INVISIBLE (E-Myth owns)**
- **Top sources:** **emyth.com (#1)**, thebootstrappedfounder.com, dulithawijewantha.medium.com, imogenroy.com, pregamehq.com, sparklight.com, **actioncoach.com**, cflambton.com, Quora, supplychaingamechanger.com.
- **SYSTEMology / Jenyns appears:** **No.**
- **Quality:** AI summary leaned heavily on EMyth's framing ("20% of time on the business").
- **Competing authorities:** **Michael Gerber / E-Myth** — and they own this query as decisively as SYSTEMology owns "Critical Client Flow." ActionCOACH (Brad Sugars) is the secondary authority.

### 7. "Best framework for business process documentation" — **INVISIBLE**
- **Top sources:** apqc.org, usewhale.io, makeautomation.co, magichow.co, cflowapps.com, navvia.com, blueprism.com, igrafx.com, eversign.com.
- **SYSTEMology / Jenyns appears:** **No.**
- **Quality:** AI defaulted to enterprise frameworks: BPMN, APQC PCF, ITIL, COBIT, Value Stream Mapping. Zero SMB lens.
- **Competing authorities:** APQC, BPMN.org, eTOM, Six Sigma, ITIL — all enterprise-grade. **The 10-50 employee buyer is unserved here**, which is exactly SYSTEMology's avatar.

### 8. "David Jenyns SYSTEMology book review" — **OWNED**
- **Top sources:** systemology.com/book/ (#1), Goodreads, Amazon, Blinkist, thirdearcr.com, systemology.com/scbook/, bitservices.us, profit-strategies.com, digitalagency.coach, systemology.com.
- **SYSTEMology / Jenyns appears:** Yes — every result.
- **Quality:** AI surfaced the Gerber foreword, the 7-step structure, and praise for the practical/SMB tone.
- **Competing authorities:** None on this branded query.

### 9. "How to hire a process documentation specialist" — **INVISIBLE**
- **Top sources:** vintti.com, indeed.com (×2), ziprecruiter.com (×3), jooble.org, avahr.com, manatal.com.
- **SYSTEMology / Jenyns appears:** **No.**
- **Quality:** Pure recruitment-platform content. JD templates, salary bands ($50k–$120k), Visio/Lucidchart skills, Six Sigma cert. **The Systems Champion concept is completely absent.**
- **Competing authorities:** Job-board SEO content. No methodology authority is cited.

### 10. "Business systemisation methodology" — **PARTIALLY VISIBLE**
- **Top sources:** beslick.com, usewhale.io (×2), **systemhub.com (#3)**, ventureharbour.com, growthidea.co.uk, **systemology.com (#7)**, businessignites.com, trainual.com, **personalmba.com (Josh Kaufman)**.
- **SYSTEMology / Jenyns appears:** Yes, but ranking 3rd and 7th — not in the top spots an AI prioritises.
- **Quality:** Generic 4-step (map → document → measure → improve). Personal MBA's "Systemization" page is a strong philosophical anchor that AIs love to cite.
- **Competing authorities:** **Josh Kaufman / Personal MBA**, Whale (EOS), Trainual, Beslick. Moe Nawaz again.

---

## Synthesis

### Where SYSTEMology Already Wins (4 of 10 queries)
1. **"What is SYSTEMology"** — branded, owned.
2. **"What is a Critical Client Flow"** — coined-term moat, fully owned.
3. **"What is a Systems Champion"** — coined-term moat, fully owned.
4. **"David Jenyns SYSTEMology book review"** — branded, owned.

**Pattern:** SYSTEMology dominates anything containing its proprietary vocabulary. The CCF + Systems Champion language strategy has worked — those terms are now SEO-defensible category labels.

### Where SYSTEMology Is Invisible (4 of 10 queries)
1. **"How to document business processes for a small team"** — owned by SaaS tools (Atlassian, Asana, Scribe, Trainual).
2. **"Should I work IN my business or ON my business"** — owned by E-Myth (emyth.com #1, with halo for Gerber).
3. **"Best framework for business process documentation"** — owned by enterprise frameworks (BPMN, APQC, ITIL, Six Sigma).
4. **"How to hire a process documentation specialist"** — owned by job boards (Indeed, ZipRecruiter, Vintti).

**Pattern:** Generic "how to" and "best framework" queries default to either (a) tooling vendors or (b) enterprise methodology bodies. The 10-50 employee SMB buyer who *should* be SYSTEMology's customer is being handed enterprise-grade BPMN diagrams or recruitment-platform JD templates.

### Where SYSTEMology Is Partially Visible (2 of 10 queries)
1. **"How do I systemise my small business"** — systemhub.com cited but framework not named.
2. **"Business systemisation methodology"** — systemhub.com #3, systemology.com #7. Beaten by Beslick, Whale, Personal MBA.

### Competing Frameworks Eating SYSTEMology's Lunch
| Competitor | Where they win | Threat level |
|---|---|---|
| **E-Myth (Michael Gerber)** | "Work ON vs IN," foundational SMB systems philosophy | High — Gerber's foreword is an asset, but the brand is being out-cited |
| **EOS / Traction (Gino Wickman)** | "Systemise" via Whale's content | Medium — Whale has hijacked the SEO with EOS framing |
| **Personal MBA (Josh Kaufman)** | "Systemization" definitional content | Medium — single-page authority that AIs love |
| **Moe Nawaz "Business Systemisation®"** | Branded competitor on the exact term | Low-medium — limited reach but trademark-positioned |
| **Trainual / Whale / Scribe / Process Street** | "How to document" tooling-led content | High — tooling vendors out-publishing methodology authors |
| **APQC / BPMN / ITIL / Six Sigma** | "Best framework" enterprise queries | High but mismatched — wrong audience for SYSTEMology |
| **ActionCOACH (Brad Sugars)** | "Work ON vs IN," SMB coaching | Medium |

---

## Recommended Chapter Targeting Priority

Score = (citation gap × commercial intent for systemHUB / SCA). Higher = launch the chapter first as a standalone /book/[chapter]/ landing page with rich snippets.

| Priority | Chapter / Concept | Target Query | Citation Gap | Commercial Intent | Notes |
|---|---|---|---|---|---|
| **1** | **Define stage / CCF** rebuild as the answer to "documenting processes" | "How to document business processes for a small team" | **High** | **High** — this is the top funnel | Build the chapter page to hijack from Atlassian/Asana/Scribe with the SMB lens. Add comparison block: "Why BPMN diagrams fail in 10-50 employee businesses." |
| **2** | **Foreword + Ch.1 (the SYSTEMology mindset)** rebutting/extending Gerber | "Should I work IN my business or ON my business" | **High** | **High** — early-funnel awareness | Lead with Gerber's foreword (asset). Position SYSTEMology as the *implementation* layer Gerber never wrote. Aim to co-cite alongside emyth.com, then displace. |
| **3** | **Ch.2 Assign / Systems Champion role** | "How to hire a process documentation specialist" | **High** | **Very high** — SCA + Champion-tier signal | Job-board SEO is a wide-open lane. Publish a JD template + hiring scorecard + "why a Systems Champion outperforms a Documentation Specialist" comparison. |
| **4** | **Whole-book pillar** vs. enterprise frameworks | "Best framework for business process documentation" | **High** | Medium — broader awareness | Write a "SYSTEMology vs BPMN vs Six Sigma vs ITIL for small business" comparison page. AIs love comparison tables; this earns citations on a query SYSTEMology currently can't crack. |
| **5** | **Ch.4 Organise / Ch.5 Integrate** for "systemisation methodology" | "Business systemisation methodology" / "How do I systemise my small business" | Medium | High — bottom funnel intent | Already partial visibility — the goal is to lift systemology.com from #7 to #1. Refresh existing pages and link to /book/ chapters. |
| **6** | **Ch.3 Extract** | (no current high-volume target) | Low | Medium | Ride along; not a standalone hijack target. |

### Quick Wins (do first, week 1)
- Publish **Ch.1 + Foreword as /book/work-on-not-in/** with a Gerber co-citation play.
- Publish **Ch.2 as /book/systems-champion/** consolidating with the existing Systems Champion authority pages.
- Publish **a "vs BPMN / Six Sigma / ITIL"** comparison under /book/process-documentation-frameworks/.

### Defend
- Continue feeding /critical-client-flow/ and /systems-champion/ — these moats are working but every competitor will keep poking.

### Watch
- Moe Nawaz "Business Systemisation®" — direct trademark-positioned competitor.
- Whale + Trainual — they're winning the EOS-flavoured "systemise your business" lane with sheer publishing volume.

---

## Re-Test Plan
Run these same 10 queries 30 / 60 / 90 days after /book/ launch. Track:
- (a) Whether systemology.com URL count in the top-10 increases for the four currently-invisible queries.
- (b) Whether AI Overview / Perplexity answers begin naming "SYSTEMology" or "the 7-step framework" on the partially-visible queries.
- (c) Whether the Gerber co-citation play earns SYSTEMology a slot alongside emyth.com on the Work IN/ON query.

A measurable win = +2 systemology.com URLs in the top 10 across the four invisible queries within 90 days, and at least one query (likely "how to document business processes for a small team") flipping from invisible to partially visible.
