"use client";

import Link from "next/link";
import { Menu, X } from "lucide-react";
import { useEffect, useId, useState } from "react";

import LanguageToggle from "@/components/LanguageToggle";
import type { Dict } from "@/lib/i18n";
import type { Lang } from "@/lib/types";
import { AuthApiError, type AuthErrorCode } from "@/lib/authClient";
import { useAuthStore } from "@/stores/authStore";

type AuthDict = Dict["auth"];
type MenuDict = Dict["menu"];

export default function MobileMenu({
  lang,
  authT,
  menuT,
}: {
  lang: Lang;
  authT: AuthDict;
  menuT: MenuDict;
}) {
  const menuId = useId();
  const { user, status, bootstrap, signOut } = useAuthStore();
  const [open, setOpen] = useState(false);
  const [errorCode, setErrorCode] = useState<AuthErrorCode | null>(null);

  useEffect(() => {
    if (status === "unknown") {
      void bootstrap();
    }
  }, [bootstrap, status]);

  useEffect(() => {
    if (!open) return;
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpen(false);
    };
    document.addEventListener("keydown", onKeyDown);
    return () => document.removeEventListener("keydown", onKeyDown);
  }, [open]);

  async function onSignOut() {
    setErrorCode(null);
    try {
      await signOut();
      setOpen(false);
    } catch (err) {
      setErrorCode(err instanceof AuthApiError ? err.code : "generic");
    }
  }

  function closeMenu() {
    setOpen(false);
  }

  const menuLinkClass =
    "block rounded-2xl px-4 py-3 text-sm font-extrabold text-slate-700 hover:bg-violet-50";

  return (
    <div className="relative">
      <button
        type="button"
        data-automation-id="nav-mobile-menu-toggle"
        aria-expanded={open}
        aria-controls={menuId}
        aria-label={open ? menuT.close : menuT.open}
        onClick={() => setOpen((v) => !v)}
        className="rounded-full border border-violet-200 bg-white/80 p-2 text-violet-700 shadow-sm hover:bg-violet-50"
      >
        {open ? <X className="h-5 w-5" aria-hidden /> : <Menu className="h-5 w-5" aria-hidden />}
      </button>

      {open && (
        <>
          <button
            type="button"
            aria-label={menuT.close}
            className="fixed inset-0 z-30 bg-slate-900/20"
            onClick={closeMenu}
          />
          <nav
            id={menuId}
            data-automation-id="nav-mobile-menu-panel"
            className="absolute right-0 z-40 mt-2 w-64 rounded-2xl border border-white/80 bg-white/95 p-3 shadow-lg ring-1 ring-violet-100 backdrop-blur"
          >
            <p className="px-4 pb-2 text-xs font-extrabold uppercase tracking-wide text-slate-400">
              {menuT.language}
            </p>
            <div className="px-2 pb-3">
              <LanguageToggle current={lang} />
            </div>

            <div className="my-2 border-t border-slate-100" />

            {status === "signed_in" && user ? (
              <>
                <Link
                  href={`/${lang}/account`}
                  data-automation-id="nav-mobile-account"
                  onClick={closeMenu}
                  className={menuLinkClass}
                >
                  {menuT.account}
                </Link>
                <button
                  type="button"
                  onClick={onSignOut}
                  data-automation-id="nav-mobile-sign-out"
                  className={`${menuLinkClass} w-full text-left`}
                >
                  {authT.signOut}
                </button>
                {errorCode && (
                  <p className="px-4 pt-2 text-xs font-bold text-rose-500">
                    {authT.errors[errorCode] ?? authT.errors.generic}
                  </p>
                )}
              </>
            ) : (
              <>
                <Link
                  href={`/${lang}/auth/sign-in`}
                  data-automation-id="nav-mobile-sign-in"
                  onClick={closeMenu}
                  className={menuLinkClass}
                >
                  {authT.signInCta}
                </Link>
                <Link
                  href={`/${lang}/auth/register`}
                  data-automation-id="nav-mobile-register"
                  onClick={closeMenu}
                  className={`${menuLinkClass} text-violet-700`}
                >
                  {authT.registerCta}
                </Link>
              </>
            )}
          </nav>
        </>
      )}
    </div>
  );
}
