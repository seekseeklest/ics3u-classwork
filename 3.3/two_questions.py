def two_questions_game():
    print("TWO QUESTIONS!")
    print("Think of an object, and I'll try to guess it.\n")
    
    category = input("Question 1) Is it animal, vegetable, or mineral?\n> ").strip().lower()
    
    size = input("Question 2) Is it bigger than a breadbox?\n> ").strip().lower()
    
    if category == "animal":
        if size == "yes":
            response = "My guess is that you are thinking of a whale."
        else:
            response = "My guess is that you are thinking of a mouse."
    elif category == "vegetable":
        if size == "yes":
            response = "You're thinking of a watermelon!"
        else:
            response = "My guess is that you are thinking of a carrot."
    elif category == "mineral":
        if size == "yes":
            response = "My guess is that you are thinking of a Camaro."
        else:
            response = "My guess is that you are thinking of a marble."
    else:
        response = "I didn't understand that. Let's try again!"

    print("\n" + response)

two_questions_game()

