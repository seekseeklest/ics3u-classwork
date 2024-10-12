PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

# Both a while loop and an if statement check if a condition is true. If the condition is true, they run the code that comes next. So they both control what the program does based on the condition.

# The main difference is that an if statement only runs the code once if the condition is true, while a while loop keeps running the code over and over again until the condition becomes false.

# We would also need to convert the input into an integer:
PIN = 12345

entry = int(input("ENTER YOUR PIN: "))

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = int(input("ENTER YOUR PIN: "))

# the program will be stuck in an infinite loop and will always print "INCORRECT PIN. TRY AGAIN." because it won't ask for a new pin after the first one and will keep checking the incorrect input.
