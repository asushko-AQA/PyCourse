---
name: write-lesson
description: >-
  Creates a new PyCourse lesson directory with README, starter code, and
  optional solution following project conventions. Use when the user asks to
  write, draft, or add a lesson, or when starting work on a specific lesson
  number from CURRICULUM.md.
---

# Write Lesson

## Before Writing

1. Read [CURRICULUM.md](../../../CURRICULUM.md) for the target lesson scope.
2. Read [AGENTS.md](../../../AGENTS.md) for structure and code style.
3. Apply **youth-python-pedagogy** for tone and pacing.
4. Confirm prerequisites from prior lessons are met.

## Directory Path

```
course-{N}-{slug}/
  block-{B}-{slug}/
    lesson-{B}-{L}-{slug}/
      README.md       # required — language chooser (links to en.md / ru.md)
      en.md           # required — full lesson in English
      ru.md           # required — full lesson in Russian
      starter/        # optional — code student starts from
      solution/       # optional — reference answer
      exercises/      # optional — extra challenge scripts
```

**Slug rules:** lowercase, hyphenated, no lesson numbers in folder name.

## Bilingual layout

Student-facing lessons are split by language:

| File | Purpose |
|------|---------|
| `README.md` | Landing page — pick English or Russian via links |
| `en.md` | Complete lesson in English |
| `ru.md` | Complete lesson in Russian |

Each language file links back to `README.md` and to the other language. Link "What's next" to the **next lesson's `README.md`** (chooser), not directly to `en.md`/`ru.md`.

**Section headings:** English files use English headings (`## Title`, `## Quick Drills`); Russian files use Russian headings (`## Заголовок`, `## Быстрые упражнения`). Keep the same section order in both languages.

Example: `course-1-python-basics/block-1-meeting-your-computer/lesson-1-1-installing-python/`

## README Template

Copy and fill in:

```markdown
# Lesson X.Y: [Title]

> **Course:** [Course name] · **Block:** [Block name] · **Time:** ~30 min

## What you'll build

[One sentence + expected output description or screenshot placeholder]

## What you'll learn

- [Concept 1]
- [Concept 2]
- [Concept 3]

## Before you start

- [ ] Prerequisite lesson completed
- [ ] [Setup check, e.g. Python 3.12 installed]

---

## Step 1: [Action title]

[1–3 sentences of explanation]

\`\`\`python
# code here
\`\`\`

**Expected output:**

\`\`\`
output here
\`\`\`

---

[Repeat Steps 2–N]

---

## Try it yourself

### Challenge 1 (required)
[Description + hint]

### Challenge 2 (bonus)
[Optional stretch]

## Debug corner

**Problem:** [Error or bug description]

**Cause:** [Why it happens]

**Fix:** [How to fix]

## What's next

→ [Next lesson title](relative/path/to/next/README.md)
```

## Starter / Solution Rules

- **starter/** — working skeleton with `# TODO` comments; must run without errors.
- **solution/** — complete working code; same filenames as starter.
- Never put solutions inside starter files.
- One main `.py` file per lesson unless the curriculum requires more.

## Code Checklist

- [ ] Runs with `python filename.py` from the lesson folder
- [ ] No external packages unless the curriculum lesson says so
- [ ] Variable names are descriptive (`player_score` not `ps`)
- [ ] No type hints in Course 1
- [ ] Windows paths explained if shown; prefer portable code

## After Writing

1. Run the starter and solution scripts locally.
2. Verify README steps match actual file names and output.
3. Link "What's next" to the following lesson (create placeholder README if needed).
4. **Mandatory:** Delegate verification — apply skill **verify-lesson-in-block** (launch a readonly subagent, file improvements to `documents/ideas/`, gaps to `documents/issues/`). Do not consider the lesson done until verification completes and documents are filed.
