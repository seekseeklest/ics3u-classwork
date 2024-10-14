import random

print("HERE COMES THE DICE!")

while True:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    
    print(f"Roll #1: {roll1}")
    print(f"Roll #2: {roll2}")
    print(f"The total is {roll1 + roll2}!\n")
    
    if roll1 == roll2:
        break