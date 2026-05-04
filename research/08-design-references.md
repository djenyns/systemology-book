# 08 — Design References for /pdf/

Research brief for the free interactive online edition of *SYSTEMology* at `systemology.com/pdf/`. We studied four canonical free-online-book sites and pulled their actual stylesheets and HTML so the recommendations below are grounded in real values, not generic web-design folk wisdom.

Sources fetched live: `basecamp.com/shapeup/`, `basecamp.com/shapeup/0.3-chapter-01`, `basecamp.com/gettingreal`, `paulgraham.com/articles.html`, `paulgraham.com/ds.html`, `press.stripe.com/`, `press.stripe.com/scaling-people`, plus their CSS bundles (`web-book.css`, Stripe `v1-Page-*.css`, `v1-BookDetails-*.css`, Typekit kit `xig7qap`).

---

## 1. Shape Up — Basecamp (the closest direct analog)

### A. Visual identity
- **Single CSS file** `/assets/css/web-book.css` (774 lines, ~22 KB) — that's the entire visual system.
- **Colour palette** is declared as RGB triplets in CSS custom properties so dark mode is one variable swap:
  ```css
  :root {
    --color-text: 0, 0, 0;
    --color-background: 255, 255, 255;
    --color-link: 0, 0, 0;
  }
  @media (prefers-color-scheme: dark) {
    --color-text: 255, 255, 255;
    --color-background: 0, 0, 0;
    --color-link: 255, 255, 255;
  }
  ```
  No accent colour. Links are the same colour as body text — they rely on context, not blue, to signal interaction. `theme-color` meta is `#000000`.
- **Typography:** body is **FF Meta Serif Web Pro** (Erik Spiekermann / Christian Schwartz), served via Adobe Typekit kit `xig7qap` with four weights (regular 500, italic 500, bold 700, bold italic 700). Headings inherit the serif. Code uses the Apple system mono stack: `SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace`.
- **Sizing is fluid, not fixed.** The body font size is a `calc()` against viewport width:
  - Mobile (< 50em): `--type-base: calc(1.6em + 0.5vw)` — ≈ 26 px on a 375 px viewport
  - Tablet/desktop (≥ 50em): `--type-base: calc(0.9em + 0.9vw)` — ≈ 23 px on 1280 px, 25 px on 1440 px
  - Massive (≥ 100em): `--type-base: 2.75em` — ≈ 44 px on 4K
- **Modular type scale** with seven steps: `--type-x-small: 75%`, `--type-small: 85%`, `--type-medium: 100%`, `--type-large: 120%`, `--type-x-large: 160%`, `--type-xx-large: 200%`, `--type-xxx-large: 300%`. Every text element references a step, never a raw px value.
- **Line height** is `1.5` for body `<p>` and `1.2` for headings. Paragraph spacing is `margin: 1em 0 0 0` — top-only, which collapses cleanly.

### B. Hub / TOC
- One landing page at `/shapeup/`. Hero is the book cover image (`cover_summary.jpeg`) sitting beside title + subtitle. Two CTAs immediately under the title: "Buy the print edition" and "Start reading →". The print buy link comes first, but is visually equal — they aren't pushing the funnel hard.
- The TOC underneath is a flat list grouped by Part. Each chapter shows: a small uppercase masthead like `CHAPTER 1` (`text-transform: uppercase; letter-spacing: 0.3rem; font-size: var(--type-xx-small)` — 65% of base), the chapter title in serif, and the section anchors as a left-bordered nested list (`.toc__sections { border-left: 0.1rem solid; }`).
- No images per chapter on the TOC. Pure typographic hierarchy.

### C. Chapter page
- HTML is brutally simple. The chapter body is just `<p>` and `<h2 id="growing-pains">` — **zero `<aside>`, `<blockquote>`, `<figure>`, or `<figcaption>` in chapter 1.** Body content is the content. Period.
- Layout is a CSS Grid with two areas: `sidebar | content` at ≥ 50em (`grid-template-columns: 0.85fr 2.5fr`). Below 50em the sidebar collapses above the content as a drawer.
- The sidebar is **sticky** (`position: sticky; top: 2em`) and contains: chapter masthead ("Chapter 1:"), chapter title, an anchor list of every H2 in the chapter, a "Next: [next chapter title]" link. It is the chapter's mini-TOC — also the de facto progress indicator (you scan which anchor is highlighted).
- The right column has `padding: 2.65em 6em 0 3.5em` on desktop, which keeps the measure tight despite a 2.5fr column.
- Pull quotes / callouts in the CSS exist (`blockquote { font-style: italic; border-left: 0.2rem solid; padding-left: 1em }`) but are used very sparingly. The styling is a classic left-rule italic — no boxes, no backgrounds.
- Drop caps: none.
- A "Heads up!" warning bar at the top of every page nags users on browsers without CSS Grid (`@supports(display: grid) { .warning { display: none; } }`). Genius progressive-enhancement fallback — the book still reads at 16px on a 2002 browser.

### D. Navigation
- Sticky left sidebar = persistent in-chapter nav.
- Hamburger button at top of sidebar opens a slide-in `.menu` with the full book TOC (`position: fixed; max-width: 30em; transform: translate(-100%, 0)` → slides in). Backdrop blur where supported.
- "Next: [chapter title]" at the bottom of each chapter. No "previous" link — direction is always forward.
- Each H2 has a hover-revealed anchor link (`a.anchor-link`) for stable URL fragments like `/shapeup/0.3-chapter-01#growing-pains`.
- No scroll-progress bar, no read-time estimate, no bookmark UI.

### E. Pull-quotes + emphasis
- Bold + italic inside paragraphs do all the work. **Bold for the canonical noun** ("we work in **six-week cycles**"); *italic for emphasis* ("How much time do we want to *spend*?"). It's a tight pattern — read three paragraphs and you've internalised it.
- No tweetable callout boxes, no pull-quotes in the typographic sense, no glyph dingbats, no rules between sections.

### F. Images, diagrams, code
- Images are full-bleed within the content column with `border-radius: 1rem` (subtle) and a `<figure>` + `<figcaption>` pattern (italic small caption). Margins `1em 0 2em 0`. Diagrams are line-art SVGs/PNGs sitting on white — they read as part of the book, not screenshots.
- Code: rounded inline pills (`background: rgba(text, 0.075); padding: 0.25rem 0.5rem; border-radius: 0.2rem`) at `--type-x-small` (75%).

### G. Footer + CTA strategy
- End-of-chapter is just the "Next: …" link and a hairline `border-top` footer with the copyright line. No re-pitch, no "buy the book" repeat. The buy link lives only on the hub.
- Sidebar contains a small "← Basecamp.com" link and the persistent book title button — that's the only product link inside the reading flow.

### H. Mobile
- Genuinely good. The fluid `calc(1.6em + 0.5vw)` makes body text readable without zoom. The sidebar collapses, the menu becomes a hamburger drawer, padding drops to `1.5em`. `viewport` meta is set. No mobile-only hacks.

### I. AI/SEO touches in source
- Full OG + Twitter card tags on every page (`og:title`, `og:description`, `og:image: /assets/images/opengraph/shape-up.png`, `twitter:card: summary_large_image`).
- Sitemap at `/sitemap.xml` — includes Shape Up chapters.
- **No `llms.txt`** at root or under `/shapeup/`.
- **No JSON-LD `Book` or `Chapter` schema** in the head — surprising. Schema is left implicit.
- Stable URL pattern `/shapeup/0.3-chapter-01`, `/shapeup/1.1-chapter-02` — Part.Chapter numbering visible in the URL.

### J. What's distinctive
- The whole book is **one CSS file, one font family, two colours**. The constraint *is* the brand — it screams "this content is the product".
- Sticky chapter sidebar that doubles as TOC + progress + next-link, all in one column.
- Prefers-color-scheme dark mode that's literally a four-line override.

**Things to steal (must steal)**
- CSS custom properties as `R, G, B` triplets so prefers-color-scheme is a one-line swap.
- Modular type scale of seven steps tied to a fluid `--type-base` — every other size is a `%` of that.
- Sticky in-chapter sidebar with chapter mini-TOC + Next link.
- Hover-reveal `.anchor-link` on every H2.
- "Heads up!" CSS-Grid `@supports` warning as the universal fallback.
- One shared template `web-book.css` reusable for *Systems Champion* and any future free book — it's already proven Basecamp uses the same file for both Shape Up and Getting Real.

**Things to skip**
- The all-black-link convention. Our brand uses `#0098ce` — keep it.
- No "previous" link is a defensible minimalist choice but our readers will want it.
- The 75% sizing on inline code — we don't have code.

---

## 2. Stripe Press

### A. Visual identity
- **Custom Ivar variable-font family**, three optical sizes: **Ivar Display, Ivar Headline, Ivar Text** — all served as variable `woff2`. Body is `font-family: Ivar Text, Georgia` weight 500. Buttons / nav use Ivar Headline 600. Book titles use Ivar Display 700.
- **Dark by default.** The home page is `background: #201819` (a near-black warm brown) with `color: #fff`. Each book page swaps to a per-book colour palette via `--backgroundColor` / `--color` custom properties, so each book has its own atmosphere (Working in Public is teal, Scaling People is muted green, etc.).
- Headings are `font-weight: 400, font-size: 16px, line-height: 1` baseline (overridden per component). Body `p` is `line-height: 1.5`. Buttons use a subtle `letter-spacing: 0.32px`.
- Book detail page measure: `font-size: 17px; line-height: 1.5` with `padding: 0 6vw calc(var(--vh) * 10) 14vw` on mobile and `padding: 0 8vw …` ≥ 900 px. The 14vw left padding is the giveaway — Stripe leaves 14% of viewport blank on the *left* to anchor the column toward the centre.
- A 60-px-wide hairline rule (`width: 60px; height: 1px`) is the universal section separator. Every label is preceded by it (`::before { content: ""; width: 60px; border-bottom: 1px solid; }`). Tiny, but it's the move that makes the whole site feel "designed".

### B. Hub / TOC (the press home)
- A WebGL-driven canvas with floating book covers you can drag/spin between. Behind the canvas is the static product list. The visual hero is the book *as object* (full cover, drop-shadow, 3D-rotated) — Stripe's sales argument is "this book deserves a place on your shelf".
- No grid of cards. Linear vertical scroll, one book at a time, each with: title in Ivar Display, italic bridging label ("a book by"), description, Buy buttons, praise blockquotes, author bio. White space and rule-marks do all the separating.

### C. Individual book page (e.g. `/scaling-people`)
- Title is `font-size: calc(19px + 0.75vw); line-height: 1.4; font-family: Ivar Display; font-weight: 700` — fluid display type. At 1600 px+ it caps at `1.75em` with `letter-spacing: 0.32px`.
- Two-column at ≥ 900 px: 58% left for the cover/canvas, 42% right for description + buy options. Below 900 px it stacks.
- Buy buttons are the headline interaction: bordered rectangles (`border: 1px solid var(--color)`) with a hover state that slides a 4 px coloured bar in from the left and translates the icon — animation is restrained but present.
- "Praise" section is a blockquote stack, each quote on its own with attribution underneath in italic. Multiple endorsements per book.

### D. Navigation
- Top nav is the standard Stripe site header (refreshed nav menu, dashboard login link). Stripe Press inherits the parent's nav rather than building its own.
- Inside the homepage canvas: drag/swipe to spin to next book. On mobile: tap the indicator dots.
- Free reading where available (e.g. *The Revolt of the Public*) lives at `/the-revolt-of-the-public/foreword` etc. — chapter URL pattern is slug-based, not numbered.

### E. Pull-quotes + emphasis
- Italic + 1.2em font-size for "labels" (`.PressHomepageBookDetails__label { font-size: 1.2em; font-style: italic; }`) prefixed by a 60 px rule mark.
- "Praise" blockquotes are full-width stacked, no quotation glyph, no box — just italic body and an attribution line.
- The "buy" call has its own typography: `.PressHomepageBook__buyGrouplabel { font-size: 21px; font-style: italic; font-weight: 500; font-family: Ivar Display; line-height: 1.2; }`. Italic Display in 21 px — a moment of self-confidence.

### F. Images, diagrams, code
- Every book has a unique hero treatment (3D cover, video, atmospheric image). On free chapter pages the body returns to text-only with figures used sparingly. No code blocks on Press itself.

### G. Footer + CTA strategy
- Newsletter signup, social links, contact email `stripepress@stripe.com`, physical address. Soft.
- Buy CTAs offer multiple retailers (Bookshop, Amazon, Barnes & Noble) at the same visual weight — Stripe doesn't care which channel you use, it cares that the book gets read.

### H. Mobile
- Canvas/3D experience degrades to static covers with a `--vh` custom property to handle iOS Safari viewport quirks. Book details restack to one column. Type scales fluidly via `calc()`.

### I. AI/SEO source signals
- Full OG/Twitter meta: `og:title`, `og:description`, `og:image: …/social.png?q=80`, Facebook domain verification, canonical link.
- Stylesheets are split per component (`v1-Page-*.css`, `v1-Book-*.css`, `v1-BookDetails-*.css`) — bundle-splitting for Core Web Vitals.
- `<meta data-js-controller="ScrollDepthTracker">` and `MonitorWebVitals` — they're tracking engagement, not just page views.
- No `llms.txt`, no `robots.txt` at `press.stripe.com` (404). No public sitemap.
- No JSON-LD `Book` schema on the pages we examined.

### J. What's distinctive
- **Variable-font typography is the brand.** Ivar at three optical sizes is doing the work that colour and ornament do on lesser sites.
- **Per-book colour palette via CSS custom properties** — same template, different soul each time.
- **60 px rule-mark before every label** as a universal punctuation glyph.
- **Italic at 1.2em as the editorial voice** — Stripe italicises section labels, buy-group labels, attributions. It's their signature.

**Things to steal (must steal)**
- Two-tone palette per *book*, expressed as CSS custom props: SYSTEMology can have `--accent: #0098ce`; *Systems Champion* (when we online it) can have its own without touching the template.
- A signature "rule-mark before label" pattern (60 × 1 px hairline + italic small caps label).
- Italic 1.2em as the editorial register for chapter abstracts, callouts, captions.
- Body 17 px, line-height 1.5 as a sane default if we don't go fluid.
- Component-split CSS (`page.css`, `chapter.css`, `toc.css`) so the chapter page doesn't ship hub-page bytes.

**Things to consider stealing**
- Variable webfont. Beautiful but adds a webfont budget; only worth it if we commit to reading-experience as primary differentiation.
- Per-book accent colour. Worth it once we have a second book online.

**Things to skip**
- The WebGL canvas. Not appropriate for a free reading site we want indexed by search/LLMs.
- Dark default. Our brand is white-ground; honour it.
- The complete absence of structured data. Don't follow Stripe here — we want LLM citation.

---

## 3. Getting Real — 37signals (2006, still live in 2026)

### A. Visual identity
- **Reuses the exact same `web-book.css` as Shape Up.** Same Typekit kit `xig7qap`, same FF Meta Serif Web Pro, same modular type scale — Basecamp ported their 2019 Shape Up template back over the 2006 source. Old book, new chrome.
- Inline `<style>` overrides only the colour:
  ```css
  --color-text: 29, 45, 53;       /* #1d2d35 */
  --color-background: 255, 255, 255;
  --color-link: 29, 45, 53;
  ```
  Body text is a desaturated near-black navy. They did **not** flip the prefers-color-scheme block — Getting Real explicitly *kills* dark mode by repeating the light values inside the dark-scheme media query. (Conscious choice.)

### B. Hub / TOC
- Identical structural template to Shape Up: cover image, title, "Buy the print edition" + "Start reading →", grouped chapter list with Part headings.

### C. Chapter page
- Same `intro` sticky sidebar pattern. Same content column. Same hairline footer. The 2006 content reads well in 2025 Basecamp's typography because the template is content-agnostic.

### D-J
- All same as Shape Up — they didn't fork the template, they republished the manuscript inside it.

**The lesson is the architecture, not the design.** Basecamp built a generic "free book online" template (`web-book.css`) and used it for two books spanning 13 years. It is the cheapest possible way to have a polished, mobile-friendly online edition.

**Things to steal (must steal)**
- The principle: **build SYSTEMology and Systems Champion on the same shared template** with a 3-line colour override per book. Don't re-design for the second book.
- Inline-style colour override pattern — keep the template canonical and override per-book on the page itself if needed.

**Things to skip**
- The 2006 link copy ("We made Basecamp using the principles in this book") — too soft. Our CTA strategy is more deliberate.

---

## 4. Paul Graham's essays

### A. Visual identity
- **No CSS file.** No `<link rel="stylesheet">`. No `<style>` block. The page is `<font size="2" face="verdana">` wrapped in nested `<table>` elements with `cellpadding="0" cellspacing="0"` and 1×1 transparent GIF spacers (`trans_1x1.gif`) for layout. This is 1998 HTML rendered in 2026.
- **Colour palette is `<body bgcolor="#ffffff" text="#000000" link="#000099" vlink="#464646">`** — body white, text black, links navy `#000099`, visited links grey `#464646`.
- **Typography is Verdana 2** (HTML `<font size="2">` ≈ 13 px). Title is a GIF image (`do-things-that-don-t-scale-3.gif`). Body content sits in a `width="435"` table cell — a hard fixed character measure of ≈ 65–70 chars at Verdana 13.

### B. Hub
- `articles.html` is one giant flat list. Each row is `[image | <a href="essay.html">Title</a> | spacer]` in a table. Reverse chronological. No descriptions, no dates on the index, no categories.

### C. Essay page
- Date plain-text at top ("July 2013"). Title is a GIF. Body is HTML `<p>` paragraphs separated by `<br /><br />`. Section headings are `<b>Recruit</b>` — bold inline, not even an `<h2>`.
- Footnotes are inline anchors `<font color=#999999>[<a href="#f1n">1</a>]</font>` linking to a Notes section at the bottom. That's the *only* navigation device on the page.

### D. Navigation
- None. No prev/next, no TOC, no sticky anything, no scroll progress, no breadcrumbs. The left rail is a clickable image-map of site sections (Articles, Books, YC, RSS, Bio, etc.) — one persistent piece of nav that doesn't change between essays.

### E. Pull-quotes + emphasis
- `<b>` inline subheads + `<i>` emphasis. No blockquotes, no boxes. Two coloured callout strips at the page top: a yellow `bgcolor=#ffcc33` with "New: …" and an orange `bgcolor=#ff9922` with "Want to start a startup? Get funded by Y Combinator." The funnel CTA is one orange table cell at the top of every essay.

### F-G. Images / footer
- Almost no images in essay bodies. Footer = translation links + "Thanks" acknowledgements. No copyright line.

### H. Mobile
- Genuinely poor. `width=435` on the body table, no viewport meta — you must pinch-zoom on a phone. PG hasn't budged on this in 20+ years.

### I. AI/SEO source signals
- No OG tags, no Twitter cards, no JSON-LD, no canonical, no sitemap.xml, no `<meta description>`. There is a `robots.txt` (200) and the site has been semi-static and unchanged at the same URLs for 20+ years.
- `llms.txt` redirects 302 → `/` (he hasn't bothered).
- **Why this works for AI citation anyway:**
  1. **Zero structural noise.** No `<div class="wrapper">` soup. The text is the DOM. LLM crawlers parse it with near-perfect signal-to-noise.
  2. **URL stability across decades.** `/ds.html` has been at that URL since 2013. Citation anchors don't rot.
  3. **Filename = topic slug.** `goodwriting.html`, `brandage.html`, `foundermode.html` — each filename is also the canonical short-name for the idea. That's how the LLM training data refers to them.
  4. **Title-only links on the index** mean an LLM scraping `articles.html` gets a clean (title, URL) tuple for each essay, no card cruft.
  5. **Footnote anchors** (`#f1n`) make every cited claim individually addressable.

### J. What's distinctive
- The aesthetic constraint is so absolute it transcends design. **The form says "the ideas are what matters; here they are."** That's a brand position you can't fake with a thoughtful design system — but you can borrow elements of it.

**Things to steal (must steal)**
- **URL stability.** Every chapter URL must outlive a redesign. Settle the slug structure before launch and never change it.
- **Filename = idea slug** convention. `/pdf/define/`, `/pdf/assign/`, `/pdf/extract/` mirror SYSTEMology's seven steps.
- **Stable fragment anchors** (e.g. `#growing-pains`) on every H2, with hover-reveal anchor links so readers can copy a deep link without ceremony.
- **Footnote pattern**: numbered inline, anchored to a Notes section at the chapter bottom. Use `<sup><a href="#fn-1" id="fnref-1">[1]</a></sup>` and back-link with `<a href="#fnref-1">↩</a>`.
- **Minimal DOM in the article body.** No wrapper divs — `<article>` containing `<h1>`, `<p>`, `<h2>`, `<p>`. Let LLMs see the prose.
- **Resist nav cruft inside the essay.** Sticky sidebars yes; floating share buttons no; chat widgets absolutely not.

**Things to skip**
- Verdana 13 px on a 435-px column. We can be readable AND citation-friendly.
- Image-as-title. Bad for screen readers, search, and LLMs alike.
- Table-based layout. CSS Grid is fine.
- Skipping OG / JSON-LD. We have brand and SEO obligations PG doesn't.

---

## Final synthesis — design rules for `/pdf/`

These eight rules are drawn from the four references combined. Each rule names its origin so you can trace it.

### Rule 1 — One CSS file, one font, two colours per book
Build `/pdf/` as a single shared template (`web-book.css`-style) so when *Systems Champion* goes online next, it's a 3-line colour override, not a redesign. Body in **one serif** (a free Google Font equivalent of FF Meta Serif: try Source Serif 4 or Spectral) with four weights: 500, 500-italic, 700, 700-italic. Use CSS custom properties for `--color-text`, `--color-background`, `--color-link`, declared as RGB triplets so dark mode is a one-line swap.
*Source: Shape Up + Getting Real shared template.*

```css
:root {
  --color-text: 29, 45, 53;       /* #1d2d35 — SYSTEMology text */
  --color-background: 255, 255, 255;
  --color-link: 0, 152, 206;      /* #0098ce — SYSTEMology brand */
  --color-rule: 29, 45, 53;
}
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: 240, 240, 240;
    --color-background: 16, 18, 20;
    --color-link: 88, 196, 232;   /* lifted blue for dark */
  }
}
```

### Rule 2 — Body 18 px / line-height 1.7 / measure 65ch
Stripe Press lands at 17 px / 1.5; Shape Up runs fluid `calc(0.9em + 0.9vw)` ≈ 23 px on desktop with `1.5`; Paul Graham crashes through at Verdana 13. **The reading-comfort sweet spot for our audience (40-something business owners on laptops at midday) is 18 px / 1.7 / 65ch.** Use a fluid clamp so it scales: `font-size: clamp(17px, 1rem + 0.25vw, 20px); line-height: 1.7; max-width: 65ch;`. Body wraps into a measure, not a column.
*Source: Stripe Press 17 px / 1.5 + readability research.*

```css
.chapter__body {
  max-width: 65ch;        /* ~720 px at 18 px */
  margin-inline: auto;
  font-size: clamp(17px, calc(1rem + 0.25vw), 20px);
  line-height: 1.7;
}
.chapter__body p { margin: 0 0 1.2em 0; }
```

### Rule 3 — Sticky in-chapter sidebar that doubles as TOC + progress + Next link
Steal Shape Up's `intro__content--sticky` pattern wholesale. Left column at ≥ 50em: chapter masthead ("Step 4:"), chapter title, anchor list of every H2 in this chapter (this is the progress indicator — highlight the current one with `IntersectionObserver`), then a "Next: Assign →" link. Below 50em, this becomes a hamburger drawer. **Must steal.**
*Source: Shape Up.*

```css
@media (min-width: 50em) {
  .wb {
    display: grid;
    grid-template-columns: 0.85fr 2.5fr;
    grid-template-areas: "sidebar content";
  }
  .intro { grid-area: sidebar; }
  .intro__content--sticky {
    position: sticky;
    top: 2em;
  }
  .content { padding: 2.65em 6em 0 3.5em; grid-area: content; }
}
```

### Rule 4 — Stable URL slugs and anchor IDs that outlive redesigns
URLs: `/pdf/`, `/pdf/foreword/`, `/pdf/define/`, `/pdf/assign/`, `/pdf/extract/`, `/pdf/organise/`, `/pdf/integrate/`, `/pdf/scale/`, `/pdf/optimise/` — slug = idea name, mirrors the seven SYSTEMology steps, also matches what an LLM would already call them. **Every H2 gets a manually-stable `id` slug**, never auto-generated, with a hover-reveal anchor link `<a class="anchor-link" href="#define">¶</a>` so readers can copy deep links. Once published, do not change a slug ever — redirect at the worst.
*Source: Paul Graham (URL stability) + Shape Up (anchor-link UX).*

### Rule 5 — Italic + bold inline are the pull-quote system
Don't build a "callout box" component. Use **bold for canonical nouns** ("the **Critical Client Flow**") and *italic for emphasis* ("the question is not how *long* — it's how *deliberate*"). Reserve `<blockquote>` (`border-left: 0.2rem solid; padding-left: 1em; font-style: italic`) for *quoting another author or member*, never for tweetable callouts. **Italic at 1.2em** with a 60 px hairline rule before it for chapter abstracts and section breaks — that's the Stripe Press editorial voice in one component.
*Source: Shape Up (inline emphasis) + Stripe Press (italic 1.2em + 60 px rule).*

```css
.chapter__abstract {
  font-size: 1.2em;
  font-style: italic;
  line-height: 1.5;
}
.chapter__abstract::before {
  content: "";
  display: block;
  width: 60px;
  height: 1px;
  margin: 0 0 1em 0;
  background: rgb(var(--color-rule));
}
blockquote {
  font-style: italic;
  margin: 1.5em 0;
  padding-left: 1em;
  border-left: 0.2rem solid rgb(var(--color-rule));
}
```

### Rule 6 — Minimal article DOM. No wrapper soup.
The chapter body should be `<article>` containing `<h1>`, `<h2 id="...">`, `<p>`, `<figure><img><figcaption>`, `<blockquote>`, `<ul>`, `<ol>`, `<sup><a>` for footnote refs. **No `<div class="content-wrapper">`-style nesting inside the article.** This is what makes Shape Up and PG both AI-citation-friendly: the LLM crawler sees prose, not chrome.
*Source: Paul Graham (zero DOM noise) + Shape Up (only `<p>` and `<h2>` in chapter body).*

### Rule 7 — Schema, OG, sitemap on every chapter — but no `llms.txt` worship
Every chapter page must ship: `og:title`, `og:description`, `og:image`, `twitter:card: summary_large_image`, canonical, JSON-LD `Chapter` schema (`@type: Chapter` nested in `@type: Book`), and be in `sitemap.xml`. None of our four references shipped a useful `llms.txt`, and PG ranks anyway — so don't burn time on `llms.txt` at the expense of schema and sitemap. Title-tag pattern: `[Chapter title] — SYSTEMology by David Jenyns`. Description: first 160 chars of chapter abstract.
*Source: Shape Up + Stripe Press (all OG); Paul Graham (proves stable URLs > metadata theatre).*

### Rule 8 — End-of-chapter is "Next →" only. The buy/upgrade CTA lives on the hub.
Shape Up does this and it's right. The bottom of every chapter is a single "Next: [next chapter title] →" link and a hairline copyright footer. **Do not** stuff a "Get the systemHUB free trial" banner at the bottom of every chapter — readers will install banner blindness within two chapters. The conversion CTA goes on `/pdf/` (hub page) and on a dedicated end-of-book "What now?" page after the final chapter, with a single clear funnel. Inside the reading flow, protect the read.
*Source: Shape Up (Next-only chapter footer) + Stripe Press (multi-retailer Buy on book page only) + 37signals 2006 (soft funnel).*

---

## Quick reference — the numbers

| | Body font | Body size | Line height | Measure | Heading scale | Background |
|---|---|---|---|---|---|---|
| Shape Up | FF Meta Serif | fluid 23–25 px | 1.5 | grid `2.5fr` ≈ 720 px | 75/85/100/120/160/200/300 % | #fff (dark mode flip) |
| Stripe Press | Ivar Text 500 | 17 px | 1.5 | up to 1280 px container | per-component | #201819 (per-book accent) |
| Getting Real | FF Meta Serif | fluid 23–25 px | 1.5 | same as Shape Up | same as Shape Up | #fff (text #1d2d35) |
| Paul Graham | Verdana 13 | 13 px | default | 435 px (fixed) | `<b>` only | #fff (text #000, link #000099) |
| **/pdf/ target** | **Source Serif 4** | **clamp 17–20 px** | **1.7** | **65ch** | **modular 7-step** | **#fff (text #1d2d35, link #0098ce)** |

---

## Implementation kickstart — minimum CSS

```css
:root {
  /* Colour system (RGB triplets for dark-mode flip) */
  --color-text: 29, 45, 53;
  --color-background: 255, 255, 255;
  --color-link: 0, 152, 206;
  --color-rule: 29, 45, 53;

  /* Modular type scale */
  --type-base: clamp(17px, calc(1rem + 0.25vw), 20px);
  --type-xs:  75%;
  --type-s:   85%;
  --type-m:  100%;
  --type-l:  120%;
  --type-xl: 160%;
  --type-xxl: 200%;
  --type-xxxl: 300%;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-text: 240, 240, 240;
    --color-background: 16, 18, 20;
    --color-link: 88, 196, 232;
  }
}

body {
  margin: 0;
  font-family: "Source Serif 4", Georgia, serif;
  font-size: var(--type-base);
  line-height: 1.7;
  color: rgb(var(--color-text));
  background: rgb(var(--color-background));
}

.chapter__body { max-width: 65ch; margin-inline: auto; padding: 0 1.5em; }
.chapter__body p  { margin: 0 0 1.2em 0; }
.chapter__body h2 { margin: 2.5em 0 0.5em; font-size: var(--type-xl); line-height: 1.2; }
.chapter__body h2:hover .anchor-link { opacity: 1; }
.anchor-link { opacity: 0; margin-left: 0.25em; text-decoration: none; transition: opacity .2s; }

blockquote {
  margin: 1.5em 0; padding-left: 1em;
  border-left: 0.2rem solid rgb(var(--color-rule));
  font-style: italic;
}

.chapter__abstract { font-size: 1.2em; font-style: italic; line-height: 1.5; margin-bottom: 2em; }
.chapter__abstract::before {
  content: ""; display: block; width: 60px; height: 1px;
  margin-bottom: 1em; background: rgb(var(--color-rule));
}

@media (min-width: 50em) {
  .wb { display: grid; grid-template-columns: 0.85fr 2.5fr; gap: 3.5em; padding: 2em; }
  .intro__content--sticky { position: sticky; top: 2em; }
}
```

That's the entire foundation. Everything else is content.
