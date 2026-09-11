"use client";

import Link from "next/link";
import { useEffect } from "react";

import type { Dict } from "@/lib/i18n";
import type { Lang } from "@/lib/types";
import { useAuthStore } from "@/stores/authStore";
import XPBadge from "@/components/XPBadge";

type NavDict = Dict["nav"];

export default function ProgressNav({
  lang,
  t,
}: {
  lang: Lang;
  t: NavDict;
}) {
  const { status, bootstrap } = useAuthStore();

  useEffect(() => {
    if (status === "unknown") {
      void bootstrap();
    }
  }, [bootstrap, status]);

  if (status === "signed_in") {
    return <XPBadge levelLabel={t.level} xpLabel={t.xp} />;
  }

  return (
    <div
      data-automation-id="nav-progress-cta"
      className="flex items-center gap-2 rounded-full bg-violet-50/90 px-3 py-1.5 ring-1 ring-violet-100"
    >
      <span className="text-xs font-bold text-violet-700">{t.progressCta}</span>
      <Link
        href={`/${lang}/auth/register`}
        data-automation-id="nav-progress-sign-up"
        className="shrink-0 rounded-full bg-violet-600 px-3 py-1 text-xs font-extrabold text-white hover:bg-violet-700"
      >
        {t.progressCtaButton}
      </Link>
    </div>
  );
}
