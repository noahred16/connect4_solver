from .game import Game

import numpy as np

class Mocker:
    def __init__(self, moves=[]):
        self.game_states = []
        game = Game()
        self.game_states.append(game)
        
        if not moves:
            moves = [
                3, 3, 3, 3, 3, 3,
                4, 5, 1, 2, 2, 2, 
                2, 2, 4, 5, 4, 4, 
                4, 5, 5, 1, 0, 1, 
                0, 0, 1, 1, 5, 5, 
                6, 6, 6, 0, 4, 2, 
                1, 0, 0, 6, 6
            ]
        for move in moves:
            game = self.deep_copy(self.game_states[-1])
            game.make_move(move)
            self.game_states.append(game)


    def deep_copy(self, game: Game):
        new_game = Game(board=game.board, current_player=game.current_player)
        new_game.result = game.result
        new_game.move_count = game.move_count
        new_game.move_history = game.move_history.copy()
        new_game.board = np.copy(game.board)
        return new_game
    
# moved over
# organized weird

    # def helper_make_move(self,moves):
    #     game = Game()
    #     for move in moves:
    #         game.make_move(move)
    #     return game

    # def player_1_next_move_win(self):
    #     end_game = np.array([
    #         [1, 1, -1, -1, 0, 1, -1],
    #         [-1, 1, 1, 1, 0, -1, 1],
    #         [1, 1, -1, -1, -1, 1, 1],
    #         [-1, -1, -1, 1, 1, -1, -1],
    #         [1, 1, 1, -1, -1, -1, 1],
    #         [-1, -1, 1, 1, 1, -1, -1]
    #     ], dtype=int)
        
    #     return self.helper_make_move(end_game)
    
    # # Red can win in 2 moves or less
    # def mock_end_game_situation(self):
    #     end_game = np.array([
    #         [1, 1, -1, -1, 0, 0, -1],
    #         [-1, 1, 1, 1, 0, -1, 1],
    #         [1, 1, -1, -1, 0, 1, 1],
    #         [-1, -1, -1, 1, 1, -1, -1],
    #         [1, 1, 1, -1, -1, -1, 1],
    #         [-1, -1, 1, 1, 1, -1, -1]
    #     ], dtype=int)
        
    #     return self.helper_make_move(end_game)

    # # Red can win in 3 moves or less
    # def mock_end_game_situation_3_moves(self):
    #     end_game = np.array([
    #         [1, 1, -1, -1, 0, 0, 0],
    #         [-1, 1, 1, 1, 0, -1, 0],
    #         [1, 1, -1, -1, 0, 1, 1],
    #         [-1, -1, -1, 1, 1, -1, -1],
    #         [1, 1, 1, -1, -1, -1, 1],
    #         [-1, -1, 1, 1, 1, -1, -1]
    #     ], dtype=int)
        
    #     return self.helper_make_move(end_game)

    # # Red can win in 4 moves or less
    # def mock_end_game_situation_4_moves(self):
    #     end_game = np.array([
    #         [1, 1, -1, -1, 0, 0, 0],
    #         [-1, 1, 1, 1, 0, 0, 0],
    #         [1, 1, -1, -1, 0, 1, 1],
    #         [-1, -1, -1, 1, 0, -1, -1],
    #         [1, 1, 1, -1, -1, -1, 1],
    #         [-1, -1, 1, 1, 1, -1, -1]
    #     ], dtype=int)
        
    #     return self.helper_make_move(end_game)
    
    # # Red can win in 5 moves or less
    # def mock_end_game_situation_5_moves(self):
    #     end_game = np.array([
    #         [1, 1, -1, -1, 0, 0, 0],
    #         [-1, 1, 1, 1, 0, 0, 0],
    #         [1, 1, -1, -1, 0, 0, 1],
    #         [-1, -1, -1, 1, 0, -1, -1],
    #         [1, 1, 1, -1, 0, -1, 1],
    #         [-1, -1, 1, 1, 1, -1, -1]
    #     ], dtype=int)
        
    #     return self.helper_make_move(end_game)
    
    # # Red can win in 6 moves or less
    # def mock_end_game_situation_6_moves(self):
    #     end_game = np.array([
    #         [1, 1, -1, -1, 0, 0, 0],
    #         [-1, 1, 1, 1, 0, 0, 0],
    #         [1, 1, -1, -1, 0, 0, 0],
    #         [-1, -1, -1, 1, 0, 0, -1],
    #         [1, 1, 1, -1, 0, -1, 1],
    #         [-1, -1, 1, 1, 1, -1, -1]
    #     ], dtype=int)
        
    #     return self.helper_make_move(end_game)
    
    