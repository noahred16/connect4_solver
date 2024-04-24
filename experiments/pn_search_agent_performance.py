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



# Lets graph the increase in time it takes to make a move as the depth increases
# for each first move lets test how long it takes. and then average the results per depth
# game = Game()
# max_depth = 12
# data_sum= np.zeros(max_depth)
# num_of_trials = 1
# for i in range(num_of_trials):
#     game.make_move(i)
#     for j in range(max_depth):
#         start = time.time()
#         agent = MinimaxAgent(game, depth=j)
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


game = Game()
max_depth = 12
data_sum = np.zeros(max_depth)
num_of_trials = 1
for i in range(num_of_trials):
    game.make_move(i)
    for j in range(max_depth):
        start = time.time()
        agent = PNS(game.board, j)
        move = agent.make_move()
        game.make_move(move)
        end = time.time()
        data_sum[j] += end - start
        game.undo_move()
    game.undo_move()
    
pns_data = []
for i in range(max_depth):
    pns_data.append((i, data_sum[i] / num_of_trials))
    
# MinimaxAgent

game2 = Game()
data_sum2 = np.zeros(max_depth)
for i in range(num_of_trials):
    game2.make_move(i)
    for j in range(max_depth):
        start = time.time()
        agent = MinimaxAgent(game2, j)
        move = agent.make_move()
        # game2.make_move(move)
        end = time.time()
        data_sum2[j] += end - start
        game2.undo_move()
    game2.undo_move()
    
minimax_data = []
for i in range(max_depth):
    minimax_data.append((i, data_sum2[i] / num_of_trials))


print(pns_data)
print(minimax_data)

# graph
plt.plot([d[0] for d in pns_data], [d[1] for d in pns_data], label="PN-Search")
plt.plot([d[0] for d in minimax_data], [d[1] for d in minimax_data], label="Alpha-Beta Pruning")
plt.title("PN-Search vs Alpha-Beta Pruning Performance")
plt.xlabel("Depth")
plt.ylabel("Time to Make Opening Move")
plt.savefig("results/pn_search_agent_performance_avg2.png")
plt.show()
plt.clf()

print("Saved to", "results/pn_search_agent_performance_avg2.png")