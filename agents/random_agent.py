import random
from game.game import Game

class RandomAgent:
    def __init__(self, game: Game):
        self.game = game

    def make_move(self):
        moves = self.game.get_legal_moves()
        self.game.make_move(random.choice(moves))