import { notFound } from "next/navigation";

import SignInForm from "@/components/SignInForm";
import { getDict } from "@/lib/i18n";
import { isLang } from "@/lib/types";

export default async function SignInPage({
  params,
}: {
  params: Promise<{ lang: string }>;
}) {
  const { lang } = await params;
  if (!isLang(lang)) notFound();
  const dict = getDict(lang);

  return <SignInForm lang={lang} t={dict.auth} />;
}
