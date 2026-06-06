# Lesson 4.4: Text Adventure Capstone

> **Course:** Python Basics & Command Line Magic · **Block:** Organizing Code · **~45–60 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 18 — Build Your Text Adventure**

---

## Explanation

Block 4 finale! You will combine **functions**, **lists**, and **dictionaries** into one playable text adventure — just like Block 2's Creator Data Pack combined variables and strings.

Create **`my_adventure/`** at your **project root** (next to `my_data/`, not inside this lesson folder). Copy the skeleton into that folder and make it yours.

The sample game has three rooms connected by directions (`north`, `south`, etc.). Pick up the **golden key** in the library, return to the **garden**, and type `open` to win.

Before you start, review [starter/game.py](starter/game.py) to see how nested dicts describe each room.

**Path A — PyCourse repo:**

```text
cd Documents\PyCourse
mkdir my_adventure
```

Copy [starter/game.py](starter/game.py) to **`my_adventure/game.py`**.

**Path B — your own folder:** Create `my_adventure` on Desktop or inside your project — same idea as `my_data`.

---

### Step 1: Understand the rooms dict

Each room is a dict inside the big `rooms` dict:

```python
"library": {
    "name": "Scroll Library",
    "description": "Dusty scrolls...",
    "south": "start",
    "item": "golden key",
}
```

- `"name"` and `"description"` are for display
- `"south": "start"` is an exit — a direction key pointing to another room id
- `"item"` is optional loot in that room

---

### Step 2: Helper functions

| Function | Job |
|----------|-----|
| `show_room(room_id)` | Print title and description |
| `move(room_id, direction)` | Return the **new room id** if exit exists (no `global` needed) |
| `show_inventory()` | Numbered list from the `inventory` list |
| `take_item(room_id)` | Move room `"item"` into `inventory` |

In `main()`, save the return value: `current_room = move(current_room, command)`.

---

### Step 3: Game loop

`main()` runs a `while True` loop:

1. Show the current room
2. Read a command with `input()`
3. Handle `north`/`south`/…, `take`, `inventory`, `open`, `quit`
4. `break` when the player wins or quits

---

### Step 4: Run from my_adventure

```text
cd my_adventure
python game.py
```

**Sample winning path:**

```text
What do you do? north
What do you do? take
What do you do? south
What do you do? east
What do you do? open
The chest opens! You win!
```

---

### Step 5: Make it yours

Rename rooms, change descriptions, add a fourth room, or invent a new win item. Keep the same structure: dict rooms + list inventory + helper functions.

---

## Code Example

See [solution/game.py](solution/game.py) after you try your own version. The starter in [starter/game.py](starter/game.py) is a working reference you can copy directly into `my_adventure/`.

---

## Code Execution

From project root:

```text
cd Documents\PyCourse\my_adventure
python game.py
```

Or test the lesson starter first:

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-4-text-adventure-capstone
python starter\game.py
```

**Mac/Linux:** Use forward slashes — `python starter/game.py`. List files with `ls` instead of `dir`.

---

## Quick Drills

1. **Map draw** — on paper, sketch the three rooms and which directions connect them.
2. **Empty pack** — type `inventory` before `take`. What prints?
3. **Locked chest** — type `open` in the garden before you have the key. Read the hint.

---

## Practice Task

**Quest name:** Your Adventure World

1. Copy [starter/game.py](starter/game.py) to **`my_adventure/game.py`** at project root.
2. Change at least one room name and description to match your story.
3. Add one new item in a room (change `"item"` text and update the win check if needed).
4. Play-test until you can win reliably.

**Bonus quest:** See [exercises/extension_prompts.md](exercises/extension_prompts.md) for stretch ideas (new commands, more rooms, health points).

**Reference solution:** [solution/game.py](solution/game.py)

---

## Debug Corner

**Problem:** `TypeError` or wrong room when you write `rooms["north"]` instead of `rooms[current_room]["north"]`.

**Cause:** You mixed **list index** thinking with **dict key** thinking. `rooms` is a dict keyed by room id (`"start"`, `"library"`). Directions like `"north"` live **inside** each room dict — not at the top level.

**Fix:** First get the current room: `room = rooms[current_room]`. Then check `if direction in room:` before moving. Never use a number index on `rooms` unless you deliberately build a list (this game uses dict keys only).

---

## What's Next

→ [Block 5: Creative Python with Turtle](../../block-5-creative-turtle/README.md) — draw shapes and patterns on screen.

Tick the [Block 4 readiness checklist](../README.md#block-4-readiness-checklist) before you start Turtle!

---

*You built a real text adventure. Next you will draw with Python's Turtle module!*

[← Choose language](README.md)
