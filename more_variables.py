store = "No Frills"
item = "Apples"
price = 0.5
quantity = 7
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal


# f-string
print(f"At {store} I bought some {item}.")
# concatenation
print("They sold for $" + str(price) + " each.")
# dot format
print("I wanted to purchase {} of them.".format(quantity))
print("the subtotal was ${:.2f} with ${:.2f} in tax.".format(subtotal, tax))
print(f"The total price, with tax included, was ${round(total, 2)})
# you forgot to add an 'f' in front of the parentheses, no longer making it a format function, and thus not printing out the value of the "total" variable.

# I noticed something interesting in the 17th line. When the code is run, the subtotal and tax are $3.50 and $0.18, however the total is $3.67. By recomfirming in the third decimal place that the values are $3.500, $0.175, and $3.675 respectively, it revealed to me a peculiarity in how Python rounds numbers, as 0.175 was rounded up but 3.675 was not.
