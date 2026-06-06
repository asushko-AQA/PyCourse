# choose_path.py — reference solution

print("=== CHOOSE YOUR PATH ===")
print("You stand at a fork in the quest trail.")

choice = input("Go left or right? (left/right): ").lower().strip()

if choice == "left":
    print("You find a glowing crystal! +10 quest points.")
elif choice == "right":
    print("You meet a friendly robot guide. It waves hello.")
else:
    print("You sit down for a snack. Adventure can wait!")

print("Thanks for choosing!")
