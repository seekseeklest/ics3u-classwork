user_string = input("Enter a string: ")

doubled_string = ""

for char in user_string:
    doubled_string += char * 2

print("Doubled string:", doubled_string)