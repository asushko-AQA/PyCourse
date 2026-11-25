# PyCourse production deployment

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

| Service  | Dockerfile            | Build context |
|----------|-----------------------|---------------|
| Frontend | `frontend/Dockerfile` | repo root (`.`) |
| Backend  | `backend/Dockerfile`  | repo root (`.`) |

## Deploy with Docker

Build both images from the **repository root** so course markdown is in the
build context. Do not set the build context to `frontend/` or `backend/`
alone.

1. **Backend**
   - Dockerfile: `backend/Dockerfile`
   - Mount a persistent volume at `/data`
   - Leave the container entrypoint unchanged so `docker-entrypoint.sh` runs
     (`alembic upgrade head`, lesson sync, then Uvicorn)
   - Set the [backend variables](#backend-variables) below
   - Confirm `GET https://<backend-host>/health` returns `"status":"ok"`

2. **Frontend**
   - Dockerfile: `frontend/Dockerfile`
   - At **build time**, set `NEXT_PUBLIC_BACKEND_URL` to the backend's public
     HTTPS URL (no trailing slash)
   - Deploy and open the frontend URL

3. **Wire CORS after both URLs exist**

   Once the frontend has a stable public URL, set on the backend service:

   ```bash
   CORS_ORIGINS=https://your-frontend.example.com
   ```

   Restart the backend so the allowlist picks up the production origin.

   For local-style testing alongside production, use a comma-separated list:

   ```bash
   CORS_ORIGINS=https://your-frontend.example.com,http://localhost:3000
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
| `PORT` | auto | `8000` | Set by the host; Uvicorn binds to this. |

Reserved for future plans (not used by current code): `SESSION_SECRET`, `EXECUTOR_URL`.

### Frontend variables

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `NEXT_PUBLIC_BACKEND_URL` | prod | `http://localhost:8000` | Public backend URL baked into the client bundle at **build time**. |
| `PORT` | auto | `3000` | Set by the host; Next.js listens on this. |

> **Important:** Changing `NEXT_PUBLIC_BACKEND_URL` requires a **frontend rebuild**.
> CORS changes only require a **backend restart**.

## Helper checklist after deploy

Set these once both public URLs are known (replace placeholders):

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
| Frontend build: no `course-*` under `/app` | Narrow build context omitted course markdown | Build from repo root. Dockerfiles clone course markdown when it is missing from the context |
| Empty lesson index / sync errors | Build context not repo root | Keep the Docker build context at repo root `/`, not `backend/` |
| Backend SQLite `unable to open database file` | Custom start command bypasses entrypoint, or Alembic used the ini dev path | Leave the image entrypoint in place; set `DATABASE_URL=sqlite:////data/pycourse.db`; mount a volume at `/data` |
| DB resets on redeploy | No volume | Mount a persistent volume at `/data` and set `DATABASE_URL=sqlite:////data/pycourse.db` |
