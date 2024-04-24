import sys
sys.path.append('/mnt/c/Users/NoahSmith/OneDrive - Northeastern University/CS5100/Assignments/Project/connect4_solver')
# sys.path.append('/Users/noahredsmith/Library/CloudStorage/OneDrive-NortheasternUniversity/CS5100/Assignments/Project/connect4_solver')

from agents.minimax_agent import MinimaxAgent
from agents.random_agent import RandomAgent
from agents.pn_search_agent import PNS
from game.game import Game

import time
from matplotlib import pyplot as plt
# np
import numpy as np





num_of_games = 10
results = [0, 0, 0]
move_counts = []

for _ in range(num_of_games):
    game = Game()
    depth = 5
    player1 = PNS(game.board, depth)
    player2 = MinimaxAgent(game, depth)
    players = [player1, player2]
    
    current_player = 0
    game.evaluate_board()
    move_num = 0
    while game.result is None:
        move_num += 1
        # if move_num == 5:
        #     game.print_pretty()
        move = players[current_player].make_move()
        if current_player == 0:
            game.make_move(move)
        current_player = 1 - current_player
        result = game.evaluate_board()
        if result is not None:
            # results[result + 1] += 1
            if result > 0:
                results[2] += 1
            elif result < 0:
                results[0] += 1
            else:
                results[1] += 1
            move_counts.append(game.move_count)
            break
    # game.print_pretty()
    game.reset()
#     # exit()

plt.bar(["Loss", "Tie", "Win"], results)
plt.title("Minimax Agent Performance vs Random Agent with Depth 5")
plt.xlabel("Results")
plt.ylabel("Number of Games")
for i, result in enumerate(results):
    plt.text(i, result, str(result), ha='center', va='bottom')
plt.savefig("results/pns_vs_minimax_v3.png")
plt.show()
plt.clf()
print("Saved to", "results/pns_vs_minimax_v3.png")
