import nextra from "nextra";

const withNextra = nextra({
  theme: "nextra-theme-docs",
  themeConfig: "./theme.config.jsx",
  latex: true,
  // Optimize search
  flexsearch: {
    codeblocks: false,
  },
});

export default withNextra({
  // Basic optimizations
  swcMinify: true,
  compress: true,

  // Image optimization
  images: {
    formats: ["image/webp"],
    minimumCacheTTL: 60,
    unoptimized: true, // Required for Cloudflare Pages static exports
  },
});
