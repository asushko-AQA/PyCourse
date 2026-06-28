# Mental Math Drills — Lesson 2.3

> [Русский →](mental_math.ru.md)

Predict the output **before** you run Python. Write your guess, then check with a tiny script or the calculator.

---

## Round 1: Pure numbers

| Expression | Your guess | Actual |
|------------|------------|--------|
| `10 + 3` | | |
| `10 - 3` | | |
| `10 * 3` | | |
| `10 / 3` | | |

**Hint:** `/` always gives a decimal (float), even when the answer is a whole number.

---

## Round 2: Variables

```python
a = 8
b = 2
```

| Expression | Your guess | Actual |
|------------|------------|--------|
| `a + b` | | |
| `a - b` | | |
| `a * b` | | |
| `a / b` | | |

---

## Round 3: int() with input

If you type `5` and `4` at the prompts:

```python
num1 = int(input("First: "))   # you type 5
num2 = int(input("Second: "))  # you type 4
print(num1 + num2)
```

What prints? _______

---

## Stretch

What happens if you type `hello` instead of a number? Run [starter/calculator.py](../starter/calculator.py) and try it — read the `ValueError` message.

[← Lesson 2.3](../README.md)
