import random

random_number = random.randint(1, 100)

max_guesses = 7
guesses = 0

print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_guesses} tries to guess it.\n")

while guesses < max_guesses:
    guess = int(input(f"Guess {guesses + 1}: "))
    guesses += 1
    
    if guess == random_number:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess > random_number:
        print("Too high.")
    else:
        print("Too low.")
    
    if guesses == max_guesses:
        print(f"\nSorry, you've used all {max_guesses} guesses. The correct number was {random_number}.")

