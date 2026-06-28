# Lesson 0.2: How Code Comes Alive

> **Course:** Python Basics & Command Line Magic · **Block:** Getting Started · **~30 min**
> [Choose language](README.md) · [Русский →](ru.md)

<!-- meta
minutes: 30
-->

---

## Title

**Warm-Up B — How Code Comes Alive: The Python Translator**

---

## Explanation

In Lesson 0.1 you learned that a program is a list of exact instructions. But how do those words you type actually *do* something? Let's follow the journey from **your code** to **a real result on screen**.

When you write Python, you save it in a file ending in `.py` — that's your **source code** (the recipe you wrote). On its own, that file is just text. To make it *run*, the computer uses a helper called the **Python interpreter**.

The interpreter is like a **translator** standing between you and the computer. It reads your Python **one line at a time, top to bottom**, and tells the computer exactly what to do for each line. The computer does it, and you see the **result** — text, a drawing, or a game window.

So the path is always:

**your code (`.py` file)** → **Python interpreter (translator)** → **result you see**

### Step 1: Source code is your written recipe

You type instructions into a file like `hello.py`. Nothing happens yet — it's just saved text, waiting.

### Step 2: The interpreter is the translator

Python comes with an interpreter (you'll install it in Lesson 1.1). When you "run" your file, the interpreter wakes up and starts reading your code.

### Step 3: Line by line, top to bottom

The interpreter reads **line 1**, does it, then **line 2**, and so on — in order. This is why **order matters**: swap two lines and the result can change.

### Step 4: The result appears

For each `print(...)`, the interpreter tells the computer to show text. Later you'll make drawings and games — but the journey is always the same: code → interpreter → result.

### Step 5: A peek at your first program

Here's the classic first program, `hello.py`:

```python
print("Hello, world!")
```

When the interpreter reads this one line, the computer shows `Hello, world!`. You'll type and run this for real in Lesson 1.1.

---

## Code Example

A first program is often just a line or two — `hello.py`:

```python
print("Hello, world!")
print("My code is alive!")
```

The interpreter reads line 1, shows its text, then reads line 2 and shows its text — always in order.

---

## Code Execution

To run a Python file, you'll type a command like this (you'll do it for real in Lesson 1.1):

```text
python hello.py
```

The Python interpreter reads the file top to bottom and the computer shows:

```text
Hello, world!
My code is alive!
```

(No need to run anything yet — this preview shows how "running" turns code into a result.)

---

## Quick Drills

No computer needed — predict and reason:

1. **Predict the output.** If the program is `print("A")` then `print("B")`, what shows first?
2. **Swap the lines.** Now the program is `print("B")` then `print("A")`. What changes, and why?
3. **Name the parts.** In the journey *code → interpreter → result*, which part is the "translator"?

---

## Practice Task

**Quest name:** Trace the Translator

On paper, "be the interpreter." Read this tiny program **line by line** and write down, in order, exactly what the computer would show:

```python
print("Loading...")
print("Ready!")
print("Go!")
```

**Rules of the game:**
- Process one line at a time, top to bottom — just like the interpreter.
- Write the output lines in the order they appear.
- Bonus: add a 4th `print(...)` line of your own and predict where it lands in the output.

---

## Debug Corner

**Problem:** A program prints lines in the "wrong" order.

```python
print("Second")
print("First")
```

Output:

```text
Second
First
```

**Cause:** The interpreter runs lines **top to bottom**, not by what the words say. It printed `Second` first because that line came first.

**Fix:** Put the lines in the order you want them to run. The computer follows position, not meaning.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What does the Python **interpreter** do?
   - **a)** Reads your code and tells the computer what to do, line by line
   - **b)** Draws the icons on your desktop
   - **c)** Stores your files forever
   - **d)** Connects your computer to the internet

2. What is "source code"?
   - **a)** The result you see on screen
   - **b)** The instructions you write and save in a `.py` file
   - **c)** The computer's battery
   - **d)** A type of error message

3. In what order does the interpreter read your program?
   - **a)** Bottom to top
   - **b)** In a random order
   - **c)** Top to bottom, one line at a time
   - **d)** Only the lines with `print`

4. The journey of a program is best described as:
   - **a)** result → interpreter → code
   - **b)** code → interpreter → result
   - **c)** interpreter → code → result
   - **d)** code → result → interpreter

5. Why might two lines print in a surprising order?
   - **a)** The computer guesses what you mean
   - **b)** Whichever line is higher in the file runs first
   - **c)** `print` always sorts text alphabetically
   - **d)** The interpreter skips the first line

---

<details><summary>Click to reveal answers</summary>

1. **a)** The interpreter reads code line by line and drives the computer.
2. **b)** Source code is the instructions you write in a `.py` file.
3. **c)** It reads top to bottom, one line at a time.
4. **b)** code → interpreter → result.
5. **b)** Lines run in file order, top to bottom — position, not meaning.

</details>

---

## What's Next

→ [Lesson 1.1: Installing Python & VS Code](../../block-1-meeting-your-computer/lesson-1-1-installing-python/README.md) — install the interpreter and run your very first script for real.

---

*You now know the journey: code → interpreter → result. Time to install Python and make it happen yourself!*

[← Choose language](README.md)
