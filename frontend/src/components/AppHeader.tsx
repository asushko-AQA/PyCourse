"use client";

import Link from "next/link";

import AuthNavControls from "@/components/AuthNavControls";
import LanguageToggle from "@/components/LanguageToggle";
import MobileMenu from "@/components/MobileMenu";
import ProgressNav from "@/components/ProgressNav";
import type { Dict } from "@/lib/i18n";
import type { Lang } from "@/lib/types";

export default function AppHeader({
  lang,
  appName,
  dict,
}: {
  lang: Lang;
  appName: string;
  dict: Pick<Dict, "auth" | "nav" | "menu">;
}) {
  return (
    <header className="sticky top-0 z-20 border-b border-white/60 bg-white/70 backdrop-blur">
      <div className="mx-auto flex max-w-4xl items-center justify-between gap-3 px-4 py-3">
        <Link
          href={`/${lang}`}
          data-automation-id="nav-logo-home"
          className="flex items-center gap-2 text-lg font-black text-violet-700"
        >
          <span className="text-xl sm:text-2xl" aria-hidden>
            🐍
          </span>
          <span className="hidden sm:inline">{appName}</span>
        </Link>

        <div className="hidden items-center gap-3 md:flex">
          <AuthNavControls lang={lang} t={dict.auth} />
          <ProgressNav lang={lang} t={dict.nav} />
          <LanguageToggle current={lang} />
        </div>

        <div className="md:hidden">
          <MobileMenu lang={lang} authT={dict.auth} menuT={dict.menu} />
        </div>
      </div>
    </header>
  );
}
