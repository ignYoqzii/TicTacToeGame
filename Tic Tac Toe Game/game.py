import numpy as np
from player import Player

class TicTacToe:
    def __init__(self, player1, player2, is_player1_bot, is_player2_bot, level_bot1, level_bot2):
        """
        Initialize the TicTacToe game.
        
        :param player1: Name of player 1
        :param player2: Name of player 2
        :param is_player1_bot: Boolean indicating if player 1 is a bot
        :param is_player2_bot: Boolean indicating if player 2 is a bot
        :param level_bot1: Difficulty level of bot 1
        :param level_bot2: Difficulty level of bot 2
        """
        self.player1 = Player(player1, is_player1_bot, level_bot1)  # Create player 1
        self.player2 = Player(player2, is_player2_bot, level_bot2)  # Create player 2
        self.winner = 0  # Stores the winner (1 for X, -1 for O, 0 for tie)
        self.turn = 1  # 1 represents X's turn, -1 represents O's turn
        self.board = np.zeros((3, 3))  # Initialize a 3x3 board with zeros (empty cells)
        self.gameover = False  # Flag to indicate if the game is over

    def play(self):
        """
        Start the game loop until the game is over.
        """
        while not self.gameover:
            self.play_turn()
            if self.gameover:
                self.show_board()
                self.announce_winner()
                self.replay()

    def play_turn(self):
        """
        Play a single turn of the game.
        """
        self.show_legend()
        self.show_board()
        moves = self.get_available_moves()  # Get all available moves
        current_player = self.player1 if self.turn == 1 else self.player2  # Determine current player
        
        # Ask player to choose a cell based on whether they are a bot or human
        player_cell = (
            current_player.take_cell_bot(self.board, self.turn) 
            if current_player.is_bot 
            else current_player.take_cell_human(moves)
        )
        
        self.update_board(player_cell)  # Update board with the chosen move
        self.check_for_win()  # Check if the game is won or tied

    def replay(self):
        """
        Ask the players if they want to play again and reset the game if they do.
        """
        replay = input("Do you want to play again? (Y/N): ")
        if replay.lower() == "y":
            self.reset()

    def show_legend(self):
        """
        Display the legend showing which player is X and which is O.
        """
        print(f"{self.player1.name} plays as X.")
        print(f"{self.player2.name} plays as O.")

    def show_board(self):
        """
        Display the current state of the board.
        """
        print("\n")
        for i in range(3):
            print("  -------------")
            row_output = str(i + 1) + " | "  # Row number
            for j in range(3):
                cell = self.board[i][j]
                token = "X" if cell == 1 else "O" if cell == -1 else " "  # Convert board values to symbols
                row_output += token + " | "
            print(row_output)
        print("  -------------")
        print("    1   2   3")  # Column numbers

    def get_available_moves(self):
        """
        Get a list of available moves on the board.
        
        :return: List of available moves as tuples (row, col)
        """
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]

    def update_board(self, cell):
        """
        Update the board with the player's move.
        
        :param cell: The cell to update as a tuple (row, col)
        """
        self.board[cell] = self.turn  # Mark the board with the current player's symbol (1 for X, -1 for O)
        self.turn *= -1  # Switch turn to the other player

    def check_for_win(self):
        """
        Check if there is a winner or if the game is a tie.
        """
        # Check rows, columns, and diagonals for a win
        for sum_val in np.concatenate((
            self.board.sum(axis=1),  # Row sums
            self.board.sum(axis=0),  # Column sums
            [self.board.trace(), np.fliplr(self.board).trace()]  # Main diagonal and anti-diagonal
        )):
            if abs(sum_val) == 3:  # If a row, column, or diagonal sums to 3 (X wins) or -3 (O wins)
                self.gameover = True
                self.winner = self.turn * -1  # Winner is the player who just played
                return
        
        # Check for a tie (no available moves left)
        if not self.get_available_moves():
            self.gameover = True
            self.winner = 0

    def announce_winner(self):
        """
        Announce the winner of the game.
        """
        if self.winner == 1:
            print(f"Winner is {self.player1.name}!")
        elif self.winner == -1:
            print(f"Winner is {self.player2.name}!")
        else:
            print("Game tie!")

    def reset(self):
        """
        Reset the game to play again.
        """
        self.gameover = False
        
        # If the last game was a tie, the same player starts. Otherwise, the winner starts.
        self.turn = self.turn if self.winner == 0 else self.winner
        self.board = np.zeros((3, 3))  # Reset the board