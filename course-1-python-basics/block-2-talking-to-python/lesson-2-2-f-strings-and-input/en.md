# Lesson 2.2: f-strings and input()

> **Course:** Python Basics & Command Line Magic · **Block:** Talking to Python · **~30–45 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 7 — Ask and Answer**

---

## Explanation

In Lesson 2.1 you filled magic boxes yourself. Now the **visitor** fills them! `input()` is like a microphone — Python asks a question and waits for you to type an answer.

**f-strings** are fill-in-the-blank scrolls. Put variables inside `{curly braces}` and Python swaps in the real values.

**Important:** `input()` always gives you **text** (a string), even if you type numbers. Lesson 2.3 will teach `int()` to fix that for math.

---

### Step 1: Ask with input()

```python
name = input("What is your name? ")
```

The text in quotes is the **prompt** — the question shown to the user. After you type and press Enter, the answer lands in `name`.

---

### Step 2: Answer with f-strings

```python
print(f"Hello, {name}!")
```

The `f` before the opening quote tells Python: "replace `{name}` with the real value."

Without `f`, Python prints the literal text `{name}` — a common bug!

---

### Step 3: Open greeting.py

Open [starter/greeting.py](starter/greeting.py). Two questions and two f-string responses are ready as TODOs.

---

### Step 4: cd and run

**Path A:**

```text
cd course-1-python-basics\block-2-talking-to-python\lesson-2-2-f-strings-and-input
python starter\greeting.py
```

**Path B:** Run from any folder where you saved `greeting.py`.

**Type when prompted:**

```text
What is your name? Alex
How old are you? 11
```

**Expected output:**

```text
Hello, Alex! Welcome to the Data Lab.
You said you are 11 years old.
Type your answers when the terminal waits for you!
```

---

## Code Example

```python
name = input("What is your name? ")
age = input("How old are you? ")

print(f"Hello, {name}! Welcome to the Data Lab.")
print(f"You said you are {age} years old.")
```

---

## Code Execution

```text
python starter\greeting.py
```

Answer both prompts. See personalized output.

---

## Quick Drills

1. **Missing f** — change `print(f"Hello...` to `print("Hello...` (remove `f`). Run. See `{name}` printed literally. Fix it.
2. **Third question** — add `color = input("What is your favorite color? ")` and an f-string response.
3. **Predict** — before running, write what you expect for your own name and age.

---

## Practice Task

**Quest name:** Personal Greeter

1. Complete both TODO f-strings in [starter/greeting.py](starter/greeting.py).
2. Add a third question — favorite color, game, or hobby.
3. Add a multiline f-string using `\n`:

```python
print(f"\n{name}, you are officially a Data Lab apprentice!")
```

**Bonus:** Ask two questions in one story line: name + favorite food.

**Reference solution:** [solution/greeting.py](solution/greeting.py)

---

## Debug Corner

**Problem:** Output shows `Hello, {name}!` instead of `Hello, Alex!`

**Cause:** You forgot the `f` before the string. Without it, `{name}` is just text, not a variable slot.

**Fix:** Write `print(f"Hello, {name}!")` — note the `f` right before the opening quote.

---

## What's Next

→ [Lesson 2.3: Math Operators](../lesson-2-3-math-operators/README.md) — cast input to numbers with `int()`.

---

*You can ask and answer now. Next: calculator spells!*

[← Choose language](README.md)
