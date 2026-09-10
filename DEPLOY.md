# PyCourse production deployment (Railway)

PyCourse runs as **two services**: a Next.js frontend and a FastAPI backend with
SQLite. Deploy each service from this monorepo using its Dockerfile. The frontend
calls the backend over HTTPS; the backend stores user data in a persistent SQLite
file on a mounted volume.

## Architecture

```
Browser ──► Frontend (Next.js, port 3000)
                │
                │  fetch(..., credentials: "include")
                ▼
            Backend (FastAPI, port 8000)
                │
                ▼
            SQLite file on /data volume
```

| Service  | Dockerfile           | Build context | Public URL example        |
|----------|----------------------|---------------|---------------------------|
| Frontend | `frontend/Dockerfile`| repo root (`.`) | `https://pycourse.up.railway.app` |
| Backend  | `backend/Dockerfile` | repo root (`.`) | `https://pycourse-api.up.railway.app` |

## Railway setup (two services)

### 1. Backend service

1. Create a **new service** → **Deploy from GitHub repo** → select this repo.
2. **Settings → Build**
   - Builder: **Dockerfile**
   - Dockerfile path: `backend/Dockerfile`
   - Root directory: `/` (repo root — required so course markdown is in the build context)
3. **Settings → Volumes**
   - Mount path: `/data`
4. **Settings → Variables** — see [Backend variables](#backend-variables) below.
5. Deploy. Confirm `GET https://<backend-host>/health` returns `"status":"ok"`.

On startup the container runs `alembic upgrade head`, syncs lesson metadata from
markdown, then starts Uvicorn on Railway's `PORT`.

### 2. Frontend service

1. Create a **second service** from the same repo.
2. **Settings → Build**
   - Builder: **Dockerfile**
   - Dockerfile path: `frontend/Dockerfile`
   - Root directory: `/`
3. **Settings → Variables → build-time**
   - Set `NEXT_PUBLIC_BACKEND_URL` to the backend's **public HTTPS URL** (no trailing slash).
   - Railway exposes Dockerfile `ARG`s as build variables when named the same.
4. Deploy. Open the frontend URL in a browser.

### 3. Wire CORS after both URLs exist

Once the frontend has a stable public URL, set on the **backend** service:

```bash
CORS_ORIGINS=https://your-frontend.up.railway.app
```

Redeploy the backend (or restart) so the allowlist picks up the production origin.

For local-style testing alongside production, use a comma-separated list:

```bash
CORS_ORIGINS=https://your-frontend.up.railway.app,http://localhost:3000
```

## Environment variables

### Backend variables

| Variable | Required | Default (local dev) | Purpose |
|----------|----------|---------------------|---------|
| `DATABASE_URL` | prod | `sqlite:///data/pycourse.db` | SQLite path. **Production:** `sqlite:////data/pycourse.db` with volume at `/data`. |
| `CORS_ORIGINS` | prod | *(falls back to `FRONTEND_ORIGIN`)* | Comma-separated browser origins allowed by CORS (credentials). |
| `FRONTEND_ORIGIN` | optional | `http://localhost:3000` | Legacy single origin; used when `CORS_ORIGINS` is unset. Also accepts comma-separated values. |
| `SESSION_COOKIE_SECURE` | prod | `false` | Set `true` in production (HTTPS). Required for auth cookies to be sent. |
| `VERIFY_URL_TEMPLATE` | prod | `http://localhost:3000/en/auth/verify?token={token}` | Link in verification emails; use your frontend URL. |
| `EMAIL_BACKEND` | optional | `console` | `console` (log link) or `smtp`. |
| `EMAIL_FROM` | smtp | `no-reply@pycourse.local` | From address when using SMTP. |
| `SMTP_HOST` | smtp | `localhost` | SMTP server host. |
| `SMTP_PORT` | smtp | `587` | SMTP port. |
| `SMTP_USER` | smtp | — | SMTP username. |
| `SMTP_PASSWORD` | smtp | — | SMTP password. |
| `SMTP_USE_TLS` | smtp | `true` | Enable STARTTLS. |
| `PORT` | auto | `8000` | Set by Railway; Uvicorn binds to this. |

Reserved for future plans (not used by current code): `SESSION_SECRET`, `EXECUTOR_URL`.

### Frontend variables

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `NEXT_PUBLIC_BACKEND_URL` | prod | `http://localhost:8000` | Public backend URL baked into the client bundle at **build time**. |
| `PORT` | auto | `3000` | Set by Railway; Next.js listens on this. |

> **Important:** Changing `NEXT_PUBLIC_BACKEND_URL` requires a **frontend rebuild**.
> CORS changes only require a **backend restart**.

## Helper checklist after deploy

Set these once both Railway URLs are known (replace placeholders):

```bash
# Backend service
DATABASE_URL=sqlite:////data/pycourse.db
CORS_ORIGINS=https://<frontend-host>
SESSION_COOKIE_SECURE=true
VERIFY_URL_TEMPLATE=https://<frontend-host>/en/auth/verify?token={token}
EMAIL_BACKEND=console   # or smtp + SMTP_* when ready

# Frontend service (build variable)
NEXT_PUBLIC_BACKEND_URL=https://<backend-host>
```

Verify:

1. `GET https://<backend-host>/health` → `"status":"ok"`.
2. Frontend loads course pages (markdown SSR).
3. Register / sign-in works (no CORS errors in browser devtools).
4. SQLite persists across backend redeploys (progress survives restart).

## Local development (unchanged)

```bash
# Terminal 1 — backend
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
alembic upgrade head
uvicorn app.main:app --reload --port 8000

# Terminal 2 — frontend
cd frontend && npm install && npm run dev
```

Defaults (`http://localhost:3000` ↔ `http://localhost:8000`) work without extra env files.

## Local Docker smoke test

From the repo root:

```bash
docker compose up --build
```

- Frontend: http://localhost:3000  
- Backend: http://localhost:8000/health  

SQLite data persists in the `backend-data` compose volume.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Browser CORS error | Backend `CORS_ORIGINS` missing frontend URL | Set `CORS_ORIGINS` to exact frontend origin (scheme + host, no path) |
| Auth cookie never set locally | `SESSION_COOKIE_SECURE=true` over HTTP | Use `false` locally; `true` only on HTTPS |
| Frontend API calls wrong host | Stale build | Rebuild frontend with correct `NEXT_PUBLIC_BACKEND_URL` |
| Empty lesson index / sync errors | Build context not repo root | Ensure Railway root directory is `/`, not `backend/` |
| DB resets on redeploy | No volume | Mount Railway volume at `/data` and set `DATABASE_URL=sqlite:////data/pycourse.db` |
