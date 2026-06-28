# Lesson 3.1: Booleans and Comparisons

> **Course:** Python Basics & Command Line Magic · **Block:** Making Choices · **~30 min**  
> [Choose language](README.md) · [Русский →](ru.md)

---

## Title

**Level 11 — True or False Quest**

---

## Explanation

Welcome to the **Quest Gate**! Before you choose paths in a story, you need to ask questions like "Are these equal?" or "Is this bigger?" Python answers with **`True`** (pass) or **`False`** (fail).

You already know variables from Block 2. Now you compare values:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | equal to | `5 == 5` → `True` |
| `!=` | not equal | `3 != 3` → `False` |
| `>` | greater than | `10 > 7` → `True` |
| `<` | less than | `4 < 2` → `False` |
| `>=` | greater or equal | `5 >= 5` → `True` |
| `<=` | less or equal | `2 <= 9` → `True` |

**`and`** — both must be True. **`or`** — at least one must be True:

```python
print(True and False)   # False
print(True or False)    # True
```

**`not`** flips True ↔ False — like reversing a quest stamp:

```python
print("not False:", not False)   # True
print("not (5 == 3):", not (5 == 3))   # True — 5 == 3 is False, not False is True
```

**Not yet:** `if` statements come in Lesson 3.2. Today you only **print** comparison results.

---

### Step 1: Open the quiz script

Open [starter/true_false_quiz.py](starter/true_false_quiz.py). Some lines are ready; others have `# TODO`.

---

### Step 2: cd to this lesson folder

**Path A — PyCourse repo:**

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-1-booleans
```

**Path B — your own folder:** Copy `true_false_quiz.py` anywhere. `cd` to that folder before running.

---

### Step 3: Run and compare

```text
python starter\true_false_quiz.py
```

**Mac/Linux:** Use forward slashes — `python starter/true_false_quiz.py`. List files with `ls` instead of `dir`.

**Expected output:**

```text
=== TRUE OR FALSE QUEST ===
5 == 5: True
5 == 3: False
10 > 7: True
4 < 2: False
'cat' == 'cat': True
5 >= 5: True
3 != 3: False
True and False: False
True or False: True
Predict each line before you run!
```

---

## Code Example

```python
print("5 == 5:", 5 == 5)
print("10 > 7:", 10 > 7)
print("True and False:", True and False)
```

Each `print()` shows a **label** and the **True/False result**.

---

## Code Execution

```text
cd course-1-python-basics\block-3-making-choices\lesson-3-1-booleans
python starter\true_false_quiz.py
```

**Expected output:** See Step 3 above.

---

## Quick Drills

1. **Predict first** — cover the screen, guess each True/False, then run.
2. **Swap numbers** — change `10 > 7` to `3 > 7`. Predict. Run.
3. **New line** — add `print("100 == 99:", 100 == 99)`.

---

## Practice Task

**Quest name:** Build Your Own Quiz Line

1. Add three new comparison lines using `==`, `<`, and `!=`.
2. Add one line with `and` comparing two numbers.
3. Add one line with `or`.

**Reference solution:** [solution/true_false_quiz.py](solution/true_false_quiz.py)

---

## Debug Corner

**Problem:** You write `if 5 = 5:` and get `SyntaxError`.

**Cause:** A single `=` **puts a value in a box** (assignment). To **compare**, use **`==`** (two equals signs).

**Fix:** Use `5 == 5` for comparisons. Save `=` for `name = "Alex"`.

---

## Quick Check

Pick the best answer for each question. Try without scrolling down first!

1. What is the result of `5 == 5`?
   - **a)** `True`
   - **b)** `False`
   - **c)** `5`
   - **d)** An error

2. What is the result of `3 != 3`?
   - **a)** `True`
   - **b)** `False`
   - **c)** `3`
   - **d)** `0`

3. A single `=` (one equals sign) is used for…
   - **a)** Putting a value in a variable (assignment)
   - **b)** Comparing two values
   - **c)** Adding numbers
   - **d)** Printing True or False

4. What is `True and False`?
   - **a)** `True`
   - **b)** `False`
   - **c)** `None`
   - **d)** `"True and False"`

5. What is `True or False`?
   - **a)** `True`
   - **b)** `False`
   - **c)** `None`
   - **d)** An error

---

<details><summary>Click to reveal answers</summary>

1. **a)** `==` checks equality; `5 == 5` is `True`.
2. **b)** `!=` means "not equal"; `3` equals `3`, so `False`.
3. **a)** One `=` assigns (`name = "Alex"`); two `==` compare.
4. **b)** `and` needs **both** True; one False makes the whole thing False.
5. **a)** `or` needs **at least one** True; True or False is True.

</details>

---

## What's Next

→ [Lesson 3.2: if, elif, else](../lesson-3-2-if-elif-else/README.md) — fork in the quest path!

---

*Comparisons give True or False. Next you will use them to choose what happens!*

[← Choose language](README.md)
