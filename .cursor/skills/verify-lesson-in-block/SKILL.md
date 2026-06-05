---
name: verify-lesson-in-block
description: >-
  Verifies a newly created or updated PyCourse lesson in block context via a
  delegated subagent. Files improvement suggestions to documents/ideas and gaps
  or issues to documents/issues. Use after write-lesson completes, or when
  checking a lesson fits its block.
---

# Verify Lesson in Block

Run this **every time** a lesson is created or substantially updated. The parent agent writes the lesson; a **separate subagent** performs verification so findings are independent.

## Parent agent workflow

1. Finish **write-lesson** (files created, scripts run locally).
2. **Immediately** launch a verification subagent — do not skip, do not self-review in place of delegation.
3. When the subagent returns, file its report into `documents/` (see [Filing rules](#filing-rules)).
4. Tell the user: verification summary, paths to filed documents, and whether the lesson passed or needs fixes.

### Launch the subagent

Use the **Task** tool:

| Parameter | Value |
|-----------|-------|
| `subagent_type` | `explore` |
| `readonly` | `true` |
| `description` | `Verify lesson in block` |

Paste the prompt from [subagent-prompt.md](subagent-prompt.md), filling in:

- `LESSON_PATH` — full path to the lesson directory
- `BLOCK_PATH` — parent block directory
- `LESSON_ID` — e.g. `1.3`
- `BLOCK_ID` — e.g. `1`

The subagent must **not** edit lesson files. It only reads, runs scripts, and returns a structured report.

## Filing rules

Classify every finding from the subagent report:

| Type | Destination | When |
|------|-------------|------|
| **Improvement** | `documents/ideas/` | Enhancements, pedagogy tweaks, stretch ideas, nice-to-haves — not blocking |
| **Gap / issue** | `documents/issues/` | Missing content, broken links, runnable failures, scope creep, block incoherence — blocking or should fix |

### File naming

One file per verification run:

```
documents/ideas/{block-slug}-lesson-{B}-{L}-improvements.md
documents/issues/{block-slug}-lesson-{B}-{L}-gaps.md
```

Examples:

- `documents/ideas/block-1-meeting-your-computer-lesson-1-3-improvements.md`
- `documents/issues/block-1-meeting-your-computer-lesson-1-3-gaps.md`

Use lowercase hyphenated slugs from the folder names. If a file already exists for the same lesson, **append** a dated section instead of overwriting.

### Templates

Copy from:

- [documents/ideas/_template.md](../../../documents/ideas/_template.md)
- [documents/issues/_template.md](../../../documents/issues/_template.md)

Add these fields at the top of every filed note:

```markdown
**Verification date:** YYYY-MM-DD
**Lesson:** course-N/.../lesson-B-L-slug/
**Block context:** block-B-slug
**Reviewer:** subagent (verify-lesson-in-block)
```

### What goes where

**→ documents/ideas/** (Suggestions / Nice to have from report)

- Optional exercises, analogies, or project hooks
- Cross-lesson reinforcement ideas
- Parent/teacher sidebar ideas
- Future stretch goals

**→ documents/issues/** (Critical / Needs work from report)

- Code that fails to run
- Wrong paths, filenames, or terminal commands
- Missing en.md / ru.md parity
- Prerequisite or "What's next" chain breaks
- Teaches concepts assigned to another lesson in the block
- CURRICULUM scope mismatch
- Missing block artifacts (e.g. STUDENT-MAP entry)

### Empty reports

If the subagent finds no gaps, still create the issues file with `**Status:** verified — no gaps` and a one-line summary.

If there are no improvements, skip the ideas file.

### Block-level registers

When a block already has a register (e.g. `documents/issues/block-1-artifacts.md`), add a **Related** link from the new per-lesson gaps file to that register. Do not duplicate resolved items.

## After filing

1. If **critical gaps** exist: fix the lesson in the same session when possible, then re-run verification.
2. If only improvements: leave them in `documents/ideas/` for a later pass — do not block the lesson on nice-to-haves unless the user asks.
3. Link filed documents in your user-facing summary.

## Skills the subagent must apply

Tell the subagent to follow (read if needed):

- **review-lesson** — completeness and runnable checks
- **youth-python-pedagogy** — age 11+ tone and pacing

## Additional resources

- Subagent prompt template: [subagent-prompt.md](subagent-prompt.md)
- Block coherence checklist: [block-checklist.md](block-checklist.md)
