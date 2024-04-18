import sys
# sys.path.append('/mnt/c/Users/NoahSmith/OneDrive - Northeastern University/CS5100/Assignments/Project/connect4_solver')
sys.path.append('/Users/noahredsmith/Library/CloudStorage/OneDrive-NortheasternUniversity/CS5100/Assignments/Project/connect4_solver')

from agents.minimax_agent_v2 import MinimaxAgentV2
from agents.random_agent_v2 import RandomAgentV2
from game.game_v2 import GameV2

import time
from matplotlib import pyplot as plt
# np
import numpy as np


# Lets compare against random

game = GameV2()

player1 = MinimaxAgentV2(game, depth=3)
player2 = RandomAgentV2(game)
players = [player1, player2]

num_of_games = 500
results = [0, 0, 0]
move_counts = []

for _ in range(num_of_games):
    current_player = 0
    # game.evaluate_board()
    while game.result is None:
        move = players[current_player].make_move()
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
    game.reset()

plt.bar(["Loss", "Tie", "Win"], results)
plt.title("Minimax Agent Performance vs Random Agent with Depth 3")
plt.xlabel("Results")
plt.ylabel("Number of Games")
for i, result in enumerate(results):
    plt.text(i, result, str(result), ha='center', va='bottom')
plt.savefig("results/minimax_agent_v2_performance.png")
plt.show()
plt.clf()



exit()



# Lets graph the increase in time it takes to make a move as the depth increases
# for each first move lets test how long it takes. and then average the results per depth
# game = GameV2()
# max_depth = 12
# data_sum= np.zeros(max_depth)
# num_of_trials = 1
# for i in range(num_of_trials):
#     game.make_move(i)
#     for j in range(max_depth):
#         start = time.time()
#         agent = MinimaxAgentV2(game, depth=j)
#         move = agent.make_move()
#         end = time.time()
#         data_sum[j] += end - start
#         game.undo_move()
#     game.undo_move()


# # so we want max_depth many data points
# final_data = []
# for i in range(max_depth):
#     final_data.append((i, data_sum[i] / num_of_trials))
# # Lets graph it
# plt.plot([d[0] for d in final_data], [d[1] for d in final_data])
# plt.title("Minimax Agent Performance")
# plt.xlabel("Depth")
# plt.ylabel("Time to Make Opening Move")
# plt.savefig("results/minimax_agent_v2_performance_avg.png")
# plt.show()
# plt.clf()
# exit()
