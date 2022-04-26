# Connect Four with Monte Carlo Tree Search 
# @author Andromeda Kepecs

# Console visualizations
EMPTY = '.'
SPACING = ' '
RED = 'R'
YELLOW = 'Y'

# Game definitions
ROWS = 6
COLUMNS = 7
NUM_TO_WIN = 4

# Connect Four game mechanics
class Game():
	def __init__(self):
		""" Initialize game """
		self.board = [[EMPTY for i in range(ROWS)] for j in range(COLUMNS)]

	def print_board(self):
		""" Prints formatted board """
		# Print number of columns
		print(SPACING.join(map(str, range(COLUMNS))))
		for row in range(ROWS):
			for col in range(COLUMNS):
				print(SPACING.join(str(self.board[col][row])), end = ' ')
			print()

	def place_player(self, player, column):
		row = self.get_next_row(column)
		(self.board[column])[row] = player

	def is_valid_move(self, column):
		if column >= COLUMNS or column < 0:
			return False
		elif (self.board[column])[0] != EMPTY:
			return False
		else:
			row = self.get_next_row(column)
			if (self.board[column])[row] == EMPTY:
				return True
		return False

	def get_next_row(self, column):
		row = -1
		while (self.board[column])[row] != EMPTY: # Traverse rows in reverse order
			row -= 1
		return row

	def player_turn(self, player):
		print(player + '\'s Turn')
		valid = self.is_valid_move(COLUMNS + 1)
		while not valid:
			column = int(input('Enter a column: '))
			valid = self.is_valid_move(column)
			if not valid:
				print('Please enter a valid move.')
		return column


	def ai_turn(self, player):
		pass

	def check_win(self, player):
		pass

	def play_game(self):
		self.place_player(RED, self.player_turn(RED))
		self.print_board()

def main():
	game = Game()
	game.play_game()


if __name__ == '__main__':
	main()

