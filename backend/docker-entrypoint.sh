#!/bin/sh
set -e

# A custom start command that bypasses Docker ENTRYPOINT will skip this script.
echo "PyCourse backend entrypoint starting..."

# Production expects a persistent volume mounted at /data for SQLite.
if ! mkdir -p /data; then
  echo "ERROR: failed to create /data directory" >&2
  exit 1
fi

if ! touch /data/.pycourse-write-test 2>/dev/null; then
  echo "ERROR: /data is not writable — mount a persistent volume at /data" >&2
  exit 1
fi
rm -f /data/.pycourse-write-test

cd /app/backend

echo "DATABASE_URL=${DATABASE_URL:-<unset>}"
python -c "from app.core.config import get_settings, sqlite_path_from_url; p=sqlite_path_from_url(get_settings().database_url); print('Resolved SQLite path:', p)"

echo "Ensuring SQLite parent directory exists..."
python -c "from app.core.db import ensure_sqlite_parent_dir; ensure_sqlite_parent_dir()"

echo "Running database migrations..."
alembic upgrade head

echo "Syncing lesson metadata from markdown..."
python -m app.sync.index_lessons

echo "Starting backend on port ${PORT:-8000}..."
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-8000}"
