import sys
sys.path.append('/mnt/c/Users/NoahSmith/OneDrive - Northeastern University/CS5100/Assignments/Project/connect4_solver')
# sys.path.append('/Users/noahredsmith/Library/CloudStorage/OneDrive-NortheasternUniversity/CS5100/Assignments/Project/connect4_solver')

from agents.minimax_agent import MinimaxAgent
from agents.random_agent import RandomAgent
from agents.pn_search_agent import PNS
from game.game import Game
from game.mocker import Mocker

import time
from matplotlib import pyplot as plt
# np
import numpy as np



def pns_time_test():
    mocker = Mocker()
    start_game: Game = mocker.game_states[-24]
    start_game.print_pretty()
    start_game.print_url()
    
    agent = PNS(start_game.board, 15)
    start = time.time()
    move = agent.make_move()
    end = time.time()
    print("Move", move, "Time", end - start)
    assert move == 4
    
def minimax_time_test():
    mocker = Mocker()
    start_game: Game = mocker.game_states[-24]
    # start_game.print_pretty()
    # start_game.print_url()
    
    agent = MinimaxAgent(start_game, 15)
    start = time.time()
    move = agent.make_move()
    end = time.time()
    print("Move", move, "Time", end - start)
    assert move == 4
    
    
pns_time_test()
minimax_time_test()