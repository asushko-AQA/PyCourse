# inventory.py
# Adventure Workshop — pack items in a list

inventory = ["torch", "rope"]
inventory.append("key")

print("=== INVENTORY ===")

for i in range(len(inventory)):
    print(f"{i + 1}. {inventory[i]}")

print(f"You are carrying {len(inventory)} items.")
