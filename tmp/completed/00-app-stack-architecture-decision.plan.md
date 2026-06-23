# 00 — App Stack & Architecture Decision

## Goal
Record the four binding architectural decisions for the PyCourse platform and lock in the monorepo layout, process topology, and session transport that every later plan builds on. This plan writes **no application code** — it produces the decision record and skeleton folder/README scaffolding so that `backend/`, `frontend/`, `bot/`, and shared course content have an agreed home before any wiring begins.

## Architectural decisions in effect

> These four binding decisions apply to every plan in `tmp/`:
> 1. **Stack** — Python **FastAPI** backend (shared core) + existing **Next.js** frontend in `frontend/`. Both the web app and the Telegram bot consume the backend over HTTP; the bot runs as a separate process/service.
> 2. **Lesson storage** — Markdown in git is **canonical**. SQLite stores only **metadata** (lesson ids, ordering, block/course refs, quiz hashes, homework/checker refs) and user data (accounts, progress, stars, streaks). Full lesson bodies are **never** stored in the DB; a sync job indexes markdown → DB.
> 3. **Gamification** — **Stars + streaks** are the primary model (3 stars/lesson: reading=1, homework=1, perfect quiz=1; 12h replay cooldown; 3/5/7-day streak achievements). The legacy XP/levels system is **migrated/retired**, not kept alongside.
> 4. **Homework checking** — Student `.py` runs on an **external executor API** (self-hosted **Piston** default, Judge0 CE alternative). Untrusted code is **never** executed inside the FastAPI process.

## Dependencies
- None. This is the root plan; **every other plan depends on 00.**

## Monorepo layout (target)

```
PyCourse/
├── course-1-python-basics/        # canonical markdown (unchanged)
├── course-2-web-apps/             # canonical markdown (unchanged)
├── course-3-game-dev/             # canonical markdown (built in 16)
├── frontend/                      # existing Next.js 15 app (web client)
├── backend/                       # NEW — FastAPI app (shared core)
│   ├── app/                       #   routers, services, repositories, models
│   ├── data/pycourse.db           #   SQLite file (persisted volume; gitignored)
│   └── pyproject.toml
├── bot/                           # NEW — Telegram bot process (HTTP client of backend)
├── shared/                        # cross-channel assets + generated API contract
└── tmp/                           # these plans
```

## Process topology
- **Web**: browser → Next.js (`frontend/`) → HTTP → FastAPI (`backend/`).
- **Bot**: Telegram → `bot/` process (long-poll or webhook) → HTTP → FastAPI (`backend/`).
- FastAPI is the **only** writer to SQLite. Frontend and bot never touch the DB directly.
- Three independently startable services: `frontend` (node), `backend` (uvicorn), `bot` (python). Document `dev` run commands for each.

## Session transport recommendation
- **Web**: HTTP-only, `Secure`, `SameSite=Lax` cookies holding an opaque session id (server-side session row). No tokens in `localStorage`.
- **Bot**: per-Telegram-user **token linking** (one-time code issued by web → redeemed by bot) → bot stores a long-lived service-scoped token per linked user. Detailed in 12.
- CORS: backend allows the frontend origin with credentials; bot uses bearer/service auth, not cookies.

## SQLite persistence / deployment notes
- Single SQLite file at `backend/data/pycourse.db`, mounted on a **persistent volume** (not the container's ephemeral fs). `gitignore` the file.
- Enable WAL mode + busy-timeout for concurrent reads. Single-writer (FastAPI) keeps contention low.
- Backups: periodic file copy / `VACUUM INTO` snapshot. Document restore steps.
- Migration path note: schema designed so a later move to Postgres is mechanical (SQLModel/SQLAlchemy abstraction in 04).

## Deliverables / Steps
- [ ] Write this decision record and link it from `AGENTS.md` (Architecture section) as the canonical source.
- [ ] Create `backend/` and `bot/` folder skeletons with `README.md` only (no app logic yet).
- [ ] Add `backend/data/` and `*.db` to `.gitignore`.
- [ ] Document the three `dev` run commands (frontend/backend/bot) and the env-var contract (`BACKEND_URL`, `DATABASE_URL`, `TELEGRAM_BOT_TOKEN`, executor URL).
- [ ] Record session-transport decision (cookies for web, token-linking for bot) and CORS policy.
- [ ] Record SQLite persistence + backup strategy.

## Verification
- [ ] `AGENTS.md` references this plan as the architecture source of truth.
- [ ] Folder skeletons exist with READMEs; `.gitignore` excludes the DB file and volumes.
- [ ] A reviewer can answer, from this doc alone: where does the bot run, who writes to the DB, how do web/bot authenticate, where does lesson content live.

## Out of scope
- Any FastAPI route, table, or bot handler implementation (see 04+, 13).
- Choosing a hosting provider / writing deploy manifests (future stretch; only persistence requirements noted here).
- Postgres migration (noted as a design constraint only).
