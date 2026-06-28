# gate_quest.py
# Block 3 capstone — guess the secret code (if + while)
# Copy to my_quest/gate_quest.py at your project root

import random

secret = random.randint(1, 10)
guesses_left = 3

print("=== QUEST GATE ===")
print("Guess the secret number from 1 to 10.")
print(f"You have {guesses_left} tries.")

while guesses_left > 0:
    guess_text = input("Your guess: ")
    guess = int(guess_text)

    if guess == secret:
        print("Correct! The gate opens. Quest complete!")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")

    guesses_left = guesses_left - 1

    if guesses_left > 0:
        print(f"Tries left: {guesses_left}")
    else:
        print(f"Out of tries! The secret was {secret}.")

print("Thanks for playing the Quest Gate!")
