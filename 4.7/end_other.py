string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

lower_str1 = string1.lower()
lower_str2 = string2.lower()

if lower_str1.endswith(lower_str2):
    print(True)
elif lower_str2.endswith(lower_str1):
    print(True)
else:
    print(False)