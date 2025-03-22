import numpy as np
import random
import time

class Player:
    def __init__(self, name, is_bot, level=None):
        """
        Initialize a Player object.
        
        :param name: Name of the player
        :param is_bot: Boolean indicating if the player is a bot
        :param level: Level of the bot (None for human players)
        """
        self.name = name  # Store player's name
        self.is_bot = is_bot  # Boolean flag for bot status
        self.level = level  # Bot difficulty level (if applicable)

    def take_cell_human(self, available_cells):
        """
        Allow a human player to choose a cell.
        
        :param available_cells: List of available cells
        :return: Chosen cell as a tuple (row, col)
        """
        print(f"{self.name}'s turn to play!\n")
        while True:
            cell = input("Enter a column and a row (col, row): ")
            try:
                # Convert input string to a tuple of integers
                cell = tuple(map(int, map(str.strip, cell.split(","))))
                # Adjust for 0-based indexing (since players input 1-based)
                cell_corrected = (cell[1] - 1, cell[0] - 1)
                # Check if the chosen cell is available
                if cell_corrected in available_cells:
                    return cell_corrected
            except ValueError:
                pass  # Ignore invalid inputs and prompt again
            print("This is not legal! Try again.")

    def take_cell_bot(self, board, turn):
        """
        Allow a bot player to choose a cell based on the difficulty level.
        Uses the Minimax algorithm with alpha-beta pruning for decision-making.
        
        :param board: Current state of the board
        :param turn: Current turn (1 for X, -1 for O)
        :return: Chosen cell as a tuple (row, col)
        """
        time.sleep(1)  # Simulate bot thinking time
        print(f"{self.name} is playing.\n")
        
        best_score = float('-inf')  # Initialize best score as negative infinity
        best_move = None  # Variable to store the best move found
        
        # Define depth limits for different difficulty levels
        depth_levels = {"1": 2, "2": 3, "3": 4, "4": 5, "5": 6, "6": 7, "7": 8, "8": 9}
        depth_limit = depth_levels.get(self.level)  # Get depth based on bot level
        
        # Evaluate all available moves
        for move in self.get_available_moves(board):
            board[move] = turn  # Make the move
            # Evaluate the move using minimax algorithm
            score = self.minimax(board, 0, False, turn, float('-inf'), float('inf'), depth_limit)
            board[move] = 0  # Undo the move
            if score > best_score:
                best_score = score
                best_move = move  # Update best move if a better score is found
        
        # Introduce randomness to bot moves to make it less predictable
        if random.random() < 0.8 - float(self.level) / 10:
            return random.choice(self.get_available_moves(board))  # Random move (to simulate imperfection)
        return best_move  # Otherwise, return the best calculated move
    
    def minimax(self, board, depth, is_maximizing, turn, alpha, beta, depth_limit):
        """
        Minimax algorithm with alpha-beta pruning to determine the best move.
        https://www.youtube.com/watch?v=l-hh51ncgDI
        
        :param board: Current state of the board
        :param depth: Current depth of the recursion
        :param is_maximizing: Boolean indicating if the current player is maximizing
        :param turn: Current turn (1 for X, -1 for O)
        :param alpha: Alpha value for alpha-beta pruning (best already explored option for maximizer)
        :param beta: Beta value for alpha-beta pruning (best already explored option for minimizer)
        :param depth_limit: Maximum depth for the recursion
        :return: Score of the board
        """
        winner = self.check_winner(board)  # Check if the game has a winner
        if winner is not None:
            # Assign scores based on winner (favoring the current player)
            if winner == turn:
                return 10 - depth  # Prioritize faster wins
            elif winner == -turn:
                return depth - 10  # Avoid opponent winning
            return 0  # Tie
        
        # Stop recursion if depth limit is reached
        if depth >= depth_limit:
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for move in self.get_available_moves(board):
                board[move] = turn
                score = self.minimax(board, depth + 1, False, turn, alpha, beta, depth_limit)
                board[move] = 0
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Prune unnecessary calculations
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves(board):
                board[move] = -turn
                score = self.minimax(board, depth + 1, True, turn, alpha, beta, depth_limit)
                board[move] = 0
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Prune unnecessary calculations
            return best_score

    def get_available_moves(self, board):
        """
        Get a list of available moves on the board.
        
        :param board: Current state of the board
        :return: List of available moves as tuples (row, col)
        """
        return [(i, j) for i in range(board.shape[0]) for j in range(board.shape[1]) if board[i][j] == 0]

    def check_winner(self, board):
        """
        Check if there is a winner on the board.
        
        :param board: Current state of the board
        :return: 1 if X wins, -1 if O wins, 0 if tie, None if no winner yet
        """
        # Check rows and columns for a win
        for i in range(3):
            if abs(sum(board[i, :])) == 3:
                return np.sign(sum(board[i, :]))  # Row win
            if abs(sum(board[:, i])) == 3:
                return np.sign(sum(board[:, i]))  # Column win
        
        # Check diagonals for a win
        if abs(np.trace(board)) == 3:
            return np.sign(np.trace(board))  # Main diagonal win
        if abs(np.trace(np.fliplr(board))) == 3:
            return np.sign(np.trace(np.fliplr(board)))  # Anti-diagonal win
        
        # Check for a tie (no available moves left)
        if not self.get_available_moves(board):
            return 0  # Tie
        
        return None  # No winner yet