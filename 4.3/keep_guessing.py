import random
n = random.randint(1,11)

guesses = 0
game_running = True

print('I have chosen an integer between 1 and 10')
while game_running:
	input_num = int(input('Guess what it is: '))
	if input_num:
		op = int(input_num)
		if op == n:
			print('Congratulations, you guessed correctly!')
			game_running=False
		elif op < n:
			print('Oopsies! your number was too small! Please try again!')
			guesses+=1
		elif op > n:
			print('Oopsies! your number was too big! Please try again!')
			guesses+=1
	else:
		print('Sorry, I could not process that. Please type an integer between 1 and 10 and try again.')