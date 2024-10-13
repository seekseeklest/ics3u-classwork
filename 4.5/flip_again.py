# change input value into string format:
import random

again = "y"

while again == "y":
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ").lower()


# change into while true loop:
import random

while True:
    flip = random.randrange(2)  # 0 or 1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ").lower()

    if again != "y":
        break
   

# In this version of the code, there is no need for the again = "y" line before the loop, because the loop no longer checks the value of again at the start. 