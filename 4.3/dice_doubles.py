import random

print("HERE COMES THE DICE!")

roll_count = 0 

while True:
    roll_count += 1
   
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    
    print(f"\nRoll #{roll_count}: {roll1}")
    print(f"Roll #{roll_count}: {roll2}")
    total = roll1 + roll2
    print(f"The total is {total}!")
    
    if roll1 == roll2:
        break  
