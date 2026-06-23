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
3. Read the canonical **lesson schema v2**: [documents/plans/lesson-schema-v2.md](../../../documents/plans/lesson-schema-v2.md) — new lessons MUST follow it.
4. Apply **youth-python-pedagogy** for tone and pacing.
5. Confirm prerequisites from prior lessons are met.

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

**Section headings (schema v2):** use the canonical headings in this exact order —
`## Title` → `## Explanation` + `### Step N` → `## Code Example` → `## Code Execution` →
`## Quick Drills` → `## Practice Task` → `## Debug Corner` → `## Quick Check` →
`## What's Next`. Russian files use the matching localized headings (`## Объяснение`,
`## Пример кода`, `## Запуск кода`, `## Быстрые упражнения`, `## Задание для практики`,
`## Уголок отладки`, `## Проверь себя`, `## Что дальше`). Use `## Practice Task` — **not**
the legacy `## Try it yourself`. `## Code Example` and `## Code Execution` are **required**.
Keep the same section set in both languages.

**Quick Check (required):** Place after Debug corner, before What's next. Include 3–5 multiple-choice questions (a–d) with collapsible answers. Quiz data for bulk updates lives in `tools/quizzes/*.json`; run `python tools/apply_lesson_quizzes.py` after editing JSON.

Example: `course-1-python-basics/block-1-meeting-your-computer/lesson-1-1-installing-python/`

## README Template

Copy and fill in:

```markdown
# Lesson X.Y: [Title]

> **Course:** [Course name] · **Block:** [Block name] · **~30 min**
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
homework: starter/main.py
checker: checkers/lesson-X-Y.yaml
minutes: 30
-->

---

## Title

**Level N — [Fun level name]**

---

## Explanation

[Intro prose — what this lesson builds and why]

### Step 1: [Action title]

[1–3 sentences of explanation]

\`\`\`python
# code here
\`\`\`

[Repeat Steps 2–N]

---

## Code Example

**File: [starter/main.py](starter/main.py)**

\`\`\`python
# full runnable snippet for this lesson
\`\`\`

---

## Code Execution

\`\`\`text
cd course-N-.../block-B-.../lesson-X-Y-...
python starter\main.py
\`\`\`

**Expected output:**

\`\`\`text
output here
\`\`\`

---

## Quick Drills

1. [Micro-drill]
2. [Micro-drill]

---

## Practice Task

[Main exercise + bonus]

**Reference solution:** [solution/main.py](solution/main.py)

---

## Debug Corner

**Problem:** [Error or bug description]

**Cause:** [Why it happens]

**Fix:** [How to fix]

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. [Question about this lesson's main concept?]
   - **a)** [wrong]
   - **b)** [correct]
   - **c)** [wrong]
   - **d)** [wrong]

[3–5 questions total — test concepts from **this lesson only**]

---

<details><summary>Click to reveal answers</summary>

1. **b)** [One-line explanation]
...

</details>

---

## What's Next

→ [Next lesson title](relative/path/to/next/README.md)
```

The `<!-- meta -->` comment is optional and invisible; include it only when the lesson has
a checkable homework/practice task. See
[lesson schema v2](../../../documents/plans/lesson-schema-v2.md) for the full contract.

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
