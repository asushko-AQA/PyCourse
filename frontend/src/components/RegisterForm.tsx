"use client";

import { useState } from "react";
import Link from "next/link";
import type { Dict } from "@/lib/i18n";
import { fill } from "@/lib/i18n";
import type { Lang } from "@/lib/types";
import { AuthApiError, register, type AuthErrorCode } from "@/lib/authClient";

type AuthDict = Dict["auth"];

export default function RegisterForm({ lang, t }: { lang: Lang; t: AuthDict }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isMinor, setIsMinor] = useState(false);
  const [guardianEmail, setGuardianEmail] = useState("");
  const [parentalConsent, setParentalConsent] = useState(false);

  const [status, setStatus] = useState<"idle" | "submitting" | "sent">("idle");
  const [errorCode, setErrorCode] = useState<AuthErrorCode | null>(null);
  const [sentTo, setSentTo] = useState("");

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setErrorCode(null);
    setStatus("submitting");
    try {
      const result = await register({
        email,
        password,
        isMinor,
        guardianEmail: isMinor ? guardianEmail : undefined,
        parentalConsent: isMinor ? parentalConsent : false,
      });
      setSentTo(isMinor ? guardianEmail : result.email);
      setStatus("sent");
    } catch (err) {
      setErrorCode(err instanceof AuthApiError ? err.code : "generic");
      setStatus("idle");
    }
  }

  if (status === "sent") {
    const body = fill(
      isMinor ? t.checkEmailGuardianBody : t.checkEmailBody,
      { email: sentTo },
    );
    return (
      <div className="mx-auto max-w-md rounded-3xl bg-white/80 p-8 text-center shadow-sm ring-1 ring-violet-100">
        <h1 className="text-2xl font-black text-slate-800">{t.checkEmailTitle}</h1>
        <p className="mt-3 font-semibold text-slate-500">{body}</p>
        <button
          data-automation-id="register-another"
          onClick={() => {
            setStatus("idle");
            setEmail("");
            setPassword("");
          }}
          className="mt-6 text-sm font-extrabold text-violet-600 hover:underline"
        >
          {t.registerAnother}
        </button>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-md rounded-3xl bg-white/80 p-8 shadow-sm ring-1 ring-violet-100">
      <h1 className="text-2xl font-black text-slate-800">{t.registerTitle}</h1>
      <p className="mt-1 font-semibold text-slate-500">{t.registerSubtitle}</p>

      <form onSubmit={onSubmit} className="mt-6 flex flex-col gap-4">
        <label className="flex flex-col gap-1">
          <span className="text-sm font-bold text-slate-600">{t.emailLabel}</span>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            data-automation-id="register-email"
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
            data-automation-id="register-password"
            className="rounded-xl border border-slate-200 px-3 py-2 font-semibold text-slate-800 outline-none focus:border-violet-400"
          />
          <span className="text-xs font-semibold text-slate-400">{t.passwordHint}</span>
        </label>

        <label className="flex items-center gap-2">
          <input
            type="checkbox"
            checked={isMinor}
            onChange={(e) => setIsMinor(e.target.checked)}
            data-automation-id="register-is-minor"
            className="h-4 w-4 rounded border-slate-300"
          />
          <span className="text-sm font-bold text-slate-600">{t.minorLabel}</span>
        </label>

        {isMinor && (
          <div className="flex flex-col gap-4 rounded-2xl bg-violet-50 p-4">
            <label className="flex flex-col gap-1">
              <span className="text-sm font-bold text-slate-600">
                {t.guardianEmailLabel}
              </span>
              <input
                type="email"
                required
                value={guardianEmail}
                onChange={(e) => setGuardianEmail(e.target.value)}
                data-automation-id="register-guardian-email"
                className="rounded-xl border border-slate-200 px-3 py-2 font-semibold text-slate-800 outline-none focus:border-violet-400"
              />
            </label>
            <label className="flex items-start gap-2">
              <input
                type="checkbox"
                checked={parentalConsent}
                onChange={(e) => setParentalConsent(e.target.checked)}
                data-automation-id="register-consent"
                className="mt-1 h-4 w-4 rounded border-slate-300"
              />
              <span className="text-sm font-semibold text-slate-600">
                {t.consentLabel}
              </span>
            </label>
          </div>
        )}

        {errorCode && (
          <p
            data-automation-id="register-error"
            className="rounded-xl bg-rose-50 px-3 py-2 text-sm font-bold text-rose-600"
          >
            {t.errors[errorCode] ?? t.errors.generic}
          </p>
        )}

        <button
          type="submit"
          disabled={status === "submitting"}
          data-automation-id="register-submit"
          className="rounded-full bg-violet-600 px-5 py-3 font-extrabold text-white shadow transition-colors hover:bg-violet-700 disabled:opacity-60"
        >
          {status === "submitting" ? t.submitting : t.submit}
        </button>
      </form>

      <Link
        href={`/${lang}`}
        className="mt-4 block text-center text-sm font-extrabold text-slate-400 hover:underline"
      >
        {t.backHome}
      </Link>
    </div>
  );
}
