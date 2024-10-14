start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the step (increment): "))

for i in range(start, end + 1, step):
    print(i)