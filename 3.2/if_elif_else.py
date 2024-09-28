team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")

# the reason it prints out the second message is because the initial value of team_a_wins is 15, and team_b_wins is 16. Because the code added 1 win to team a, it became 16 and the two values were equal.
# elif ensures only one block of code is run based on the first true condition.
# else runs code if none of the code before it is true. 
# by changing the elif in line 10 to an if statement, the code will return Tie. after Team A wins!