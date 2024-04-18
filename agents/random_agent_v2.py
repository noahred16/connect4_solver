import random
from game.game_v2 import GameV2

class RandomAgentV2:
    def __init__(self, game: GameV2):
        self.game = game


    
    def make_move(self):
        moves = self.game.get_legal_moves()
        self.game.make_move(random.choice(moves))