# Tic-Tac-Toe AI

A simple Tic-Tac-Toe game with human and AI players. The AI uses the Minimax algorithm with alpha-beta pruning for decision-making.

## Features

- **Player vs Player**

- **Player vs AI** (choose difficulty level 1-8)

- **AI vs AI** (watch two AIs battle it out!)

- **Minimax algorithm with alpha-beta pruning** for optimal AI moves

- **Replay option** after a game ends

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/ignYoqzii/TicTacToeGame.git
   cd TicTacToeGame
   ```
2. Install dependencies (only requires NumPy):
   ```sh
   pip install numpy
   ```
3. Run the game:
   ```sh
   python main.py
   ```

## How to Play

1. Choose a game mode:
   - **1**: Player vs Player
   - **2**: Player vs AI
   - **3**: AI vs AI
2. If playing against an AI, choose the difficulty level (1-8).
3. Players take turns placing **X** and **O** on the board by entering coordinates.
4. The game ends when a player wins or the board is full (tie).
5. Option to replay after a game ends.

## AI Decision-Making
The AI uses the **Minimax algorithm with alpha-beta pruning**:
- Explores future moves up to a certain depth (higher levels explore more deeply).
- Prioritizes moves leading to a win while blocking opponent strategies.
- Uses a random factor to avoid predictable moves at lower difficulties.

## File Structure
```
📂 Tic Tac Toe Game
├── main.py         # Entry point of the game
├── game.py         # Tic-Tac-Toe game logic
└── player.py       # Player and AI logic
```
