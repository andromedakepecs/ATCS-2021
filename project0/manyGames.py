games = ['monopoly', 'tic tac toe', 'hangman',]
print("I like playing", ', '.join(games))

print('Type \"done\" when finished with adding games')
done = False
while not done:
	new_game = input("What's a game you like to play? ")
	if new_game == 'done':
		break
	games.append(new_game)

print("We like playing", ', '.join(games))
