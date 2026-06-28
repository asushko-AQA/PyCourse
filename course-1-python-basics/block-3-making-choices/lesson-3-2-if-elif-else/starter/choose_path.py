# choose_path.py
# Quest Gate — pick a path and see what happens

print("=== CHOOSE YOUR PATH ===")
print("You stand at a fork in the quest trail.")

# TODO: Ask left or right with input(); use .lower() so "Left" works too
choice = input("Go left or right? (left/right): ").lower().strip()

# TODO: If choice is "left", print about finding a crystal
if choice == "left":
    print("You find a glowing crystal! +10 quest points.")

# TODO: Elif choice is "right", print about a robot guide
elif choice == "right":
    print("You meet a friendly robot guide. It waves hello.")

# TODO: Else print a snack break message
else:
    print("You sit down for a snack. Adventure can wait!")

print("Thanks for choosing!")
