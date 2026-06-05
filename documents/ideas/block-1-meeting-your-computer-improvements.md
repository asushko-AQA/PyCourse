# Idea: Block 1 — Cross-platform terminal callouts

**Status:** draft  
**Date:** 2026-06-06  
**Course / block:** Course 1 / block-1-meeting-your-computer

**Verification date:** 2026-06-06  
**Block context:** block-1-meeting-your-computer  
**Reviewer:** subagent (verify-lesson-in-block)

## Summary

Add Mac/Linux path and command callouts to Lessons 1.3–1.5, mirroring the pattern already used in Lesson 1.2.

## Why it matters

AGENTS.md requires macOS/Linux equivalents for Windows-first instructions. Block 1 is otherwise Windows-heavy after 1.2; non-Windows learners may get stuck on `python starter\file.py` or miss that `ls` replaces `dir`.

## Example

In Lesson 1.3 **Code Execution** (en + ru), add a short sidebar:

```text
Mac/Linux: use forward slashes — python starter/hello.py
List files: ls (instead of dir)
```

Repeat in 1.4 and 1.5 run steps.

## Notes

- Keep callouts one line each — do not duplicate full lessons.
- Link to 1.2 quest_paths exercise as “already practiced `ls` here.”

## Related

- Lesson 1.2 `en.md` — existing Mac/Linux pattern
- [block-1-meeting-your-computer-gaps.md](../issues/block-1-meeting-your-computer-gaps.md) — B1-V01

---

# Idea: Block 1 — Family “wrong folder” drill in block README

**Status:** draft  
**Date:** 2026-06-06  
**Course / block:** Course 1 / block-1-meeting-your-computer

**Verification date:** 2026-06-06  
**Block context:** block-1-meeting-your-computer  
**Reviewer:** subagent (verify-lesson-in-block)

## Summary

Add a parent/teacher tip on the block README linking to Lesson 1.3’s `wrong_folder_scenarios` exercise as a 5-minute family drill.

## Why it matters

`can't open file` is the most common real-world frustration after install. Block 1 teaches the fix in 1.3 and 1.4, but parents may not discover the exercise. A block-level pointer reinforces the skill before Block 2’s interactive scripts.

## Example

Under **For parents and teachers** on `block-1-meeting-your-computer/README.md`:

> **5-minute drill:** Run [wrong folder scenarios](lesson-1-3-running-your-first-script/exercises/wrong_folder_scenarios.md) together — deliberately run Python from the wrong folder, read the error, then `cd` and fix it.

Russian equivalent on `README` or cross-link to `wrong_folder_scenarios.ru.md`.

## Notes

- Pairs well with STUDENT-MAP Path B section.
- Optional: badge sticker / checklist item “I fixed a wrong-folder error without help.”

## Related

- [wrong_folder_scenarios.md](../../course-1-python-basics/block-1-meeting-your-computer/lesson-1-3-running-your-first-script/exercises/wrong_folder_scenarios.md)
- Lesson 1.4 — CLI vs SyntaxError distinction

---

# Idea: Block 1 — STUDENT-MAP starter tree completeness

**Status:** draft  
**Date:** 2026-06-06  
**Course / block:** Course 1 / block-1-meeting-your-computer

**Verification date:** 2026-06-06  
**Block context:** block-1-meeting-your-computer  
**Reviewer:** subagent (verify-lesson-in-block)

## Summary

Extend STUDENT-MAP folder tree to include `lesson-1-1-installing-python/starter/hello.py` and clarify the 1.3 tick: “after you create `launch.py` in Double Launch quest.”

## Why it matters

Students on Path A may not realize 1.1 also has a `starter/` script. The 1.3 progress tick implies `launch.py` exists in starter before the student creates it.

## Example

Progress tick change:

```markdown
- [ ] 1.3 — `python starter\hello.py` works; after Double Launch, `python starter\launch.py` too
```

## Related

- [STUDENT-MAP.md](../../course-1-python-basics/block-1-meeting-your-computer/STUDENT-MAP.md)
- [block-1-meeting-your-computer-gaps.md](../issues/block-1-meeting-your-computer-gaps.md) — B1-V02
