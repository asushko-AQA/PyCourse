# Documents

Planning and notes for PyCourse — not student-facing content.

Use this folder to collect ideas, plans, and issues before they become lessons or curriculum changes.

## Structure

| Folder | Purpose |
|--------|---------|
| [ideas/](ideas/) | Raw ideas — topics, projects, hooks, feedback |
| [plans/](plans/) | Work plans — milestones, lesson drafts, block outlines |
| [issues/](issues/) | Problems to fix — typos, bugs, gaps, open questions |

## Conventions

- One topic per file: `short-descriptive-name.md`
- Start from a template in each subfolder (`_template.md`)
- Link related lessons when relevant: `course-1/.../lesson-1-1-installing-python`
- When an idea is approved, move the outcome into [CURRICULUM.md](../CURRICULUM.md) or a lesson README — don't let this folder replace the curriculum

### After lesson verification

When **verify-lesson-in-block** runs (automatic after each new lesson):

| Output | Folder | Example filename |
|--------|--------|------------------|
| Improvement suggestions | `ideas/` | `block-1-meeting-your-computer-lesson-1-3-improvements.md` |
| Gaps and issues | `issues/` | `block-1-meeting-your-computer-lesson-1-3-gaps.md` |
| MCP tool run logs (local) | `agent-runs/` | `mcp-tools.jsonl` (gitignored) |

Local dev + MCP setup: [local-dev-and-mcp.md](local-dev-and-mcp.md)

Append dated sections if the same lesson is verified again. Link block-level registers (e.g. `issues/block-1-artifacts.md`) from per-lesson gap files when relevant.

## Status tags (optional, in file title or front matter)

- `draft` — still thinking
- `ready` — approved to implement
- `done` — implemented; add link to resulting commit or lesson
- `wontfix` — rejected; note why
