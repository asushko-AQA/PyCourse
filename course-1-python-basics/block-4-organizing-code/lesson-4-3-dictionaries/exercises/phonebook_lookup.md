# Phonebook Lookup — Lesson 4.3 Stretch

> [Русский →](phonebook_lookup.ru.md)

Build a tiny **phonebook** with a dictionary of names and numbers.

---

## Goal

Create `phonebook.py` that:

1. Stores at least three contacts in a dict — keys are names, values are phone strings
2. Asks `Whose number? ` with `input()`
3. Uses `.get()` to print the number, or `"Not found"` if the name is missing

---

## Sample dict

```python
phonebook = {
    "Alex": "555-0100",
    "Sam": "555-0200",
    "Jordan": "555-0300",
}
```

---

## Sample run

```text
=== PHONEBOOK ===
Whose number? Sam
Number: 555-0200
```

Second run:

```text
Whose number? Riley
Number: Not found
```

---

## Hints

- Lookup: `number = phonebook.get(name, "Not found")`
- Use `.strip()` on input so spaces do not break lookups
- **Bonus:** Loop through all contacts and print `Name: number` on separate lines

[← Lesson 4.3](../README.md)
