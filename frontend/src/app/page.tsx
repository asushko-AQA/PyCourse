import { redirect } from "next/navigation";

/** Root entry — the app lives under /[lang]. */
export default function RootPage() {
  redirect("/en");
}
