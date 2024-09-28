def quiz():
    print("Are you ready for a quiz? (Y/N)")
    ready = input().lower()
    correct_answers = 0
    if ready == 'n':
        print("Well come back when you're ready!")
        exit()
    elif ready == 'y':
        print("Okay, here it comes!\n")
    else:
        print("Please type Y or N.")
        exit()

    answer1 = int(input("\nQ1) What is the capital of Alaska?\n1) Melbourne\n2) Anchorage\n3) Juneau\n"))
    if answer1 == 3:
        print("Correct!")
        correct_answers = correct_answers + 1
    else:
        print("Incorrect!")      

    answer2 = int(input("\nQ2) In Python, the way you get keyboard input is the keyboard_input function.\n1) true\n2) false\n"))
    if answer2 == 2:
        print("Correct!")
        correct_answers = correct_answers + 1
    else:
        print("Incorrect!")    
    
    answer3 = int(input("\nQ3) What is the result of 9 + 6 / 3?\n1) 5\n2) 11\n3) 15/3\n"))
    if answer3 == 2:
        print("Correct!")
        correct_answers = correct_answers + 1
    else:
        print("Incorrect!")     

    print(f"\nYou got {correct_answers}/3 questions right!")

quiz()
