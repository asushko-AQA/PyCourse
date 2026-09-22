import { notFound } from "next/navigation";
import { getDict } from "@/lib/i18n";
import { isLang, LANGS } from "@/lib/types";
import AppHeader from "@/components/AppHeader";

export function generateStaticParams() {
  return LANGS.map((lang) => ({ lang }));
}

export const dynamicParams = false;

export default async function LangLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ lang: string }>;
}) {
  const { lang } = await params;
  if (!isLang(lang)) notFound();
  const dict = getDict(lang);

  return (
    <div className="flex min-h-screen flex-col bg-gradient-to-b from-sky-50 via-violet-50/50 to-white">
      <AppHeader lang={lang} appName={dict.appName} dict={dict} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-4 py-8">
        {children}
      </main>
      <footer className="py-6 text-center text-sm font-semibold text-slate-400">
        {dict.tagline} ✨
      </footer>
    </div>
  );
}
