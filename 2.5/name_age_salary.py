name = input("What is your name? ")
print()
age = int(input(f"Hi {name}! How old are you? "))
print()
if age <= 10:
    abduct = str.lower(input(f"Wow {name} you're only {age}? Do you want to come get some candy from my van? "))
    if abduct in ["yes", "sure", "of course"]:
        print(f"Alright come and follow me {name}... I'll show you a real surprise...")
        print("BAM!")
        print()
        print("the sound of a body being dragged could be heard...")
    elif abduct in ["no", "nah", "i dont wan't to"]:
        print(f"Alright then, your loss {name}. that candy would've tasted reaaaallly good.")
    else:
        print("I'm not quite sure I understand.")
elif age > 10 and age < 18:
    print(f"{name} babe, I think you're really hot for a {age} year old, can we exchange numbers?")
elif age >= 18:
    print(f"Gosh damn you're old {name}! If you're {age} I guess I'm dead and buried!")
    salary = round(float(input("Anyways, how much do you make a year? ")))
    if salary > 0 and salary <= 40000:
        print(f"Wow only ${salary} huh? I think you should find a better job mate.")
    elif salary > 40000 and salary <= 80000:
        print(f"${salary}? It's honest work, I'll give you that.")
    elif salary > 80000 and salary < 120000:
        print(f"${salary}? You're living well.")
    elif salary >= 120000 and salary <= 200000:
        print(f"you make ${salary}?? Spare me some change!")
    elif salary > 200000:
        print(f"${salary}?!?!? That's absolutely nuts!! I'd give my left nut to be that wealthy!!")
    else:
        print("are you in debt or something???")
else:
    print("are you still a fetus little bro?")
