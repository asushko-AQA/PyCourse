"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";

import type { Dict } from "@/lib/i18n";
import type { Lang } from "@/lib/types";
import { AuthApiError, type AuthErrorCode } from "@/lib/authClient";
import { useAuthStore } from "@/stores/authStore";

type AuthDict = Dict["auth"];

export default function SignInForm({ lang, t }: { lang: Lang; t: AuthDict }) {
  const router = useRouter();
  const signIn = useAuthStore((s) => s.signIn);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [status, setStatus] = useState<"idle" | "submitting">("idle");
  const [errorCode, setErrorCode] = useState<AuthErrorCode | null>(null);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setErrorCode(null);
    setStatus("submitting");
    try {
      await signIn(email, password);
      router.push(`/${lang}`);
    } catch (err) {
      setErrorCode(err instanceof AuthApiError ? err.code : "generic");
      setStatus("idle");
    }
  }

  return (
    <div className="mx-auto max-w-md rounded-3xl bg-white/80 p-8 shadow-sm ring-1 ring-violet-100">
      <h1 className="text-2xl font-black text-slate-800">{t.signInTitle}</h1>
      <p className="mt-1 font-semibold text-slate-500">{t.signInSubtitle}</p>

      <form onSubmit={onSubmit} className="mt-6 flex flex-col gap-4">
        <label className="flex flex-col gap-1">
          <span className="text-sm font-bold text-slate-600">{t.emailLabel}</span>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            data-automation-id="sign-in-email"
            className="rounded-xl border border-slate-200 px-3 py-2 font-semibold text-slate-800 outline-none focus:border-violet-400"
          />
        </label>

        <label className="flex flex-col gap-1">
          <span className="text-sm font-bold text-slate-600">{t.passwordLabel}</span>
          <input
            type="password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            data-automation-id="sign-in-password"
            className="rounded-xl border border-slate-200 px-3 py-2 font-semibold text-slate-800 outline-none focus:border-violet-400"
          />
        </label>

        {errorCode && (
          <p
            data-automation-id="sign-in-error"
            className="rounded-xl bg-rose-50 px-3 py-2 text-sm font-bold text-rose-600"
          >
            {t.errors[errorCode] ?? t.errors.generic}
          </p>
        )}

        <button
          type="submit"
          disabled={status === "submitting"}
          data-automation-id="sign-in-submit"
          className="rounded-full bg-violet-600 px-5 py-3 font-extrabold text-white shadow transition-colors hover:bg-violet-700 disabled:opacity-60"
        >
          {status === "submitting" ? t.signingIn : t.signInSubmit}
        </button>
      </form>

      <div className="mt-4 text-center text-sm font-semibold text-slate-500">
        {t.noAccountYet}{" "}
        <Link href={`/${lang}/auth/register`} className="font-extrabold text-violet-600 hover:underline">
          {t.registerCta}
        </Link>
      </div>
    </div>
  );
}
