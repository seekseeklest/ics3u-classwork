# sum 1 to 10:
sum_1_to_10 = 0
n = 1
while n <= 10:
    sum_1_to_10 += n
    n += 1

print(f"Sum of numbers from 1 to 10: {sum_1_to_10}")


# sum of numbers 100 to 200:
sum_100_to_200 = 0
n = 100
while n <= 200:
    sum_100_to_200 += n
    n += 1

print(f"Sum of numbers from 100 to 200: {sum_100_to_200}")


# difference between sum of numbers 100 to 200 and sum of numbers 200 to 300:
sum_100_to_200 = 0
n = 100
while n <= 200:
    sum_100_to_200 += n
    n += 1

sum_200_to_300 = 0
n = 200
while n <= 300:
    sum_200_to_300 += n
    n += 1

difference = sum_100_to_200 - sum_200_to_300
print(f"Difference between the sum from 100-200 and 200-300: {difference}")


# calculate the sum of the multiples of 5 between the numbers 1000 and 10000:
sum_multiples_of_5 = 0
n = 1000
while n <= 10000:
    if n % 5 == 0:
        sum_multiples_of_5 += n
    n += 1

print(f"Sum of multiples of 5 between 1000 and 10000: {sum_multiples_of_5}")


# calculate the sum of the multiples of 5 between 1 and 100, but exclude multiples of 3:
sum_multi_5_no_3 = 0
n = 1
while n <= 100:
    if n % 5 == 0 and n % 3 != 0:  # Multiple of 5 but not multiple of 3
        sum_multi_5_no_3 += n
    n += 1

print(f"Sum of multiples of 5 between 1 and 100, excluding multiples of 3: {sum_multi_5_no_3}")
