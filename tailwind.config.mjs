/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        brand: {
          navy: "#1a2b4a",
          "navy-deep": "#0f1d3a",
          orange: "#f97316",
          "orange-deep": "#ea580c",
          cream: "#faf7f2",
          stone: "#e8e4dc",
          ink: "#1f2937",
          muted: "#6b7280",
        },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        serif: ['"Source Serif 4"', '"Source Serif Pro"', 'Georgia', 'serif'],
        display: ['"Inter Tight"', 'Inter', 'sans-serif'],
      },
      maxWidth: {
        prose: '42rem',
        wide: '56rem',
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
