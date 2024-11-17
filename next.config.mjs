import nextra from "nextra";

const withNextra = nextra({
  theme: "nextra-theme-docs",
  themeConfig: "./theme.config.jsx",
  latex: true,
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
