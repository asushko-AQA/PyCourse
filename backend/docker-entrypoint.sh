#!/bin/sh
set -e

cd /app/backend

echo "Running database migrations..."
alembic upgrade head

echo "Syncing lesson metadata from markdown..."
python -m app.sync.index_lessons

echo "Starting backend on port ${PORT:-8000}..."
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-8000}"
