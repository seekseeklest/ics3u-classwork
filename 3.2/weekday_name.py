day1, day2, day3, day4, day5, day6, day7 = ["Weekday 1: Monday", "Weekday 2: Tuesday", "Weekday 3: Wednesday", "Weekday 4: Thursday", "Weekday 5: Friday", "Weekday 6: Saturday", "Weekday 7:Sunday"]

weekday_mapping = {1:day1, 2:day2, 3:day3, 4:day4, 5:day5, 6:day6, 7:day7}

what_day = int(input("Enter the number of any weekday (1-7): "))

if what_day in weekday_mapping:
    print(weekday_mapping[what_day])
else:
    print("error: no weekday matches that number.")