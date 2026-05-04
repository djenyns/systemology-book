import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import tailwind from "@astrojs/tailwind";
import rehypeSlug from "rehype-slug";
import rehypeAutolinkHeadings from "rehype-autolink-headings";

export default defineConfig({
  site: "https://www.systemology.com",
  base: "/pdf",
  trailingSlash: "always",
  integrations: [
    mdx({
      rehypePlugins: [
        rehypeSlug,
        [
          rehypeAutolinkHeadings,
          {
            behavior: "append",
            properties: { className: ["anchor-link"], "aria-label": "Direct link" },
            content: { type: "text", value: "¶" },
          },
        ],
      ],
    }),
    sitemap({
      changefreq: "monthly",
      priority: 0.9,
    }),
    tailwind({ applyBaseStyles: false }),
  ],
  build: {
    format: "directory",
  },
  markdown: {
    shikiConfig: {
      theme: "github-light",
      wrap: true,
    },
    rehypePlugins: [
      rehypeSlug,
      [
        rehypeAutolinkHeadings,
        {
          behavior: "append",
          properties: { className: ["anchor-link"], "aria-label": "Direct link" },
          content: { type: "text", value: "¶" },
        },
      ],
    ],
  },
});
