user_string = input("Enter a string: ")

index = 0

found = False

while index < len(user_string) - 2:  
    if user_string[index:index + 3] == "xyz" and (index == 0 or user_string[index - 1] != "."):
        found = True
        break 
    index += 1

if found:
    print(True)
else:
    print(False)