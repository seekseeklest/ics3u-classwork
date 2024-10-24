print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(0, 5, 1):
    print(f"{n}. {message}")


# Question 1:
# It still works. You can name it anything like i or count.

# Question 2:
# 0 is where the loop starts, and 5 is where it stops (not including 5). If you change them, it changes where the loop starts and stops.

# Question 3:
# It’s the “step.” It tells the loop how much to count by. Changing it to 2 makes it count by twos.

# Question 4:
# It counts from 0 to 6.

# Question 5:
# It starts at 3 and counts up to 8 (not including 9).

# Question 6 (repeat 10 times):
print("Type in a message, and I'll display it ten times.")

message = input("Message: ")

for n in range(0, 10):
    print(f"{n}. {message}")


# Question 7 (count by twos):
print("Type in a message, and I'll display it five times, starting at 2 and counting by 2.")

message = input("Message: ")

for n in range(2, 12, 2):
    print(f"{n}. {message}")