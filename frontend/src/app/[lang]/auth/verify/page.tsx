import { notFound } from "next/navigation";
import { getDict } from "@/lib/i18n";
import { isLang } from "@/lib/types";
import VerifyPanel from "@/components/VerifyPanel";

export default async function VerifyPage({
  params,
}: {
  params: Promise<{ lang: string }>;
}) {
  const { lang } = await params;
  if (!isLang(lang)) notFound();
  const dict = getDict(lang);

  return <VerifyPanel lang={lang} t={dict.auth} />;
}
