from datetime import datetime


def main():
    # Print a bunch of test days
    print("Weekday 1: " + weekday_name(1))
    print("Weekday 2: " + weekday_name(2))
    print("Weekday 3: " + weekday_name(3))
    print("Weekday 4: " + weekday_name(4))
    print("Weekday 5: " + weekday_name(5))
    print("Weekday 6: " + weekday_name(6))
    print("Weekday 7: " + weekday_name(7))
    print("Weekday 0: " + weekday_name(0))
    print()
    print("Weekday 43: " + weekday_name(43))
    print("Weekday 17: " + weekday_name(17))
    print("Weekday -1: " + weekday_name(-1))

    # Figure out today's weekday name
    today = datetime.now()
    weekday = today.isoweekday()
    print()
    print("Today is a {}!".format(weekday_name(weekday)))


def weekday_name(weekday: int) -> str:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    if weekday >= 0 and weekday <= 7:
        return(days[weekday - 1])
    else:
        return("error")


if __name__ == "__main__":
    main()