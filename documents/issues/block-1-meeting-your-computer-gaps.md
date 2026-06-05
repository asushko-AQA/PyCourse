# Issue: Block 1 — Verification gaps

**Status:** open  
**Date:** 2026-06-06  
**Severity:** low (block publish-ready)  
**Location:** course-1-python-basics/block-1-meeting-your-computer/

**Verification date:** 2026-06-06  
**Block context:** block-1-meeting-your-computer  
**Reviewer:** subagent (verify-lesson-in-block)

## Summary

Block 1 **passes** verification. All five lessons match CURRICULUM, navigation chain is intact, EN/RU parity is solid, and all starter/solution scripts run. No critical gaps. Items below are polish.

## Problem

| ID | Severity | Finding |
|----|----------|---------|
| B1-V01 | Medium | Mac/Linux path parity: only Lesson 1.2 documents `ls`, `clear`, and forward-slash paths. Lessons 1.3–1.5 use Windows backslashes only in terminal examples (AGENTS.md requires macOS/Linux equivalents). |
| B1-V02 | Low | STUDENT-MAP progress tick 1.3 lists `python starter\launch.py` before the student creates `launch.py` (file exists only in `solution/` in repo). |
| B1-V03 | Low | Lesson 1.1 README has double-spaced blank lines; lessons 1.2–1.5 use tighter formatting. |
| B1-V04 | Low | CURRICULUM.md lesson README template still describes inline 7-section README; actual lessons split content into `en.md`/`ru.md`. |
| B1-V05 | Low | Lesson 1.5 `starter/badge.py` prints an em-dash; some Windows consoles render it as a replacement character. |

## Expected

- Non-Windows learners have equivalent path/run examples in every lesson that shows terminal commands.
- STUDENT-MAP ticks match what exists on disk at each step.
- Curriculum doc matches bilingual chooser convention.

## Verified working

- All `starter/` and `solution/` scripts in lessons 1.1–1.5 (Windows PowerShell, exit 0 or expected errors for buggy starters).
- Lesson chain 1.1 → 1.5 → Block 2 README.

## Related

- [block-1-artifacts.md](block-1-artifacts.md) — prior review (resolved)
- [block-1-meeting-your-computer-improvements.md](../ideas/block-1-meeting-your-computer-improvements.md)
