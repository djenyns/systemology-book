# 09 — SYSTEMology Publishing Archive Inventory

**Source:** `~/Downloads/!SYSTEMology Book/` (38GB, 45 top-level folders)

What follows is a triaged inventory of what's in the archive, ranked by how much value each piece adds to `systemology.com/pdf/`. The categories are: **steal now** (Phase 2 of the build), **steal later** (post-launch enhancement), **archive only** (nice to have but not needed for this site), **skip** (irrelevant or already covered).

---

## 🥇 STEAL NOW — high-impact for the launch

### 1. Photos – Holding Book (63 files, 5.3 GB)

**This is the single highest-value asset in the archive.** Sixty-three real industry leaders, business owners, and "book in the wild" shots holding the SYSTEMology book.

Notable people:
- **Allan Dib** (1-Page Marketing Plan author) + a separate "Allan Dibb and Dave" shot
- **Andrew Griffiths**, **Dale Beaumont**, **Dr Sabrina** (The Business Psychologist)
- **Esther Anderson**, **Jurgen Strauss**, **Mike O'Hagan**, **Pete Williams**
- **Simon Bowen** (The Genius Model), **Tim Hyde**, **Walt Hampton**, **Troy Dean**
- **Meryl** (Bean Ninjas), **Adam Franklin**, **Adam Houlihan**, **Ben Cashman**, **Brad Korn**
- **Geoff Grist**, **Glen KPI**, **Jaryd Krause**, **Kathryn**, **Kristian**, **Lihn**, **Linh**, **Lisa Henesse**
- **Matt Jones**, **Maxim Filimonov**, **Nick**, **Nomiki**, **Pete Williams**, **Peter Butler**
- **Rick Hadrava**, **Scott Gellatley**, **Sharon Neo**, **Stella Gianotto**, **Steve Ovens**, **Valerie Koo**

Plus "book in the wild" shots — book on a tradie's truck, with a dog, in a box, on a desk, lined up with other books. Plus a "Team reading" group photo. Plus one short video (`VID_20201005_153205.mp4`).

**Where to use:**
- **Hub page** — a "Real people are reading SYSTEMology" gallery section below the chapter list (rotating mosaic of 6-12 photos)
- **End of book** — "Join the readers" testimonial wall before the final CTA
- **Social-proof callouts** in the appropriate chapters (e.g. Allan Dib reading the book → next to his testimonial in the Praise section)
- **Open Graph images** — generate per-chapter OG cards using these photos as the social-share preview

**Action:** copy curated 30-40 photos into `public/photos/readers/`, build a hub gallery section.

---

### 2. !Resources Page (760 KB) — the actual templates from the book

Six PDF templates that are literally referenced by name in the book chapters. These are the "go to systemology.com/resources and download the CCF" downloads:

- `Critical Client Flow (CCF) - melbourneSEOservices.com - V1.pdf`
- `Critical Client Flow (CCF) - melbourneSEOservices.com - V2.pdf`
- `DRRC & SAS - melbourneSEOservices.com.pdf` — Departments/Responsibilities Chart + Systems Assign Sheet
- `Pre-extraction Form.pdf`
- `SYSTEMology Process.pdf`
- `Software Buying Guide.pdf`
- `Systems Assign Sheet (SAS).pdf`

**Where to use:**
- Each template embeds inline at the relevant chapter point — e.g. CCF template inline in `/pdf/define/` where the book says "go to /resources and download the CCF"
- Resources page link in CTAs throughout
- Could be extracted to PNG previews for visual reference + PDF download buttons

**Action:** copy to `public/templates/`, add download buttons + PNG previews inline in chapters where referenced.

---

### 3. Video — Michael Gerber Foreword + Endorsement Videos

Inside `Video/`:

- **`michael-gerber-foreword.mp4`** ← Gerber on camera talking about the foreword. Embed this on `/pdf/foreword/` — instant credibility lift.
- **`allan-dib-review.MOV`** — Allan Dib endorsement video. Embed in Praise section + Define chapter.
- **`Linh podetti - testimonial.mp4`** — reader testimonial video.
- **`The Book Promotion3.mp4`**, **`book promo v2.mp4`** — book promo videos for the hub.
- **`SYSTEMology Ad (Square Final).mp4`** — square-format ad, useful for OG/social embed.
- **`FULL_Render 1920x1080_V2.mp4`** — high-res book render.
- **`Dave Speaker Reel.mp4`** — Dave's speaker reel for the About page.

Plus subfolder `Video/Podcast clips/` with named topical clips:
- `01S/V - Content that stands the test of time.mp4` (Short + Vertical)
- `02S/V - What is a Systemologist.mp4`
- `03S/V - Why having systems in business is important.mp4`
- `BOB_075 FB Snippet`
- `BPS_Allan Dib Snippet`
- `David Jenyns - Audiogram.mp4`
- `David Jenyns - Do I need complex systems and tools FINAL.mp4`

These are shareable social clips — perfect for inline embedding at relevant chapter points.

**Where to use:**
- Gerber foreword video → top of `/pdf/foreword/`
- Allan Dib video → Praise section
- Linh testimonial → near her photo, possibly Define or Scale chapter
- Promo video → hub page, below "Start reading" CTA, optional auto-play on hover
- "What is a Systemologist" clip → relevant in `/pdf/assign/`
- "Why having systems in business is important" → top of `/pdf/introduction/`
- Speaker Reel → `/pdf/about/`

**Action:** upload select videos to Wistia (already have audit infrastructure), embed via Wistia hashed_id. Don't host the raw MOV/MP4 files in the repo.

---

### 4. !Book Draft / foreword.docx + foreword.pdf

The original Gerber foreword in source format. Useful for verifying the migrated text matches the original (typography, italics, structure) and potentially for finding any Gerber content cut from the printed book.

**Action:** spot-check against the migrated `/pdf/foreword/` text. If differences, decide whether to restore.

---

### 5. !Book Draft / SYSTEMology Executive Summary.pdf

A pre-existing executive summary of the book. Could become an **"If you're short on time, read this"** entry on the hub — an alternative entry point for readers who want a 10-minute version before committing to the full book.

**Where to use:** new optional URL `/pdf/summary/` — high-value for AI citation (LLMs like dense, definitional content) and for time-poor readers.

**Action:** convert to MDX, link from hub as a side option.

---

### 6. 3D Renders + Cover folder (3.1 GB combined)

- `3D renders/MAIN MOCKUP/` — high-quality 3D book renders
- `3D renders/dusk jacket/` — dust jacket variants (01.png through 07.png)
- `3D renders/Book funnel graphic/Sys_Book_1080x560_v1F.pdf` — wide-format promo (the one we tried earlier)
- `cover/systemology-audio-01.jpg` — audiobook cover
- `cover/systemology-ebook.jpg` — ebook cover

**Where to use:**
- A nicer hero treatment than the current 840×1195 cover — e.g. a 3D render with shadow/perspective
- "Get on Audible" button gets the audiobook cover thumbnail
- "Get the paperback" button gets the paperback cover
- OG images use the highest-quality renders

**Action:** review the renders, pick 2-3 favourites, swap the hub cover image. Stage audiobook + ebook cover thumbnails next to the buy buttons.

---

### 7. Graphics / Quote Templates / !Dave (10 files)

Ten ready-made quote graphics featuring David's quotes from the book. These are professionally-designed Instagram-square quote cards (Quote1.jpg through Quote10.jpg).

**Where to use:**
- Mid-chapter pull-quote callouts could use these as graphic block-quotes alongside text quotes
- The "share quote" feature (Phase 3) can use these as the share-image template
- Social/OG card templates

**Action:** review the 10 quotes, match each to the chapter where the source quote appears, use as visual pull-quote alternative.

---

### 8. Graphics / Quotes (multiple .jpg + .psd source)

Pre-made quote cards with PSD source files — meaning we can edit/add new ones using your existing template. PSD source = brand-aligned quote-card generator template.

**Action:** save the PSD as the canonical quote-card template for future use.

---

### 9. Graphics / Headshots - endorsements

Headshot images of every endorser (in a zipped folder). Pair these with the praise quotes in the Foreword/Praise section.

**Action:** extract the zip, build a "Praise" component that pairs each endorsement with its endorser's headshot.

---

## 🥈 STEAL LATER — Phase 2 / post-launch enhancement

### 10. Updates folder — book launch update videos (437 MB)

Three "book launch update" videos showing David's progress in the lead-up to launch:
- `2020.06.12 book-update.mp4`
- `2020.06.26 book-launch-update.mp4`
- `2020.07.04 book-launch-update-3-6-2020.mp4`

**Use:** "Behind the scenes" section on `/pdf/about/` — humanises the journey, gives the book a real-history feel.

### 11. Charlie podcast (479 MB)

The launch interview podcast. Could be:
- Embedded as audio on `/pdf/about/`
- Transcribed for additional pull-quotes / extra content
- Mined for chapter-specific anecdotes that didn't make the book

### 12. Photos - In the Studio (33 files, 244 MB)

Behind-the-scenes photos of David recording the audiobook in the studio. Good for `/pdf/about/` or a "How this book was made" page.

### 13. Swipe File (496 MB)

Marketing swipe — competitor book launch material, email templates. Not for the reader, but useful for our launch strategy phase. Skip for now.

### 14. !Funnel Hacking (277 MB)

The book launch funnel — landing pages, email sequences. Useful for understanding what worked, but not for the reader site. Skip for now.

### 15. blueprint article.docx (in !Book Draft)

David's standalone article that became part of the book. Could be a lead-in piece on the blog or a `/pdf/preview/` reading sample. Lower priority.

---

## 📦 ARCHIVE ONLY — keep, don't use directly

- **Audio book** (3.1 GB) and **Audible** (319 MB) — already have the chapter MP3s
- **Acadium** (2.3 GB) — internships, not relevant to the reader
- **Steve Harris** (194 MB) — designer files (PSD source), keep for reference
- **Amazon Ads** (64 MB) — advertising assets, irrelevant for the site
- **iannotate** (6.5 MB) — annotation files
- **BookBoon** (312 KB) — a partner platform export

---

## 🗑️ SKIP

- **Hacking PR for Fun and Profit.pdf** (root) — third-party PR ebook
- **Page Two PDFs** (root) — publisher service catalogue
- **partners-mailing.doc** — partner outreach, irrelevant
- **Templates** (1.7 MB) — old marketing templates, mostly outdated

---

## Recommended additions to the build (concrete actions)

### Phase 2 — Content polish (after the chapter cleanup pass)

1. **"Real readers" gallery on the hub** — copy 30-40 best photos from `Photos - Holding book` into `public/photos/readers/`, build a CSS-grid mosaic component below the chapter TOC. Each photo links to its endorsement (where one exists in our existing endorsement data).

2. **Embed Gerber foreword video** at top of `/pdf/foreword/` — upload `michael-gerber-foreword.mp4` to Wistia, embed via hashed_id.

3. **Embed Allan Dib endorsement video** in the Praise / Foreword section.

4. **Inline templates in chapters** — extract PDFs from `!Resources Page/` to `public/templates/`, add "Download CCF Template (PDF)" buttons inline at the right chapter points.

5. **Swap hub cover image** to a higher-quality 3D render from the `3D renders/MAIN MOCKUP/` folder.

6. **Add Audible + paperback cover thumbnails** next to the buy buttons in hub footer.

7. **Build a "Praise" component** with endorser headshots + quotes (using the headshots zip).

### Phase 3 — Optional enhancements

8. **Add Executive Summary at `/pdf/summary/`** — convert the existing PDF, mark it as a 10-minute read alternative entry point.

9. **Behind-the-scenes section on `/pdf/about/`** — embed the studio photos + book-launch-update videos.

10. **Quote-card generator** uses the existing PSD as the template.

11. **Podcast embed** (Charlie) on `/pdf/about/` if desired.

---

## What I'm NOT doing right now

This is a **research inventory** — I haven't copied any files into the project yet. The `!SYSTEMology Book/` folder lives in your Downloads (38GB), and I'd rather not duplicate gigabytes into the repo. Most of these assets will live in three places:

- **Wistia** — videos go here (existing infrastructure, transcripts auto-generate, AI-crawlable)
- **public/photos/** + **public/templates/** in the repo — only curated, web-optimised versions (downsampled to ≤300KB each)
- **Source originals** — stay in your Downloads or get pushed to Drive for archival

Tell me which items from "Steal Now" you want me to action first and I'll start copying/optimising/embedding. My recommendation: do items **1, 2, 3, 6** first (readers gallery + Gerber video + Allan Dib video + hub cover swap) — biggest visual impact for the smallest effort.
