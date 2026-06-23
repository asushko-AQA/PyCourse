# PyCourse Telegram Bot

A second client for the PyCourse platform, alongside the web app. The bot runs as a
**separate process** and consumes the FastAPI backend (`../backend/`) over HTTP using the
same shared API contract as the frontend — so a learner can switch between web and
Telegram at any point in their progress.

> Architecture source of truth: [documents/plans/platform-architecture.md](../documents/plans/platform-architecture.md)

## Status

Skeleton only. No bot logic yet. Built in later plans:

- **11** — shared API contract (typed client generated from the backend's OpenAPI)
- **12** — cross-channel identity: account linking via a one-time code issued by the web app
- **13** — bot handlers: lesson/quiz/progress/homework flows
- **14** — cross-channel resume UX ("continue where you left off", web↔TG deep links)

## How it talks to the backend

- Telegram → `bot/` process (long-poll or webhook) → HTTP → FastAPI (`backend/`).
- The bot **never** touches SQLite directly; all reads/writes go through backend APIs.
- Auth: per-Telegram-user **token linking**. The user redeems a one-time code from the web
  app; the bot then stores a long-lived service-scoped token per linked user.

## Dev run command (once implemented)

```bash
# from bot/, with the virtualenv active
python -m bot
```

## Key environment variables

See the env-var contract in
[documents/plans/platform-architecture.md](../documents/plans/platform-architecture.md):
`TELEGRAM_BOT_TOKEN`, `BACKEND_URL`.
