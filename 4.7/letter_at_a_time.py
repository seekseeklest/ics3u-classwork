message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

a_count = 0
for i in range(len(message)):
    letter = message[i].lower()
    if letter == 'a':
        a_count += 1

print(f"\nYour message contains the letter 'a' {a_count} times.")

# Question 1:
# If you print range(7), you'll see something like range(0, 7). It shows the start and stop but doesn’t actually list the numbers.
# If you convert it to a list using list(range(7)), you'll get [0, 1, 2, 3, 4, 5, 6], which lists all the numbers from 0 up to (but not including) 7.

# Question 2:
# The length of "Hello" is 5, so range(5) would be sent to the loop.
# The numbers inside that range would be: [0, 1, 2, 3, 4].

# Question 3:
# The length of "box" is 3.
# The last character 'x' has an index of 2 (since indexing starts at 0).

# Question 4 (updated code):

message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastposition = len(message) - 1
print(f"The last character is at position {lastposition} and is '{message[lastposition]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

vowel_count = 0
vowels = 'aeiou'

for i in range(len(message)):
    letter = message[i].lower()
    if letter in vowels:
        vowel_count += 1

print(f"\nYour message contains {vowel_count} vowels.")
