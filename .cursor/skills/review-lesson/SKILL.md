---
name: review-lesson
description: >-
  Reviews a PyCourse lesson for completeness, age-appropriateness, runnable
  code, and convention compliance. Use when the user asks to review, QA, or
  check a lesson before publishing or merging.
---

# Review Lesson

## Quick Checklist

Copy and mark each item when reviewing:

```
Lesson Review: [lesson path]
- [ ] README follows write-lesson template (all 7 sections)
- [ ] Matches CURRICULUM.md scope (no scope creep)
- [ ] One primary concept; pacing fits ~30 min
- [ ] Every code block has expected output shown
- [ ] Starter code runs without errors
- [ ] Solution code runs and matches README steps
- [ ] Debug corner present with real error example
- [ ] Try it yourself has at least one required challenge
- [ ] "What's next" link is correct
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

## Critical
- [items]

## Suggestions
- [items]

## Nice to have
- [items]
```
