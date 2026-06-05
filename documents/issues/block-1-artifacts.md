# Block 1 Artifacts — Review Register

**Status:** resolved (2026-06-06)  
**Scope:** Course 1, Block 1 — Lessons 1.1–1.5  
**Original review:** 2026-06-06

---

## Summary

| Severity | Found | Fixed |
|----------|-------|-------|
| High | 1 | 1 |
| Medium | 8 | 8 |
| Low | 6 | 5 |
| Documented only | 1 | B1-015 (convention in write-lesson skill) |

---

## Resolution log

| ID | Fix applied |
|----|-------------|
| **B1-001** | Lesson 1.3: both scripts in `starter/`; commands `python starter\hello.py` + `python starter\launch.py` (or `cd starter`); en/ru/README/exercises updated |
| **B1-002** | Lesson 1.2: corrected `dir` examples at project root vs inside block folder (en + ru) |
| **B1-003** | Lesson 1.3 Step 6: `dir starter` only; removed ambiguous "lesson root" wording |
| **B1-004** | Added `quest_paths.ru.md`, `wrong_folder_scenarios.ru.md`; cross-links in EN files |
| **B1-005** | Path B callouts in lessons 1.3, 1.4, 1.5; added STUDENT-MAP.md + STUDENT-MAP.ru.md; linked from block README |
| **B1-006** | Lesson 1.1 README: What you'll learn, Before you start, Quick drills |
| **B1-007** | Lesson 1.1 en/ru: Quick Drills / Быстрые упражнения sections |
| **B1-008** | Lesson 1.5 en/ru: explicit `cd` to project root before `mkdir my_mission`; clearer `cd my_mission` paths |
| **B1-009** | `wrong_folder_scenarios.md` rewritten for `starter/` paths |
| **B1-010** | Lesson 1.3 en/ru: cross-link to Level 1 `my_intro.py` (workflow focus) |
| **B1-011** | Practice example moved to `solution/my_intro.py`; `solution/hello.py` trimmed |
| **B1-012** | `starter/badge.py`: placeholder `print()` so empty skeleton is not silent |
| **B1-013** | AGENTS.md: Block 1 five-lesson table + capstone + STUDENT-MAP link |
| **B1-014** | Lesson 2.1: full chooser with en.md / ru.md placeholders |
| **B1-015** | Documented in write-lesson skill — EN/RU section heading convention |

---

## Verified after fixes

- `python starter\hello.py` and `python starter\launch.py` (student creates launch.py in starter/)
- `python starter\treasure.py` outputs `Treasure found!`
- `python starter\badge.py` prints placeholder line

---

## Related

- [block-1-lessons-revised.md](../plans/block-1-lessons-revised.md)
- [STUDENT-MAP.md](../../course-1-python-basics/block-1-meeting-your-computer/STUDENT-MAP.md)
