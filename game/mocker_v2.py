from .game_v2 import GameV2

import numpy as np

class MockerV2:
    def __init__(self, moves=[]):
        self.game_states = []
        game = GameV2()
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


    def deep_copy(self, game: GameV2):
        new_game = GameV2(board=game.board, current_player=game.current_player)
        new_game.result = game.result
        new_game.move_count = game.move_count
        new_game.move_history = game.move_history.copy()
        new_game.board = np.copy(game.board)
        return new_game