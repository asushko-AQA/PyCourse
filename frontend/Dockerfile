# Build from repo root: docker build -f frontend/Dockerfile .
FROM node:22-bookworm-slim AS deps

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

FROM node:22-bookworm-slim AS builder

# Repo layout: /app/course-*, /app/frontend/
WORKDIR /app

ARG RAILWAY_GIT_BRANCH=main
ARG RAILWAY_GIT_COMMIT_SHA=
ARG GIT_REPO=https://github.com/asushko-AQA/PyCourse.git

# Railway watchPatterns such as frontend/** can omit course-* from the build
# archive. fetch-course-dirs.sh clones them when missing, then overlays any
# course trees present in the build context (local docker compose).
COPY scripts/docker/fetch-course-dirs.sh /tmp/fetch-course-dirs.sh
COPY . /tmp/buildctx/
RUN chmod +x /tmp/fetch-course-dirs.sh \
  && RAILWAY_GIT_BRANCH="${RAILWAY_GIT_BRANCH}" \
       RAILWAY_GIT_COMMIT_SHA="${RAILWAY_GIT_COMMIT_SHA}" \
       GIT_REPO="${GIT_REPO}" \
       /tmp/fetch-course-dirs.sh /app /tmp/buildctx \
  && rm -rf /tmp/buildctx /tmp/fetch-course-dirs.sh

WORKDIR /app/frontend
COPY --from=deps /app/frontend/node_modules ./node_modules
COPY frontend/ ./

ENV PYCOURSE_CONTENT_ROOT=/app

ARG NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
ENV NEXT_PUBLIC_BACKEND_URL=${NEXT_PUBLIC_BACKEND_URL}

RUN npm run build

FROM node:22-bookworm-slim AS runner

WORKDIR /app/frontend

ENV NODE_ENV=production \
    PORT=3000 \
    PYCOURSE_CONTENT_ROOT=/app

RUN addgroup --system --gid 1001 nodejs \
    && adduser --system --uid 1001 --ingroup nodejs nextjs

COPY --from=builder /app/frontend/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/frontend/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/frontend/.next/static ./.next/static
COPY --from=builder --chown=nextjs:nodejs /app/course-* /app/

USER nextjs

EXPOSE 3000
CMD ["node", "server.js"]
