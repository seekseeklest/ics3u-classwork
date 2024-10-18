number = int(input("Enter an integer: "))

total = 0

for i in range(1, number + 1):
    total += i 

print(f"The total sum of numbers from 1 to {number} is: {total}")
