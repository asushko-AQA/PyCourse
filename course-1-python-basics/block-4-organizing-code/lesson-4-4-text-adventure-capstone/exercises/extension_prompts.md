# Extension Prompts — Lesson 4.4

> [Русский →](extension_prompts.ru.md)

Finished the base adventure? Level up with one or more of these ideas.

---

## New commands

| Command | Idea |
|---------|------|
| `look` | Reprint the room description without moving |
| `help` | Print the command list again |
| `drop sword` | Remove an item from inventory back into the room |

---

## More rooms

Add a `"cave"` room connected from `"garden"` with `"north": "cave"`. Put a `"magic gem"` item inside and require **both** the key and the gem to win.

---

## Health points

Store `"hp": 100` in a player dict. Subtract 10 HP in a `"trap"` room. Game over when HP reaches 0.

---

## Random encounter

```python
import random

if random.randint(1, 3) == 1:
    print("A friendly fox blocks the path!")
```

Use sparingly — one surprise room is enough for now.

---

## Share your world

Draw a map on paper and label room ids (`start`, `library`, …) so a friend can play without reading your code.

[← Lesson 4.4](../README.md)
