def start_game():
    print("Welcome to the Mysterious Cave!")
    choice1 = input("Go left (narrow passage) or right (faint light)? (left/right): ").strip().lower()
    
    if choice1 == "left":
        choice2 = input("Take the damp path or the dry path? (damp/dry): ").strip().lower()
        if choice2 == "damp":
            choice3 = input("Open the chest or leave it? (open/leave): ").strip().lower()
            print("You found gold!" if choice3 == "open" else "You found a hidden exit!")
        else:
            choice3 = input("Sneak past the dragon or wake it? (sneak/wake): ").strip().lower()
            print("You escaped!" if choice3 == "sneak" else "You made a new friend!")
    
    elif choice1 == "right":
        choice2 = input("Go through the vines or climb the staircase? (vines/staircase): ").strip().lower()
        if choice2 == "vines":
            choice3 = input("Explore the garden or look for another exit? (explore/exit): ").strip().lower()
            print("You discovered magical plants!" if choice3 == "explore" else "You found a secret passage out!")
        else:
            choice3 = input("Open the door or inspect the runes? (open/inspect): ").strip().lower()
            print("You entered a realm of wonders!" if choice3 == "open" else "You gained wisdom!")

    else:
        print("Invalid choice. Please try again.")
        start_game()

# Start the game
start_game()
