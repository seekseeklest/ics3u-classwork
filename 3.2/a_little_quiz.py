def check_answer(answer, correct_answer):
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

def quiz():
    print("Are you ready for a Dark Souls quiz, Chosen Undead? (Y/N)")
    ready = input().lower()
    correct_answers = 0
    
    if ready == 'n':
        print("Well, come back when you're ready!")
        exit()
    elif ready == 'y':
        print("Get ready to kindle the flame!\n")
    else:
        print("Please type Y or N.")
        exit()

    answer1 = int(input("\nQ1) Which of the following are not one of Gwyn's Four Knights?\n1) Artorias the Abysswalker\n2) Executioner Smough\n3) Lord's Blade Ciaran\n4) Hawkeye Gough\nAnswer: "))
    correct_answers += check_answer(answer1, 2)

    answer2 = int(input("\nQ2) In a failed attempt to recreate the First Flame, the Bed of Chaos was born. Which central figure was responsible for this?\n1) Gwyn, Lord of Cinder\n2) Aldia, Scholar of the First Sin\n3) Manus, Father of the Abyss\n4) Witch of Izalith\nAnswer: "))
    correct_answers += check_answer(answer2, 4)

    answer3 = int(input("\nQ3) Who is so easily forgotten?\n1) The Furtive Pygmy\n2) Covetous Demon\n3) Nameless King\n4) Seath the Scaleless\nAnswer: "))
    correct_answers += check_answer(answer3, 1)

    print(f"\nYou got {correct_answers}/3 questions right!")

quiz()
