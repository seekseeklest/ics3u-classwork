total = 0

print("Enter integers to sum them up. Enter 0 to stop.")

while True:
    number = int(input("Enter an integer: "))
    
    if number == 0:
        break 
    
    total += number  

print(f"The total sum of the numbers you entered is: {total}")
