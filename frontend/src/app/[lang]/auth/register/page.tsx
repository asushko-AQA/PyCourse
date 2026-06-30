import { notFound } from "next/navigation";
import { getDict } from "@/lib/i18n";
import { isLang } from "@/lib/types";
import RegisterForm from "@/components/RegisterForm";

export default async function RegisterPage({
  params,
}: {
  params: Promise<{ lang: string }>;
}) {
  const { lang } = await params;
  if (!isLang(lang)) notFound();
  const dict = getDict(lang);

  return <RegisterForm lang={lang} t={dict.auth} />;
}
