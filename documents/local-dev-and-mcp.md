# Local development and MCP inspection

This guide covers running the PyCourse web frontend locally and using the project MCP server in Cursor to inspect lesson content and observe agent tool activity.

## Prerequisites

- **Node.js** 20+ and npm
- **Python** 3.12+ (for `quiz_hash` tool)
- **Cursor** with MCP enabled for this workspace

One-time setup:

```bash
cd frontend
npm install

cd ../tools/mcp
npm install
```

## Run the project (frontend)

From the repo root:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). The frontend reads lesson markdown from the repo at build/dev time and stores learner progress in `localStorage`.

Other root scripts:

| Command | Purpose |
|---------|---------|
| `npm run build` | Production build |
| `npm run lint` | ESLint (frontend) |
| `npm run validate-content` | CLI content validation |
| `npm run mcp` | Start the MCP server (stdio; used by Cursor) |
| `npm run mcp:check` | Typecheck MCP server |

## Open MCP in Cursor

1. Open this repository as the Cursor workspace (`PyCourse/`).
2. Confirm [`.cursor/mcp.json`](../.cursor/mcp.json) defines the `pycourse` server.
3. In Cursor: **Settings → MCP** (or the MCP panel) and enable **pycourse**.
4. Restart MCP if needed after `tools/mcp` dependency changes.

The server launches via:

```json
"command": "npm",
"args": ["run", "mcp"],
"cwd": "${workspaceFolder}"
```

## MCP tools (for agents)

| Tool | Description |
|------|-------------|
| `validate_content` | Parse lessons and report fatal problems + schema-v2 warnings. Optional filters: `course`, `block`, `lesson` (substring match). |
| `quiz_hash` | Canonical quiz hashes via `tools/apply_lesson_quizzes.py --hash`. Optional `lesson` filter. |
| `inspect_lesson` | Deep inspection of one lesson folder: sections, quiz parity, starter/solution files. Requires `lesson_path`. |
| `agent_run_logs` | Read recent MCP tool invocation logs (for observing what agents ran). |

### Example agent prompts

- “Use `inspect_lesson` on `course-1-python-basics/block-1-meeting-your-computer/lesson-1-1-installing-python`.”
- “Run `validate_content` with `course` = `course-2-web-apps` and summarize warnings.”
- “Call `quiz_hash` for `lesson-2-1-variables` and list mismatches.”
- “Show the last 10 entries from `agent_run_logs`.”

## Observe agent feature realization

Every MCP tool call is appended to a local JSONL log:

```
documents/agent-runs/mcp-tools.jsonl
```

Each line is a JSON object:

```json
{
  "timestamp": "2026-06-28T15:30:00.000Z",
  "tool": "inspect_lesson",
  "args": { "lesson_path": "course-1-python-basics/..." },
  "status": "success",
  "durationMs": 42,
  "summary": "Lesson lesson-1-1 has 0 issue(s)"
}
```

- **In Cursor:** ask the agent to call `agent_run_logs`, or open the file directly.
- **On disk:** `Get-Content documents/agent-runs/mcp-tools.jsonl -Tail 20` (PowerShell) or `tail documents/agent-runs/mcp-tools.jsonl` (macOS/Linux).

Log files are gitignored; the `documents/agent-runs/` folder is for local observability only.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| MCP server won’t start | Run `npm install` in `tools/mcp/`; then `npm run mcp:check` |
| `quiz_hash` fails | Ensure `python` is on PATH; run `python tools/apply_lesson_quizzes.py --hash` manually |
| Lesson not found | Pass full path `course-…/block-…/lesson-…` or a unique lesson slug |
| Empty logs | Logs appear after the first MCP tool call in a session |

## Related docs

- [AGENTS.md](../AGENTS.md) — lesson authoring and verification workflow
- [documents/README.md](README.md) — planning notes and verify-lesson filing
- [platform-architecture.md](plans/platform-architecture.md) — full stack (backend/bot) — not required for this minimal setup
