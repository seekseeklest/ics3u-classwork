import random
number = random.randint(1,11)

print("TEH WORST NUBMER GESSING GAME EVAR!!!!!!!1!\n")

guess = int(input("I'M THKING OF A NMBR FROM 1-10.  TRY 2 GESS! "))

if guess == number:
    print("\nLOL!!! U GOT IT!  I CANT BELEIVE U GESSED IT WAS 4!")
elif guess != number and guess in range(1,11):
    print("\nW00T!  U SUX0R!!!  I BEET J00!!!  IT WAS 4!")
else:
    print("\nHAHAHA YOO STUPJID!! ZAT NMBFR IZINT BTWEIN 1-10!! STOOPIDDDDDD!!!!")