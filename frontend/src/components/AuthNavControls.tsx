"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

import type { Dict } from "@/lib/i18n";
import type { Lang } from "@/lib/types";
import { useAuthStore } from "@/stores/authStore";
import { AuthApiError, type AuthErrorCode } from "@/lib/authClient";

type AuthDict = Dict["auth"];

export default function AuthNavControls({ lang, t }: { lang: Lang; t: AuthDict }) {
  const { user, status, bootstrap, signOut } = useAuthStore();
  const [errorCode, setErrorCode] = useState<AuthErrorCode | null>(null);

  useEffect(() => {
    if (status === "unknown") {
      void bootstrap();
    }
  }, [bootstrap, status]);

  async function onSignOut() {
    setErrorCode(null);
    try {
      await signOut();
    } catch (err) {
      setErrorCode(err instanceof AuthApiError ? err.code : "generic");
    }
  }

  if (status === "signed_in" && user) {
    return (
      <div className="flex items-center gap-2">
        <span className="hidden text-xs font-bold text-slate-500 sm:block">{user.email}</span>
        <button
          onClick={onSignOut}
          data-automation-id="nav-sign-out"
          className="rounded-full border border-slate-200 px-3 py-1 text-xs font-extrabold text-slate-600 hover:bg-slate-100"
        >
          {t.signOut}
        </button>
        {errorCode && (
          <span className="text-xs font-bold text-rose-500">{t.errors[errorCode] ?? t.errors.generic}</span>
        )}
      </div>
    );
  }

  return (
    <div className="flex items-center gap-2">
      <Link
        href={`/${lang}/auth/sign-in`}
        data-automation-id="nav-sign-in"
        className="rounded-full border border-violet-200 px-3 py-1 text-xs font-extrabold text-violet-700 hover:bg-violet-50"
      >
        {t.signInCta}
      </Link>
      <Link
        href={`/${lang}/auth/register`}
        data-automation-id="nav-register"
        className="rounded-full bg-violet-600 px-3 py-1 text-xs font-extrabold text-white hover:bg-violet-700"
      >
        {t.registerCta}
      </Link>
    </div>
  );
}
