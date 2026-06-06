# inventory.py
# Adventure Workshop — pack items in a list

inventory = ["torch", "rope"]

# TODO: Add a new item with .append()
inventory.append("key")

print("=== INVENTORY ===")

# TODO: Print a numbered list with a for loop
for i in range(len(inventory)):
    print(f"{i + 1}. {inventory[i]}")

print(f"You are carrying {len(inventory)} items.")
