/**
 * Canonical book metadata. Single source of truth for schema, llms.txt,
 * citation blocks, and the chapter manifest.
 *
 * Sourced from research/07-amazon-mining.md verified Amazon/Goodreads data.
 */

export const book = {
  title: "SYSTEMology",
  subtitle: "Create Time, Reduce Errors and Scale Your Profits with Proven Business Systems",
  author: {
    name: "David Jenyns",
    url: "https://davidjenyns.com",
    sameAs: [
      "https://www.linkedin.com/in/davidjenyns/",
      "https://twitter.com/davidjenyns",
      "https://www.davidjenyns.com",
      // Wikidata + ORCID populated in Phase 3
    ],
  },
  publisher: {
    name: "Rethink Press",
    url: "https://www.rethinkpress.com/",
  },
  isbn13: "978-0648871002",
  datePublished: "2020-09-15",
  inLanguage: "en",
  pageCount: 212,
  audioDuration: "PT5H31M",
  audioNarrator: "David Jenyns",
  license: "https://creativecommons.org/licenses/by-nc-nd/4.0/",
  licenseShort: "CC BY-NC-ND 4.0",
  canonicalUrl: "https://www.systemology.com/pdf/",
  amazonUrl: "https://www.amazon.com/dp/B08CDY993G",
  audibleUrl: "https://www.audible.com/pd/SYSTEMology-Audiobook/B08FLBPP9R",
  goodreadsUrl: "https://www.goodreads.com/book/show/54609541-systemology",
  // Comparable books per Audible "Listeners Also Bought" — drives isSimilarTo schema
  isSimilarTo: [
    { name: "Clockwork", author: "Mike Michalowicz" },
    { name: "Built to Sell", author: "John Warrillow" },
    { name: "Beyond the E-Myth", author: "Michael E. Gerber" },
    { name: "Fix This Next", author: "Mike Michalowicz" },
    { name: "They Ask You Answer", author: "Marcus Sheridan" },
  ],
} as const;

export type Chapter = {
  slug: string;
  number: number | null; // 1-7 for stages, null for non-chapter sections
  title: string;
  subtitle: string;
  realPoint: string; // Seth-Godin-style "what this chapter is really about"
  myth?: string; // for stages 1-7
  audioFile: string; // matches source-assets/audio/Mastered MP3 Files/
  audioWistiaId?: string; // Wistia hashed_id for the audio chapter (preferred over local MP3)
  audioNarrator?: string; // override for the audio narrator (default: David Jenyns)
  videoWistiaId?: string; // Optional inline video at top of chapter (Gerber foreword, Allan Dib endorsement, etc.)
  videoLabel?: string; // Caption for the inline video
  cogImage?: string; // Path to per-stage cog illustration (e.g. /pdf/brand/cogs/stage-01.png)
  estReadMinutes: number;
  estAudioMinutes: number;
};

export const chapters: Chapter[] = [
  {
    slug: "foreword",
    number: null,
    title: "Foreword",
    subtitle: "by Michael E. Gerber, author of The E-Myth",
    realPoint:
      "Michael Gerber, who invented \"work ON your business, not IN it\" forty-three years ago, says David Jenyns has actually done it — and built the system to teach you how.",
    // Video covers the audio narration — skip the audio player to avoid redundancy.
    audioFile: "",
    videoWistiaId: "fkeues1uxt",
    videoLabel: "Watch Michael E. Gerber read the foreword",
    estReadMinutes: 4,
    estAudioMinutes: 6,
  },
  {
    slug: "introduction",
    number: null,
    title: "Introduction",
    subtitle: "Why most business owners stay trapped",
    realPoint:
      "Most business owners are too buried in operations to grab the opportunities life sends them — SYSTEMology is the system that buys back the headspace.",
    audioFile: "003_SYSTEMology_Introduction.mp3",
    audioWistiaId: "q197pathg6",
    estReadMinutes: 18,
    estAudioMinutes: 28,
  },
  {
    slug: "define",
    number: 1,
    title: "Define",
    subtitle: "Identify your Critical Client Flow",
    realPoint:
      "You don't need hundreds of systems — you need 10 to 15. Pick one client, one product, and trace the path between them.",
    myth: "You will need to create hundreds of systems to systemise a business.",
    audioFile: "004_SYSTEMology_Step 1 - Define.mp3",
    audioWistiaId: "2mooy28f0s",
    cogImage: "/pdf/brand/cogs/stage-01.png",
    estReadMinutes: 26,
    estAudioMinutes: 38,
  },
  {
    slug: "assign",
    number: 2,
    title: "Assign",
    subtitle: "Find your Systems Champion and your Knowledgeable Workers",
    realPoint:
      "The knowledge you need is already in your team's heads. Your job is to find it and assign someone else to extract it.",
    myth: "The business owner is the only one who can create the systems.",
    audioFile: "005_SYSTEMology_Step 2 - Assign.mp3",
    audioWistiaId: "qb72o5vnb8",
    cogImage: "/pdf/brand/cogs/stage-02.png",
    estReadMinutes: 16,
    estAudioMinutes: 24,
  },
  {
    slug: "extract",
    number: 3,
    title: "Extract",
    subtitle: "Capture how the work is actually done",
    realPoint:
      "Stop trying to write systems from scratch. Record someone doing the job — that's your first draft.",
    myth: "Creating systems is time-consuming.",
    audioFile: "006_SYSTEMology_Step 3 - Extract.mp3",
    audioWistiaId: "9qzt16ajpx",
    cogImage: "/pdf/brand/cogs/stage-03.png",
    estReadMinutes: 22,
    estAudioMinutes: 32,
  },
  {
    slug: "organise",
    number: 4,
    title: "Organise",
    subtitle: "Make systems findable at the point of need",
    realPoint:
      "Systems that aren't accessible aren't systems. Get them out of Google Drive and into one tool everyone uses.",
    myth: "You need to invest in expensive and complex software.",
    audioFile: "007_SYSTEMology_Step 4 - Organise.mp3",
    audioWistiaId: "62kn9sa0au",
    cogImage: "/pdf/brand/cogs/stage-04.png",
    estReadMinutes: 18,
    estAudioMinutes: 26,
  },
  {
    slug: "integrate",
    number: 5,
    title: "Integrate",
    subtitle: "Get the team to use the systems",
    realPoint:
      "Documentation only matters if people use it. Build a culture where the system is the default, not the exception.",
    myth: "Even if you have systems in place, your team won't follow them.",
    audioFile: "008_SYSTEMology_Step 5 - Integrate.mp3",
    audioWistiaId: "nnqaa2q77k",
    cogImage: "/pdf/brand/cogs/stage-05.png",
    estReadMinutes: 20,
    estAudioMinutes: 30,
  },
  {
    slug: "scale",
    number: 6,
    title: "Scale",
    subtitle: "Build out your Minimum Viable Systems",
    realPoint:
      "Once the Critical Client Flow is documented, the rest is just repetition across the rest of the business.",
    myth: "Systemisation destroys creativity.",
    audioFile: "009_SYSTEMology_Step 6 - Scale.mp3",
    audioWistiaId: "su2ayn1u4b",
    cogImage: "/pdf/brand/cogs/stage-06.png",
    estReadMinutes: 22,
    estAudioMinutes: 32,
  },
  {
    slug: "optimise",
    number: 7,
    title: "Optimise",
    subtitle: "Build dashboards, find the leaks, compound improvements",
    realPoint:
      "Once systems run, you measure them. Once you measure them, you improve them. That's the engine.",
    myth: "You need to systemise like McDonald's.",
    audioFile: "010_SYSTEMology_Step 7 - Optimise.mp3",
    audioWistiaId: "plztueaud9",
    cogImage: "/pdf/brand/cogs/stage-07.png",
    estReadMinutes: 18,
    estAudioMinutes: 26,
  },
  {
    slug: "now-is-the-time",
    number: null,
    title: "Now is the time",
    subtitle: "What to do tomorrow morning",
    realPoint:
      "The question isn't whether to systemise. It's whether you start this week or pretend for another year.",
    audioFile: "011_SYSTEMology_Now Is The Time.mp3",
    audioWistiaId: "114fx1yy4n",
    estReadMinutes: 12,
    estAudioMinutes: 18,
  },
  {
    slug: "epilogue",
    number: null,
    title: "Epilogue",
    subtitle: "The Final Secret",
    realPoint:
      "The whole framework reduces to one principle: the business owner is the bottleneck. Remove them.",
    audioFile: "012_SYSTEMology_Epilogue.mp3",
    audioWistiaId: "7noc8d3lm7",
    estReadMinutes: 8,
    estAudioMinutes: 12,
  },
  {
    slug: "myths-summary",
    number: null,
    title: "7 Myths Summary",
    subtitle: "Each myth, and the chapter where it gets busted",
    realPoint:
      "A one-page recap of the seven systemisation myths the book busts — useful as a quick reference or to share with sceptical team members.",
    audioFile: "",
    estReadMinutes: 2,
    estAudioMinutes: 0,
  },
  {
    slug: "glossary",
    number: null,
    title: "Glossary",
    subtitle: "Defined terms",
    realPoint:
      "Every named concept, defined precisely. Each term has its own URL — quote the page, link the page.",
    audioFile: "", // no audio
    estReadMinutes: 6,
    estAudioMinutes: 0,
  },
  {
    slug: "about",
    number: null,
    title: "About the Author",
    subtitle: "David Jenyns — founder, SYSTEMology",
    realPoint:
      "How a Melbourne SEO agency owner accidentally invented a methodology — and why he gave it away.",
    audioFile: "015_SYSTEMology_Acknowledgements.mp3",
    audioWistiaId: "gard1b8n9e",
    estReadMinutes: 6,
    estAudioMinutes: 10,
  },
];

export const chaptersBySlug: Record<string, Chapter> = Object.fromEntries(
  chapters.map((c) => [c.slug, c])
);

export const stageChapters = chapters.filter((c) => c.number !== null);

/**
 * SAMPLE MODE — the Kindle edition is enrolled in Kindle Unlimited (KDP
 * Select), whose terms require ebook exclusivity, so only front matter is
 * published online (~13% of the text). Locked chapters stay in content/
 * untouched; their TOC cards grey out and link to the book sales page.
 *
 * To restore the full free web edition: set to false, remove the sample-mode
 * 301 block from public/_redirects, and restore the full-text llms.txt.
 */
export const SAMPLE_MODE = true;

export const BOOK_URL = "https://www.systemology.com/book/";

export function isLive(c: Chapter): boolean {
  if (!SAMPLE_MODE) return true;
  return c.slug === "foreword" || c.slug === "introduction" || c.slug === "about";
}

export const liveChapters = chapters.filter(isLive);
