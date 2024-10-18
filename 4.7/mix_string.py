a = input("Enter the first string: ")
b = input("Enter the second string: ")

result = ""

min_length = min(len(a), len(b))

for i in range(min_length):
    result += a[i] + b[i]

result += a[min_length:] + b[min_length:]

print("The merged string is:", result)