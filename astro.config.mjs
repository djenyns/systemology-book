import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import tailwind from "@astrojs/tailwind";

export default defineConfig({
  site: "https://systemology.com",
  base: "/pdf",
  trailingSlash: "always",
  integrations: [
    mdx(),
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
  },
});
