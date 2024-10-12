# 1. Loop that counts from 0 to 10 but skips 7
for i in range(11):
    if i == 7:
        continue
    print(i)

print("\n")

# 2. Loop that adds numbers from 5 to 20 but skips multiples of 3
total = 0
for i in range(5, 21):
    if i % 3 == 0:
        continue
    total += i
print(f"Sum from 5 to 20 excluding multiples of 3: {total}")

print("\n")

# 3. Ask user for start and end, sum numbers but stop at 13 or 31
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
sum_total = 0

for i in range(start, end + 1):
    if i == 13 or i == 31:
        break
    sum_total += i

print(f"Sum from {start} to {end} (stopped if 13 or 31 encountered): {sum_total}")

print("\n")

# 4. Infinite loop asking for words, breaking on "stop"
while True:
    word = input("Enter a word (type 'stop' to exit): ")
    if word.lower() == "stop":
        print("Goodbye!")
        break
    print(f"Your word: {word}")
