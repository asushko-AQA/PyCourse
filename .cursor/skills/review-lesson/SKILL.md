---
name: review-lesson
description: >-
  Reviews a PyCourse lesson for completeness, age-appropriateness, runnable
  code, convention compliance, and block fit. Use when the user asks to review,
  QA, or check a lesson before publishing or merging. After creating a lesson,
  prefer verify-lesson-in-block (subagent + document filing) instead of
  reviewing in the same agent turn.
---

# Review Lesson

Used by the verification subagent (**verify-lesson-in-block**) and for manual QA. When reviewing a **newly created** lesson, the parent agent should delegate to a subagent per **verify-lesson-in-block** rather than self-review.

## Block context

Read the block README and one prior lesson before judging fit. Full block checks: [verify-lesson-in-block/block-checklist.md](../verify-lesson-in-block/block-checklist.md).

## Quick Checklist

Copy and mark each item when reviewing:

```
Lesson Review: [lesson path]
- [ ] Follows lesson schema v2 section order (documents/plans/lesson-schema-v2.md)
- [ ] Matches CURRICULUM.md scope (no scope creep)
- [ ] One primary concept; pacing fits ~30 min
- [ ] ## Code Example present (full runnable snippet + file ref)
- [ ] ## Code Execution present (run command + expected output)
- [ ] Uses canonical ## Practice Task heading (not legacy "Try it yourself")
- [ ] Starter code runs without errors
- [ ] Solution code runs and matches the steps
- [ ] Debug Corner present with real error example
- [ ] Quick Check / Проверь себя: 3–5 MC questions with collapsible answers
- [ ] EN/RU parity: same sections + same number of quiz questions
- [ ] "What's Next" links to the next lesson's README
- [ ] Optional <!-- meta --> comment valid if present (homework/checker/minutes)
- [ ] Language is age 11+ appropriate (youth-python-pedagogy)
- [ ] No banned topics (see AGENTS.md boundaries)
```

## Run Verification

From the lesson directory:

```bash
python starter/main.py    # if starter exists
python solution/main.py   # if solution exists
```

For Flask lessons: confirm venv instructions and that `app.py` serves on localhost.

For Pygame lessons: confirm window opens and closes cleanly (no hang on exit).

## Common Issues to Flag

| Issue | Severity | Action |
|-------|----------|--------|
| Lesson teaches two major concepts | 🔴 | Split or trim |
| Code block won't run as written | 🔴 | Fix before merge |
| Missing expected output | 🟡 | Add output block |
| Jargon without definition | 🟡 | Add plain-English note |
| Solution in starter folder | 🔴 | Move to solution/ |
| Lesson > 80 lines main example (Course 1) | 🟡 | Refactor or split |

## Review Output Format

Provide feedback as:

```markdown
## Summary
[Pass / Needs work — one sentence]

## Block fit
[How the lesson fits its block and sequence]

## Critical (→ documents/issues/)
- [items]

## Gaps (→ documents/issues/)
- [items]

## Suggestions (→ documents/ideas/)
- [items]

## Nice to have (→ documents/ideas/)
- [items]
```

## Document routing (verify-lesson-in-block)

When verification is delegated after lesson creation, the **parent agent** files findings — not the subagent:

| Finding type | Folder |
|--------------|--------|
| Critical, gaps, block issues | `documents/issues/` |
| Suggestions, nice to have | `documents/ideas/` |

Use templates in each subfolder. See **verify-lesson-in-block** for naming and append rules.
