def space_boxing(earth_weight: float, planet: int) -> float:
    gravity = {1: 0.78, 2: 0.39, 3: 2.65, 4: 1.17, 5: 1.05, 6: 1.23}
    if planet not in gravity: 
        return -1
    else:
        return earth_weight * gravity[planet]

if __name__ == "__main__":
    earth_weight = float(input("please enter your current earth weight (lb): "))

    print()
    print("I have information for the following planets:")
    print("     1. Venus    2. Mars    3. Jupiter")
    print("     4. Saturn   5. Uranus  6. Neptune")
    print()
    planet = int(input("which planet are you visiting? "))

    space_weight = space_boxing(earth_weight, planet)
    if space_weight < 0:
        print("Invalid.")
    else:
        print(f"Your weight would be {space_weight} lb on that planet.")