# Plan: Registration & COPPA / Parental-Consent Decision

**Status:** implemented
**Date:** 2026-06-30
**Target:** Backend auth (plan 06 — Email Registration Flow)
**Supersedes:** (none)

See [documents/plans/README.md](README.md) for the plan registry and
[platform-architecture.md](platform-architecture.md) for the binding decisions.

## Goal

Record how the registration flow handles a learner audience that is **11+** and
therefore includes children **under 13**, who in the United States are covered by
**COPPA** (Children's Online Privacy Protection Act). The aim is a clear, minimal
gate — not a full identity-verification system.

## Decision

1. **Self-declared age gate.** The register form includes an *"I am under 13"*
   checkbox (`is_minor` in the API payload). We do **not** collect a date of birth
   or store any more personal data than necessary.
2. **Guardian email + explicit consent for minors.** When `is_minor` is true the
   payload **must** include a `guardian_email` and `parental_consent: true`.
   Registration is rejected (`422 parental_consent_required`) otherwise.
3. **Verification email goes to the guardian.** For a minor, the confirmation
   link is sent to the guardian's address, so an adult performs the email
   confirmation step. For adults it goes to the learner's own address.
4. **What we persist.** On the `users` row: `is_minor`, `guardian_email`,
   `parental_consent`, and `parental_consent_at` (timestamp of consent). No extra
   PII. Passwords are stored only as Argon2id hashes.
5. **Account is inert until verified.** Registration creates the account but
   `email_verified_at` stays null until the (guardian-confirmed for minors) link
   is redeemed. Sign-in gating on verification is plan 07.

## Why this shape

- COPPA requires *verifiable parental consent* before collecting a child's
  personal information. A guardian-email round-trip is a lightweight, widely-used
  approximation appropriate for an educational MVP; it is intentionally easy to
  strengthen later (e.g. a signed consent form or a small charge) without schema
  changes — the `parental_consent*` columns already exist.
- Keeping the gate **self-declared** avoids collecting birth dates we would then
  have to protect.

## Where it lives in code

| Concern | Location |
|---------|----------|
| Request fields | `backend/app/schemas/auth.py` (`RegisterRequest`) |
| Gate enforcement | `backend/app/services/auth_service.py` (`ParentalConsentRequired`) |
| Persisted columns | `backend/app/models/tables.py` (`User`) + migration `0002_registration_coppa` |
| Tests | `backend/tests/test_coppa.py` |

## Out of scope / future

- Stronger verifiable-consent mechanisms (signed form, micro-charge, ID checks).
- Regional variants (e.g. GDPR-K age thresholds differ by member state).
- Data-deletion / guardian dashboard (future privacy work).
