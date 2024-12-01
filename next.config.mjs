import nextra from "nextra";

const withNextra = nextra({
  theme: "nextra-theme-docs",
  themeConfig: "./theme.config.jsx",
  latex: true,
});

export default withNextra({
  compress: true,

  images: {
    formats: ["image/webp"],
    minimumCacheTTL: 60,
    unoptimized: true,
  },
});
