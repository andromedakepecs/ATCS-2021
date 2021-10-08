games = ['monopoly', 'tic tac toe', 'hangman',]
print("I like playing", ', '.join(games))

new_game = input("What's a game you like to play? ")
games.append(new_game)

print("We like playing", ', '.join(games))
