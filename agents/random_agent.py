import random
from game.board import Board
from game.game import Game

class RandomAgent:
    def __init__(self, player_id):
        self.player_id = player_id  

    def choose_move(self, board: Board):
        """
        Selects a random move from available valid moves.
        Args:
            board (Board): The game board object with a method get_valid_moves.

        Returns:
            int: The column number of the chosen move.
        """
        valid_moves = board.get_valid_moves()
        if not valid_moves:
            return None  # No moves possible
        return random.choice(valid_moves)  # Randomly choose from valid moves
    
    def make_move(self, game: Game):
        """
        Make a move for the agent in the game.
        Args:
            game (Game): The game object with a method make_move_and_evaluate.
        """
        move = self.choose_move(game.board)
        # print(f"Player {self.player_id} chose column {move}")
        return game.make_move_and_evaluate(move)
