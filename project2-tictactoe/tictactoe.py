import random

'''
Tic-Tac-Toe
@author Andromeda Kepecs
'''

ROWS, COLS = (3, 3)

class TicTacToe:
    def __init__(self):
        """ Defines board using '-' """
        self.board = [['-'] * COLS] * ROWS

    def print_instructions(self):
        """ Prints game instructions """
        print('Welcome to TicTacToe!')
        print('Player 1 is X and Player 2 is O')
        print('Take turns placing your pieces - the first to 3 in a row wins!')

    def print_board(self):
        """ Prints formatted board """
        for i in range (0, ROWS + 1):
            for j in range (0, COLS + 1):
                # If statements to print additional info about board
                if i == 0 and j == 0:
                    print(' ', end = ' ')
                elif i == 0:
                    print(j - 1, end = ' ')
                elif j == 0:
                    print(i - 1, end = ' ')
                else:
                    print(self.board[i - 1][j - 1], end = ' ') # Printing actual board
            print() # Break line


    def is_valid_move(self, row, col):
        """ 
        Checks if move is valid using input int row and col
        Returns boolean if move is valid 
        """
        if row < len(self.board) and row >= 0:
            if col < len(self.board) and col >= 0:
                return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        """ Places player on board """
        self.board[row][col] = player

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        """
        Takes manual turn using user input
        Returns a 1D list containing player's row and column placement
        """
        print(player + '\'s Turn')
        valid = self.is_valid_move(self, ROWS + 1, COLS + 1)
        while not valid:
            row = input('Enter a row: ')
            col = input('Enter a column: ')
            valid = self.is_valid_move(self, row, col)
            print('Please enter a valid move.')

        return [row, col]

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        placement = self.take_manual_turn(self, player)
        self.place_player(self, player, placement[0], placement[1])
        

    def check_col_win(self, player):
        # TODO: Check col win
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        return False

    def check_win(self, player):
        # TODO: Check win
        return False

    def check_tie(self):
        # TODO: Check tie
        return False

    def play_game(self):
        # TODO: Play game
        return
