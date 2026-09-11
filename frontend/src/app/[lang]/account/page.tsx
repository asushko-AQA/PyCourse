import { notFound } from "next/navigation";

import AccountPanel from "@/components/AccountPanel";
import { getDict } from "@/lib/i18n";
import { isLang } from "@/lib/types";

export default async function AccountPage({
  params,
}: {
  params: Promise<{ lang: string }>;
}) {
  const { lang } = await params;
  if (!isLang(lang)) notFound();
  const dict = getDict(lang);

  return <AccountPanel lang={lang} t={dict.account} authT={dict.auth} />;
}
