# Slice Practice — Bonus Quest

Slicing grabs part of a string: `word[0:3]` means "from index 0 up to (but not including) 3."

## Safe slices

```python
game = "Minecraft"
print(game[0:3])   # Min
print(game[0:4])   # Mine
```

## Bonus challenge — IndexError

What happens if you slice past the end?

```python
word = "Hi"
print(word[0:10])  # Try this — does it crash?
```

**Answer:** Python is forgiving — it gives `"Hi"`, not an error. But an **empty** wrong slice on a one-letter word can surprise you:

```python
letter = "A"
print(letter[5:10])  # What prints?
```

**Answer:** Empty string `""` — no crash, just nothing!

## Your quest

1. Pick a game name at least 5 letters long
2. Print the first 3 letters with `[0:3]`
3. Print the whole name in `.upper()` and `.lower()`

---

**Русская версия:** [slice_practice.ru.md](slice_practice.ru.md)
