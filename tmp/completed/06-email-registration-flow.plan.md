# 06 — Email Registration Flow

## Goal
Implement account creation on the FastAPI backend: `register` with strong validation and hashed passwords, plus email-verification tokens with expiry. Provide a dev-console email adapter and a production-provider abstraction. Because the audience is 11+, document the COPPA / parental-consent consideration and how the flow accommodates it.

## Architectural decisions in effect

> 1. **Stack** — endpoints live in **FastAPI** (`backend/`); the Next.js frontend renders register/verify UI and calls the API over HTTP with credentials.
> 2. **Lesson storage** — N/A to content; uses the `users` / `email_verification_tokens` tables from 04.
> 3. **Gamification** — verified accounts are the identity that stars/streaks (09) attach to.
> 4. **Homework checking** — N/A.

## Dependencies
- **04** (users + token tables), **00** (session/cookie + CORS policy). Wave 2 (with 07).
- Consumed by: 07 (sign-in requires verified email), 08 (progress per user), 12 (identity linking).

## Deliverables / Steps
- [ ] `POST /auth/register`: validate email + password strength, reject duplicates, hash password (argon2/bcrypt), store `created_at`.
- [ ] Issue email-verification token (single-use, expiring) → `email_verification_tokens`.
- [ ] `GET/POST /auth/verify`: validate token, set `email_verified_at`, reject expired/used tokens.
- [ ] **Email adapter abstraction**: `EmailSender` interface with a **dev console adapter** (prints verification link to logs) and a prod provider stub (SMTP/transactional API) selected by env.
- [ ] Frontend register + "check your email" + verify-landing states.
- [ ] **COPPA / parental-consent note**: for under-13 users, document a parental-email/consent field or gate; record decision (e.g. capture guardian email, consent checkbox) without over-engineering.

## Verification
- [ ] Register → token row created → dev console prints link → verify sets `email_verified_at`.
- [ ] Duplicate email and weak password rejected with clear errors; passwords stored only as hashes.
- [ ] Expired/reused token rejected.
- [ ] Parental-consent field/decision documented and present in the register payload.

## Out of scope
- Sign-in/session issuance (07).
- Password reset / OAuth (future).
- Choosing a specific email vendor (abstraction only).
