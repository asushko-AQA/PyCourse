# Idea: Course 2 verification improvements

**Status:** draft  
**Date:** 2026-06-08  
**Course / block:** Course 2 — all blocks

**Verification date:** 2026-06-08  
**Reviewer:** parent agent (bulk verify resumed after subagent abort)

## Summary

Non-blocking enhancements identified during Course 2 bulk verification.

## Suggestions

- **Lesson 0.2:** Add a one-line preview screenshot placeholder for the mermaid diagram in a future pass.
- **Block 1:** Optional sidebar in 1.2 comparing `127.0.0.1` vs `localhost` for students who type URLs manually.
- **Lesson 2.3:** Stretch exercise — add a fourth word field (adverb) to Mad-Libs story.
- **Lesson 2.4:** Bonus challenge — dark-mode CSS variant using `prefers-color-scheme`.
- **Course index:** Add estimated total hours to `course-2-web-apps/README.md` (currently per-block only in block READMEs).

## Nice to have

- Shared `shared/flask-base.css` asset for Block 2 styling consistency across lessons.
- Parent sidebar on first `pip install` explaining disk space (~few MB for Flask).
- Automated CI script to Flask test-client all solution apps (future repo tooling).

## Related

- [documents/issues/course-2-verification-gaps.md](../issues/course-2-verification-gaps.md)
