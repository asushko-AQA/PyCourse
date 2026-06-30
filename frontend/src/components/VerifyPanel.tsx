"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import type { Dict } from "@/lib/i18n";
import type { Lang } from "@/lib/types";
import { AuthApiError, verifyEmail, type AuthErrorCode } from "@/lib/authClient";

type AuthDict = Dict["auth"];

/**
 * Reads the `token` from the URL query and confirms it against the backend.
 * The token is read from `window.location` (in an effect) rather than
 * `useSearchParams` so the page needs no Suspense boundary.
 */
export default function VerifyPanel({ lang, t }: { lang: Lang; t: AuthDict }) {
  const [state, setState] = useState<"verifying" | "ok" | "error">("verifying");
  const [errorCode, setErrorCode] = useState<AuthErrorCode>("generic");

  useEffect(() => {
    const token = new URLSearchParams(window.location.search).get("token");
    const run = token
      ? verifyEmail(token)
      : Promise.reject(new AuthApiError("missing_token"));
    run
      .then(() => setState("ok"))
      .catch((err) => {
        setErrorCode(err instanceof AuthApiError ? err.code : "generic");
        setState("error");
      });
  }, []);

  return (
    <div className="mx-auto max-w-md rounded-3xl bg-white/80 p-8 text-center shadow-sm ring-1 ring-violet-100">
      {state === "verifying" && (
        <>
          <h1 className="text-2xl font-black text-slate-800">{t.verifyTitle}</h1>
          <p className="mt-3 font-semibold text-slate-500">{t.verifying}</p>
        </>
      )}

      {state === "ok" && (
        <div data-automation-id="verify-success">
          <h1 className="text-2xl font-black text-emerald-600">{t.verifiedTitle}</h1>
          <p className="mt-3 font-semibold text-slate-500">{t.verifiedBody}</p>
        </div>
      )}

      {state === "error" && (
        <div data-automation-id="verify-error">
          <h1 className="text-2xl font-black text-rose-600">{t.verifyFailedTitle}</h1>
          <p className="mt-3 font-semibold text-slate-500">
            {t.errors[errorCode] ?? t.errors.generic}
          </p>
        </div>
      )}

      <Link
        href={`/${lang}`}
        className="mt-6 inline-block text-sm font-extrabold text-violet-600 hover:underline"
      >
        {t.backHome}
      </Link>
    </div>
  );
}
