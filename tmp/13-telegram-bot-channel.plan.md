# 13 — Telegram Bot Channel

## Goal
Build the `bot/` package as a second client over the shared backend: a separate process that authenticates users via account linking (12), uses the generated Python contract client (11), and delivers lesson browsing, lesson content, quiz answering, progress updates, and homework submission — all sharing the same core as the web app.

## Architectural decisions in effect

> 1. **Stack** — `bot/` runs as a **separate process/service** (long-poll or webhook) and calls FastAPI over HTTP. It contains no business logic that the backend owns.
> 2. **Lesson storage** — bot fetches lesson **content via the API** (content endpoint from 11), which serves from canonical markdown; bot never reads the DB or files directly.
> 3. **Gamification** — bot shows stars/streaks from the shared endpoints (09); completing flows grants the same stars as the web app.
> 4. **Homework checking** — bot forwards `.py` submissions to the homework API (10); execution stays in the external executor.

## Dependencies
- **11** (Python contract client), **12** (linking + service auth), and the APIs in 08/09/10. Wave 4 — after 11 and 12.
- Consumed by: 14 (web↔TG handoff).

## Deliverables / Steps
- [ ] `bot/` skeleton: framework (aiogram/python-telegram-bot), config (`TELEGRAM_BOT_TOKEN`, `BACKEND_URL`), run command.
- [ ] `/start` + linking flow: prompt user to redeem a web-issued link code (12); store the per-user service token.
- [ ] Learning flows: list courses/blocks/lessons, deliver lesson content (paginated/Telegram-formatted), run Quick Check quiz (one question at a time), submit homework `.py`.
- [ ] Progress + stars: update progress via API; show earned stars/streaks; "continue" entry point (basic; deep handoff in 14).
- [ ] Message formatting rules (markdown→Telegram, pagination, code blocks) consistent with lesson structure.
- [ ] Error handling for unlinked users and rate-limited submissions.

## Verification
- [ ] An unlinked user is guided through linking; a linked user can browse and open a lesson.
- [ ] Answering a quiz in the bot updates the same progress/stars visible on the web.
- [ ] Submitting homework via bot runs through the executor and grants the homework star.
- [ ] Bot makes only API calls — no direct DB/file access.

## Out of scope
- Identity linking internals (12) and contract generation (11).
- Last-position resume/deep-link handoff polish (14).
- Bot-only gamification that diverges from the shared model.
