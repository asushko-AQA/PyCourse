# character_stats.py
# Adventure Workshop — labeled stat boxes (dictionaries)

character = {
    "name": "Alex",
    "level": 5,
    "hp": 42,
}

print("=== CHARACTER STATS ===")
print(f"Name: {character['name']}")
print(f"Level: {character['level']}")
print(f"HP: {character['hp']}")

magic = character.get("magic", 0)
print(f"Magic: {magic}")

skill = character.get("skill", "none")
print(f"Special skill: {skill}")

print("Edit the dict keys above, then run again!")
