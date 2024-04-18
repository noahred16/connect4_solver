from game.board import Board
from game.game import Game
from agents.random_agent import RandomAgent
from matplotlib import pyplot as plt

board = Board()
game = Game(board)

player1 = RandomAgent(1)
player2 = RandomAgent(-1)
players = [player1, player2]

num_of_games = 10_000
# loss, tie, win
results = [0, 0, 0]
move_counts = []

for _ in range(num_of_games):
    current_player = 0
    # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
    while players[current_player].make_move(game) is None:
        current_player = 1 - current_player
    move_count, result = game.reset()
    results[result + 1] += 1
    move_counts.append(move_count)


# plot 1 bar chart for loss, tie, win with labels on the bars
plt.bar(["Loss", "Tie", "Win"], results)
plt.title("Player 1 Random Agent Performance vs Other Random Agent")
plt.xlabel("Results")
plt.ylabel("Number of Games")
for i, result in enumerate(results):
    plt.text(i, result, str(result), ha='center', va='bottom')
# plt.show()
plt.savefig("results/random_agent_performance.png")
plt.clf()

# plot 2 histogram for move counts
plt.hist(move_counts, bins=range(0, 43, 1), edgecolor='black')
plt.title("Player 1 Random Agent Performance vs Other Random Agent")
plt.xlabel("Number of Moves")
plt.ylabel("Number of Games")
# plt.show()
plt.savefig("results/random_agent_performance_histogram.png")
