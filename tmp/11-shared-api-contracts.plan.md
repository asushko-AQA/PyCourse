# 11 — Shared API Contracts (OpenAPI / Typed Client)

## Goal
Establish a single source of truth for the backend's HTTP surface so the Next.js frontend and the Telegram bot consume the **same structure**: an OpenAPI schema generated from FastAPI plus generated typed clients (TypeScript for frontend, Python for bot). This formalizes the "both channels share one core" requirement before the bot is built.

## Architectural decisions in effect

> 1. **Stack** — FastAPI auto-generates OpenAPI; **frontend + bot** are both generated clients of it. No hand-maintained duplicate types.
> 2. **Lesson storage** — contract exposes lesson **metadata** + content-fetch endpoints (bot needs lesson text via API; frontend reads markdown at build time but uses the API for progress/stars).
> 3. **Gamification** — stars/streaks/achievements endpoints are part of the shared contract.
> 4. **Homework checking** — submission endpoints are part of the shared contract.

## Dependencies
- **04–10** (the endpoints to be contracted: auth, progress, stars, homework). Wave 4 — with 12, before 13.
- Consumed by: 13 (bot client), and frontend refactors in 08/09.

## Deliverables / Steps
- [ ] Ensure all FastAPI routes have explicit request/response Pydantic models + tags so OpenAPI is complete and stable.
- [ ] Publish `openapi.json` to `shared/` (committed artifact) generated from the running app.
- [ ] Generate a **TypeScript client** for the frontend (e.g. openapi-typescript / orval) and a **Python client** for the bot.
- [ ] Versioning + drift check: CI regenerates the contract and fails if `shared/openapi.json` is stale.
- [ ] Document the lesson-content delivery endpoint(s) the bot will use (text/sections by lesson id).

## Verification
- [ ] `openapi.json` covers every endpoint with typed schemas; no untyped `Any` bodies.
- [ ] Generated TS client compiles in `frontend/`; generated Python client imports in `bot/`.
- [ ] CI drift check fails on an intentional schema change until the contract is regenerated.

## Out of scope
- Implementing new endpoints (owned by 04–10).
- Bot conversation logic (13).
- Public/external API publishing (internal contract only).
