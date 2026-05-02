# Cannibalisation Audit + Redirect/Canonical Plan

Pulled: 2026-05-02. Source: GSC last-90-days data ([04-gsc-rankings.md](04-gsc-rankings.md)) + live page audits.

---

## TL;DR — the architecture-defining finding

**`/book/` already exists** on systemology.com as the current SALES page for the printed book, with strong rankings:

| Query | Page | Position | Clicks (90d) | Impressions (90d) |
|---|---|---:|---:|---:|
| systemology | `/book/` | 1.8 | 40 | 2,646 |
| systemology book | `/book/` | 1.4 | 30 | 379 |
| systemology pdf | `/book/` | 9.8 | 2 | 165 |

We **cannot delete or redirect this URL** — it's a major authority page already absorbing high-intent traffic.

**Architecture decision (recommended):** Transform `/book/` from a pure sales page into a **dual-purpose hub**: free interactive reader at the top, distribution links (Amazon/Audible/etc) preserved below. New chapter URLs live at `/book/chapter-1-define/` etc. This preserves all existing SEO equity while making the content AI-citable.

---

## Existing pages and what to do with each

### TIER 1 — Major book-intent pages (preserve & repurpose)

#### `/book/` — Current book sales page
- **H1:** "The Simple System To Systemise Your Business."
- **Purpose:** Sells physical/digital book via Amazon, Audible, Apple, B&N, Google Play
- **GSC equity:** ranks #1.4 for "systemology book", #1.8 for "systemology"
- **Decision:** **TRANSFORM, don't redirect.** New `/book/` is the free-online-book hub.
  - Hero: "Read SYSTEMology free, online — start with Chapter 1"
  - Section: chapter cards (visual TOC)
  - Keep below: testimonials, author bio, Amazon/Audible/Apple/B&N links ("Prefer a physical copy or audio?")
  - Migrate the existing testimonials and praise section verbatim
  - Outcome: Page now serves both "I want to read it free" + "I want to buy a copy" + AI citation

#### `/book-resources/` — Stage-by-stage downloads page
- **H1:** "Book Resources"
- **Purpose:** Downloads (CCF template, DRTC, SAS, System for Systems, dashboard) organised by 7 stages
- **GSC equity:** ranks #3.1 for "systemology" (636 imp), #1.5 for "systemology book" (321 imp)
- **Decision:** **Decommission gracefully.**
  - Each stage section becomes a CTA inside the matching chapter (CCF template → embedded download in Chapter 1 / Define)
  - 301 redirect `/book-resources/` → `/book/` (the new chapter-list hub)
  - Anchors: `/book-resources/#define` → `/book/chapter-1-define/`

#### `/launchpad/` — Email-gated resources hub
- **H1:** "FREE Business Systemisation Templates & Playbooks"
- **Purpose:** Lead capture for book readers (every printed book points here)
- **GSC equity:** ranks #2.1 for "systemology" (1,881 imp)
- **Decision:** **Keep but rewire.** This is the lead capture asset for printed-book readers — it's printed in the book itself, can't be removed.
  - Update content: new "now you've finished the book, here's what's next" framing
  - Add prominent link: "Reading the book online? Visit `/book/`"
  - Keep email capture (this is the audiobook trade)
  - **Important:** the printed book still says `/launchpad/` — never break this URL.

---

### TIER 2 — Chapter-content overlapping pages (resolve via canonical/internal-link)

These pages rank for queries that the new chapters will also target. Don't redirect — they're earning real traffic. Establish canonical hierarchy and cross-link.

#### `/business-systems-guide/` — Major asset
- Ranks **#3.3 for "business systems"** (6,880 imp/mo, 72 clicks)
- **Decision:** UNTOUCHED. Highest-traffic page on systemology.com. Book chapters link TO this guide as a "deep dive" reference. Guide gets one prominent inline link to the book at the top.

#### `/critical-client-flow/`
- Ranks #5.9 for "systemology" + chapter-relevant
- **Decision:** Keep as standalone landing page (CCF lead magnet entry).
  - Add `<link rel="canonical">` pointing to itself (it's a tool, not a chapter)
  - Cross-link to/from Chapter 1 (Define): "Read the chapter that introduces CCF →" / "Use the interactive CCF tool →"

#### `/mvs/` (Minimum Viable Systems)
- Ranks #5.7-10.5 for "mvs", "mvs meaning", "what is mvs" (1,275+193+186 imp = 1,654 imp/mo)
- **Decision:** Same pattern as CCF — keep landing page, cross-link with Chapter 6 (Scale)

#### `/process/`
- Ranks #1.8 for "systemology" (2,025 imp)
- Likely the homepage of a process/methodology section
- **Decision:** Audit content. Probably keep + cross-link to chapter intro.

#### `/about/`
- Ranks #1.7 for "systemology" (989 imp), #7.5 for "david jenyns" (132 imp)
- **Decision:** Untouched. Cross-link from book "About the author" section.

#### `/scbook/` (Systems Champion book)
- Ranks #3.9 for "systemology" (296 imp)
- **Decision:** Untouched. The Systems Champion book is the companion volume — it gets its own /book/ treatment in Phase 2 if this works.

#### `/getcertified/`
- Ranks #2.2 for "systemology" (445 imp)
- **Decision:** Untouched. Cross-link from end-of-book CTA ("Become a certified SYSTEMologist").

---

### TIER 3 — Misc pages catching book-PDF intent (high-value redirect targets)

These pages are absorbing "systemology pdf" / "systemology download" intent in roundabout ways — they should funnel cleanly into `/book/`.

#### `/wp-content/uploads/2020/07/SYSTEMology-preview.pdf`
- Ranks **#1.2 for "systemology pdf"** (264 imp, **89 clicks/mo** — significant!)
- **Decision:** This is a sample PDF being downloaded directly. **Replace the file with a single-page PDF** that says:
  - "You found the SYSTEMology preview. The full book is now available free online: systemology.com/book/"
  - Link to the new reader
  - Keeps the URL alive (don't break inbound links) but redirects user intent
  - Alternatively: 301 redirect this URL via .htaccess to `/book/`

#### `/systems-cheatsheet/`
- Ranks #3.6 for "systemology pdf" (209 imp, 21 clicks)
- **Decision:** Keep page, but add prominent "Looking for the full book? Read it free →" banner at top.

#### `/free-resources/`
- Ranks #2.1 for "systemology" (2,186 imp), #6.5 for "systemology pdf" (145 imp)
- **Decision:** Keep, but feature `/book/` prominently as the #1 resource ("Read the book free, online").

#### `/12-must-read-books-for-small-business-owners-entrepreneurs/`
- Ranks #11.4 for "small business books" (478 imp), and similar for related queries (1,300+ imp combined)
- **Decision:** Add internal link to `/book/` as one of the recommended books. SYSTEMology should be #1 on its own list with "Read it free" CTA.

---

## "SYSTEMology PDF" intent — total addressable volume

Combining all queries containing "pdf":

| Query | Total Imp (90d) | Best Position | Best Page |
|---|---:|---:|---|
| systemology pdf | 281 | 1.2 | preview.pdf |
| systemology book pdf | 106 | 1.9 | (various) |
| systemology david jenyns pdf | 123 | 1.4 | (various) |
| **TOTAL** | **~510 imp/mo** | | |

That's **~170 imp/mo, ~30+ clicks/mo** of pure PDF intent currently scattered across multiple pages. Consolidating this into `/book/` could materially lift the asset.

**Implementation:**
- New `/book/` h1: "Read SYSTEMology free, online" (or similar)
- Meta description includes: "...read the full book free as a PDF, web, or audiobook..."
- A `/systemology-pdf/` URL slug that 301s to `/book/` — captures the intent in URL form
- The preview PDF gets replaced as described above
- Add structured FAQ markup answering: "Where can I download the SYSTEMology PDF?" → "Read it free at systemology.com/book/"

---

## Internal linking map (book ↔ rest of site)

```
/ (homepage)
  ├─ Hero/nav: "Read the book free →" link to /book/
  └─ Footer: book link

/book/ (NEW — chapter hub)
  ├─ Chapter 1 → cross-link to /critical-client-flow/, /get-ccf/
  ├─ Chapter 2 → cross-link to /systems-champion-position/, /system-champion-training/
  ├─ Chapter 3 → cross-link to /lp/system-for-systems/ (systemHUB)
  ├─ Chapter 4 → cross-link to /pricing/ (systemHUB), /systems-cheatsheet/
  ├─ Chapter 5 → cross-link to /onboarding-accelerator/
  ├─ Chapter 6 → cross-link to /mvs/, case studies (Stannard, Successwise)
  ├─ Chapter 7 → cross-link to /ai-first-company/, /ai-first-accountant/
  └─ End-of-book → /getcertified/, /pricing/, /launchpad/

/business-systems-guide/ (UNTOUCHED, top traffic)
  └─ Add: "Want the full methodology? Read SYSTEMology free →" link

/launchpad/ (UNCHANGED URL — printed book points here)
  └─ Add: "Reading online? Continue at /book/"

/free-resources/
  └─ Feature /book/ as #1 resource

/wp-content/.../SYSTEMology-preview.pdf
  └─ Replace file with redirect-PDF or 301 redirect URL
```

---

## Risks & mitigations

**Risk 1: Transforming `/book/` could lose its #1.4 ranking for "systemology book"**
- *Mitigation:* Keep H1 mention "SYSTEMology book", keep all testimonials, keep Amazon/Audible links. The page is *expanding*, not changing topic. Google should reward more content depth.

**Risk 2: Stage-named queries already rank for blog content (e.g. "what is mvs" → /mvs/)**
- *Mitigation:* Don't aim chapter URLs at "what is mvs" head term — let the existing /mvs/ page own it. Aim chapter URLs at long-tail like "minimum viable systems systemology" + framework-specific queries.

**Risk 3: AI crawlers may prefer the existing `/business-systems-guide/` over new /book/ chapters**
- *Mitigation:* The book is BookChapter-marked, the guide is Article-marked. Different schema types. Both can coexist in AI answers — the guide for "what are business systems" definitional, the book for methodology citations.

**Risk 4: Sales page conversion drops if free version cannibalises print sales**
- *Mitigation:* Print/audiobook offers stay prominent. Free HTML readers are not the same audience as print buyers. Track Amazon affiliate clicks pre/post launch.

---

## Decisions Dave needs to confirm

1. **Confirmed by Dave already:** `/book/` is the canonical URL (Cloudflare Worker routes `/book/*` to Pages). Existing sales page content gets folded into the new build at the same URL.
2. **NEW DECISION REQUIRED:** Approve the dual-purpose structure (free reader on top, distribution CTAs preserved below)?
3. **NEW DECISION REQUIRED:** Approve repurposing `/book-resources/` (301 to `/book/`)?
4. **NEW DECISION REQUIRED:** Approve replacing the `/wp-content/uploads/.../SYSTEMology-preview.pdf` with a redirect-PDF?
5. **NEW DECISION REQUIRED:** Comfortable with the printed book still pointing readers to `/launchpad/` separately from `/book/`? (Yes is the recommended answer — they serve different intents.)
