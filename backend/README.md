# PyCourse Backend (FastAPI)

The **shared core** of the PyCourse platform. Both the web app (`../frontend/`) and the
Telegram bot (`../bot/`) consume this backend over HTTP — they never touch the database
directly. FastAPI is the **only** writer to SQLite.

> Architecture source of truth: [documents/plans/platform-architecture.md](../documents/plans/platform-architecture.md)

## Status

Plans 04–06 are implemented:

- FastAPI app entrypoint and `/health` endpoint with DB connectivity checks.
- SQLModel schema for metadata tables + user data tables (no lesson body columns).
- Alembic migrations: initial schema (`0001`) + registration/COPPA (`0002`).
- Thin repositories for lessons, users, sessions, progress, and email tokens.
- Markdown → DB lesson sync job (plan 05).
- Email registration + verification: `POST /auth/register`, `GET|POST /auth/verify`
  with Argon2id hashing, single-use expiring tokens, a pluggable email adapter
  (console dev / SMTP stub), and a COPPA parental-consent gate (plan 06).

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

## Auth: registration & verification (plan 06)

```bash
# Register (dev: the verification link is printed to the backend log)
curl -X POST localhost:8000/auth/register \
  -H 'Content-Type: application/json' \
  -d '{"email":"kid@example.com","password":"snakes123"}'

# Under-13 registration requires guardian email + consent
curl -X POST localhost:8000/auth/register \
  -H 'Content-Type: application/json' \
  -d '{"email":"kid@example.com","password":"snakes123","is_minor":true,
       "guardian_email":"parent@example.com","parental_consent":true}'

# Verify (token comes from the emailed link)
curl -X POST localhost:8000/auth/verify \
  -H 'Content-Type: application/json' -d '{"token":"<token>"}'
```

The COPPA / parental-consent decision is documented in
[documents/plans/registration-coppa-decision.md](../documents/plans/registration-coppa-decision.md).

## Tests

```bash
# from backend/, with the venv active
pytest
```

## Key environment variables

See the env-var contract in
[documents/plans/platform-architecture.md](../documents/plans/platform-architecture.md):
`DATABASE_URL`, `EXECUTOR_URL`, `SESSION_SECRET`, `FRONTEND_ORIGIN`.

Plan 06 auth/email settings (all optional, with safe dev defaults):
`PASSWORD_MIN_LENGTH`, `EMAIL_VERIFICATION_TTL_HOURS`, `VERIFY_URL_TEMPLATE`,
`EMAIL_BACKEND` (`console` | `smtp`), `EMAIL_FROM`, and the `SMTP_*` settings.
The frontend reads `NEXT_PUBLIC_BACKEND_URL` to reach these endpoints.

## Data & persistence

- Single SQLite file at `backend/data/pycourse.db` (WAL mode, busy-timeout).
- The file lives on a persistent volume and is **gitignored** — never commit it.
- Backups via file copy / `VACUUM INTO` snapshots.
