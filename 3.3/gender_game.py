gender = input("What is your gender (M or F): ").strip().lower()
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
title = ""
if age >= 20:
    if gender == "m":
        title = "Mr."
    elif gender == "f":
        married = input(f"Are you married, {first_name} (y or n)? ").strip().lower()
        if married == "y":
            title = "Mrs."
        elif married == "n":
            title = "Ms."
        else: 
            print("I do not understand. please answer y/n.")
    else:
        print("no such gender exists. Please try again.")

print(f"Then I shall call you {title} {first_name} {last_name}.")