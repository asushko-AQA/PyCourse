# PyCourse Backend (FastAPI)

The **shared core** of the PyCourse platform. Both the web app (`../frontend/`) and the
Telegram bot (`../bot/`) consume this backend over HTTP — they never touch the database
directly. FastAPI is the **only** writer to SQLite.

> Architecture source of truth: [documents/plans/platform-architecture.md](../documents/plans/platform-architecture.md)

## Status

Skeleton only. No application code yet — routers, models, repositories, and the SQLite
schema arrive in later plans:

- **04** — SQLite schema + migrations + repository interfaces (SQLModel/SQLAlchemy)
- **05** — markdown → DB sync job (lesson metadata is indexed, never lesson bodies)
- **06 / 07** — email registration, sign-in/sign-out, sessions
- **08** — progress sync APIs
- **09** — stars + streaks
- **10** — homework checking via external executor (Piston/Judge0)
- **11** — generated OpenAPI contract for the frontend and bot

## Planned layout

```
backend/
├── app/                # routers, services, repositories, models (added in 04+)
├── data/pycourse.db    # SQLite file — gitignored, on a persistent volume
├── pyproject.toml      # added in 04
└── README.md
```

## Dev run command (once implemented)

```bash
# from backend/, with the virtualenv active
uvicorn app.main:app --reload --port 8000
```

## Key environment variables

See the env-var contract in
[documents/plans/platform-architecture.md](../documents/plans/platform-architecture.md):
`DATABASE_URL`, `EXECUTOR_URL`, `SESSION_SECRET`, `FRONTEND_ORIGIN`.

## Data & persistence

- Single SQLite file at `backend/data/pycourse.db` (WAL mode, busy-timeout).
- The file lives on a persistent volume and is **gitignored** — never commit it.
- Backups via file copy / `VACUUM INTO` snapshots.
