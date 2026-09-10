# Build from repo root: docker build -f backend/Dockerfile .
FROM python:3.12-slim-bookworm

WORKDIR /app/backend

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATABASE_URL=sqlite:////data/pycourse.db

# Mount point for Railway persistent volume (entrypoint also mkdir -p at runtime).
RUN mkdir -p /data && chmod 1777 /data

COPY backend/pyproject.toml backend/README.md ./
COPY backend/app ./app
COPY backend/alembic ./alembic
COPY backend/alembic.ini ./

# Course markdown lives beside backend/; required for the sync job.
COPY course-* /app/

RUN pip install --no-cache-dir .

COPY backend/docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
