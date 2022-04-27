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
		""" Place player """
		row = self.get_next_row(column)
		(self.board[column])[row] = player

	def is_valid_move(self, column):
		""" Check if move is valid """
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
		""" Returns next placeable row """
		row = -1
		while (self.board[column])[row] != EMPTY: # Traverse rows in reverse order
			row -= 1
		return row

	def player_turn(self, player):
		""" Take player turn """
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
		""" Check if four of the same color are in a row """
		# Check horizontal wins
		for col in range(COLUMNS - 3): # Number required to win is 4 so index doesn't get out of range for checks
			for row in range(ROWS):
				if (self.board[col])[row] == player and (self.board[col+1])[row] == player and (self.board[col+2])[row] == player and (self.board[col+3])[row] == player:
					return True

		# Check vertical wins
		for col in range(COLUMNS):
			for row in range(ROWS - 3): # Prevent row index out of range
				if (self.board[col])[row] == player and (self.board[col])[row+1] == player and (self.board[col])[row+2] == player and (self.board[col])[row+3] == player:
					return True

		# Check positive diagonal wins
		for col in range(COLUMNS - 3):
			for row in range(ROWS - 3):
				if (self.board[col])[row] == player and (self.board[col+1])[row+1] == player and (self.board[col+2])[row+2] == player and (self.board[col+3])[row+3] == player:
					return True

		# Check negative diagonal wins
		for col in range(COLUMNS - 3):
			for row in range(3, ROWS):
				if (self.board[col])[row] == player and (self.board[col+1])[row-1] == player and (self.board[col+2])[row-2] == player and (self.board[col+3])[row-3] == player:
					return True

		return False

	def check_tie(self):
		""" Check tie (if all spaces are filled and there are no wins) """
		for col in range(COLUMNS):
			for row in range(ROWS):
				if (self.board[col])[row] == EMPTY:
					return False
		return True

	def play_game(self):
		""" Play connect four game (2 player TODO one player is AI) """
		game_over = False
		turn = RED
		while not game_over:
			self.print_board()
			self.place_player(turn, self.player_turn(turn))
			if self.check_win(turn):
				self.print_board()
				print('Red wins')
				game_over = True
			if self.check_tie():
				self.print_board()
				print('Tie')
				game_over = True

			if turn == RED:
				turn = YELLOW
			else:
				turn = RED

def main():
	game = Game()
	game.play_game()


if __name__ == '__main__':
	main()

