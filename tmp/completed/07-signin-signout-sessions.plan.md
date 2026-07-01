# 07 — Sign-In / Sign-Out & Sessions

## Goal
Implement secure login, logout, and session bootstrap on FastAPI using server-side sessions delivered via HTTP-only cookies (per 00). Sign-out must revoke the session row and clear the client credential. This plan folds in an **end-to-end auth integration checkpoint**: register → verify → sign-in → sign-out → 401.

## Architectural decisions in effect

> 1. **Stack** — auth endpoints in FastAPI; web uses **HTTP-only `Secure` `SameSite=Lax` cookies** holding an opaque session id (server-side `sessions` table). No tokens in `localStorage`.
> 2. **Lesson storage** — N/A.
> 3. **Gamification** — an authenticated session is the precondition for server-side stars/streaks (09) and progress (08).
> 4. **Homework checking** — N/A.

## Dependencies
- **06** (verified accounts), **04** (`sessions` table). Wave 2.
- Consumed by: 08 (progress reads session), 09, 10, 12, 13 (bot service auth references this model).

## Deliverables / Steps
- [ ] `POST /auth/sign-in`: verify credentials + `email_verified_at` guard; create session row; set HTTP-only cookie. Rate-limit attempts.
- [ ] `POST /auth/sign-out`: revoke/delete session row; clear cookie; idempotent.
- [ ] `GET /auth/session` (bootstrap): returns current user or 401; frontend calls on app start.
- [ ] FastAPI dependency/guard for protected routes; clear 401 contract.
- [ ] Frontend auth store: bootstrap on load, sign-in/out flows, clear local progress cache on sign-out.
- [ ] **Auth integration checkpoint** (automated test): register → verify → sign-in (cookie set) → access protected route (200) → sign-out → same route returns **401**.

## Verification
- [ ] Unverified user cannot sign in.
- [ ] Cookie is HTTP-only/Secure/SameSite; not readable by JS.
- [ ] Sign-out revokes session server-side (reusing old cookie → 401).
- [ ] The full register→verify→signin→signout→401 checkpoint passes in CI.

## Out of scope
- Registration/verification (06).
- Bot token linking (12) — references this session model but is separate.
- Refresh-token rotation / multi-device session management (future).
