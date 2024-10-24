happiness = 0
treats = {"milky bone":1, "chewy bone":3, "ice cream":5}
n = 0
while n < 5:
    treats_fed = input("""What treats do you want to feed your dog:
    Milky Bone
    Chewy Bone
    Ice Cream: """).strip().lower()
    happiness += treats[treats_fed]
    n += 1
if happiness in range(0,6):
    print("your dog is sad :(")
elif happiness in range(6, 14):
    print("your dog is happy :)")
elif happiness in range(14,20):
    print("your dog is extremely happy :D")
elif happiness in range(20,26):
    print("your dog is sick")
