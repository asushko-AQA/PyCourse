# game.py
# Adventure Workshop capstone — room-based text adventure (skeleton)

rooms = {
    "start": {
        "name": "Workshop Door",
        "description": "You stand at the workshop entrance. Paths lead north and east.",
        "north": "library",
        "east": "garden",
    },
    "library": {
        "name": "Scroll Library",
        "description": "Dusty scrolls line the shelves. A golden key glints on a desk.",
        "south": "start",
        "item": "golden key",
    },
    "garden": {
        "name": "Hidden Garden",
        "description": "Moonlight filters through leaves. A treasure chest waits here.",
        "west": "start",
    },
}

inventory = []


def show_room(room_id):
    # TODO: Print === room name === and description
    room = rooms[room_id]
    print(f"\n=== {room['name']} ===")
    print(room["description"])


def move(room_id, direction):
    # TODO: If direction exists, return the new room id; else return room_id unchanged
    room = rooms[room_id]
    if direction in room:
        print(f"You go {direction}.")
        return room[direction]
    print("You cannot go that way.")
    return room_id


def show_inventory():
    # TODO: Print numbered list or "Your pack is empty."
    if len(inventory) == 0:
        print("Your pack is empty.")
        return
    print("=== INVENTORY ===")
    for i in range(len(inventory)):
        print(f"{i + 1}. {inventory[i]}")


def take_item(room_id):
    # TODO: If room has "item", append to inventory and remove from room
    room = rooms[room_id]
    item = room.get("item")
    if item is None:
        print("Nothing to take here.")
        return
    inventory.append(item)
    del room["item"]
    print(f"You picked up the {item}.")


def main():
    print("=== ADVENTURE WORKSHOP ===")
    print("Commands: north, south, east, west, take, inventory, open, quit")

    current_room = "start"

    # TODO: Game loop — show room, read command, update current_room from move()
    while True:
        show_room(current_room)
        command = input("What do you do? ").lower().strip()

        if command == "quit":
            print("Thanks for playing!")
            break
        elif command in ("north", "south", "east", "west"):
            current_room = move(current_room, command)
        elif command == "take":
            take_item(current_room)
        elif command == "inventory":
            show_inventory()
        elif command == "open":
            if current_room == "garden" and "golden key" in inventory:
                print("The chest opens! You win!")
                break
            else:
                print("The chest is locked. You need a key from the library.")
        else:
            print("Try: north, south, east, west, take, inventory, open, quit")


main()
