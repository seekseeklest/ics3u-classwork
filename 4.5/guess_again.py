import random

random_number = random.randint(1, 100)

MAX_GUESSES = 7
guesses = 0

print("I'm thinking of a number between 1 and 100.")
print(f"You have {MAX_GUESSES} tries to guess it.\n")

while True:
    guess = int(input(f"Guess #{guesses + 1}: "))
    guesses += 1

    if guess == random_number:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess > random_number:
        print("Too high.")
    else:
        print("Too low.")
    
    if guesses == MAX_GUESSES:
        print(f"\nSorry, you've used all {MAX_GUESSES} guesses. The correct number was {random_number}.")
        break
