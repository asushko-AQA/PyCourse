# ascii_pattern.py
# Quest Gate — nested loops draw a star pyramid

print("=== ASCII PATTERN ===")

# TODO: Outer loop: rows 1 to 5
for row in range(1, 6):
    # TODO: Inner loop: print row number of stars
    for star in range(row):
        print("*", end="")
    print()

print("Pattern complete!")
