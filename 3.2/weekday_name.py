days = ["Weekday 1: Monday", "Weekday 2: Tuesday", "Weekday 3: Wednesday", "Weekday 4: Thursday", "Weekday 5: Friday", "Weekday 6: Saturday", "Weekday 7:Sunday"]

what_day = int(input("Enter the number of any weekday (1-7): "))

if what_day > 0 and what_day <= 7:
    print(days[what_day - 1])
else:
    print("error: no weekday matches that number.")