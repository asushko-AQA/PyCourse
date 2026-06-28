import Link from "next/link";
import { notFound } from "next/navigation";
import { getDict } from "@/lib/i18n";
import { isLang, LANGS } from "@/lib/types";
import LanguageToggle from "@/components/LanguageToggle";
import XPBadge from "@/components/XPBadge";

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
      <header className="sticky top-0 z-20 border-b border-white/60 bg-white/70 backdrop-blur">
        <div className="mx-auto flex max-w-4xl items-center justify-between gap-3 px-4 py-3">
          <Link
            href={`/${lang}`}
            data-automation-id="nav-logo-home"
            className="flex items-center gap-2 text-lg font-black text-violet-700"
          >
            <span className="text-2xl" aria-hidden>
              🐍
            </span>
            {dict.appName}
          </Link>
          <div className="flex items-center gap-3">
            <XPBadge levelLabel={dict.nav.level} xpLabel={dict.nav.xp} />
            <LanguageToggle current={lang} />
          </div>
        </div>
      </header>
      <main className="mx-auto w-full max-w-4xl flex-1 px-4 py-8">
        {children}
      </main>
      <footer className="py-6 text-center text-sm font-semibold text-slate-400">
        {dict.tagline} ✨
      </footer>
    </div>
  );
}
