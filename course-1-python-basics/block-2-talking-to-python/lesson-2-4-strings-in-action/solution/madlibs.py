# madlibs.py
# Data Lab — Story Factory

hero = input("Name a hero: ")
creature = input("Name a silly creature: ")
place = input("Name a place: ")
power = input("Name a superpower: ")

short_creature = creature[0:3]

print("=== STORY FACTORY ===")
print(f"{hero} battled a {creature.lower()} in {place}.")
print(f"The creature's first three letters: {short_creature}")
print(f"{hero} used {power.upper()} to win!")
print("The end.")
