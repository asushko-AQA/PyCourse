# Plan: Lesson Schema v2 (Canonical Lesson Format)

**Status:** approved
**Date:** 2026-06-24
**Target:** Every lesson in every course (Courses 1, 1.5, 2, 3)
**Supersedes:** the informal lesson layout in `AGENTS.md` § "Lesson `en.md` / `ru.md` section order"

This is the **canonical lesson format** for PyCourse. It is the contract that the
markdown→DB sync job (plan 05), the frontend parser
(`frontend/src/lib/courseParser.ts`), the content validator
(`frontend/scripts/validate-content.ts`), the quiz tool
(`tools/apply_lesson_quizzes.py`), and the Telegram bot all rely on. Markdown in git
stays **canonical**; the DB only stores extracted metadata.

See [documents/plans/README.md](README.md) for the plan registry and
[platform-architecture.md](platform-architecture.md) for the binding decisions.

## Goal

One comprehensive, machine-friendly, bilingual lesson format so that:

- the frontend can split every lesson into **Theory / Assignments / Quiz** tabs with no
  per-lesson special-casing;
- the sync job can extract stable **metadata** (ids, ordering, quiz hash, homework/checker
  refs) without parsing prose;
- the three **star sources** (reading, homework, perfect quiz) are derivable from
  structure;
- EN and RU stay in lock-step (parity).

## Lesson folder

```
lesson-{B}-{L}-{slug}/
├── README.md      # language chooser ONLY (links to en.md + ru.md)
├── en.md          # full lesson, English
├── ru.md          # full lesson, Russian — same section set + same #Quick Check questions
├── starter/       # runnable skeleton with TODOs (usually)
└── solution/      # reference code (usually)
```

## Section order (`en.md` / `ru.md`)

Use matching localized headings in `ru.md` (RU heading shown in parentheses).

| # | Heading (EN) | Heading (RU) | Required | Tab | Notes |
|---|--------------|--------------|----------|-----|-------|
| 1 | H1 title + intro blockquote | H1 + intro | Yes | — | `# Lesson B.L: …` / `# Урок B.L: …` |
| 2 | `## Title` | `## Title` | Yes | — | bold level name, e.g. `**Level 6 — …**` |
| 3 | `## Explanation` | `## Explanation` / `## Объяснение` | Yes | Theory | intro prose |
| 4 | `### Step N: …` | `### Шаг N: …` | Yes | Theory | numbered tutorial steps |
| 5 | `## Code Example` | `## Code Example` / `## Пример кода` | **Yes (NEW)** | Theory | the full runnable snippet + file ref |
| 6 | `## Code Execution` | `## Code Execution` / `## Запуск кода` | **Yes (NEW)** | Theory | exact run command + **Expected output** |
| 7 | `## Quick Drills` | `## Быстрые упражнения` | Yes | Assignments | 2–3 micro-drills |
| 8 | `## Practice Task` | `## Задание для практики` | Yes | Assignments | main exercise (**canonical heading**) |
| 9 | `## Debug Corner` | `## Уголок отладки` | Yes | Assignments | one+ problem/cause/fix |
| 10 | `## Quick Check` | `## Проверь себя` | Yes | Quiz | 3–5 MCQ + collapsible answers |
| 11 | `## What's Next` | `## Что дальше` | Yes | — | link to **next lesson's `README.md`** |

### Sections 5 & 6 are new in v2

Course 1 already has `## Code Example` + `## Code Execution`. Many Course 2 lessons do
not — closing that is plan 15's job. The parser/validator treat them as **Theory** and
**warn** (non-fatal) when missing, so the build still passes while the gap is tracked.

### Heading normalization (parser-enforced)

The parser normalizes these legacy variants; **new lessons must use the canonical
heading**:

- `## Try it yourself` → treat as **Practice Task** (Course 2 Block 1 uses this).
- `## Дальше` → treat as **What's Next** (some Block 1 RU files).
- `## Try it yourself` / `## Практическое задание` / `## Задание для практики` all map to
  the Practice Task / assignments tab.

## Optional metadata comment (NEW)

A single HTML comment may declare machine-readable metadata. It is **not rendered**
(invisible in the app and on GitHub) and does not affect canonical prose. Place it in the
preamble, right under the intro blockquote:

```markdown
<!-- meta
homework: starter/character_sheet.py
checker: checkers/lesson-2-1.yaml
minutes: 35
-->
```

| Key | Meaning | Consumed by |
|-----|---------|-------------|
| `homework` | relative path to the file/task a learner submits | star source "homework" (09), checker (10) |
| `checker` | relative path to the checker spec (hidden tests) | homework checking (10) |
| `minutes` | estimated lesson length (integer) | DB metadata / UI |

All keys are optional. Unknown keys are ignored (forward-compatible).

## Quiz block format (stable, hashable)

Uniform shape across the repo so the quiz can be parsed **and hashed** identically in both
the frontend parser and the sync job:

```markdown
## Quick Check

1. Question text?
   - **a)** Option
   - **b)** Option
   - **c)** Option
   - **d)** Option

<details><summary>Click to reveal answers</summary>

1. **b)** Explanation.

</details>
```

Rules: 3–5 questions; options `a)`–`d)` as `- **x)** …`; one `<details>` answer block with
`N. **x)** explanation` lines. EN and RU **must** have the **same number of questions**.

### Canonical quiz hash (used by plan 05)

To detect quiz drift without storing quiz bodies, the hash is computed as:

1. Take the `## Quick Check` / `## Проверь себя` section body (heading excluded), up to the
   next `## ` or end of file.
2. Normalize: convert CRLF→LF, strip trailing whitespace per line, strip leading/trailing
   blank lines.
3. `sha256(normalized_utf8)`, hex, **first 12 chars**.

`tools/apply_lesson_quizzes.py --hash` prints these for every lesson; plan 05 stores them
as `quiz_hash` in the DB.

## Bilingual parity rules

- `en.md` and `ru.md` have the **same section set** and **same number of Quick Check
  questions**.
- Quiz option markers (`a)`–`d)`) and the `<details>` answer block format are identical
  across languages.
- Localized headings follow the table above; the parser maps both languages to the same
  tab.

## Tooling hooks (kept in sync with this schema)

| Tool | What v2 requires |
|------|------------------|
| `frontend/src/lib/courseParser.ts` | recognizes Code Example/Code Execution, parses the `<!-- meta -->` comment into `LessonContent.meta`, records which canonical sections are `present`, keeps `Try it yourself`/`Дальше` normalization |
| `frontend/scripts/validate-content.ts` | **errors** (exit 1) on missing title/theory/assignments/quiz; **warnings** (exit 0) on missing Code Example / Code Execution — surfaces the migration gap without breaking the build |
| `tools/apply_lesson_quizzes.py` | idempotent under v2 headings; `--hash` mode prints the canonical quiz hash |

## Dependencies

- Plan 00 (architecture/decisions). Runs in parallel with 02 in Wave 0.
- Consumed by 04/05 (sync), 09 (stars), 10 (checkers), 15 (migration), 16 (Course 3).

## Done criteria

- This schema doc is approved and linked from `AGENTS.md`.
- `courseParser.ts` parses a v2 sample lesson (EN+RU) with no missing-section **warnings**.
- `npm run validate-content` exits 0 (warnings allowed) and lists the Code Example/Execution gaps.
- `apply_lesson_quizzes.py` is a no-op on a lesson that already has a quiz and `--hash`
  prints a stable hash.
- The per-block gap list ([documents/issues/lesson-schema-v2-gap-list.md](../issues/lesson-schema-v2-gap-list.md)) exists and feeds plan 15.

## Out of scope

- Migrating the existing 32 lessons to v2 (plan 15).
- DB tables / sync implementation (plans 04/05).
- Authoring new Course 3 lessons (plan 16).
