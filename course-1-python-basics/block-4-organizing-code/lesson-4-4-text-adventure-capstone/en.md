# Lesson 4.4: Text Adventure Capstone

> **Course:** Python Basics & Command Line Magic · **Block:** Organizing Code · **~45–60 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 18 — Build Your Text Adventure**

---

## Explanation

Block 4 finale! You will combine **functions**, **lists**, and **dictionaries** into one playable text adventure — just like Block 2's Creator Data Pack combined variables and strings.

Create **`my_adventure/`** at your **project root** (next to `my_data/`, not inside this lesson folder). Copy the skeleton into that folder, finish its TODO functions, then make the game yours.

The sample game has three rooms connected by directions (`north`, `south`, etc.). Pick up the **golden key** in the library, return to the **garden**, and type `open` to win.

Before you start, review [starter/game.py](starter/game.py) to see how nested dicts describe each room.

**Path A — PyCourse repo:** In the VS Code terminal (the prompt ends in `PyCourse>`), create the folder at the project root:

```text
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

### Step 2: Write the helper functions

| Function | Job |
|----------|-----|
| `show_room(room_id)` | Print title, description, and the item if one is still there (already written) |
| `move(room_id, direction)` | Return the **new room id** if exit exists (no `global` needed) |
| `show_inventory()` | Numbered list from the `inventory` list |
| `take_item(room_id)` | Move room `"item"` into `inventory` |

In `main()`, save the return value: `current_room = move(current_room, command)`.

**Your job:** In `my_adventure/game.py`, replace the `# TODO` lines in `move()`, `show_inventory()`, and `take_item()` with real code. Two new tools help:

- `direction in room` is `True` when the room dict has that key — for example `"north" in rooms["start"]` is `True`.
- `del room["item"]` removes the `"item"` key from the room dict, so the key cannot be taken twice.

Here is `move()` finished — use it as a pattern for the other two:

```python
def move(room_id, direction):
    room = rooms[room_id]
    if direction in room:
        print(f"You go {direction}.")
        return room[direction]
    print("You cannot go that way.")
    return room_id
```

`show_inventory()` is the numbered loop from Lesson 4.2, plus a check for an empty pack with `len(inventory) == 0`.

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

**Sample winning path (your commands only — full output is in Code Execution below):**

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

**File: [solution/game.py](solution/game.py)** — the finished game. Open it only after you try your own `move()`, `show_inventory()`, and `take_item()`. The [starter/game.py](starter/game.py) skeleton you copy into `my_adventure/` runs, but you cannot move or pick up anything until you finish its TODOs.

---

## Code Execution

From the project root:

```text
cd my_adventure
python game.py
```

Or run the reference solution to compare:

```text
cd course-1-python-basics\block-4-organizing-code\lesson-4-4-text-adventure-capstone
python solution\game.py
```

**Mac/Linux:** Use forward slashes — `python solution/game.py`. List files with `ls` instead of `dir`.

**Expected output** when you type `north`, `take`, `south`, `east`, `open` (your typing is not shown here):

```text
=== ADVENTURE WORKSHOP ===
Commands: north, south, east, west, take, inventory, open, quit

=== Workshop Door ===
You stand at the workshop entrance. Paths lead north and east.
What do you do? You go north.

=== Scroll Library ===
Dusty scrolls line the shelves. An old desk stands in the corner.
You see a golden key here.
What do you do? You picked up the golden key.

=== Scroll Library ===
Dusty scrolls line the shelves. An old desk stands in the corner.
What do you do? You go south.

=== Workshop Door ===
You stand at the workshop entrance. Paths lead north and east.
What do you do? You go east.

=== Hidden Garden ===
Moonlight filters through leaves. A treasure chest waits here.
What do you do? The chest opens! You win!
```

---

## Quick Drills

1. **Map draw** — on paper, sketch the three rooms and which directions connect them.
2. **Empty pack** — type `inventory` before `take`. What prints?
3. **Locked chest** — type `open` in the garden before you have the key. Read the hint.

---

## Practice Task

**Quest name:** Your Adventure World

1. Copy [starter/game.py](starter/game.py) to **`my_adventure/game.py`** at project root and finish the TODOs in `move()`, `show_inventory()`, and `take_item()` (Step 2). Play the winning path until your output matches Code Execution.
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

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. Where should you create `my_adventure/` for this capstone?
   - **a)** On the Python install drive only
   - **b)** Inside this lesson's `starter` folder
   - **c)** At your **project root**, next to `my_data/` — not inside a lesson folder
   - **d)** Only inside `game.py` as a comment

2. In the `rooms` dict, where does `"south": "start"` live?
   - **a)** Inside the `inventory` list
   - **b)** In a `print()` statement only
   - **c)** At the top level of `rooms` as `rooms["south"]`
   - **d)** **Inside** one room's dict — a direction key pointing to another room id

3. Which data structure holds picked-up items like the golden key?
   - **a)** A list called `inventory`
   - **b)** A single string variable only
   - **c)** The `while True` loop itself
   - **d)** `turtle.Turtle()`

4. What is the job of `show_room(room_id)`?
   - **a)** Add items to inventory automatically
   - **b)** Print the room's title and description
   - **c)** Close the game window
   - **d)** Install Flask

5. Why is `rooms[current_room]["north"]` correct but `rooms["north"]` is wrong?
   - **a)** Python does not allow nested dicts
   - **b)** `rooms` is a list indexed by numbers only
   - **c)** Directions like `"north"` are **inside** each room dict, keyed by room id first
   - **d)** `"north"` is always index 0

---

<details><summary>Click to reveal answers</summary>

1. **c)** Capstone folders (`my_adventure/`) live at project root, like `my_data/` and `my_mission/`.
2. **d)** Each room dict can have direction keys (`"south"`, `"north"`…) whose values are other room ids.
3. **a)** The `inventory` **list** grows when you `take` items from rooms.
4. **b)** `show_room` displays the current room's name and description to the player.
5. **c)** First pick the room with `current_room`, then look for a direction **inside** that room's dict.

</details>

---

## What's Next

→ [Lesson 5.1: Turtle Basics](../../block-5-creative-turtle/lesson-5-1-turtle-basics/README.md) — Block 5 starts: draw shapes and patterns on screen.

Tick the [Block 4 readiness checklist](../README.md#block-4-readiness-checklist) before you start Turtle!

---

*You built a real text adventure. Next you will draw with Python's Turtle module!*

[← Choose language](README.md)
