#!/usr/bin/env python3
"""
Migrate the SYSTEMology book PDF→MDX with structural section detection.

Source: source-assets/book-from-pdf.md (markitdown conversion of SYSTEMology-final-v1.pdf)
Output: src/content/chapters/<slug>.mdx

Improvements over v1:
  - Aggressive paragraph rejoin (fragments that don't end in sentence punctuation
    get joined with the next line, fixing the "to systemise\\n\\nyour business" break)
  - Auto-detect and wrap "Chapter Summary" intro blocks in <ChapterSummary>
  - Auto-detect and wrap "Highlights from this chapter include" + bullet list
  - Auto-detect and wrap "Case Study" sections in <CaseStudy name="…">
  - Auto-detect "[Name] action steps" → bottom-of-chapter action component
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source-assets" / "book-from-pdf.md"
OUT_DIR = ROOT / "src" / "content" / "chapters"

CHAPTERS = [
    {"slug": "foreword", "title": "Foreword",
     "description": "Foreword to SYSTEMology by Michael E. Gerber, author of The E-Myth Books. Gerber, who coined 'work ON your business, not IN it,' explains why this book is essential reading for any small business owner who wants to escape the trap of being indispensable.",
     "start": 260, "end": 320},
    {"slug": "introduction", "title": "Introduction",
     "description": "The opportunity-of-a-lifetime test: could your business survive a three-month absence? David Jenyns introduces the four stages of business systemisation (Survival, Stationary, Scalable, Saleable) and the seven-step SYSTEMology framework.",
     "start": 321, "end": 1023},
    {"slug": "define", "title": "Define",
     "description": "Stage 1 of SYSTEMology. Identify the 10-15 systems that move a customer from lead to repeat buyer using the Critical Client Flow (CCF). Stop trying to document everything; document only what matters.",
     "start": 1024, "end": 1835,
     "myth": "You will need to create hundreds of systems to systemise a business."},
    {"slug": "assign", "title": "Assign",
     "description": "Stage 2 of SYSTEMology. The business owner is not the right person to systemise the business. Appoint a Systems Champion and identify the Knowledgeable Workers whose process expertise you'll extract.",
     "start": 1836, "end": 2386,
     "myth": "The business owner is the only one who can create the systems."},
    {"slug": "extract", "title": "Extract",
     "description": "Stage 3 of SYSTEMology. Capture how work actually gets done by screen-recording your Knowledgeable Workers. The System For Creating Systems turns that recording into a living SOP without forcing the owner to write it.",
     "start": 2387, "end": 3251,
     "myth": "Creating systems is time-consuming."},
    {"slug": "organise", "title": "Organise",
     "description": "Stage 4 of SYSTEMology. Pick a single source of truth for your systems and project management — and stop spreading documentation across Google Drive, Slack, and people's heads.",
     "start": 3252, "end": 4105,
     "myth": "You need to invest in expensive and complex software."},
    {"slug": "integrate", "title": "Integrate",
     "description": "Stage 5 of SYSTEMology. Get the team to actually use the systems. Build a culture where 'is there a system for that?' becomes the default question.",
     "start": 4106, "end": 4977,
     "myth": "Even if you have systems in place, your team won't follow them."},
    {"slug": "scale", "title": "Scale",
     "description": "Stage 6 of SYSTEMology. Once the Critical Client Flow is documented, expand to your Minimum Viable Systems — the ~42 systems across six departments that move you from owner-dependent to scalable.",
     "start": 4978, "end": 5735,
     "myth": "Systemisation destroys creativity."},
    {"slug": "optimise", "title": "Optimise",
     "description": "Stage 7 of SYSTEMology. Once systems run, you measure them. Once you measure them, you improve them. Build the CCF Dashboard, identify constraints, and create a kaizen culture of continuous 1% improvements.",
     "start": 5736, "end": 6421,
     "myth": "You need to systemise like McDonald's."},
    {"slug": "now-is-the-time", "title": "Now is the time",
     "description": "The closer. What to do tomorrow morning. The question isn't whether to systemise — it's whether you start this week or pretend for another year.",
     "start": 6422, "end": 6771},
    {"slug": "epilogue", "title": "Epilogue",
     "description": "Tragedy or opportunity. The whole framework reduces to one principle: the business owner is the bottleneck. Remove them, and what's left is something durable.",
     "start": 6772, "end": 6972},
    # Skipped: Appendix (lines 6973-7358) — contains sample SOPs from David's
    # agency. Useful as references but not part of the reading flow.
    {"slug": "glossary", "title": "Glossary",
     "description": "Defined terms used throughout SYSTEMology — Critical Client Flow, Systems Champion, Knowledgeable Worker, Minimum Viable Systems, System For Creating Systems, and more.",
     "start": 7359, "end": 7391},
    {"slug": "about", "title": "About the Author",
     "description": "About David Jenyns — founder of SYSTEMology, three-time bestselling business author, TEDx speaker, and the SEO-agency-owner who systemised himself out of his own business.",
     "start": 7392, "end": None},
]

# ── Cleanup regexes ────────────────────────────────────────────────────────

PAGE_HEADER_RE = re.compile(r"^\s*S\s*Y\s*S\s*T\s*E\s*M\s*o\s*l\s*o\s*g\s*y\s*$", re.MULTILINE)

# Catch ANY line that's mostly single-letter "words" separated by spaces.
# Examples: "S T A G E   O N E", "S T A G E O N E :   D E F I N E", "N O W   I S   T H E   T I M E"
# Heuristic: a line where >60% of non-space chars are followed by a space.
SPACED_CAPS_RE = re.compile(
    r"^\s*(?:[A-Z](?:\s+|$))+(?:[:.]\s*(?:[A-Z](?:\s+|$))+)?\s*$",
    re.MULTILINE,
)

# Also catch "STAGE TWO :   ASSIGN" with normal spacing variant
STAGE_HEADER_RE = re.compile(
    r"^\s*S\s*T\s*A\s*G\s*E\s+(?:O\s*N\s*E|T\s*W\s*O|T\s*H\s*R\s*E\s*E|F\s*O\s*U\s*R|F\s*I\s*V\s*E|S\s*I\s*X|S\s*E\s*V\s*E\s*N)\s*[:]?\s*[A-Z\s]*$",
    re.MULTILINE,
)
OTHER_HEADER_RE = re.compile(
    r"^\s*(?:N\s*O\s*W\s+I\s*S\s+T\s*H\s*E\s+T\s*I\s*M\s*E"
    r"|E\s*P\s*I\s*L\s*O\s*G\s*U\s*E"
    r"|A\s*P\s*P\s*E\s*N\s*D\s*I\s*X(?:\s+\d+(?:\.\d+)?)?"
    r"|G\s*L\s*O\s*S\s*S\s*A\s*R\s*Y"
    r"|A\s*B\s*O\s*U\s*T\s+T\s*H\s*E\s+A\s*U\s*T\s*H\s*O\s*R)\s*$",
    re.MULTILINE,
)
PAGE_NUM_RE = re.compile(r"^\s*\d{1,3}\s*$", re.MULTILINE)
MYTH_RE = re.compile(r"^\s*M\s*Y\s*T\s*H\s*$", re.MULTILINE)
HYPHEN_BREAK_RE = re.compile(r"(\w)-\n\s*(\w)")
FORM_FEED_RE = re.compile(r"\f")
BULLET_RE = re.compile(r"^[ \t]*(?:•|■|▶|;|y(?=[ \t]))[ \t]+", re.MULTILINE)
MULTI_BLANK_RE = re.compile(r"\n{3,}")

# Sentence-ending: . ! ? : ; … (ellipsis) or quote/bracket close after one of those
SENTENCE_END_RE = re.compile(r'(?:[.!?:;…”"\)\]]|\.\.\.)\s*$')

# Section markers that should never be absorbed into preceding prose during reflow
SECTION_MARKER_RE = re.compile(
    r"^(Case Study"
    r'|[“"]?[A-Za-z]+[”"]?\s+Chapter\s+Summary'
    r'|[“"]?[A-Za-z]+[”"]?\s+action\s+steps'
    r"|Highlights\s+from\s+this\s+chapter)\b",
    re.IGNORECASE,
)


def extract_lines(source_lines: list[str], start: int, end: int | None) -> str:
    chunk = source_lines[start - 1 : end] if end else source_lines[start - 1 :]
    return "\n".join(chunk)


def initial_clean(raw: str, chapter_title: str, myth: str = "") -> str:
    """First-pass cleanup before paragraph reflow."""
    text = raw

    text = FORM_FEED_RE.sub("", text)
    text = PAGE_HEADER_RE.sub("", text)
    text = STAGE_HEADER_RE.sub("", text)
    text = OTHER_HEADER_RE.sub("", text)
    text = SPACED_CAPS_RE.sub("", text)  # catches anything else that's spaced-caps chrome
    text = MYTH_RE.sub("", text)
    text = PAGE_NUM_RE.sub("", text)

    # Strip the chapter's myth statement from the body (it's rendered separately
    # via the chapter layout's "Myth busted" callout). The book.ts myth field
    # uses straight apostrophes; the PDF source uses curly. Make the apostrophe
    # variants interchangeable in the match.
    if myth:
        myth_words = myth.split()
        myth_pattern = r"\s+".join(re.escape(w) for w in myth_words)
        # Allow either straight or curly apostrophe (the book.ts myth uses
        # straight, the PDF source uses curly).
        myth_pattern = myth_pattern.replace("'", "['’]")
        text = re.sub(
            rf"(?:^|(?<=\n\n))\s*{myth_pattern}\s*(?=\n\n|\Z)",
            "",
            text,
        )

    # Collapse double-spaces (PDF extraction artefact) early so downstream regex
    # using literal single spaces matches reliably (e.g. "IMPORTANT NOTE:")
    text = re.sub(r"  +", " ", text)

    # Drop-cap fix: "Y ou've" → "You've" (large first letter spaced from rest of word).
    # Only applies to capitals that aren't valid single-letter words (skip A and I).
    text = re.sub(
        r"(?:^|(?<=\n))([B-HJ-Z]) ([a-z])",
        r"\1\2",
        text,
        flags=re.MULTILINE,
    )

    # Strip the chapter title appearing alone
    title_re = re.compile(r"^\s*" + re.escape(chapter_title) + r"\s*$", re.MULTILINE | re.IGNORECASE)
    text = title_re.sub("", text)
    if chapter_title == "Epilogue":
        text = re.sub(r"^\s*Epilogue\s*[–—-]\s*Tragedy\s*$", "", text, flags=re.MULTILINE)
        text = re.sub(r"^\s*or\s+opportunity\s*$", "", text, flags=re.MULTILINE)

    # Rejoin hyphenated line breaks
    text = HYPHEN_BREAK_RE.sub(r"\1\2", text)

    # Rejoin SYSTEMology URLs that got split across lines/spaces by the PDF.
    # The book mentions www.SYSTEMology.com/resources and /podcast in many places;
    # PDF wrapping leaves variants like "www.SYSTEMology.\ncom/resources" or
    # "www.SYSTEMology.com/\n resources" or "www.SYSTEMology. com/resources".
    text = re.sub(
        r"www\.SYSTEMology\.\s*com\s*/\s*(resources|podcast)",
        lambda m: f"www.SYSTEMology.com/{m.group(1)}",
        text,
        flags=re.IGNORECASE,
    )

    # Convert weird bullet markers to standard markdown dashes
    text = BULLET_RE.sub("- ", text)

    # Targeted Integrate fix: the print book has a paragraph break between
    # bullet 3 ("These can be the trickiest to tackle.") and the trailing
    # prose ("Let's not wait..."). PDF extraction lost the break — restore it.
    text = re.sub(
        r"(These can be the trickiest to tackle\.)\n(Let’s not wait)",
        r"\1\n\n\2",
        text,
    )

    # Pre-promote standalone subhead-style lines to ### BEFORE smart_reflow runs.
    # These are short title-case lines on their own that smart_reflow would
    # otherwise absorb into the next paragraph as prose.
    # Patterns:
    #   "How X works", "How to X", "What is X", "A word of/on X",
    #   "Don't X", "Keep X", "Be X"
    subhead_patterns = [
        r"How\s+[A-Z][\w\s]{2,30}",
        r"How\s+(?:to|do|does|can|will)\s+[\w\s]{2,30}\??",
        r"What\s+(?:is|are|if|about)\s+[\w\s]{2,30}\??",
        r"Why\s+[\w\s]{2,30}\??",
        r"Where\s+[\w\s]{2,30}\??",
        r"When\s+[\w\s]{2,30}\??",
        r"Which\s+[\w\s]{2,30}\??",
        r"A word\s+(?:of|on)\s+[\w\s]{2,20}",
        r"Don't\s+[\w\s]{2,30}",
        r"Don’t\s+[\w\s]{2,30}",  # curly apostrophe variant
        r"Keep\s+[\w\s]{2,30}",
        r"Be prepared\s+[\w\s]{2,20}",
        r"Get\s+[\w\s]{2,20}!?",
        r"Model\s+[\w\s]{2,20}",
        r"Limit\s+[\w\s]{2,30}",
        r"You might not be\s+[\w\s]{2,40}",
    ]
    # IMPORTANT: require a blank line AFTER the subhead pattern.
    # This prevents promoting inline rhetorical questions like "Why is that important?"
    # that flow into the next sentence without a paragraph break.
    for pat in subhead_patterns:
        text = re.sub(
            r"(?:^|(?<=\n\n))(" + pat + r")(?=\n\n)",
            r"### \1",
            text,
            flags=re.MULTILINE,
        )

    # Glue prose lead-in into a colon-ending header that introduces a list.
    # e.g. "...here are a few\n\ncriteria to look out for:" → one paragraph
    text = re.sub(
        r"^([A-Z][^\n.!?:]+[a-z,])\n\s*\n([a-z][^\n]*:)$",
        r"\1 \2",
        text,
        flags=re.MULTILINE,
    )

    # Pre-promote "Step #N: ..." headers BEFORE the bullet-glue rule, otherwise
    # the previous bullet (if it ends without punct) absorbs the Step header
    # as a continuation. Pre-promoting them as ### makes the bullet glue
    # exclude them (it skips lines starting with `#`).
    text = re.sub(
        r"(?:^|(?<=\n\n))(Step\s*#\d+:\s*[^\n]+)$",
        r"### \1",
        text,
        flags=re.MULTILINE,
    )

    # Pre-promote known short title-case subheads (e.g. "Business benefits",
    # "Team member benefits") BEFORE the bullet glue. Otherwise these standalone
    # subhead paragraphs get absorbed by the previous bullet's last item.
    _early_subheads = [
        "Business benefits",
        "Team member benefits",
        "Don't over-document your business",
        "Don’t over-document your business",
        "You might not be the best person for this job",
        "Model the best",
        "Limit your scope to sharpen your focus",
        "Set yourself up for success",
        "Flow charts come last",
        "The money is in the systems",
        "Your systems champion",
        "Not everyone is a systems person",
        "The leader and the manager",
        "The yin to my yang",
        "Finance department",
        "Human resources department",
        "Sales department",
        "Marketing department",
        "Operations department",
        "Management department",
        "Recruitment system",
        "Team member onboarding system",
        "Problems become opportunities",
        "Listen to your business",
        "The accelerated method of optimisation",
        "The magic pair",
        "Project management software",
        "Systems management software",
        "Start with simple",
        "Final word on software",
        "Making the final decision",
        "Systems-run businesses are always worth more",
    ]
    for sh in _early_subheads:
        words = sh.split()
        pattern = r"\s+".join(re.escape(w) for w in words)
        text = re.sub(
            rf"(?:^|(?<=\n\n))({pattern})(?=\n\n|\Z)",
            lambda m: f"### {' '.join(m.group(1).split())}",
            text,
        )

    # Glue bullet/numbered-list continuations across blank lines.
    # Rule: a list item that ends WITHOUT sentence-terminating punctuation (.?!)
    # absorbs the next non-list, non-blank line ONLY IF the next line starts
    # with a lowercase letter (i.e. a sentence-mid continuation orphaned across
    # a page break). Capital starts are almost always new paragraphs.
    # Covers both bullet (- item) and numbered (1. item) forms.
    prev = None
    while prev != text:
        prev = text
        text = re.sub(
            r"^((?:-\s+|\*\s+|\d+[.)]\s+)[^\n]+[^.!?\)\]”\"])\n\s*\n((?!-\s|\*\s|\d+[.)]\s|#)[a-z][^\n]*)$",
            r"\1 \2",
            text,
            flags=re.MULTILINE,
        )
        # Special case: URL split across page break.
        # Two variants:
        #   1. "www.X." + "com/Y" → merge
        #   2. "www." + "SYSTEMology.com/Y" → merge
        text = re.sub(
            r"^((?:-\s+|\*\s+|\d+[.)]\s+)[^\n]*www\.[\w.]+\.)\n\s*\n((?:com|org|io|net|au|co|info)/[^\n]+)$",
            r"\1\2",
            text,
            flags=re.MULTILINE,
        )
        text = re.sub(
            r"^((?:-\s+|\*\s+|\d+[.)]\s+)[^\n]*www\.)\n\s*\n([a-zA-Z][\w]*\.(?:com|org|io|net|co\.uk|com\.au|au|info)[/\w.\-]*\.?)$",
            r"\1\2",
            text,
            flags=re.MULTILINE,
        )

    # Force-split known subhead phrases that get absorbed into surrounding prose
    # (e.g. when the previous sentence ends with `…` ellipsis which doesn't read
    # as a sentence terminator). Insert blank lines around them.
    # Subhead phrases discovered across chapters that don't end with terminal
    # punctuation and were getting absorbed into surrounding prose. Force-promote
    # to ### so smart_reflow treats them as structural and doesn't re-merge.
    known_subheads = [
        # Define
        "Don't over-document your business",
        "Don’t over-document your business",
        # Assign
        "You might not be the best person for this job",
        "Model the best",
        "Limit your scope to sharpen your focus",
        # Extract
        "Set yourself up for success",
        "Flow charts come last",
        "The money is in the systems",
        "Your systems champion",
        "The first secret: creating systems is a two-person job",
        "The second secret: the System for Creating Systems",
        # Integrate
        "Business benefits",
        "Team member benefits",
        "Not everyone is a systems person",
        "The leader and the manager",
        "The yin to my yang",
        # Scale — 6 departments
        "Finance department",
        "Human resources department",
        "Sales department",
        "Marketing department",
        "Operations department",
        "Management department",
        # Scale — sub-systems and concepts
        "Capture what you're currently doing, except",
        "Capture what you’re currently doing, except",
        "Recruitment system",
        "Team member onboarding system",
        "Batch 1: the CCF",
        "Batch 2: critical department systems",
        "Problems become opportunities",
        "You can't improve what you don't measure",
        "You can’t improve what you don’t measure",  # curly apostrophe
        # Optimise
        "Listen to your business",
        "The accelerated method of optimisation",
        # Organise
        "The magic pair",
        "Project management software",
        "Systems management software",
        "Start with simple",
        "Final word on software",
        "Making the final decision",
        "Identify your strengths and understand your flaws",
        "Identify your strengths and understand your ﬂaws",  # ligature variant
        "Systems-run businesses are always worth more",
    ]

    # Checklist breakout subheads — these appear FIRST as bulleted checklist items,
    # then later in the chapter as section subheads. Each gets a ☐ checkbox prefix.
    checkbox_subheads = [
        "Basic task creation",
        "Sub-task creation",
        "Task descriptions and links",
        "Task list templates or duplication",
        "Permission levels and project visibility",
        "Intuitive and easy to use",
        "Dedicated systems management software",
        "Attaching rich media",
        "Permission levels",
        "Sign off",
    ]
    for sh in checkbox_subheads:
        words = sh.split()
        pattern = r"\s+".join(re.escape(w) for w in words)

        # Case 1: bullet-form breakout (- {phrase} + absorbed body) → split into ### + body
        # Use ✅ green check for the breakout subhead (visual continuity from the
        # checklist; the breakout shows the item being "addressed" in detail)
        text = re.sub(
            rf"(?:^|(?<=\n\n))-\s+({pattern})\s+([A-Z].+)$",
            lambda m: f"### ✅ {' '.join(m.group(1).split())}\n\n{m.group(2)}",
            text,
            flags=re.MULTILINE,
        )

        # Case 2: lone bullet in checklist (- {phrase} on its own) → keep as plain bullet
        # No checkbox prefix needed; the bullet-list rendering already provides visual cue

        # Case 3: standalone paragraph form (no bullet, just phrase alone) → ### subhead
        text = re.sub(
            rf"(?:^|(?<=\n\n))({pattern})(?=\n\n|\Z)",
            lambda m: f"### ✅ {' '.join(m.group(1).split())}",
            text,
        )
    for sh in known_subheads:
        # Whitespace-flexible match: PDF can split phrases across line breaks.
        # Build pattern that matches words separated by any whitespace.
        # Require paragraph boundaries so we don't promote mid-prose mentions.
        words = sh.split()
        pattern = r"\s+".join(re.escape(w) for w in words)
        text = re.sub(
            rf"(?:^|(?<=\n\n)|(?<=\n\n ))({pattern})(?=\n\n|\Z)",
            lambda m: f"### {' '.join(m.group(1).split())}",
            text,
        )

    return text


def smart_reflow(text: str) -> str:
    """
    Aggressive paragraph reflow: split on blank lines, then walk through
    fragments and merge any that don't end with sentence-ending punctuation
    (those are mid-sentence line breaks the PDF introduced).

    Preserves: list items, headings, blockquotes, table rows.
    """
    # Insert paragraph breaks before strong section markers that often get
    # collapsed into prose (Case Study, "X" Chapter Summary, "X" action steps).
    text = re.sub(r"\s+(Case Study)\s+", r"\n\n\1\n\n", text)
    text = re.sub(r'(\.|\!|\?)\s+([“"]?[A-Za-z]+[”"]?\s+action\s+steps)\b', r"\1\n\n\2", text)

    paragraphs = re.split(r"\n\s*\n+", text)
    paragraphs = [p.strip() for p in paragraphs if p.strip()]

    # First, reflow internal newlines within each paragraph
    cleaned_paragraphs: list[str] = []
    for p in paragraphs:
        lines = [line.strip() for line in p.split("\n") if line.strip()]
        if not lines:
            continue
        is_structural = any(
            line.startswith(("- ", "* ", "#", ">", "|"))
            or re.match(r"^\d+[.)]\s", line)
            for line in lines
        )
        if is_structural:
            # Merge continuation lines (lines that don't start a new bullet/number)
            # into their parent bullet item. EXCEPT: when a non-bullet line starts
            # with a capital letter, looks like a new sentence (long enough), AND
            # the previous bullet was a full short list item (≤80 chars, no
            # mid-sentence ending), treat the new line as a fresh paragraph that
            # got orphaned from the list — push it into a separate paragraph.
            merged_items: list[str] = []
            split_off: list[str] = []  # paragraphs to append after this block
            for line in lines:
                is_new_item = (
                    line.startswith(("- ", "* ", "#", ">", "|"))
                    or bool(re.match(r"^\d+[.)]\s", line))
                )
                if is_new_item or not merged_items:
                    merged_items.append(line)
                    continue

                # Heuristic split: previous item is a short, complete-looking
                # bullet (≤80 chars, doesn't end with conjunction/preposition) and
                # the current line starts with a capital letter — this is almost
                # always a new paragraph the PDF lost the break for.
                last_item = merged_items[-1]
                last_is_bullet = last_item.startswith(("- ", "* "))
                first_char = line.strip()[0] if line.strip() else ""
                ends_with_dependent = bool(
                    re.search(
                        r"\b(?:and|or|but|the|a|an|of|to|in|on|at|for|with|by|from|that|which|who|because)\s*$",
                        last_item,
                        re.IGNORECASE,
                    )
                )
                if (
                    last_is_bullet
                    and len(last_item) <= 100
                    and first_char.isupper()
                    and not ends_with_dependent
                    and split_off == []  # only first split per paragraph
                ):
                    split_off.append(line)
                    continue
                if split_off:
                    # Already split — keep accumulating into the trailing prose
                    split_off[-1] = split_off[-1] + " " + line
                else:
                    merged_items[-1] = merged_items[-1] + " " + line
            cleaned_paragraphs.append("\n".join(merged_items))
            if split_off:
                cleaned_paragraphs.append(" ".join(split_off))
        else:
            cleaned_paragraphs.append(" ".join(lines))

    # Second pass: merge consecutive fragments where the previous one
    # doesn't end with sentence-ending punctuation. But preserve:
    #   - Section markers (Case Study, Chapter Summary, action steps)
    #   - For "Case Study" specifically: the TITLE paragraph and BODY paragraph
    #     are preserved (because Case Study has a separate name line like "Ecosystem Solutions")
    merged: list[str] = []
    prev_was_section_marker = False
    prev_was_section_title = False
    for p in cleaned_paragraphs:
        is_structural = (
            p.startswith(("- ", "* ", "#", ">", "|"))
            or bool(re.match(r"^\d+[.)]\s", p))
            or "\n" in p
        )
        is_section_marker = bool(SECTION_MARKER_RE.match(p))
        # Only "Case Study" (alone, exactly) carries a separate title line.
        # Other section markers (Chapter Summary, action steps, Highlights) include
        # their context inline so don't need title-preservation.
        is_titled_section_marker = p.strip() == "Case Study"

        if is_structural:
            merged.append(p)
            prev_was_section_marker = is_titled_section_marker
            prev_was_section_title = False
            continue

        # A paragraph immediately after a section marker is its title — preserve it
        if prev_was_section_marker:
            merged.append(p)
            prev_was_section_marker = False
            prev_was_section_title = True
            continue

        # A paragraph immediately after a section title is the body's first line
        # — preserve it (don't absorb into title)
        if prev_was_section_title:
            merged.append(p)
            prev_was_section_title = False
            continue

        if merged:
            prev = merged[-1]
            prev_is_structural = (
                prev.startswith(("- ", "* ", "#", ">", "|"))
                or bool(re.match(r"^\d+[.)]\s", prev))
                or "\n" in prev
                or bool(SECTION_MARKER_RE.match(prev))
            )
            if not prev_is_structural and not SENTENCE_END_RE.search(prev) and not is_section_marker:
                merged[-1] = prev + " " + p
                continue

        merged.append(p)
        prev_was_section_marker = is_titled_section_marker

    return "\n\n".join(merged)


def consolidate_bullet_blocks(text: str) -> str:
    """
    Join consecutive bullet-start paragraphs (separated by blank lines) into a
    single bullet block. The PDF→MD conversion left blank lines between bullets
    that should be one list.
    """
    paragraphs = text.split("\n\n")
    merged: list[str] = []
    for p in paragraphs:
        is_bullet_para = p.lstrip().startswith("- ")
        if is_bullet_para and merged and merged[-1].lstrip().startswith("- "):
            merged[-1] = merged[-1] + "\n" + p
        else:
            merged.append(p)
    return "\n\n".join(merged)


def merge_broken_bullets(text: str) -> str:
    """
    Fix bullets that got their tail orphaned across blank lines.
    Handles two cases:
      1. Whole paragraph is a bullet list, last bullet missing its tail.
      2. Paragraph contains a bullet list (e.g. preceded by 'Highlights:'),
         last bullet missing its tail.
    """
    paragraphs = text.split("\n\n")
    merged = []
    i = 0
    while i < len(paragraphs):
        cur = paragraphs[i]
        cur_lines = cur.split("\n")
        last_line = cur_lines[-1] if cur_lines else ""

        contains_bullets = any(line.startswith("- ") for line in cur_lines)
        last_is_unfinished_bullet = (
            last_line.startswith("- ")
            and not SENTENCE_END_RE.search(last_line)
        )

        if contains_bullets and last_is_unfinished_bullet and i + 1 < len(paragraphs):
            nxt = paragraphs[i + 1]
            if (
                not nxt.startswith(("- ", "* ", "#", ">", "|"))
                and not re.match(r"^\d+[.)]\s", nxt)
                and (
                    nxt[0].islower()
                    or nxt.split()[0].lower() in {"that", "and", "or", "but", "which", "who"}
                )
            ):
                # Only absorb the PROSE PREFIX of the next paragraph (lines before
                # any subsequent bullet). The remainder stays as a new paragraph.
                nxt_lines = nxt.split("\n")
                prose_prefix: list[str] = []
                remainder: list[str] = []
                hit_bullet = False
                for line in nxt_lines:
                    if not hit_bullet and line.lstrip().startswith(("- ", "* ")):
                        hit_bullet = True
                    (remainder if hit_bullet else prose_prefix).append(line)

                if prose_prefix:
                    cur_lines[-1] = last_line + " " + " ".join(l.strip() for l in prose_prefix)
                    merged.append("\n".join(cur_lines))
                    if remainder:
                        # Replace next paragraph with the leftover (typically more bullets)
                        paragraphs[i + 1] = "\n".join(remainder)
                        i += 1
                    else:
                        i += 2
                    continue

        merged.append(cur)
        i += 1
    return "\n\n".join(merged)


# Map case study name (or distinctive substring) → video ID for embedded interview.
# Each entry: ("wistia"|"youtube", "video_id")
CASE_STUDY_VIDEOS: dict[str, tuple[str, str]] = {
    "Ecosystem Solutions": ("wistia", "lr2maqn1wh"),  # Gary McMahon
    "Absolute Immigration": ("wistia", "vlcc2p1p1p"),  # Jamie Lingham
    "Oh Crap": ("wistia", "2ldsr2y9g1"),
    "Inception Websites": ("youtube", "fEkMcFsTTt8"),
    "Den Lennie": ("youtube", "99Ip3pdBswI"),
    "diggiddydoggydaycare": ("wistia", "fquxcsbiak"),  # Jeanette Farren
    # Mount Martha Preschool — no video provided yet
}


def detect_subheads(text: str) -> str:
    """
    Detect subheads from the original PDF that lost their formatting.
    Run AFTER smart_reflow so multi-line subheads have been joined into single lines.

    Skips:
      - Section markers (Case Study, Chapter Summary, action steps, etc.)
      - The line immediately after a section marker (the section title)
      - Subject lines following an incomplete bullet (continuations)
      - Dialogue (lines ending in quote-punct)
    """
    paragraphs = text.split("\n\n")
    out = []
    prev_was_section_marker = False
    for i, p in enumerate(paragraphs):
        s = p.strip()
        # Skip if already a heading or component
        if s.startswith(("#", "<", "- ", "* ", ">", "|")):
            out.append(p)
            prev_was_section_marker = False
            continue
        if "\n" in s:
            out.append(p)
            prev_was_section_marker = False
            continue
        if not s or not s[0].isupper():
            out.append(p)
            prev_was_section_marker = False
            continue

        # Don't promote section markers — they're handled by the wrapper logic later
        is_section_marker = (
            bool(SECTION_MARKER_RE.match(s))
            or s.lower() in {"case study", "chapter summary"}
        )
        if is_section_marker:
            out.append(p)
            prev_was_section_marker = True
            continue

        # The line immediately after a section marker is its title — preserve it
        if prev_was_section_marker:
            out.append(p)
            prev_was_section_marker = False
            continue

        # Don't promote if previous paragraph is a bullet that didn't terminate
        # AND this paragraph reads like a sentence-mid continuation (starts
        # lowercase or with a discourse-connector word). Capital-letter starts
        # are almost always new paragraphs, not bullet continuations.
        prev = out[-1].strip() if out else ""
        if prev.startswith("- "):
            last_line = prev.split("\n")[-1].strip()
            first_word = s.split()[0].lower() if s.split() else ""
            looks_like_continuation = (
                s[0].islower()
                or first_word in {"that", "and", "or", "but", "which", "who"}
            )
            if (
                last_line
                and not SENTENCE_END_RE.search(last_line)
                and looks_like_continuation
            ):
                out[-1] = out[-1].rstrip() + " " + s
                continue

        length = len(s)
        # Exclude dialogue (lines ending in quote+question = someone's speech)
        is_dialogue = s.endswith(('?"', '?”', '!"', '!”', '."', '.”'))
        if is_dialogue:
            out.append(p)
            continue

        # Don't promote a question if the previous paragraph ALSO ends with `?`
        # — successive questions are usually clarifying follow-ups, not section breaks
        prev_para = out[-1].strip() if out else ""
        if s.endswith("?") and prev_para.endswith("?"):
            out.append(p)
            continue

        # Don't promote a question if the previous paragraph ends with a bolded label
        # like "**Enquiry:** ..." — the next question is usually a clarifier
        if s.endswith("?") and re.match(r"\*\*[A-Z][\w\s]*:\*\*", prev_para):
            out.append(p)
            continue
        if s.endswith("?") and re.search(r"\*\*[\w\s]+:\s+[^*]+\*\*\s*$", prev_para):
            # Previous paragraph ends with a bolded labeled-sentence (CCF stages)
            out.append(p)
            continue

        # Ends with ? — short question subhead
        if length < 70 and s.endswith("?") and "." not in s and ":" not in s:
            out.append(f"### {s}")
            continue
        # Ends with ! — short exclamation subhead (rare)
        if length < 50 and s.endswith("!") and "." not in s and ":" not in s and "?" not in s:
            out.append(f"### {s}")
            continue
        # Short statement subhead (no terminal punctuation, title-case start)
        if (
            length < 55
            and not s.endswith((".", "?", "!", ":", ";", ","))
            and "." not in s
            and ":" not in s
            and not s.startswith(("And ", "But ", "So ", "Or "))
        ):
            out.append(f"### {s}")
            continue

        out.append(p)
        prev_was_section_marker = False
    return "\n\n".join(out)


def inject_case_study_videos(text: str) -> str:
    """Add video prop to <CaseStudy name="..."> tags where we have a video.
    Supports both Wistia and YouTube IDs."""
    def repl(m: re.Match) -> str:
        name = m.group(1)
        for key, (kind, vid) in CASE_STUDY_VIDEOS.items():
            if key.lower() in name.lower():
                prop = "videoWistiaId" if kind == "wistia" else "videoYoutubeId"
                return f'<CaseStudy name="{name}" {prop}="{vid}">'
        return m.group(0)

    return re.sub(r'<CaseStudy name="([^"]+)">', repl, text)


# Per-chapter image injections.
# Each entry: (anchor_phrase, figure_markup) → inserts figure AFTER the matching paragraph.
# Or: (anchor_phrase, figure_markup, "before") → inserts figure BEFORE the matching paragraph.
CHAPTER_IMAGES: dict[str, list[tuple] ] = {
    "introduction": [
        (
            "complete business reliability",
            '<aside class="quiz-callout not-prose"><p><strong>Curious to go a little deeper?</strong> Take the quick quiz to discover your <a href="https://www.systemology.com/tools/dependency-score/" target="_blank" rel="noopener">Business Dependency Score →</a></p></aside>',
        ),
        (
            "four stages of business systemisation",
            '<BookFigure src="/pdf/brand/4-stages.png" alt="The four stages of business systemisation: Survival, Stationary, Scalable, Saleable" caption="The four stages of business systemisation" />',
        ),
        (
            "Here are the seven stages we",
            '<BookFigure src="/pdf/brand/seven-stages-wheel.png" alt="The SYSTEMology 7-stage wheel" caption="The seven stages of SYSTEMology" />',
        ),
    ],
    "define": [
        (
            "Sounds like a great idea",
            '<BookFigure src="/pdf/brand/mike-rhodes-wall.png" alt="Mike Rhodes\' wall of systems" caption="Mike Rhodes\' wall of systems — what over-documentation looks like" />',
            "before",
        ),
        (
            "Head to www.SYSTEMology.com/resources",
            '<BookFigure src="/pdf/brand/ccf-blank.png" alt="Blank Critical Client Flow template" caption="The blank CCF template — print and fill in the blanks" />',
        ),
        (
            "Here are a few sample CCFs",
            '<BookFigure src="/pdf/brand/ccf-planet.png" alt="Critical Client Flow example: Planet 13 rock-and-roll clothing store" caption="Sample CCF — Planet 13, rock-and-roll clothing store" />\n\n<BookFigure src="/pdf/brand/ccf-seo.png" alt="Critical Client Flow example: Melbourne SEO Services" caption="Sample CCF — Melbourne SEO Services (David\'s digital agency)" />\n\n<BookFigure src="/pdf/brand/ccf-medical.png" alt="Critical Client Flow example: medical practice" caption="Sample CCF — medical practice" />',
        ),
        (
            "Keep your systems simple",
            '<BookFigure src="/pdf/brand/department-cogs-shaded.png" alt="Department cogs interlocking — the SYSTEMology metaphor" caption="Departments as interlocking cogs" />',
            "before",
        ),
    ],
    "assign": [
        (
            "Departments, Responsibilities",
            '<BookFigure src="/pdf/brand/drtc.png" alt="Departments, Responsibilities and Team Chart (DRTC)" caption="The Departments, Responsibilities and Team Chart" />',
        ),
        (
            "Below is a typical set of departments",
            '<BookFigure src="/pdf/brand/drtc-3-03.png" alt="Typical set of departments" caption="A typical set of departments" />',
        ),
        (
            "an example from my digital agency",
            '<BookFigure src="/pdf/brand/drtc-3-02.png" alt="DRTC example from Melbourne SEO Services" caption="DRTC example — Melbourne SEO Services" />',
        ),
        (
            "capture things as they are",
            '<BookFigure src="/pdf/brand/drtc-3-01.png" alt="Departments and responsibilities filled in" caption="Capture as-is, not aspirational" />',
        ),
        (
            "how it’s all coming together",
            '<BookFigure src="/pdf/brand/drtc-version-2-01.png" alt="Completed DRTC with all team assignments" caption="The completed DRTC" />',
        ),
        (
            "Let me share my pre-populated example",
            '<BookFigure src="/pdf/brand/sas.png" alt="Systems Assign Sheet (SAS) example" caption="The Systems Assign Sheet (SAS)" />',
        ),
    ],
    "integrate": [
        (
            "It can be pretty scary as a business owner",
            '<BookFigure src="https://www.systemology.com/wp-content/uploads/2020/03/15084_098_WEB.jpg" alt="Melissa Crowhurst — David\'s long-time business partner" caption="Melissa Crowhurst — the yin to my yang" />',
            "before",
        ),
    ],
    "optimise": [
        (
            "CCF Dashboard",
            '<BookFigure src="/pdf/brand/ccf-dashboard.png" alt="CCF Dashboard for tracking system metrics" caption="The CCF Dashboard — track the metrics that matter" />',
        ),
    ],
    "organise": [
        (
            "no software alone will be the silver bullet",
            '<figure class="chapter-video"><div style="position:relative;padding-top:56.25%;"><iframe src="https://www.youtube-nocookie.com/embed/hHPbQ48V7ho" title="SYSTEMology software recommendations" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"></iframe></div><figcaption>Watch David walk through software recommendations</figcaption></figure>',
        ),
    ],
    "now-is-the-time": [
        (
            "takes clear, decisive action",
            '<BookFigure src="/pdf/brand/decisive-action.png" alt="The path forward — decisive action" caption="The path forward is never a straight line — riding the curve up takes decisive action" />',
        ),
    ],
}


def inject_chapter_images(text: str, slug: str) -> str:
    """Insert BookFigure illustrations at specific anchor phrases per chapter.
    Each entry can be (anchor, figure) or (anchor, figure, "before"|"after").
    Whitespace in the paragraph is normalised before matching, since PDF extraction
    can leave double-spaces between words."""
    images = CHAPTER_IMAGES.get(slug, [])
    if not images:
        return text

    paragraphs = text.split("\n\n")
    out: list[str] = []
    inserted: set[str] = set()

    def matches(anchor: str, paragraph: str) -> bool:
        # Normalise whitespace and case for substring match
        p_norm = re.sub(r"\s+", " ", paragraph.lower())
        a_norm = re.sub(r"\s+", " ", anchor.lower())
        return a_norm in p_norm

    for p in paragraphs:
        # Check for "before" inserts first
        for entry in images:
            anchor = entry[0]
            figure = entry[1]
            position = entry[2] if len(entry) > 2 else "after"
            if figure in inserted:
                continue
            if position == "before" and matches(anchor, p):
                out.append(figure)
                inserted.add(figure)

        out.append(p)

        # Then check for "after" inserts
        for entry in images:
            anchor = entry[0]
            figure = entry[1]
            position = entry[2] if len(entry) > 2 else "after"
            if figure in inserted:
                continue
            if position == "after" and matches(anchor, p):
                out.append(figure)
                inserted.add(figure)
                break
    return "\n\n".join(out)


def add_emphasis(text: str) -> str:
    """
    Make walls of text more scannable by bolding known callout prefixes.
    These are formatting cues that exist in the printed book (heavy type)
    that our PDF→MD pipeline lost.
    """
    # Bold "IMPORTANT NOTE:", "NOTE:", "TIP:", "WARNING:" at start of line/paragraph
    # Whitespace-flexible: PDF can leave double-spaces between words
    text = re.sub(
        r"(?:^|(?<=\n))(IMPORTANT\s+NOTE|IMPORTANT|NOTE|TIP|WARNING|REMEMBER|From\s+the\s+desk\s+of)(:)",
        lambda m: "**" + re.sub(r"\s+", " ", m.group(1)) + m.group(2) + "**",
        text,
    )

    # Bold "Step #N: <whole sentence>" — full-sentence bold (covers prefix too)
    text = re.sub(
        r"(?:^|(?<=\n))(Step\s*#\d+:\s*[^\n]+)$",
        r"**\1**",
        text,
        flags=re.MULTILINE,
    )

    # Bold the System For Creating Systems labels (System title, System description,
    # Team members, Relevant links) — label-only, not whole sentence
    text = re.sub(
        r"(?:^|(?<=\n))(System title:|System description:|Team members:|Relevant links:|Knowledgeable worker:)",
        r"**\1**",
        text,
    )

    # Bold "Stage #N:" anywhere (with the # version)
    text = re.sub(r"(Stage\s*#\d+:)", r"**\1**", text)

    # Bold "Stage N:" at start of paragraph (no #, e.g. "Stage 3: Scalable")
    text = re.sub(
        r"(?:^|(?<=\n))(Stage\s+\d+:)",
        r"**\1**",
        text,
        flags=re.MULTILINE,
    )

    # Bold dialogue speaker labels at start of paragraph: "David:", "Luz Delia:", etc.
    # Pattern: 1-3 capitalized words ending with colon, at start of line, followed by speech
    text = re.sub(
        r'(?:^|(?<=\n))((?:[A-Z][a-z]+\s){0,2}[A-Z][a-z]+:)(?=\s+[“"])',
        r"**\1**",
        text,
        flags=re.MULTILINE,
    )

    # Bold all-caps emphatic words like "PATIENCE!" or "MUST!" — anywhere they appear
    # (these are stylistic emphasis carried over from the printed book's bold caps)
    text = re.sub(
        r"\b([A-Z]{4,}!)",
        r"**\1**",
        text,
    )

    # Bold full CCF stage description sentences (Attention: ... / Enquiry: ... etc.)
    text = re.sub(
        r"^(Attention|Enquiry|Sales|Money|Onboarding|Delivery|Repeat or referral):\s*([^\n]+)$",
        r"**\1: \2**",
        text,
        flags=re.MULTILINE,
    )

    return text


def detect_and_wrap_sections(text: str, chapter_title: str) -> str:
    """
    Find structural patterns and wrap them in MDX components:
      - "X Chapter Summary" + body + "Highlights from this chapter include:" + list
      - "Case Study" + name + body
      - "X action steps" + bullet list
    """
    # ── Chapter Summary block ────
    # The chapter summary may have its title joined to the first prose line by reflow:
    # '"Define" Chapter Summary The first stage in...'
    # We need to split it back out.
    summary_pattern = re.compile(
        r'[“"]?([A-Za-z][A-Za-z\s]+?)[”"]?\s+Chapter\s+Summary\s*'
        r'(?:\n+|\s+)'
        r'(.+?)'  # the summary prose
        r'\n+\s*Highlights\s+from\s+this\s+chapter\s+include:\s*\n+'
        r'((?:-\s+[^\n]+\n?)+)',
        re.MULTILINE | re.DOTALL,
    )

    def replace_summary(m: re.Match) -> str:
        chapter_name = m.group(1).strip()
        prose = m.group(2).strip()
        highlights = m.group(3).strip()

        # Clean up double-spacing in highlights bullets
        highlights = re.sub(r"\s+", " ", highlights)
        # Re-split bullets
        bullet_lines = []
        for piece in re.split(r"\s*-\s+", highlights):
            piece = piece.strip()
            if piece:
                bullet_lines.append(f"- {piece}")
        highlights = "\n".join(bullet_lines)

        out = '<ChapterSummary chapter="' + chapter_name + '">\n\n'
        out += prose + "\n\n"
        if highlights:
            out += "**Highlights from this chapter:**\n\n" + highlights + "\n"
        out += "\n</ChapterSummary>"
        return out

    text = summary_pattern.sub(replace_summary, text, count=1)

    # ── Case Study block ────
    # "Case Study" then name (one full line) then body until next chapter-end pattern
    case_study_pattern = re.compile(
        r"^\s*Case Study\s*\n+"
        r"([^\n]+)\s*\n+"  # case study name = one full line
        r"(.+?)"  # body
        r"(?=\n+\s*[“\"]?[A-Za-z]+[”\"]?\s+(?:action steps|Chapter Summary)|\Z)",
        re.MULTILINE | re.DOTALL,
    )

    def replace_case_study(m: re.Match) -> str:
        name = m.group(1).strip().strip('"').strip('“”')
        body = m.group(2).strip()
        return f'<CaseStudy name="{name}">\n\n{body}\n\n</CaseStudy>'

    text = case_study_pattern.sub(replace_case_study, text)

    # ── "**IMPORTANT NOTE:**" + following 2 paragraphs → Callout ────
    important_pattern = re.compile(
        r"(\*\*IMPORTANT NOTE:\*\*[^\n]+(?:\n\n(?!\n)[^\n<#-][^\n]+){0,2})",
        re.MULTILINE,
    )

    def replace_important(m: re.Match) -> str:
        block = m.group(1).strip()
        return f"<Callout variant=\"warning\">\n\n{block}\n\n</Callout>"

    text = important_pattern.sub(replace_important, text)

    # ── "X action steps" → ActionSteps wrapper ────
    # Allow heading and bullets to be on consecutive lines (no blank line required)
    action_pattern = re.compile(
        r'^\s*[“"]?([A-Za-z][A-Za-z\s]+?)[”"]?\s+action\s+steps\s*\n+'
        r'((?:-\s+[^\n]+(?:\n(?!-\s|\n).+)*\n?)+)',
        re.MULTILINE,
    )

    def replace_actions(m: re.Match) -> str:
        steps = m.group(2).strip()
        return f'<ActionSteps>\n\n{steps}\n\n</ActionSteps>'

    text = action_pattern.sub(replace_actions, text)

    return text


def post_process(text: str) -> str:
    """Final whitespace cleanup + escape stray angle brackets that confuse MDX."""
    # Collapse runs of multiple spaces (artefact of PDF text extraction) to single
    text = re.sub(r"  +", " ", text)

    # Escape <<X>> placeholders (e.g. <<Your Name>>) — MDX parses these as JSX
    text = text.replace("<<", "&lt;&lt;").replace(">>", "&gt;&gt;")

    # Escape <X> patterns where X is lowercase text NOT a known HTML tag.
    # The book uses placeholders like <theirURL>, <name>, etc. that would
    # otherwise be interpreted as JSX. Whitelist standard HTML tags so the
    # injected callouts/figures still parse.
    html_tags = (
        "a|abbr|address|area|article|aside|b|bdi|bdo|blockquote|br|button|canvas|"
        "caption|cite|code|col|colgroup|data|datalist|dd|del|details|dfn|dialog|"
        "div|dl|dt|em|embed|fieldset|figcaption|figure|footer|form|h1|h2|h3|h4|"
        "h5|h6|head|header|hr|html|i|iframe|img|input|ins|kbd|label|legend|li|"
        "link|main|mark|menu|meta|nav|noscript|object|ol|optgroup|option|output|"
        "p|param|picture|pre|progress|q|rp|rt|ruby|s|samp|script|section|select|"
        "small|source|span|strong|style|sub|summary|sup|table|tbody|td|template|"
        "textarea|tfoot|th|thead|time|title|tr|track|u|ul|var|video|wbr"
    )
    # Escape `<` only if NOT followed by: capital letter (component), `/` (closing),
    # `!` (HTML comment), or a known HTML tag name + space/`>`/`/`/whitespace
    text = re.sub(
        r"<(?![A-Z/!])(?!(?:" + html_tags + r")[\s>/])",
        "&lt;",
        text,
    )

    text = MULTI_BLANK_RE.sub("\n\n", text)
    return text.strip()


def is_locked(slug: str) -> bool:
    out_path = OUT_DIR / f"{slug}.mdx"
    if not out_path.exists():
        return False
    return "migrate:locked" in out_path.read_text(encoding="utf-8")[:400]


def write_chapter_mdx(slug: str, description: str, body: str, has_components: bool) -> Path:
    out_path = OUT_DIR / f"{slug}.mdx"
    desc_safe = description.replace('"', '\\"')

    imports = []
    if has_components:
        imports.extend([
            'import ChapterSummary from "@components/ChapterSummary.astro";',
            'import CaseStudy from "@components/CaseStudy.astro";',
            'import ActionSteps from "@components/ActionSteps.astro";',
        ])
    if "<Callout" in body:
        imports.append('import Callout from "@components/Callout.astro";')
    if "<BookFigure" in body:
        imports.append('import BookFigure from "@components/BookFigure.astro";')

    # Chapter-specific extras
    suffix = ""
    if slug == "foreword":
        imports.append('import EMythCard from "@components/EMythCard.astro";')
        # Strip the original signoff line if present (smart_reflow joins it onto one line)
        body = re.sub(
            r"\n\s*Michael E\.\s*Gerber\s+Author of the E[\-‑]Myth Books\s+The E[\-‑]Myth Founder\s*$",
            "",
            body,
        )
        suffix = (
            '\n\n<figure class="signature">\n'
            '  <img src="/pdf/brand/gerber-signature.png" alt="Michael E. Gerber\'s signature" />\n'
            '  <p class="signature__signoff">\n'
            '    <strong>Michael E. Gerber</strong>\n'
            '    <em>Author of the E-Myth Books</em>\n'
            '    <em>The E-Myth Founder</em>\n'
            '  </p>\n'
            '</figure>\n\n'
            '<EMythCard />\n'
        )

    import_block = "\n".join(imports)
    if import_block:
        import_block = "\n" + import_block + "\n"

    content = f"""---
slug: {slug}
description: "{desc_safe}"
---
{import_block}
{body}{suffix}
"""
    out_path.write_text(content, encoding="utf-8")
    return out_path


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Source not found: {SOURCE}")

    source_lines = SOURCE.read_text(encoding="utf-8").splitlines()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Source: {SOURCE.relative_to(ROOT)} ({len(source_lines)} lines)")
    print(f"Output: {OUT_DIR.relative_to(ROOT)}/")
    print()

    for ch in CHAPTERS:
        slug, title, desc = ch["slug"], ch["title"], ch["description"]
        start, end = ch["start"], ch["end"]

        if is_locked(slug):
            print(f"  [lock]  {slug:20} (manual polish — not overwritten)")
            continue

        raw = extract_lines(source_lines, start, end)
        myth = ch.get("myth", "")
        cleaned = initial_clean(raw, title, myth)
        reflowed = smart_reflow(cleaned)
        with_subheads = detect_subheads(reflowed)  # AFTER reflow joins multi-line subheads
        bullet_fixed = merge_broken_bullets(with_subheads)
        consolidated = consolidate_bullet_blocks(bullet_fixed)
        emphasised = add_emphasis(consolidated)
        wrapped = detect_and_wrap_sections(emphasised, title)
        with_videos = inject_case_study_videos(wrapped)
        with_images = inject_chapter_images(with_videos, slug)
        final_text = post_process(with_images)

        if not final_text.strip():
            print(f"  [empty] {slug:20} (lines {start}-{end})")
            continue

        # Detect whether MDX components are referenced (so we add imports)
        has_components = any(
            tag in final_text
            for tag in ("<ChapterSummary", "<CaseStudy", "<ActionSteps")
        )

        out = write_chapter_mdx(slug, desc, final_text, has_components)
        word_count = len(final_text.split())
        line_range = f"L{start}-{end}" if end else f"L{start}-end"
        comp_marker = " [components]" if has_components else ""
        print(f"  [ok]    {slug:20} {word_count:>6} words  {line_range:>15}  -> {out.relative_to(ROOT)}{comp_marker}")

    print()
    print("Migration complete.")


if __name__ == "__main__":
    main()
