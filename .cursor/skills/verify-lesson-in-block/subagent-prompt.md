# Subagent prompt (copy into Task tool)

Replace placeholders before sending.

---

Verify the PyCourse lesson at `LESSON_PATH` in the context of its block at `BLOCK_PATH`.

**Lesson ID:** LESSON_ID · **Block ID:** BLOCK_ID

You are an independent reviewer. Do **not** edit any files. Read, run scripts, compare against curriculum and sibling lessons, then return a structured report.

## Read first

1. [CURRICULUM.md](CURRICULUM.md) — scope for lesson LESSON_ID and block BLOCK_ID
2. [AGENTS.md](AGENTS.md) — conventions and boundaries
3. Block README at `BLOCK_PATH/README.md` (and STUDENT-MAP if present)
4. Prior lesson in the block (if any) — check prerequisite chain
5. Next lesson README or CURRICULUM entry (if any) — check forward links
6. The target lesson: `README.md`, `en.md`, `ru.md`, `starter/`, `solution/`, `exercises/`

Apply skills **review-lesson** and **youth-python-pedagogy**.

## Block-context checks

- [ ] Lesson fits block theme and lesson sequence (no duplicate major concepts from siblings)
- [ ] Prerequisites match what prior lessons actually teach
- [ ] Terminology and folder conventions match sibling lessons (e.g. `starter/` paths, `python starter\file.py`)
- [ ] "What's next" points to the correct next lesson README (chooser), not en.md/ru.md
- [ ] en.md and ru.md have matching section order; headings localized per write-lesson convention
- [ ] Block index / STUDENT-MAP updated if this lesson introduces new student folders or paths
- [ ] Capstone or block milestone alignment (if this is the last or capstone lesson)

## Run verification

From the lesson directory, run starter and solution scripts:

```bash
python starter/<main>.py
python solution/<main>.py
```

Note any failures with exact command and error output.

## Return format

Use exactly this structure:

```markdown
## Verification: LESSON_ID — [lesson title]

**Block:** BLOCK_ID — [block name]
**Result:** Pass | Needs work

## Block fit
[2–4 sentences: how this lesson fits the block, prerequisite chain, forward link]

## Critical (→ documents/issues/)
- [ID optional] [finding + file:line or path]

## Gaps (→ documents/issues/)
- [finding]

## Suggestions (→ documents/ideas/)
- [improvement idea]

## Nice to have (→ documents/ideas/)
- [optional enhancement]

## Verified working
- [commands that succeeded]
```

Severity guide:

- **Critical** — broken code, wrong scope, broken navigation, EN/RU mismatch on substance
- **Gaps** — missing sections, missing expected output, pedagogy issues, block inconsistency
- **Suggestions** — clarity, extra drills, analogies
- **Nice to have** — optional polish

Be specific. Cite paths. Do not fix files yourself.
