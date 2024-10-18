user_string = input("Enter a string: ")
n = int(input("Enter an integer n: "))

last_n_chars = user_string[-n:]

result = last_n_chars * n

print("The result is:", result)