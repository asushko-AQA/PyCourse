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
        "description": "Dusty scrolls line the shelves. An old desk stands in the corner.",
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
    room = rooms[room_id]
    print(f"\n=== {room['name']} ===")
    print(room["description"])
    if "item" in room:
        print(f"You see a {room['item']} here.")


def move(room_id, direction):
    room = rooms[room_id]
    # TODO: If direction in room: print(f"You go {direction}.") and return room[direction]
    # TODO: Otherwise: print("You cannot go that way.") and return room_id
    return room_id


def show_inventory():
    # TODO: If len(inventory) == 0: print("Your pack is empty.")
    # TODO: Otherwise: print("=== INVENTORY ===") and a numbered list
    #       with a for loop, like Lesson 4.2: f"{i + 1}. {inventory[i]}"
    pass


def take_item(room_id):
    room = rooms[room_id]
    # TODO: If "item" in room:
    #           item = room["item"]
    #           add it to the list with inventory.append(item)
    #           remove it from the room with del room["item"]
    #           print(f"You picked up the {item}.")
    # TODO: Otherwise: print("Nothing to take here.")
    pass


def main():
    print("=== ADVENTURE WORKSHOP ===")
    print("Commands: north, south, east, west, take, inventory, open, quit")

    current_room = "start"

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
