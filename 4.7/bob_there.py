user_string = input("Enter a string: ")

index = 0

found = False

while index < len(user_string) - 2:
    if user_string[index] == 'b' and user_string[index + 2] == 'b':
        found = True
        break
    index += 1
if found:
    print(True)
else:
    print(False)
