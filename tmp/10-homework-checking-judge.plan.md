# 10 — Homework Checking (External Executor: Piston/Judge0)

## Goal
Implement automated homework verification for student `.py` submissions using an **external code-execution API**. Untrusted code is **never** run inside the FastAPI process. This plan picks a default executor, defines the checker contract and hidden-tests format, the submission API/flow, and rate limits, and grants the homework star (09) on a pass.

## Architectural decisions in effect

> 1. **Stack** — FastAPI accepts submissions and calls the executor over HTTP; the executor runs as a **separate sandboxed service**.
> 2. **Lesson storage** — `checker_ref`/`homework_ref` come from lesson metadata (01/05); hidden tests stored beside lessons or in a protected checker store, never in the lesson body.
> 3. **Gamification** — a passing run reports `homework_done` to the stars engine (09).
> 4. **Homework checking** — **default: self-hostable Piston** (simple, container-friendly); **alternative: Judge0 CE**. No untrusted execution in-process.

## Dependencies
- **04** (`submissions` table), **05** (`checker_ref`), **09** (homework star). Wave 3 — parallel with 09.
- Consumed by: 13 (bot can submit homework), 15 (lessons gain checkers during migration).

## Executor decision
- **Default Piston** (self-host via container) for safety + cost; **Judge0 CE** documented as a drop-in alternative. Backend talks to whichever via an `Executor` interface (URL + language=python3, stdin, time/mem limits).

## Checker contract & flow
- Per-lesson checker (`checker_ref`): `{ language, entrypoint, cases: [{stdin, expected_stdout | assertions}], visible_cases, hidden_cases, time_ms, mem_mb }`.
- **Hidden tests format**: stored separately from visible examples; never shipped in `en.md`/`ru.md`; referenced by id.
- Flow: student submits `.py` → `POST /homework/{lesson_id}/submit` → backend builds run request (code + cases) → executor runs sandboxed → backend compares outputs/assertions → persists `submissions` row → on all-pass, calls stars (09).
- **Rate limits**: per-user submission throttle (e.g. N/min + daily cap) + executor concurrency cap; reject oversized payloads.

## Deliverables / Steps
- [ ] `Executor` abstraction with Piston adapter (default) + Judge0 adapter; env-configured URL/limits.
- [ ] Checker metadata format + loader keyed by `checker_ref`; hidden-test storage scheme.
- [ ] `POST /homework/{lesson_id}/submit` + `GET` result; `submissions` persistence; pass→`homework_done` to 09.
- [ ] Rate limiting + payload/time/memory guards; clear student-facing feedback (which case failed, no hidden-test leakage).
- [ ] Author checkers for a small initial lesson set as proof.

## Verification
- [ ] Correct solution passes all cases and grants the homework star; wrong solution fails with safe feedback.
- [ ] Malicious/looping code is contained by the executor (time/mem limits) and never affects the FastAPI process.
- [ ] Hidden tests are not exposed in any client response or markdown.
- [ ] Rate limits enforced.

## Out of scope
- Browser inline code editor (future option).
- AST/semantic checkers (future option).
- Teacher manual-review workflow for capstones (future).
