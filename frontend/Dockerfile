# Build from repo root: docker build -f frontend/Dockerfile .
FROM node:22-bookworm-slim AS deps

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

FROM node:22-bookworm-slim AS builder

# Repo layout: /app/course-*, /app/frontend/ — courses must land at /app, not
# under frontend/, so the build-time parser and SSR can find them reliably.
WORKDIR /app
COPY course-* ./

WORKDIR /app/frontend
COPY --from=deps /app/frontend/node_modules ./node_modules
COPY frontend/ ./

ENV PYCOURSE_CONTENT_ROOT=/app

ARG NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
ENV NEXT_PUBLIC_BACKEND_URL=${NEXT_PUBLIC_BACKEND_URL}

# Fail fast when Railway/build context is not the monorepo root.
RUN test -n "$(ls -d /app/course-[0-9]* 2>/dev/null | head -1)" \
  || (echo "ERROR: no course-* directories under /app — build context must be the repo root (.)" >&2 && exit 1)

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
