# gate_quest.py
# Block 3 capstone skeleton — copy to my_quest/gate_quest.py
# Change the secret range to 1–20 and guesses_left to 5, then fill the loop.

import random

# TODO: Pick a secret number from 1 to 20 with random.randint
secret = 0
# TODO: Give the player 5 tries
guesses_left = 0

print("=== QUEST GATE ===")
print("Guess the secret number from 1 to 20.")
print(f"You have {guesses_left} tries.")

# TODO: while guesses_left > 0:
#   ask for a guess and convert it with int()
#   if the guess equals secret: print the win line and break
#   elif the guess is lower: print "Too low."
#   else: print "Too high."
#   subtract 1 from guesses_left
#   if tries remain, print how many are left
#   else print the secret number

print("Thanks for playing the Quest Gate!")
