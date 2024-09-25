# we are assigning the variable name "team" with a value of "Toronto Blue Jays" which is a string
team = "Toronto Blue Jays"
# the variable name "current_date" has been assigned a value of "July 18, 2021" which is a string
current_date = "July 18, 2021"
# the variable name "player" has been assigned a value of "Vladimir Guerrero Jr."
player = "Vladimir Guerrero Jr."
# the variable name "home_runs_to_date" is assigned an value of an integer, 31
home_runs_to_date = 31
# the variable named "games_played" is assigned a value of 88
games_played = 88
# the variable named "total_season_games" is assigned a value of 162
total_season_games = 162
# the variable named "home_run_record" is assigned a value of 73
home_run_record = 73

# the variable named "games_remaining" is assigned a value of total_season_games - games_played, which is equal to 162 - 88 = 74
games_remaining = total_season_games - games_played
# the variable named "home_runs_per_game" is assigned a value of home_runs_to_date / games_played, which is equal to 31 / 88 = 0.35227272727
home_runs_per_game = home_runs_to_date / games_played
# the variable named "projected_home_runs" is assigned a value of home_runs_per_game * total_season_games, which is equal to 0.35227272727 * 162 = 57.0681818182
projected_home_runs = home_runs_per_game * total_season_games
# the variable named "can_break_record" is assigned a value of when projected_home_runs is bigger than home_run_record
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs)} home runs this season.")

# the two empty lines serve to group certain lines of code together. The first group are the base values of variables. the second group introduces new variables with values that include previous defined variables, arranged with operators. the third group is for all the print commands.
# I know that games_remaining = total_season_games - games_played because it means how many games are left over, excluding the games that have already been played.
