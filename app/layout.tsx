import { Footer, Layout, Navbar } from "nextra-theme-docs";
import { Head } from "nextra/components";
import { getPageMap } from "nextra/page-map";
import "nextra-theme-docs/style.css";
import "../styles/styles.css";

export const metadata = {};

const navbar = <Navbar logo={<span>T9</span>} />;
const footer = (
  <Footer>
    T9 &copy; {new Date().getFullYear()} | Owned and managed by Dev Patel
  </Footer>
);
const sidebar = {
  defaultMenuCollapseLevel: 1,
  toggleButton: true,
  autoCollapse: true,
};
const editLink = null;
const feedback = {
  content: null,
};
const navigation = {
  prev: false,
  next: false,
};

export default async function RootLayout({ children }) {
  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head>
        <link rel="shortcut icon" href="/images/general/icon.svg" />
        {/* Your additional tags should be passed as `children` of `<Head>` element */}
      </Head>
      <body>
        <Layout
          navbar={navbar}
          pageMap={await getPageMap()}
          sidebar={sidebar}
          editLink={editLink}
          feedback={feedback}
          footer={footer}
          navigation={navigation}
        >
          {children}
        </Layout>
      </body>
    </html>
  );
}
