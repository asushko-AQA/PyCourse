"use client";

/**
 * EN / RU switch. Swaps the [lang] URL segment of the current pathname —
 * gamification state is untouched (it lives in localStorage, not the route).
 */

import { usePathname, useRouter } from "next/navigation";
import type { Lang } from "@/lib/types";

const OPTIONS: { code: Lang; label: string }[] = [
  { code: "en", label: "EN" },
  { code: "ru", label: "РУ" },
];

export default function LanguageToggle({ current }: { current: Lang }) {
  const router = useRouter();
  const pathname = usePathname();

  function switchTo(lang: Lang) {
    if (lang === current) return;
    const segments = pathname.split("/");
    segments[1] = lang; // ["", lang, ...rest]
    router.push(segments.join("/") || `/${lang}`);
  }

  return (
    <div className="flex rounded-full bg-white/80 p-1 shadow-sm ring-1 ring-sky-200">
      {OPTIONS.map((opt) => (
        <button
          key={opt.code}
          onClick={() => switchTo(opt.code)}
          className={`rounded-full px-3 py-1 text-xs font-extrabold transition-colors ${
            opt.code === current
              ? "bg-sky-500 text-white shadow"
              : "text-sky-600 hover:bg-sky-100"
          }`}
          aria-pressed={opt.code === current}
        >
          {opt.label}
        </button>
      ))}
    </div>
  );
}
