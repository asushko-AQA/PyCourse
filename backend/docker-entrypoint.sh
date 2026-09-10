#!/bin/sh
set -e

# Railway mounts a persistent volume at /data for SQLite. Ensure the directory
# exists and is writable before Alembic opens the database file.
if ! mkdir -p /data; then
  echo "ERROR: failed to create /data directory" >&2
  exit 1
fi

if [ ! -w /data ]; then
  echo "ERROR: /data is not writable — check the Railway volume mount at /data" >&2
  exit 1
fi

cd /app/backend

echo "Running database migrations..."
alembic upgrade head

echo "Syncing lesson metadata from markdown..."
python -m app.sync.index_lessons

echo "Starting backend on port ${PORT:-8000}..."
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-8000}"
