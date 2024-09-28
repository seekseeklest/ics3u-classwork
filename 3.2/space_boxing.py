gravity = {1: 0.78, 2: 0.39, 3: 2.65, 4: 1.17, 5: 1.05, 6: 1.23}
earth_weight = float(input("please enter your current earth weight: "))

print()
print("I have information for the following planets:")
print("     1. Venus    2. Mars    3. Jupiter")
print("     4. Saturn   5. Uranus  6. Neptune")

planet = int(input("which planet are you visiting? "))

if planet not in gravity: 
    print("Invalid planet number. Try again.")
else:
    space_weight = earth_weight * gravity[planet]
    print(f"Your weight would be {space_weight} on that planet.")