gender = input("What is your gender (M or F): ").strip().lower()
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
if age >= 20:
    if gender == "m":
        first_name = "Mr. " + first_name
    elif gender == "f":
        married = input(f"Are you married, {first_name} (y or n)? ").strip().lower()
        if married == "y":
            first_name = "Mrs. " + first_name
        elif married == "n":
            first_name = "Ms. " + first_name
        else: 
            print("I do not understand. please answer y/n.")
    else:
        print("no such gender exists. Please try again.")

print(f"Then I shall call you {first_name} {last_name}.")