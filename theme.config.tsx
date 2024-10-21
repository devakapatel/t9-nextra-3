import React from "react";
import { DocsThemeConfig } from "nextra-theme-docs";

const config: DocsThemeConfig = {
  logo: <span>T9</span>,
  navigation: {
    prev: false,
    next: false,
  },
  sidebar: {
    defaultMenuCollapseLevel: 1,
    toggleButton: true,
    autoCollapse: true,
  },
  editLink: {
    text: null,
    component: null,
  },
  feedback: {
    content: null,
  },
  footer: {
    text: "T9 © 2024",
  },
  head: (
    <>
      <link
        rel="icon"
        type="image/svg+xml"
        href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏁</text></svg>"
      />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    </>
  ),
  useNextSeoProps() {
    return {
      titleTemplate: "%s",
    };
  },
};

export default config;
