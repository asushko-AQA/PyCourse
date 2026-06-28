# 12 — Cross-Channel Identity (Account Linking)

## Goal
Add the identity layer that lets one user account span web and Telegram: an `external_identities` schema mapping Telegram users to accounts, plus secure link/unlink APIs using one-time codes. This is the split of the old cross-channel plan that owns **identity** (the resume UX is 14). It must exist before the bot (13) so the bot can authenticate users against their web account.

## Architectural decisions in effect

> 1. **Stack** — linking APIs in FastAPI; web issues link codes (cookie-auth), bot redeems them (service auth) per 00's token-linking recommendation.
> 2. **Lesson storage** — N/A.
> 3. **Gamification** — once linked, stars/streaks/progress are shared across channels (single user id).
> 4. **Homework checking** — linked identity lets bot submissions attribute to the same account.

## Dependencies
- **07** (sessions/accounts), **04** (`external_identities` table), **11** (contract includes link APIs). Wave 4 — with 11, before 13.
- Consumed by: 13 (bot linking), 14 (handoff/deep links use linked identity).

## Deliverables / Steps
- [ ] `external_identities` schema: `(user_id, provider='telegram', external_id, linked_at)` with uniqueness constraints.
- [ ] `POST /link/telegram/start` (web, authenticated): issue a short-lived one-time link code.
- [ ] `POST /link/telegram/redeem` (bot/service): redeem code + Telegram id → create mapping; reject expired/reused codes.
- [ ] `POST /link/telegram/unlink`: remove mapping (from web or bot).
- [ ] Bot service auth: per-linked-user token model (issued on redeem) used for subsequent API calls.
- [ ] Security: codes single-use + expiring; rate-limit redeem attempts; audit linked/unlinked events.

## Verification
- [ ] Web issues a code → bot redeems → `external_identities` row created → bot calls authenticated endpoints as that user.
- [ ] Expired/reused codes rejected; unlink removes access.
- [ ] A Telegram id cannot map to two accounts (and vice versa per policy).

## Out of scope
- Bot conversation/learning flows (13).
- "Continue where you left off" UX and deep links (14).
- OAuth providers beyond Telegram (future).
