# Issue: Block 0 (lessons 0.1 & 0.2) verification gaps

**Status:** resolved — fixed in the same session (plan 03)
**Date:** 2026-06-28
**Severity:** low
**Verification date:** 2026-06-28
**Lesson:** course-1-python-basics/block-0-getting-started/ (lesson-0-1, lesson-0-2)
**Block context:** block-0-getting-started
**Reviewer:** subagent (verify-lesson-in-block)

## Problem

Independent verification of the two new Block 0 warm-up lessons returned **Pass** with
**no critical findings**. The following non-blocking gaps were raised and **fixed in the
same session**:

| # | Finding | Resolution |
|---|---------|-----------|
| 1 | `lesson-0-2/en.md` & `ru.md`: "often just one line" but Code Example shows two `print` lines | Reworded to "a line or two" (EN) / "одна-две строки" (RU) |
| 2 | `lesson-0-2/ru.md`: loanword «превью» inconsistent with 0.1's natural Russian | Reworded to "здесь мы лишь заглядываем…" |
| 3 | `AGENTS.md` stale: "5 blocks, 21 lessons"; dev order started at Block 1; suggested start Lesson 1.1 | Added Block 0 to repo tree (23 lessons), dev order (Block 0 → 1 → …), Block 0 table, and suggested-start line |
| 4 | Course `STUDENT-MAP.md` heading "all 21 lessons" but lists Block 0 ticks | Heading now "Block 0 warm-up + 21 lessons" |
| 5 | Course `STUDENT-MAP.md` intro linked only Block 1's map | Now links both Block 0 and Block 1 maps |

## Expected

Docs consistently reflect the new pre-install Block 0; lesson prose matches its own code
examples; RU prose avoids unnecessary loanwords.

## Steps to reproduce

1. Before fix: `rg "21 lessons" AGENTS.md course-1-python-basics/STUDENT-MAP.md`
2. Before fix: read `lesson-0-2-how-code-runs/en.md` Code Example heading line.

## Proposed fix

Done (see table). No further action required.

## Related

- `documents/plans/lesson-schema-v2.md`
- `tmp/completed/03-intro-programming-unit.plan.md`
- Improvements: `documents/ideas/block-0-getting-started-lessons-improvements.md`
