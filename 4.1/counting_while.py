print("Type in a message, and I'll display it ten times.")

message = input("Message: ")
print()

n = 0
while n < 10:
    print(f"{n + 1}. {message}")
    n += 1

# n += 1 will increase the value of variable n by 1. the code will continue looping until it has increased to no longer be smaller than 5.
