# Build from repo root: docker build -f backend/Dockerfile .
FROM python:3.12-slim-bookworm

WORKDIR /app/backend

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATABASE_URL=sqlite:////data/pycourse.db

# Mount point for Railway persistent volume (entrypoint also verifies at runtime).
RUN mkdir -p /data && chmod 1777 /data

COPY backend/pyproject.toml backend/README.md ./
COPY backend/app ./app
COPY backend/alembic ./alembic
COPY backend/alembic.ini ./

# Course markdown for the sync job — same fetch/overlay logic as the frontend.
WORKDIR /app
ARG RAILWAY_GIT_BRANCH=main
ARG RAILWAY_GIT_COMMIT_SHA=
ARG GIT_REPO=https://github.com/asushko-AQA/PyCourse.git
COPY scripts/docker/fetch-course-dirs.sh /tmp/fetch-course-dirs.sh
COPY . /tmp/buildctx/
RUN chmod +x /tmp/fetch-course-dirs.sh \
  && RAILWAY_GIT_BRANCH="${RAILWAY_GIT_BRANCH}" \
       RAILWAY_GIT_COMMIT_SHA="${RAILWAY_GIT_COMMIT_SHA}" \
       GIT_REPO="${GIT_REPO}" \
       /tmp/fetch-course-dirs.sh /app /tmp/buildctx \
  && rm -rf /tmp/buildctx /tmp/fetch-course-dirs.sh

WORKDIR /app/backend

RUN pip install --no-cache-dir .

COPY backend/docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
