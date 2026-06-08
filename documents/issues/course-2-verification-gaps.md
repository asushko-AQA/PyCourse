# Issue: Course 2 bulk verification gaps

**Status:** resolved  
**Date:** 2026-06-08  
**Severity:** low–medium  
**Location:** Course 2 — post-implementation review

**Verification date:** 2026-06-08  
**Reviewer:** parent agent (bulk verify resumed after subagent abort)

## Problem

Manual bulk verification after bulk verify subagent was aborted.

## Gaps found (all fixed)

| Gap | Resolution |
|-----|------------|
| Lesson 2.5 What's next missing graduation + Course 3 links | Updated `en.md` and `ru.md` |
| `check_setup.py` used deprecated `flask.__version__` | Solution + `ru.md` examples now use `importlib.metadata.version('flask')` |
| `course-2-complete.md` stale status | Plan marked **implemented** with accurate state table |

## Verified working

- Flask solution apps: 1.2, 1.4, 2.1, 2.2, 2.3, 2.4, 2.5 — `GET /` returns 200 via test client
- All 11 lessons have `README.md`, `en.md`, `ru.md`
- What's next chain 0.1 → … → 2.5 uses lesson `README.md` choosers
- Dual-project design present: URL calc (1.4), Mad-Libs (2.3), POST calc (2.5)

## Related

- [documents/plans/course-2-complete.md](../plans/course-2-complete.md)
- [documents/ideas/course-2-verification-improvements.md](../ideas/course-2-verification-improvements.md)
