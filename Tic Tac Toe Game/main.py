from game import TicTacToe
import random

# List of possible bot names for the game (Created with ChatGPT)
bot_names = [
    "AIronMan", "ByteBot", "CyberChamp", "DeepMindX", "EchoAI",
    "FutureBot", "GlitchMaster", "HoloAI", "IntelX", "JoltBot",
    "KappaBot", "LogicMaster", "MatrixAI", "NeoBot", "OmegaAI",
    "PixelBot", "QuantumX", "RoboGenius", "SynthAI", "TuringTest",
    "UltraBot", "VectorX", "WarpAI", "XenonBot", "ZenithAI"
]


def get_random_bot_name():
    """
    Select a random bot name from the list, ensuring uniqueness until the list is exhausted.
    :return: A random bot name
    """
    if bot_names:
        return bot_names.pop(random.randrange(len(bot_names)))
    return "DefaultBot"


def main():
    """
    Main function to start the Tic Tac Toe game and handle player choices.
    """
    print("Welcome to the Tic Tac Toe game!\n")
    
    # Ask user to select a game mode
    choice = input("Choose a gamemode (Player vs Player (1), Player vs Bot (2) or Bot vs Bot (3)): ")
    
    # Determine if the players are bots based on the game mode
    is_player1_bot = choice == "3"
    is_player2_bot = choice in ["2", "3"]
    
    level_bot1, level_bot2 = None, None  # Default bot levels
    name1, name2 = "", ""  # Player names
    
    if choice == "1":  # Player vs Player mode
        name1 = input("Enter Player 1's name: ")
        name2 = input("Enter Player 2's name: ")
    elif choice == "2":  # Player vs Bot mode
        level_bot2 = input("Choose the bot difficulty level (1 - 8): ")
        name1 = input("Enter your name: ")
        name2 = f"{get_random_bot_name()} (Level {level_bot2})"
    elif choice == "3":  # Bot vs Bot mode
        level_bot1 = input("Choose the first bot's difficulty level (1 - 8): ")
        level_bot2 = input("Choose the second bot's difficulty level (1 - 8): ")
        name1 = f"{get_random_bot_name()} (Level {level_bot1})"
        name2 = f"{get_random_bot_name()} (Level {level_bot2})"
    
    # Initialize and start the game
    game = TicTacToe(name1, name2, is_player1_bot, is_player2_bot, level_bot1, level_bot2)
    game.play()


if __name__ == "__main__":
    main()