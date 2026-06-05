# Issue: Block 2 — Verification gaps

**Status:** open (B2-CRIT-001 resolved 2026-06-06)  
**Date:** 2026-06-06  
**Severity:** low (critical item fixed; polish remains)  
**Location:** course-1-python-basics/block-2-talking-to-python/

**Verification date:** 2026-06-06  
**Block context:** block-2-talking-to-python  
**Reviewer:** subagent (verify-lesson-in-block)

## Summary

Block 2 **passes** after Lesson 2.4 fix (2026-06-06). Remaining items are polish.

## Problem

| ID | Severity | Finding |
|----|----------|---------|
| ~~**B2-CRIT-001**~~ | ~~High~~ | **Resolved:** `en.md`/`ru.md` aligned to 4-input battle `madlibs.py`; Path B + Mac/Linux callouts added in 2.4. |
| B2-GAP-001 | Medium | Lesson 2.3 still lacks inline Path B callouts in `en.md`/`ru.md` (2.4 now has them; STUDENT-MAP covers Path B globally). |
| B2-GAP-002 | Low | `exercises/slice_practice.md` (+ `.ru.md`) not linked from 2.4 README or lesson body (only `slice_challenge` is linked). |
| B2-GAP-003 | Low | Lessons 2.1 and 2.4 starters are effectively complete despite `# TODO` — weak scaffold. |
| B2-GAP-004 | Low | Lesson 2.2 Code Execution section lacks a concrete sample output transcript. |

## Expected

- Lesson 2.4: student following `en.md`/`ru.md` sees the same prompts and story shape as `madlibs.py`.
- Path B one-liners in every lesson with run steps (mirror Block 1 pattern).
- Optional exercises discoverable from lesson README.

## Steps to reproduce (B2-CRIT-001)

1. Open `lesson-2-4-strings-in-action/en.md` — note five inputs and fairy-tale expected output.
2. Run `python starter\madlibs.py` with sample input `Sam`, `dragon`, `castle`, `laser`.
3. Output is a battle story with four prompts, not the fairy-tale template in the lesson.

## Proposed fix

Pick one direction for 2.4:

- **Option A:** Rewrite `en.md`/`ru.md` to match the 4-input battle `madlibs.py`, or
- **Option B:** Update `starter/`/`solution/` to the 5-input fairy-tale described in the lesson.

Align README, en, ru, code comments, and sample expected output.

## Verified working

- 2.1–2.5 starter and solution scripts run (interactive lessons tested with piped stdin on Windows).
- Lesson chain 1.5 → 2.1 → … → 2.5 → Block 3 placeholder.
- STUDENT-MAP EN/RU parity; Block 1 handoff checklist present.

## Related

- [block-2-talking-to-python-improvements.md](../ideas/block-2-talking-to-python-improvements.md)
- [block-1-meeting-your-computer](../issues/block-1-meeting-your-computer-gaps.md) — handoff from Block 1 verified
