print("I have a class of 33 students.")
# this line prints out the string "I have a class of 33 students." marked in quotation marks within the parentheses.
print("There are 11 girls, so that means..")
# This line prints out "there are 11 girls, so that means..." when run.
print("there are " + str(33 - 11) + " boys.")
# this line takes three strings, and with the '+' sign adds them together to form one phrase "there are 22 boys."
print()
# Here we note that there is nothing within the parentheses of the print function. When run, it will print out an empty line, which in the context of this code acts as a double space to seperate phrases.
print(f"That means {11 / 33} % are girls...")
# We can see in front of the quotation marks within the parentheses is an "f". this stands for format. Despite being within a string (as marked by the quotations), math done within the squiggly brackets is applicable and when run will print out the answer. This is called an f-string.
print("and {} % are boys.".format((33 - 11) / 33))
# In this line, "dot format" is being used. similar to the one above, it uses squiggly brackets within a string to to except the no math rule. However unlike the example before, the calculations are not done within the quotation marks, but within the parentheses of .format()
print()
print("If we made groups of six...")
# prints out "if we made groups of six..."
print(f"There would be {33 // 6} groups of six.")
# the double slash is known as something called a "floor divide." unlike the usual division function, this will first divide and then round down the answer to the nearest whole number.
print(f"And then a smaller group of {33 % 6} people.")
# the % symbol is called a modulus. In the first few lines of code, we also see the percent symbol being used, however it was done within a string, so it didn't serve any purpose other than as a percentage symbol. Modulus divides the number as a whole number but instead of outputting the answer, it will instead print the remainder.
print("-" * 30)
# this prints the string "-" 30 times.
print("If we had 17 apples and 3 people...")
# prints a string "If we had 17 apples and 3 people..."
print(f"Each person would get {17 // 3} whole apples.")
# floor divide 17 by 3 = 5.6666 which rounds down to 5 apples.
print("There would be " + str(17 % 3) + " apples remaining.")
# This adds multiple strings together. in the middle, modulus is used within parentheses of the string function, allowing it to be added with the other strings. strings cannot be added with floats or integers.
print()
print("If we charged each person $2 each for their 5 apples..")
# prints out the string
print("they would each pay ${}.".format(2 * 5))
# Uses dot format. Prints out "they would each pay $10."
