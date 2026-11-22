# character_stats.py
# Adventure Workshop — labeled stat boxes (dictionaries)

character = {
    "name": "Alex",
    "level": 5,
    "hp": 42,
}

print("=== CHARACTER STATS ===")
print(f"Name: {character['name']}")
# TODO: Print the level and the HP the same way:
#       f"Level: {character['level']}" and f"HP: {character['hp']}"

# TODO: Replace "?" with character.get("magic", 0)
magic = "?"
print(f"Magic: {magic}")

# TODO: Replace "?" with character.get("skill", "none")
skill = "?"
print(f"Special skill: {skill}")

print("Edit the dict keys above, then run again!")
