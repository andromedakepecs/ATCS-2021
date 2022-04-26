import random

'''
Tic-Tac-Toe
A game of 3x3 Tic Tac Toe
@author Andromeda Kepecs
'''

ROWS, COLS = (3, 3)
USER = 'X'
COMPUTER = 'O'
DEPTH = 2

class TicTacToe:
    def __init__(self):
        """ Defines board using '-' """
        self.board = [['-' for i in range(ROWS)] for j in range(COLS)]

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
                if self.board[row][col] == '-': # Check if other player has made move
                    return True
        return False

    def place_player(self, player, row, col):
        """ Places player on board """
        self.board[row][col] = player

    def take_manual_turn(self, player):
        """
        Takes manual turn using user input, checking if valid
        Returns a 1D list containing player's row and column placement
        """
        print(player + '\'s Turn')
        valid = self.is_valid_move(ROWS + 1, COLS + 1)
        while not valid:
            row = int(input('Enter a row: '))
            col = int(input('Enter a column: '))
            valid = self.is_valid_move(row, col)
            if not valid:
                print('Please enter a valid move.')

        return [row, col]

    def take_random_turn(self, player):
        """
        Takes a random turn, checking if valid
        Returns a 1D list containing row and column
        """
        print(player + '\'s Turn')
        valid = self.is_valid_move(ROWS + 1, COLS + 1)
        while not valid:
            row = random.randint(0, ROWS)
            col = random.randint(0, COLS)
            valid = self.is_valid_move(row, col)
            if valid:
                break
        return [row, col]

    def take_minimax_turn(self, player, depth, alpha = (-100, ), beta = (100, )):
        """ Take optimal turn using minimax algorithm with set depth and alpha-sbeta pruning"""
        # Base case
        win = self.check_win(player)
        if win:
            if player == COMPUTER:
                return (1, )
            elif player == USER:
                return (-1, )
        tie = self.check_tie()
        if tie:
            return (0, )
        elif depth <= 0:
            return (0, )

        # Computer turn
        if player == COMPUTER:
            best = -10000
            best_move = (-1, -1)
            for row in range(ROWS):
                for col in range(COLS):
                    if self.is_valid_move(row, col):
                        self.place_player(COMPUTER, row, col)
                        move = self.take_minimax_turn(USER, depth - 1, alpha, beta)
                        if best < move[0]:
                            best = move[0]
                            best_move = (row, col)
                        if best < alpha:
                            alpha = best
                        if alpha >= beta:
                            break
                        self.board[row][col] = '-' # Reset board
            return best, best_move

        # User turn
        elif player == USER:
            worst = 10000
            worst_move = (-1, -1)
            for row in range(ROWS):
                for col in range(COLS):
                    if self.is_valid_move(row, col):
                        self.place_player(USER, row, col)
                        move = self.take_minimax_turn(COMPUTER, depth - 1, alpha, beta)
                        if worst > move[0]:
                            worst = move[0]
                            worst_move = (row, col)
                        if worst > beta:
                            beta = worst
                        if alpha >= beta:
                            break
                        self.board[row][col] = '-'
            return worst, worstmove

        return (0, )

    def take_turn(self, player):
        """ Takes turn """
        if player == USER:
            placement = self.take_manual_turn(player) # Method returns list of row and column
        else:
            placement = self.take_minimax_turn(player, DEPTH)
        self.place_player(player, placement[0], placement[1])

    def check_col_win(self, player):
        """ Dumb column check for a 3x3 Tic Tac Toe """
        if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True
        elif self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
            return True
        elif self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
            return True
        return False

    def check_row_win(self, player):
        """ Dumb row check for a 3x3 Tic Tac Toe """
        if self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player:
            return True
        elif self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player:
            return True
        elif self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player:
            return True
        return False
        

    def check_diag_win(self, player):
        """ Dumb diagnoal check for a 3x3 Tic Tac Toe """
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        elif self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_win(self, player):
        """ Check if player has won game """
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        """ Dumb method to check if each board space is filled """
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] == '-':
                    return False
        return True

    def play_game(self):
        """ Runs Tic Tac Toe """
        self.print_instructions()
        self.print_board()

        win = False
        tie = False
        while not win and not tie:
            # Player 1 turn and check win, tie
            self.take_turn(USER)
            self.print_board()

            win = self.check_win(USER)
            if win:
                print(USER + ' wins!')
                break

            # Check for tie after checking for wins 
            # because method only tells if board is filled
            tie = self.check_tie()
            if tie:
                print('Tie')
                break

            # Player 2 turn
            self.take_turn(COMPUTER)
            self.print_board()

            win = self.check_win(COMPUTER)
            if win:
                print(COMPUTER + ' wins!')
                break

            tie = self.check_tie()
            if tie:
                print('Tie')
                break


