import { useRouter } from "next/router";
import { useEffect, useState } from "react";

const DynamicHead = () => {
  const router = useRouter();
  const [pageTitle, setPageTitle] = useState("T9");

  useEffect(() => {
    const path = router.pathname;
    const title = path.split("/").pop() || "T9";
    const formattedTitle = title
      .split("-")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(" ")
      .replace(/\.[^/.]+$/, "");

    setPageTitle(formattedTitle);
  }, [router.pathname]);

  return (
    <>
      <link
        rel="icon"
        type="image/svg+xml"
        href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏁</text></svg>"
      />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>{pageTitle}</title>
    </>
  );
};

export default {
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
    component: null,
  },
  feedback: {
    content: null,
  },
  footer: {
    content: (
      <span>
        T9 &copy; {new Date().getFullYear()} | Owned and managed by
        <a
          href="https://github.com/devakapatel"
          target="_blank"
          rel="noopener noreferrer"
        >
          {" "}
          Dev Patel
        </a>
      </span>
    ),
  },
  head: DynamicHead,
};
