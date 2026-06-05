# Block-context verification checklist

Use alongside **review-lesson** when verifying a lesson inside its block.

## Sequence and scope

| Check | Question |
|-------|----------|
| Curriculum match | Does the lesson teach only what CURRICULUM assigns to this lesson ID? |
| One concept | Is there one primary new idea (~30 min)? |
| No steal | Does it avoid teaching major concepts assigned to later lessons in the block? |
| No repeat | Does it avoid re-teaching what a prior lesson already covered? |

## Navigation chain

| Check | Question |
|-------|----------|
| Back link | Does README / en.md / ru.md link back to README chooser? |
| Cross-language | Do en.md and ru.md link to each other? |
| What's next | Does "What's next" target the next lesson's `README.md`? |
| Block index | Is the lesson listed in the block README table? |

## Block conventions

| Check | Question |
|-------|----------|
| Path style | Do terminal examples match how sibling lessons run scripts? |
| Student folders | If students create folders (e.g. `my_mission/`), is STUDENT-MAP updated? |
| Shared vocabulary | Same terms for terminal, errors, VS Code as earlier block lessons? |
| Bilingual parity | Same steps and code in en.md and ru.md; only headings differ by language |

## Capstone lessons

For the last lesson in a block:

| Check | Question |
|-------|----------|
| Combines skills | Does the capstone use techniques from earlier lessons in the block? |
| Block checklist | Does the block README readiness checklist reflect what students can now do? |
| Handoff | Does "What's next" point to the first lesson of the next block (or placeholder)? |

## Severity quick reference

| Severity | Route to | Examples |
|----------|----------|----------|
| High | `documents/issues/` | Script won't run, wrong lesson scope, broken next link |
| Medium | `documents/issues/` | Missing debug corner, EN/RU step mismatch, jargon |
| Low / idea | `documents/ideas/` | Extra challenge, analogy, parent tip, stretch project |
