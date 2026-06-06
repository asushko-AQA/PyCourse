# ascii_pattern.py — reference solution

print("=== ASCII PATTERN ===")

for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()

print("Pattern complete!")
