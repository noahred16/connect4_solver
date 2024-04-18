from .board import Board
from .game import Game

import numpy as np

class Mocker:
    def player_1_next_move_win(self):
        end_game = np.array([
            [1, 1, -1, -1, 0, 1, -1],
            [-1, 1, 1, 1, 0, -1, 1],
            [1, 1, -1, -1, 0-1, 1, 1],
            [-1, -1, -1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1, -1, 1],
            [-1, -1, 1, 1, 1, -1, -1]
        ], dtype=int)
        
        board = Board(board=end_game)
        # board = Board()
        game = Game(board)
        
        return game
        
        # game.make_move_and_evaluate(0)
        # board.showPrettyBoard()
    
    # Red can win in 2 moves or less
    def mock_end_game_situation(self):
        end_game = np.array([
            [1, 1, -1, -1, 0, 0, -1],
            [-1, 1, 1, 1, 0, -1, 1],
            [1, 1, -1, -1, 0, 1, 1],
            [-1, -1, -1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1, -1, 1],
            [-1, -1, 1, 1, 1, -1, -1]
        ], dtype=int)
        
        board = Board(board=end_game)
        # board = Board()
        game = Game(board)
        return game
        # game.make_move_and_evaluate(0)
        # board.showPrettyBoard()

    # Red can win in 3 moves or less
    def mock_end_game_situation_3_moves(self):
        end_game = np.array([
            [1, 1, -1, -1, 0, 0, 0],
            [-1, 1, 1, 1, 0, -1, 0],
            [1, 1, -1, -1, 0, 1, 1],
            [-1, -1, -1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1, -1, 1],
            [-1, -1, 1, 1, 1, -1, -1]
        ], dtype=int)
        
        board = Board(board=end_game)
        # board = Board()
        game = Game(board)
        return game
        # game.make_move_and_evaluate(0)
        # board.showPrettyBoard()

    # Red can win in 4 moves or less
    def mock_end_game_situation_4_moves(self):
        end_game = np.array([
            [1, 1, -1, -1, 0, 0, 0],
            [-1, 1, 1, 1, 0, 0, 0],
            [1, 1, -1, -1, 0, 1, 1],
            [-1, -1, -1, 1, 0, -1, -1],
            [1, 1, 1, -1, -1, -1, 1],
            [-1, -1, 1, 1, 1, -1, -1]
        ], dtype=int)
        
        board = Board(board=end_game)
        # board = Board()
        game = Game(board)
        return game
    
    # Red can win in 5 moves or less
    def mock_end_game_situation_5_moves(self):
        end_game = np.array([
            [1, 1, -1, -1, 0, 0, 0],
            [-1, 1, 1, 1, 0, 0, 0],
            [1, 1, -1, -1, 0, 0, 1],
            [-1, -1, -1, 1, 0, -1, -1],
            [1, 1, 1, -1, 0, -1, 1],
            [-1, -1, 1, 1, 1, -1, -1]
        ], dtype=int)
        
        board = Board(board=end_game)
        # board = Board()
        game = Game(board)
        return game
    
    # Red can win in 6 moves or less
    def mock_end_game_situation_6_moves(self):
        end_game = np.array([
            [1, 1, -1, -1, 0, 0, 0],
            [-1, 1, 1, 1, 0, 0, 0],
            [1, 1, -1, -1, 0, 0, 0],
            [-1, -1, -1, 1, 0, 0, -1],
            [1, 1, 1, -1, 0, -1, 1],
            [-1, -1, 1, 1, 1, -1, -1]
        ], dtype=int)
        
        board = Board(board=end_game)
        # board = Board()
        game = Game(board)
        return game
    
    
# mocker = Mocker()
# mocker.mock_end_game_situation()
# mocker.player_1_next_move_win()
# TypeError: mock_end_game_situation() takes 0 positional arguments but 1 was given

