import dynamic from "next/dynamic";
import "../styles/styles.css";

const DynamicHeader = dynamic(() => import("../components/header"), {
  loading: () => <p>Loading...</p>,
});

export default function App({ Component, pageProps }) {
  return (
    <>
      <Component {...pageProps} />
      <script
        defer
        src="https://static.cloudflareinsights.com/beacon.min.js"
        data-cf-beacon='{"token": "d56a42c085dd4918bf504a2f33f140f4"}'
      ></script>
    </>
  );
}
