# Idea: Block 2 — Reconcile Lesson 2.4 Mad-Libs story (lesson vs code)

**Status:** done (2026-06-06 — en/ru aligned to battle madlibs.py)  
**Date:** 2026-06-06  
**Course / block:** Course 1 / block-2-talking-to-python

**Verification date:** 2026-06-06  
**Block context:** block-2-talking-to-python  
**Reviewer:** subagent (verify-lesson-in-block)

## Summary

Align Lesson 2.4 `en.md`/`ru.md` with `starter/madlibs.py` and `solution/madlibs.py` — either update the lesson to the 4-input battle story or rewrite the scripts to the 5-input fairy-tale template.

## Why it matters

Students who follow the lesson text get different prompts and output than the code on disk. This breaks trust in “Expected output” blocks and is the top Block 2 defect (B2-CRIT-001).

## Example

**If keeping battle story (Option A):** Update en/ru Steps 1–3 to four inputs (`hero`, `creature`, `place`, `power`), sample input `Sam`, `dragon`, `castle`, `laser`, and expected battle output matching `solution/madlibs.py`.

**If keeping fairy tale (Option B):** Change `madlibs.py` to five inputs and fairy-tale `print()` lines from current lesson text.

## Notes

- README already matches battle code — only full lesson files drifted.
- After fix, re-run verification and close B2-CRIT-001 in issues file.

## Related

- [block-2-talking-to-python-gaps.md](../issues/block-2-talking-to-python-gaps.md) — B2-CRIT-001
- Lesson 2.4 `en.md`, `starter/madlibs.py`

---

# Idea: Block 2 — Path B callouts in Lessons 2.3 and 2.4

**Status:** partial (2.4 done; 2.3 still open)  
**Date:** 2026-06-06  
**Course / block:** Course 1 / block-2-talking-to-python

**Verification date:** 2026-06-06  
**Block context:** block-2-talking-to-python  
**Reviewer:** subagent (verify-lesson-in-block)

## Summary

Add one-line Path B run instructions to Lessons 2.3 and 2.4 `en.md`/`ru.md`, matching 2.1/2.2 and Block 1’s pattern.

## Why it matters

STUDENT-MAP documents Path B globally, but students often read only the lesson steps. Without per-lesson callouts, Path B learners may assume they need the full repo path for `calculator.py` and `madlibs.py`.

## Example

In 2.3 **Code Execution** (en):

```text
Path B: Copy calculator.py to any folder, cd there, run python calculator.py
```

Russian mirror in `ru.md`. Same pattern for `madlibs.py` in 2.4.

## Notes

- Do not duplicate STUDENT-MAP table — one sentence + link to STUDENT-MAP Path B section.

## Related

- [STUDENT-MAP.md](../../course-1-python-basics/block-2-talking-to-python/STUDENT-MAP.md)
- [block-2-talking-to-python-gaps.md](../issues/block-2-talking-to-python-gaps.md) — B2-GAP-001

---

# Idea: Block 2 — Surface slice_practice as optional bonus in 2.4

**Status:** draft  
**Date:** 2026-06-06  
**Course / block:** Course 1 / block-2-talking-to-python

**Verification date:** 2026-06-06  
**Block context:** block-2-talking-to-python  
**Reviewer:** subagent (verify-lesson-in-block)

## Summary

Link `exercises/slice_practice.md` and `slice_practice.ru.md` from Lesson 2.4 README Files table and Practice Task as an optional step after `slice_challenge`.

## Why it matters

Bilingual `slice_practice` exercises exist but are orphaned — students only see `slice_challenge`. Extra slicing practice reinforces `.upper()`/`.lower()` lesson without adding scope.

## Example

In 2.4 Practice Task bonus:

> Finished the slice challenge? Try [slice_practice](exercises/slice_practice.md) for more index practice (preview of IndexError).

Add row to README **Files** table.

## Related

- `lesson-2-4-strings-in-action/exercises/slice_practice.md`
- [block-2-talking-to-python-gaps.md](../issues/block-2-talking-to-python-gaps.md) — B2-GAP-002

---

# Idea: Block 2 — Stronger starter scaffolds in 2.1 and 2.4

**Status:** draft  
**Date:** 2026-06-06  
**Course / block:** Course 1 / block-2-talking-to-python

**Verification date:** 2026-06-06  
**Block context:** block-2-talking-to-python  
**Reviewer:** subagent (verify-lesson-in-block)

## Summary

Replace pre-filled variable values in `character_sheet.py` and pre-complete logic in `madlibs.py` starters with `# TODO` placeholders so students must edit before output feels “theirs.”

## Why it matters

Block 2 plan expects skeleton code students complete. Running starter without edits already prints a full character sheet / story — less engagement on first contact with variables and string transforms.

## Example

```python
# character_sheet.py starter
name = ""  # TODO: your name
age = 0    # TODO: your age
favorite_game = ""  # TODO: your favorite game
```

Lesson step: “Fill in the three variables, then run.”

## Related

- Lesson 2.1 `starter/character_sheet.py`
- Lesson 2.4 `starter/madlibs.py`
- [block-2-talking-to-python-gaps.md](../issues/block-2-talking-to-python-gaps.md) — B2-GAP-003
