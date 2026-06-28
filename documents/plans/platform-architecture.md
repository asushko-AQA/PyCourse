# Plan: PyCourse Platform Architecture (Decision Record)

**Status:** approved
**Date:** 2026-06-24
**Target:** Whole platform (web app + Telegram bot + backend)
**Supersedes:** (none)

This is the **canonical architecture source of truth** for turning PyCourse from a
markdown-only course repo into a gamified, multi-channel learning platform. Every
platform plan in `tmp/` (00–17) builds on the decisions recorded here. Implementation
detail lands in the later plans referenced below.

See [documents/plans/README.md](README.md) for the full plan registry.

## Goal

A reviewer should be able to answer, from this document alone:
where does the bot run, who writes to the database, how do the web app and bot
authenticate, and where does lesson content live.

## Binding architectural decisions

These four decisions apply to **every** platform plan and must not be re-litigated
inside a single plan:

1. **Stack** — Python **FastAPI** backend (the shared core) + the existing **Next.js**
   frontend in `frontend/`. Both the web app and the Telegram bot consume the backend
   over HTTP. The bot runs as a **separate process/service**.
2. **Lesson storage** — Markdown in git is **canonical**. SQLite stores only
   **metadata** (lesson ids, ordering, block/course refs, quiz hashes, homework/checker
   refs) and **user data** (accounts, progress, stars, streaks). Full lesson bodies are
   **never** stored in the DB; a sync job indexes markdown → DB (plan 05).
3. **Gamification** — **Stars + streaks** are the primary model (3 stars/lesson:
   reading = 1, homework = 1, perfect quiz = 1; 12h replay cooldown; 3/5/7-day streak
   achievements). The legacy XP/levels system is **migrated/retired**, not kept
   alongside (plan 09).
4. **Homework checking** — Student `.py` runs on an **external executor API**
   (self-hosted **Piston** default, **Judge0 CE** alternative). Untrusted code is
   **never** executed inside the FastAPI process (plan 10).

## Monorepo layout (target)

```
PyCourse/
├── course-1-python-basics/        # canonical markdown (unchanged)
├── course-1_5-leveling-up/        # bridge course markdown (built in 17)
├── course-2-web-apps/             # canonical markdown (unchanged)
├── course-3-game-dev/             # canonical markdown (built in 16)
├── frontend/                      # existing Next.js app (web client)
├── backend/                       # FastAPI app (shared core)
│   ├── app/                       #   routers, services, repositories, models
│   ├── data/pycourse.db           #   SQLite file (persisted volume; gitignored)
│   └── pyproject.toml
├── bot/                           # Telegram bot process (HTTP client of backend)
├── shared/                        # cross-channel assets + generated API contract
├── documents/                     # planning notes (this file)
└── tmp/                           # atomic plans (00–17)
```

## Process topology

- **Web**: browser → Next.js (`frontend/`) → HTTP → FastAPI (`backend/`).
- **Bot**: Telegram → `bot/` process (long-poll or webhook) → HTTP → FastAPI (`backend/`).
- FastAPI is the **only** writer to SQLite. The frontend and bot **never** touch the DB directly.
- Three independently startable services: `frontend` (node), `backend` (uvicorn), `bot` (python).

### Dev run commands (target)

| Service | Working dir | Command |
|---------|-------------|---------|
| Backend | `backend/` | `uvicorn app.main:app --reload --port 8000` |
| Frontend | `frontend/` | `npm run dev` |
| Bot | `bot/` | `python -m bot` |

### Environment-variable contract

| Variable | Used by | Purpose |
|----------|---------|---------|
| `BACKEND_URL` | frontend, bot | Base URL of the FastAPI backend |
| `DATABASE_URL` | backend | SQLite path (e.g. `sqlite:///data/pycourse.db`) |
| `TELEGRAM_BOT_TOKEN` | bot | Telegram Bot API token |
| `EXECUTOR_URL` | backend | Piston/Judge0 executor endpoint |
| `SESSION_SECRET` | backend | Signs/derives opaque session ids |
| `FRONTEND_ORIGIN` | backend | Allowed CORS origin (credentials) |

All secrets live in `.env` files (gitignored), never committed.

## Session transport

- **Web**: HTTP-only, `Secure`, `SameSite=Lax` cookies holding an **opaque session id**
  (server-side session row). No tokens in `localStorage`.
- **Bot**: per-Telegram-user **token linking** — a one-time code issued by the web app is
  redeemed by the bot, after which the bot stores a long-lived service-scoped token per
  linked user (detailed in plan 12).
- **CORS**: backend allows the frontend origin **with credentials**; the bot uses
  bearer/service auth, not cookies.

## SQLite persistence & deployment notes

- Single SQLite file at `backend/data/pycourse.db`, on a **persistent volume** (not the
  container's ephemeral filesystem). The file is **gitignored**.
- Enable **WAL mode** + busy-timeout for concurrent reads. Single-writer (FastAPI) keeps
  contention low.
- **Backups**: periodic file copy / `VACUUM INTO` snapshot. Restore = stop backend, swap
  file, restart.
- **Migration path**: schema is designed (via SQLModel/SQLAlchemy in plan 04) so a later
  move to Postgres is mechanical.

## Steps (this plan)

- [x] Write this decision record and link it from `AGENTS.md` as the canonical source.
- [x] Create `backend/` and `bot/` folder skeletons with `README.md` only (no app logic).
- [x] Add `backend/data/` and `*.db` to `.gitignore`.
- [x] Document the three dev run commands and the env-var contract (above).
- [x] Record the session-transport decision (cookies for web, token-linking for bot) and CORS policy.
- [x] Record the SQLite persistence + backup strategy.

## Dependencies

None. This is the root decision; **every other platform plan depends on it.**

## Open questions

- Hosting provider and deploy manifests (deferred; only persistence requirements fixed here).

## Done criteria

- `AGENTS.md` references this document as the architecture source of truth.
- `backend/` and `bot/` skeletons exist with READMEs; `.gitignore` excludes the DB file.
- The reviewer questions in **Goal** are answerable from this document alone.

## Out of scope

- Any FastAPI route, table, or bot handler implementation (plans 04+, 13).
- Choosing a hosting provider / writing deploy manifests (future stretch).
- Postgres migration (a design constraint only).
