# times_table.py
# Quest Gate — for loop prints the 3 times table

print("=== TIMES TABLE ===")
number = 3

# TODO: Use for and range(1, 11) to print "3 x 1 = 3" through "3 x 10 = 30"
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

print("Table complete!")
