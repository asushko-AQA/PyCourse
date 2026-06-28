# PyCourse Backend (FastAPI)

The **shared core** of the PyCourse platform. Both the web app (`../frontend/`) and the
Telegram bot (`../bot/`) consume this backend over HTTP — they never touch the database
directly. FastAPI is the **only** writer to SQLite.

> Architecture source of truth: [documents/plans/platform-architecture.md](../documents/plans/platform-architecture.md)

## Status

Plan 04 core is implemented:

- FastAPI app entrypoint and `/health` endpoint with DB connectivity checks.
- SQLModel schema for metadata tables + user data tables (no lesson body columns).
- Alembic migrations with initial schema (`0001_initial_schema`).
- Thin repositories for lessons, users, sessions, and progress.
- Core API/DB tests (migrations + repositories + health endpoint).

## Layout

```
backend/
├── app/                # routers, services, repositories, models (added in 04+)
├── data/pycourse.db    # SQLite file — gitignored, on a persistent volume
├── pyproject.toml      # added in 04
└── README.md
```

## Setup

```bash
# from backend/
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -e ".[dev]"
```

## Dev run command

```bash
uvicorn app.main:app --reload --port 8000
```

## Migrations

```bash
# from backend/
alembic upgrade head
alembic downgrade -1
```

## Markdown sync (plan 05)

```bash
# from backend/
python -m app.sync.index_lessons

# drift check only (no writes)
python -m app.sync.index_lessons --check
```

Optional flags:
- `--root <path>` to index a different content root.
- `--database-url <url>` to target another database for one run.

## Tests

```bash
# from repo root
pytest tools/mcp/tests/api_db
```

## Key environment variables

See the env-var contract in
[documents/plans/platform-architecture.md](../documents/plans/platform-architecture.md):
`DATABASE_URL`, `EXECUTOR_URL`, `SESSION_SECRET`, `FRONTEND_ORIGIN`.

## Data & persistence

- Single SQLite file at `backend/data/pycourse.db` (WAL mode, busy-timeout).
- The file lives on a persistent volume and is **gitignored** — never commit it.
- Backups via file copy / `VACUUM INTO` snapshots.
