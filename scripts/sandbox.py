import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from game.game import Game
from game.mocker import Mocker
from agents.minimax_agent import MinimaxAgent
from agents.pn_search_agent import PNS, Node
from game.util import get_legal_moves, evaluate_board, make_move, undo_move, print_pretty

# time
import time
import pickle


def test(max_depth=1):
    start_time = time.time()
    board_ind = 0
    
    mocker = Mocker()
    board: Game = mocker.game_states[board_ind]
    # board.print_url()
    
    agent = PNS(board.board, max_depth)
    # start_game.make_move(move)
    # start_game.print_pretty()
    # start_game.print_url()
    
    # 
    # move = 3
    next_board: Game = mocker.game_states[board_ind+1]
    move = next_board.move_history[-1][1]

    
    new_board, indx = make_move(agent.board, move, 1)
    
    # return 1
    root: Node = agent.pnsearch(new_board)
    root.move = move
    

    
    # print("Move: ", move)
    # print("Proof: ", root.proof)
    # print("Disproof: ", root.disproof)
    # root.print_node()
    
    children = root.children
    # print("Children: ", len(children))
    
    # valid_moves = get_legal_moves(new_board)
    # print("valid_moves: ", valid_moves)
    # for child in children:
    #     # if child.move[1] not in valid_moves:
    #     #     print("Invalid move: ", child.move)
    #     #     continue
    #     # print("Child: ", child)
    #     child.print_node()
        # returngvfffffffffffffffffffffff
    
    # filename = "tree.pkl"
    # filepath = os.path.join(os.path.dirname(__file__), filename)
    # print("Filepath: ", filepath)
    # with open(filepath, 'wb') as file:
    #     pickle.dump(root, file)
    end_time = time.time()
    rounded = round(end_time - start_time, 2)
    # print("Time: ", rounded , " seconds for max_depth: ", max_depth)
    print("Max depth: ", max_depth, " Time: ", rounded)

    
for i in range(1,25):
    test(i)
# test()


# PN-search. We can update the game class to keep track of number of available moves. Once a move is placed at row 0 or whatever, we can do node_count--. 
# Depth of 10 or more is reasonable. 