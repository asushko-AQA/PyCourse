# Wrong Folder Scenarios — Fix It!

Practice diagnosing launch problems. Do each scenario in order.

All scripts for this lesson live in **`starter/`**.

## Scenario 1 — Wrong folder

1. Open terminal in VS Code while `starter/hello.py` is visible in the Explorer.
2. `cd` to this lesson folder, then `cd ..` twice so you are **outside** the lesson folder.
3. Run:

```text
python starter\hello.py
```

**What happened?** Write down the error message.

**Fix:** `cd` back to the lesson folder (where `starter/` lives). Run again until you see three lines of output.

- [ ] I saw the error
- [ ] I fixed it by changing folder

## Scenario 2 — Wrong filename

1. From the **lesson folder**, run:

```text
python starter\helloo.py
```

(extra letter on purpose)

**What happened?**

**Fix:** Type the exact filename: `python starter\hello.py`

- [ ] I saw the error
- [ ] I fixed the filename

## Scenario 3 — Hidden .txt extension

1. In **`starter/`**, save a copy of your script as `test.py`.
2. In File Explorer, check **View → Show → File name extensions** (Windows).
3. If the file shows as `test.py.txt`, rename it to `test.py`.
4. From the lesson folder, run:

```text
python starter\test.py
```

- [ ] I confirmed the file ends with `.py` only
- [ ] `python starter\test.py` works

---

**Русская версия:** [wrong_folder_scenarios.ru.md](wrong_folder_scenarios.ru.md)
