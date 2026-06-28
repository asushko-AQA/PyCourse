# Regression Tests

All automated test suites live under `tools/mcp/tests`:

- `ui/` — Playwright UI tests via pytest
- `api_db/` — FastAPI API and DB migration/repository tests via pytest
- `smoke-test.ts` — MCP smoke test via `tsx`

## One-time setup

From repo root:

```bash
pip install -r tools/mcp/tests/requirements.txt
pip install -e "backend[dev]"
playwright install chromium
```

Windows PowerShell:

```powershell
pip install -r tools/mcp/tests/requirements.txt
pip install -e "backend[dev]"
playwright install chromium
```

## Run by group

From repo root:

```bash
npm run test:ui
npm run test:api
npm run test:db
npm run test:api-db
npm run test:mcp
```

Equivalent direct commands:

```bash
pytest tools/mcp/tests/ui
pytest tools/mcp/tests/api_db/test_health_api.py
pytest tools/mcp/tests/api_db/test_migrations.py tools/mcp/tests/api_db/test_repositories.py
npm run mcp:smoke-test
```

## Full regression

```bash
npm run test:regression
```

This runs UI + API/DB + MCP smoke tests in sequence.

## UI test behavior

UI fixtures in `tools/mcp/tests/ui/conftest.py` auto-build and serve the frontend on port `3100`.
Set `E2E_BASE_URL` to reuse an already-running app:

```bash
E2E_BASE_URL=http://127.0.0.1:3000 npm run test:ui
```

PowerShell:

```powershell
$env:E2E_BASE_URL = "http://127.0.0.1:3000"; npm run test:ui
```
