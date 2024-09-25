
print("Enter the following information about an item you wish to purchase..")
print()

name = input(print("The name of the item:"))

price = float(input("The price: $"))

quantity = int(input("How many do you want?"))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print("the price of your " + name + f" will come out to ${total}")

# The first difference is that the name asks for the input without prompting for a data type, while the price input is specifically converted to a float. 
# The second difference is that the name is printed as a separate statement, whereas the price input is combined with the prompt itself.

# A prompt is a message displayed to the user that indicates what to enter for the input.
# Switching the order can cause usability issues because the user will first see the input cursor without the prompt, leading to confusion about what information is required. By the time they see the prompt, they may have already entered something incorrectly. Displaying the prompt first can lead to less mistakes.

# inputs are normally saved as strings. Typing float and int will change the input to be saved as their respective data types. If they are not added, the code in the last group will not work, as multiplication between strings is impossible.
