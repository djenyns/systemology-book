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
  license: "https://creativecommons.org/licenses/by/4.0/",
  licenseShort: "CC BY 4.0",
  canonicalUrl: "https://systemology.com/pdf/",
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
  estReadMinutes: number;
  estAudioMinutes: number;
};

export const chapters: Chapter[] = [
  {
    slug: "introduction",
    number: null,
    title: "Introduction",
    subtitle: "Why most business owners stay trapped",
    realPoint:
      "Most business owners are too buried in operations to grab the opportunities life sends them — SYSTEMology is the system that buys back the headspace.",
    audioFile: "003_SYSTEMology_Introduction.mp3",
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
    estReadMinutes: 8,
    estAudioMinutes: 12,
  },
  {
    slug: "appendix",
    number: null,
    title: "Appendix",
    subtitle: "Templates, sample systems, additional resources",
    realPoint:
      "Print-ready versions of every template referenced in the book, plus the TEDx talk and supplementary material.",
    audioFile: "013_SYSTEMology_TEDx Talk & Additional Resources.mp3",
    estReadMinutes: 10,
    estAudioMinutes: 15,
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
    estReadMinutes: 6,
    estAudioMinutes: 10,
  },
];

export const chaptersBySlug: Record<string, Chapter> = Object.fromEntries(
  chapters.map((c) => [c.slug, c])
);

export const stageChapters = chapters.filter((c) => c.number !== null);
