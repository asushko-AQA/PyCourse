"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

import type { Dict } from "@/lib/i18n";
import type { Lang } from "@/lib/types";
import { AuthApiError, type AuthErrorCode } from "@/lib/authClient";
import { useAuthStore } from "@/stores/authStore";

type AccountDict = Dict["account"];
type AuthDict = Dict["auth"];

export default function AccountPanel({
  lang,
  t,
  authT,
}: {
  lang: Lang;
  t: AccountDict;
  authT: AuthDict;
}) {
  const router = useRouter();
  const { user, status, bootstrap, signOut } = useAuthStore();
  const [errorCode, setErrorCode] = useState<AuthErrorCode | null>(null);

  useEffect(() => {
    if (status === "unknown") {
      void bootstrap();
    }
  }, [bootstrap, status]);

  useEffect(() => {
    if (status === "signed_out") {
      router.replace(`/${lang}/auth/sign-in`);
    }
  }, [lang, router, status]);

  async function onSignOut() {
    setErrorCode(null);
    try {
      await signOut();
      router.push(`/${lang}`);
    } catch (err) {
      setErrorCode(err instanceof AuthApiError ? err.code : "generic");
    }
  }

  if (status !== "signed_in" || !user) {
    return (
      <div className="mx-auto max-w-md rounded-3xl bg-white/80 p-8 text-center shadow-sm ring-1 ring-violet-100">
        <p className="font-semibold text-slate-500">{authT.signingIn}</p>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-md rounded-3xl bg-white/80 p-8 shadow-sm ring-1 ring-violet-100">
      <h1 className="text-2xl font-black text-slate-800">{t.title}</h1>
      <p className="mt-1 font-semibold text-slate-500">{t.subtitle}</p>

      <dl className="mt-6 rounded-2xl bg-violet-50/80 px-4 py-3">
        <dt className="text-xs font-extrabold uppercase tracking-wide text-violet-500">
          {t.emailLabel}
        </dt>
        <dd
          data-automation-id="account-email"
          className="mt-1 text-sm font-bold text-slate-800"
        >
          {user.email}
        </dd>
      </dl>

      {errorCode && (
        <p className="mt-4 rounded-xl bg-rose-50 px-3 py-2 text-sm font-bold text-rose-600">
          {authT.errors[errorCode] ?? authT.errors.generic}
        </p>
      )}

      <button
        type="button"
        onClick={onSignOut}
        data-automation-id="account-sign-out"
        className="mt-6 w-full rounded-full border border-slate-200 px-5 py-3 font-extrabold text-slate-600 hover:bg-slate-100"
      >
        {authT.signOut}
      </button>

      <div className="mt-4 text-center">
        <Link
          href={`/${lang}`}
          data-automation-id="account-back-home"
          className="text-sm font-extrabold text-violet-600 hover:underline"
        >
          {t.backHome}
        </Link>
      </div>
    </div>
  );
}
