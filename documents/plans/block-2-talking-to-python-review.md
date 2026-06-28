# Block 2 Plan Review — Talking to Python

**Date:** 2026-06-06  
**Reviewer:** Block 2 review agent (readonly)  
**Plan reviewed:** [block-2-talking-to-python.md](block-2-talking-to-python.md)  
**References:** [CURRICULUM.md](../../CURRICULUM.md), [block-1-lessons-revised.md](block-1-lessons-revised.md), [block-1-artifacts.md](../issues/block-1-artifacts.md)

---

## Summary

**Verdict: Approve with minor amendments.** The five-lesson arc (variables → input/f-strings → math → string methods → capstone) aligns with CURRICULUM.md, Block 1 exit skills, and youth-python-pedagogy. Apply six concrete amendments below before implementation.

---

## 1. Alignment check

| Check | Result |
|-------|--------|
| CURRICULUM Block 2 scope | ✅ Matches; Lesson 2.5 capstone fills gap |
| Prerequisites (Block 1 checklist) | ✅ Explicit gate; no `if`/`for`/`def` |
| One primary concept per lesson | ✅ Each lesson has one main skill |
| Runnable every lesson | ✅ All five end with terminal output |
| Bilingual + Path A/B | ✅ Inherited from Block 1 plan |
| Block 1 artifact fixes | ✅ STUDENT-MAP, RU exercises, starter layout addressed |

**Sequence:** 1.5 → 2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 3.1 placeholder is correct. Lesson 2.1 correctly defers `input()` to 2.2.

---

## 2. Argued trade-offs

### 2.1 — Three types in one lesson

**Trade-off:** Variables + strings + integers in Lesson 2.1 is denser than strict one-concept-per-lesson.

**Decision:** **Keep combined.** Frame as "two kinds of magic boxes" (text in quotes, numbers without). Splitting ints to 2.2 would collide with f-strings/`input()`. Fallback documented in plan if pacing fails in classroom testing.

### 2.3 — `int()` only here

**Trade-off:** Students type numbers in 2.2 as strings without conversion.

**Decision:** **Correct.** Foreshadow in 2.2 ("input returns text"); teach `int()` when math begins. Debug corner in 2.5 reinforces the lesson.

### 2.4 — Mad-Libs separate from 2.2 greeting

**Trade-off:** Reusing `greeting.py` would reduce file count.

**Decision:** **Stay separate.** Mad-Libs needs 4–5 inputs and string transforms; merging would exceed ~40 lines and blend two lesson outcomes.

### 2.5 — Capstone without `if`

**Trade-off:** No branching limits interactivity.

**Decision:** **Acceptable.** Sequential `input()` + calculation + `.upper()` proves Block 2 skills; mirrors Block 1.5 capstone pattern.

### Capstone folder — `my_data/` at project root

**Trade-off:** Root folder vs inside lesson.

**Decision:** **Project root** (mirror `my_mission/`). STUDENT-MAP must show tree clearly.

---

## 3. Risk register

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| B2-001 | 2.1 overlaps Lesson 1.1 `my_intro.py` | Medium | Cross-link in 2.1: "You printed text before; now you store it in boxes" |
| B2-002 | Path B learners skip long `cd` paths | Medium | Path B callout in every lesson en/ru |
| B2-003 | RU exercise parity for 2.3, 2.4 | Medium | Require `*.ru.md` for all exercise sheets |
| B2-004 | 2.3 calculator too long (four ops) | Low | Starter prints all four; practice offers "+ and * only" shortcut |
| B2-005 | Interactive lessons need stdin | Low | Document: type answers when terminal waits |
| B2-006 | Block 1 README still says "coming soon" for Block 2 | Low | Update next-block link when 2.1 ships |

---

## 4. Concrete amendments (merge into main plan)

1. **Amendment 1:** In Lesson 2.1 en/ru, add one sentence cross-linking Level 1 `my_intro.py` — variables upgrade static prints to reusable boxes.
2. **Amendment 2:** Confirm `my_data/` at **project root** (not inside lesson folder); STUDENT-MAP shows `my_data/creator_pack.py` beside `my_mission/`.
3. **Amendment 3:** Lesson 2.4 Mad-Libs stays a **new script** (`madlibs.py`), not an extension of `greeting.py`.
4. **Amendment 4:** Lesson 2.3 starter prints **all four** operations; practice task offers shortened "+ and * only" variant for fast finishers.
5. **Amendment 5:** Add `exercises/` to 2.5 with optional `debug_quotes.md` + `.ru.md` (break/fix quote challenge sidebar).
6. **Amendment 6:** Update Block 1 `README.md` next-block link from "coming soon" to Block 2 index when implemented.

---

## 5. Verdict

**Approve** — merge amendments 1–6 into [block-2-talking-to-python.md](block-2-talking-to-python.md); set status to `approved`; proceed with implementation order in plan.

---

## Post-implementation checklist (for verify step)

- [ ] All starter/solution scripts run
- [ ] What's Next chain: 1.5 → 2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 3.1
- [ ] Block 2 readiness checklist on block README
- [ ] CURRICULUM.md includes Lesson 2.5 row
