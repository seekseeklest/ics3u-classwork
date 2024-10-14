max_tries = 4

pin = "12345"
tries = 0

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != pin and tries < max_tries:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == pin:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= max_tries:
    print(f"\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED AFTER {max_tries} FAILED ATTEMPTS.")
