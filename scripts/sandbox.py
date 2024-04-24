import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from game.game import Game
from game.mocker import Mocker
from agents.minimax_agent import MinimaxAgent
from agents.pn_search_agent import PNS
# time
import time


def test():
    
    # mocker = Mocker()
    # end_game: Game = mocker.game_states[-4]
    # end_game.print_pretty()
    # pns = PNS(end_game.board)
    # move = pns.make_move()
    # pns.pnsearch(end_game.board)
    
    
    all_moves = [
                3, 3, 3, 3, 3, 3,
                4, 5, 1, 2, 2, 2, 
                2, 2, 4, 5, 4, 4, 
                4, 5, 5, 1, 0, 1, 
                0, 0, 1, 1, 5, 5, 
                6, 6, 6, 0, 4, 2, 
                1, 0, 0, 6, 6
            ]
    stringbuilder = ''
    for move in all_moves:
        stringbuilder += str(move+1)
    print(stringbuilder)
    # game = Game()
    # pns = PNS(game)
    # pns.make_move()
    
    
    
test()


# PN-search. We can update the game class to keep track of number of available moves. Once a move is placed at row 0 or whatever, we can do node_count--. 
# Depth of 10 or more is reasonable. 