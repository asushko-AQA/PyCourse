# Lesson 1.2: Using the Terminal / CLI

> **Course:** Python Basics & Command Line Magic · **Block:** Meeting Your Computer's Best Friend · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 2 — Navigate the Folder Maze**

---

## Explanation

Welcome back, Creator! In Level 1 you opened the **Command Portal** (terminal) and took your first steps. Now you become a **maze master** — walking through folders like rooms in a dungeon.

**What Level 1 already gave you:** open terminal, one `cd` example, run `python hello.py`.

**What is new in Level 2:** go **back** with `cd ..`, **list** files with `dir`, read your **current path**, and clear the screen.

Think of folders as **rooms**:

- `cd folder_name` — walk **into** a room
- `cd ..` — walk **back** to the previous room
- `dir` — look around and see what is in the room

---

### Step 1: Open your Command Portal

1. Open VS Code with your project folder.
2. Click **Terminal → New Terminal** (or press **Ctrl + `**).
3. Look at the text before the blinking cursor. That is your **current path** — the folder you are standing in right now.

**Example prompt:**

```text
C:\Users\YourName\Documents\PyCourse>
```

The path before `>` is your location in the maze.

---

### Step 2: Walk into a folder with `cd`

`cd` means **c**hange **d**irectory — go to another folder.

```text
cd Documents
```

**Expected:** The prompt updates. You are now inside `Documents`.

**Tip:** Type the first few letters of a folder name and press **Tab** — the terminal can autocomplete the name for you!

---

### Step 3: Walk back with `cd ..`

Two dots `..` mean "the folder above" — one level up.

```text
cd ..
```

**Expected:** The prompt shows the parent folder. You moved back one room.

---

### Step 4: List files with `dir`

`dir` shows everything in your current folder (Windows).

```text
dir
```

**Expected output (example at project root):**

```text
 Directory of C:\Users\YourName\Documents\PyCourse

course-1-python-basics
documents
README.md
...
```

**Inside Block 1** (after `cd course-1-python-basics\block-1-meeting-your-computer`):

```text
 Directory of ...\block-1-meeting-your-computer

lesson-1-1-installing-python
lesson-1-2-using-the-terminal
lesson-1-3-running-your-first-script
...
```

On **Mac/Linux**, use `ls` instead of `dir`.

Look for `.py` files — those are Python scripts!

---

### Step 5: Clear the screen

Too much text? Clean the portal:

```text
cls
```

On **Mac/Linux**, use `clear`.

**Expected:** A fresh, empty terminal screen. Your path is still the same.

---

### Step 6: Navigate to this lesson's folder

From your project root, walk into this lesson (adjust if your path is different):

```text
cd course-1-python-basics\block-1-meeting-your-computer\lesson-1-2-using-the-terminal
```

**Expected:** Prompt ends with `lesson-1-2-using-the-terminal>`.

```text
dir
```

**Expected:** You see `starter`, `solution`, `README.md`, and more.

---

### Step 7: Meet your treasure script

Inside `starter/` there is a tiny victory script: `treasure.py`. It has one job — celebrate when you find the right folder.

Open [starter/treasure.py](starter/treasure.py) in VS Code to peek at the code (just one `print()` line).

---

## Code Example

### Command scroll (terminal commands)

```text
# Walk into a folder
cd Documents

# Walk back up one level
cd ..

# List files in current folder (Windows)
dir

# List files (Mac/Linux)
# ls

# Clear screen (Windows)
cls

# Clear screen (Mac/Linux)
# clear
```

### Victory script: `treasure.py`

**File: [starter/treasure.py](starter/treasure.py)**

```python
# treasure.py
# Victory script — run this after you navigate to the right folder!

print("Treasure found!")
```

---

## Code Execution

You should already be in `lesson-1-2-using-the-terminal` from Step 6. If not, `cd` there now.

### 1. Confirm you are in the right room

```text
dir
```

**Expected:** `starter` folder is listed.

### 2. Run the treasure script

```text
python starter\treasure.py
```

On Mac/Linux: `python starter/treasure.py`

**Expected output:**

```text
Treasure found!
```

If you see that line — **Level 2 Complete!** You navigated the maze and ran a real script.

---

## Quick Drills

Do these three mini-quests (about 2 minutes each):

1. **`cd` to Desktop and back** — `cd Desktop`, then `cd ..`. Watch how the prompt changes.
2. **Count Python files** — `dir` in any folder. How many `.py` files do you see? Write the number down.
3. **Copy your path** — write the full path shown in your terminal prompt in a notebook. That is your "you are here" marker on the maze map.

---

## Practice Task

**Quest name:** Treasure Hunt

**Your mission:** Navigate like a detective and find treasure. Pick **Path A** or **Path B** (or do both!).

### Path A — PyCourse folder layout

1. Start from your project root (`PyCourse` or similar).
2. `cd course-1-python-basics\block-1-meeting-your-computer`
3. `dir` — list all lesson folders.
4. `cd lesson-1-1-installing-python`
5. `dir` — find `starter` and `README.md`.
6. `cd ..` — return one level up.
7. Confirm you are back in `block-1-meeting-your-computer`.

Use the tick-box checklist: [exercises/quest_paths.md](exercises/quest_paths.md)

### Path B — Any computer (build your own maze)

1. On Desktop, create folders: `quests\treasure`
2. Create `clue.txt` inside with: `The treasure is in treasure.py`
3. Copy `starter/treasure.py` into `quests\treasure`
4. In terminal: `cd Desktop\quests\treasure` (adjust path to your Desktop)
5. `dir` — see `clue.txt` and `treasure.py`
6. `python treasure.py` — see `Treasure found!`

**Bonus stars (optional):**

- Draw a paper map of 4 folders from your project. Label where `treasure.py` lives.
- Use **Tab** autocomplete for every `cd` in this quest.

**Stuck?** Check Debug Corner below.

---

## Debug Corner

**Problem:** The terminal says `The system cannot find the path specified`.

**Cause:** A folder name has a typo, or that folder does not exist where you think it does.

**Fix:**

1. `cd ..` to go back to a folder you know.
2. `dir` to see the **exact** folder names (spelling matters!).
3. Type `cd` again using the exact name from the list.
4. Use **Tab** after a few letters to avoid typos.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What does `cd ..` do?
   - **a)** Deletes the current folder
   - **b)** Walks back one folder level to the parent folder
   - **c)** Lists all files in the folder
   - **d)** Clears the terminal screen

2. On Windows, which command shows files in your current folder?
   - **a)** `ls`
   - **b)** `dir`
   - **c)** `show`
   - **d)** `list`

3. What does the text before `>` in your terminal prompt show?
   - **a)** Your Python version
   - **b)** Your current folder path
   - **c)** The last error message
   - **d)** Your password

4. How do you clear a messy terminal screen on Windows?
   - **a)** `cls`
   - **b)** `clear`
   - **c)** `cd ..`
   - **d)** `dir`

5. Pressing **Tab** after typing part of a folder name in `cd` can…
   - **a)** Delete the folder
   - **b)** Autocomplete the folder name for you
   - **c)** Run Python automatically
   - **d)** Close VS Code

---

<details><summary>Click to reveal answers</summary>

1. **b)** Two dots `..` mean "the folder above" — you move up one level.
2. **b)** `dir` lists everything in the current folder on Windows (`ls` on Mac/Linux).
3. **b)** The path before `>` is your current location in the folder maze.
4. **a)** `cls` clears the screen on Windows; Mac/Linux use `clear`.
5. **b)** Tab helps avoid typos by completing folder names as you type.

</details>

---

## What's Next

→ [Lesson 1.3: Running Your First Script](../lesson-1-3-running-your-first-script/README.md) — master the full launch sequence: save, `cd`, run.

---

*You can walk the maze. You can list what is inside each room. You found the treasure. Maze master status: unlocked!*

[← Choose language](README.md)
