# Slice Challenge (Bonus) — Lesson 2.4

> [Русский →](slice_challenge.ru.md)

Slicing cuts a piece out of a string. Format: `word[start:end]` — includes `start`, stops **before** `end`.

---

## Warm-up

```python
word = "Minecraft"
print(word[0:3])
```

**Your guess:** _______  
**Answer:** `Min` (letters at index 0, 1, 2)

---

## Challenge 1

```python
hero = "Alex"
print(hero[0:2])
```

What prints? _______

---

## Challenge 2 — IndexError (optional)

```python
short = "Hi"
print(short[0:10])
```

This actually works in Python — it stops at the end of the string. Output: `Hi`

But this crashes:

```python
print(short[5])
```

**Error:** `IndexError: string index out of range`  
**Cause:** Index 5 does not exist in a 2-letter string.

---

## Your turn

In [madlibs.py](../starter/madlibs.py), change `[0:3]` to `[0:2]` on the hero slice. Run and see the difference.

[← Lesson 2.4](../README.md)
