# High Score List — Lesson 4.2 Stretch

> [Русский →](high_score.ru.md)

Build a **high score board** using a list — no functions required yet.

---

## Goal

Create `high_scores.py` (any folder you like) that:

1. Starts with a list of three scores: `[120, 85, 200]`
2. Asks the player to type a new score with `input()` and `int()`
3. Uses `.append()` to add the new score
4. Prints every score on its own line with a rank number (`1.`, `2.`, …)

---

## Sample run

```text
=== HIGH SCORES ===
Enter your score: 150
1. 120
2. 85
3. 200
4. 150
```

---

## Hints

- Convert input: `new_score = int(input("Enter your score: "))`
- Use the same `for i in range(len(scores)):` pattern from [inventory.py](../starter/inventory.py)
- **Stuck on sorting?** Bonus only — try `scores.sort(reverse=True)` after you finish the basic version

---

## Bonus stars

Print the **highest** score after the list (hint: loop through and track the biggest number, or explore `max(scores)`).

[← Lesson 4.2](../README.md)
