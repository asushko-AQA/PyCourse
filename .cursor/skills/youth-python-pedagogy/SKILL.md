---
name: youth-python-pedagogy
description: >-
  Applies age-appropriate teaching principles for Python lessons aimed at
  learners age 11+. Use when writing, editing, or reviewing student-facing
  lesson content, exercises, explanations, or examples in PyCourse.
---

# Youth Python Pedagogy (Age 11+)

## Core Rules

1. **One concept per lesson** — never introduce functions and lists in the same lesson.
2. **Runnable every time** — student must see output (print, Turtle canvas, browser page, game window) before the lesson ends.
3. **30–45 minute sessions** — 5–8 numbered steps max in the main tutorial portion.
4. **Errors are detectives** — frame bugs as puzzles; show the error message and what it means in plain English.

## Voice

| Do | Don't |
|----|-------|
| "Let's build a greeting machine" | "Implement an I/O subroutine" |
| "A variable is a labeled box" | "A variable is a memory address binding" |
| "Try changing the number to 10" | "Modify the initializer expression" |

## Complexity Limits

| Course | Max lines in main example | New concepts per lesson |
|--------|---------------------------|-------------------------|
| Course 1 | 15 early → 50 by Block 4 | 1 primary, 1 secondary max |
| Course 2 | 80 | 1 Flask concept + 1 HTML concept |
| Course 3 | 150 (capstone) | 1 Pygame concept |

## Engagement Hooks

Rotate themes young learners relate to:

- Games (inventory, scores, characters)
- School (grades, schedules, quizzes)
- Creative (drawing, stories, jokes)
- Web (personal page, fan site, calculator)

## Debugging Section (required in every lesson)

Include a **Debug corner** with:

- One common mistake (copy-pasteable wrong code)
- The error message it produces
- Plain-English explanation + fix

Example pattern:

```markdown
## Debug corner

**Problem:** `SyntaxError: invalid syntax` on the `if` line.

**Cause:** Python needs a colon `:` at the end of `if`, `elif`, and `else`.

**Fix:** Write `if score > 10:` not `if score > 10`
```

## Accessibility

- Define every new term on first use.
- Show expected output after every code block.
- Offer "Stuck?" hints before full solutions.
- Avoid culturally specific references without context.

## Assessment (lightweight)

Each lesson has two check-ins:

1. **Try it yourself** (coding) — 1 required challenge + 1 optional stretch.
2. **Quick Check** / **Проверь себя** (reading) — 3–5 multiple-choice questions after Debug corner, before What's next. Use collapsible `<details>` for answers so students try first.

Never grade; use encouraging language: "Bonus quest", "Level up". Wrong quiz answers are fine — they are for self-check only.
