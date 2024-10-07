day = input("What day is it today? ").strip().lower()
holiday = input("Is today a holiday? (y/n) ").strip().lower()
if holiday == "y" or day in ["saturday", "sunday"]:
    print("You should sleep in.")
elif holiday == "n" and day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("You should wake up.")
else:
    print("error processing. please input the correct values.")
