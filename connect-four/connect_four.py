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

	def place_player(self, player, row, column):
		pass

	def is_valid_move(self, row, column):
		pass

	def player_turn(self, player):
		pass

	def ai_turn(self, player):
		pass

	def check_win(self, player):
		pass

	def play_game(self):
		pass

def main():
	game = Game()
	game.play_game()

if __name__ == '__main__':
	main()

