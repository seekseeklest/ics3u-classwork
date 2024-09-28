def how_old(name: str, age: int) -> str:
    if age <= 0:
        return f"Are you a fetus, {name}?"
    elif age < 16:
        return f"you can't drive, {name}."
    elif age in range(16, 18):
        return f"you can drive but you can't vote, {name}."
    elif age in range(18, 21):
        return f"you can vote, but you can't rent a car, {name}."
    else:
        return f"you can do pretty much anything as long as it's legal, {name}."
    
if __name__ == "__main__":
    name = str(input("What's your name choom? "))
    age = int(input(f"Okay how old are you {name}? "))
    print(how_old(name, age))