# 14 — Cross-Channel Resume UX

## Goal
Deliver the "continue where you left off" experience across web and Telegram using the last-position cursor (defined in 08) and the linked identity (12): resume entry points in both clients and web↔Telegram handoff via deep links. This is the UX split of the old cross-channel plan; identity and storage are already done.

## Architectural decisions in effect

> 1. **Stack** — both Next.js and the bot read/write the same last-position cursor via FastAPI.
> 2. **Lesson storage** — resume targets a lesson **id**; content is served from canonical markdown (web build-time / bot API).
> 3. **Gamification** — resume surfaces streak nudges ("keep your 3-day streak!") from 09.
> 4. **Homework checking** — N/A (links may deep-link into a homework tab).

## Dependencies
- **08** (last-position cursor), **12** (linked identity), **13** (bot client). Wave 4 — after 13.

## Deliverables / Steps
- [ ] Web: "Continue where you left off" card on home + CourseMap focus on the cursor lesson/tab.
- [ ] Bot: `/continue` command jumping to the cursor lesson; streak nudge message.
- [ ] **Deep-link handoff**: web → Telegram (`t.me/<bot>?start=<deeplink>`) and Telegram → web (signed resume URL) that both land on the same lesson/tab for the linked user.
- [ ] Cursor write-through: opening a lesson/tab in either channel updates the shared cursor (debounced).
- [ ] Edge cases: unlinked user prompted to link before handoff; stale cursor (deleted/reordered lesson) falls back gracefully.

## Verification
- [ ] Progress to lesson X tab on web → open bot `/continue` → lands on lesson X (and vice versa).
- [ ] Deep links route to the correct lesson/tab for the linked account only.
- [ ] Streak nudge appears when a streak is at risk.
- [ ] Stale cursor degrades to nearest valid lesson without error.

## Out of scope
- Cursor field definition/storage (08) and identity (12).
- Bot core flows (13).
