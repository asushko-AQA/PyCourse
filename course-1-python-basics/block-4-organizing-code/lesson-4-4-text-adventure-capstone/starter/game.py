# game.py
# Adventure Workshop capstone — fill in the helpers, then copy to my_adventure/game.py

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
    # TODO: Look up rooms[room_id]
    # TODO: Print === room name === and the description
    pass


def move(room_id, direction):
    # TODO: If direction is a key in this room, print "You go ..." and return the new room id
    # TODO: Otherwise print "You cannot go that way." and return room_id
    # Save the result in the game loop: current_room = move(current_room, command)
    return room_id


def show_inventory():
    # TODO: If inventory is empty, print "Your pack is empty."
    # TODO: Otherwise print a numbered list of items
    pass


def take_item(room_id):
    # TODO: If the room has an "item", append it to inventory and delete it from the room
    # TODO: Otherwise print "Nothing to take here."
    pass


def main():
    print("=== ADVENTURE WORKSHOP ===")
    print("Commands: north, south, east, west, take, inventory, open, quit")

    current_room = "start"

    # TODO: Loop forever:
    #   show_room(current_room)
    #   command = input("What do you do? ").lower()
    #   quit -> print thanks and break
    #   north/south/east/west -> current_room = move(current_room, command)
    #   take -> take_item(current_room)
    #   inventory -> show_inventory()
    #   open in the garden with "golden key" in inventory -> print the win line and break
    #   anything else -> print the command list
    print("Finish the game loop, then run again!")


main()
