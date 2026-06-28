# Debug Quotes Challenge — Lesson 2.5

> [Русский →](debug_quotes.ru.md)

Practice fixing broken strings — the same skill you need in the capstone.

---

## Broken code 1

```python
print("=== CREATOR DATA PACK ===)
```

**Error:** `SyntaxError` — unterminated string  
**Fix:** Add the missing closing quote: `"=== CREATOR DATA PACK ==="`

---

## Broken code 2

```python
name = input("What is your name? )
```

**Error:** `SyntaxError` — missing `"` before the closing `)`  
**Fix:** `name = input("What is your name? ")`

---

## Your mission

1. In your `my_data/creator_pack.py`, break one quote on purpose.
2. Run the script — read the error line number.
3. Fix and run until you see `Block 2 complete!`

[← Lesson 2.5](../README.md)
