import numpy as np
from typing import List
# from game.game import Game
from game.util import get_legal_moves, evaluate_board, make_move, undo_move, print_pretty

# no more game class. raw board array.
# w utils such as get_legal_moves, make_move, undo_move, evaluate_board


class Node:
    def __init__(self, state, move=None, type='OR', parent=None, depth=0):
        self.state = state # board
        self.move = move # move that led to this state
        self.type = type # OR or AND
        self.parent = parent # parent node
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.children: List[Node] = [] # list of child nodes
        self.expanded = False # True if children have been generated
        # self.proof = float('inf') # proof number
        # self.disproof = float('inf') # disproof number
        self.proof = 1 # proof number
        self.disproof = 1 # disproof number
        self.value = 'unknown'  # Values can be 'proven', 'disproven', 'unknown'
        
class PNS:
    def __init__(self, board, depth=50):
        self.board = board
        self.depth = depth
        

    def make_move(self):
        # board = np.zeros((6, 7), dtype=int)
        move = self.best_move(self.board)
        # move = self.pnsearch(self.board)
        # print
        # self.game.make_move(move)
        return move
    
    def best_move(self, board: np.ndarray):
        possible_moves = get_legal_moves(board)

        non_losing_moves = []        
        
        for move in possible_moves:
            new_board, indx = make_move(board, move, 1)
            pns: Node = self.pnsearch(new_board)

            # print("Move: ", move, "Proof: ", pns.proof, "Disproof: ", pns.disproof)

            if pns.proof == 0:
                return move
            if pns.disproof == 0:
                continue
            non_losing_moves.append(move)

        # if no winning moves, return a non-losing move
        if len(non_losing_moves) == 0:
            return possible_moves[0]
        # if there are non-losing moves, return the first one
        else:
            return non_losing_moves[0]
            
        
        
    def pnsearch(self, board: np.ndarray):
        root = Node(board)
        evaluation = "unknown"
        root.value = evaluation
        if board.sum() == 0: # player 1
            root.type = 'OR'
        else: # player 2
            root.type = 'AND'
        # print(f"Initial evaluation: {evaluation}")
        
        self.setProofAndDisproofNumbers(root)
        # exit() 
        # print("NumOfChildren: ", len(root.children))
        
        current: Node = root
        i = 0
        while root.proof != 0 and root.disproof != 0:
            # print(i, current.proof, current.disproof, current.expanded, current.move)
            mostProving: Node = self.selectMostProvingNode(current)
            if mostProving.depth == self.depth:
                # return None
                return root
            # print("MostProving: ", mostProving.move)
            self.expandNode(mostProving)
            current = self.updateAncestors(mostProving, root)
            
            # print(i, current.proof, current.disproof, current.expanded, current.move)
            # print("___")
            # exit()
        # print("Final evaluation: ", root.proof, root.disproof)
        return root
        
        
    def setProofAndDisproofNumbers(self, n: Node):
        if n.expanded:
            if n.type == 'AND':
                # print("AND", n.proof, n.disproof, n.move)
                n.proof = 0
                n.disproof = float('inf')
                for child in n.children:
                    n.proof += child.proof
                    n.disproof = min(n.disproof, child.disproof)
            else: # OR
                # print("OR", n.proof, n.disproof, n.move)
                n.proof = float('inf')
                n.disproof = 0
                for child in n.children:
                    n.proof = min(n.proof, child.proof)
                    n.disproof += child.disproof
        else: # leaf node
            results = {
                'disproven': [float('inf'), 0],
                'proven': [0, float('inf')],
                'unknown': [1, 1]
            }
            n.proof = results[n.value][0]
            n.disproof = results[n.value][1]
            # print("Leaf node", n.proof, n.disproof, n.move)
            

            
    def selectMostProvingNode(self, n: Node):
        while n.expanded:
            value = float('inf')
            best: Node = None
            if n.type == 'AND':
                for child in n.children:
                    if value > child.disproof:
                        best = child
                        value = child.disproof
            else: # OR
                for child in n.children:
                    if value > child.proof:
                        best = child
                        value = child.proof
            n = best
        return n
        
    def expandNode(self, n: Node):
        self.generateChildren(n)
        for child in n.children:
            evaluate = evaluate_board(child.state, child.move)
            if evaluate is None:
                child.value = 'unknown'
            elif evaluate == 1:
                child.value = 'proven'
            # elif evaluate == -1:
            elif evaluate <= 0:
                child.value = 'disproven'
            # else:
            #     child.value = 'unknown'
                # child.value = 'disproven'
            self.setProofAndDisproofNumbers(child)
            if n.type == 'AND' and child.disproof == 0:
                break
            elif n.type == 'OR' and child.proof == 0: 
                break
        # print("Num of children",len(n.children))
        n.expanded = True
                
    def generateChildren(self, n: Node):
        if n.expanded:
            return
        n.expanded = True
        child_type = 'AND' if n.type == 'OR' else 'OR'
        player = 1 if n.type == 'OR' else -1
        children = get_legal_moves(n.state)
        for child in children:
            board, (row, column) = make_move(n.state, child, player)
            new_node = Node(board, (row, column), child_type, n)
            n.children.append(new_node)
        
        
    def updateAncestors(self, n: Node, root: Node):
        while n != root:
            # print("Ancestor")
            oldProof = n.proof
            oldDisproof = n.disproof
            self.setProofAndDisproofNumbers(n)
            if n.proof == oldProof and n.disproof == oldDisproof:
                return n
            n = n.parent
        # exit()
        # print("---")
        self.setProofAndDisproofNumbers(root)
        # print("~~~")
        # exit()
        return root
        
        
        
        
        
        
        
    #     self.setProofAndDisproofNumbers(isPlayer1)
        
    # def setProofAndDisproofNumbers(self, isPlayer1):
    #     # if count game has valid moves > 0 
    #     # player 1 is the OR player aka the maximizing player
    #     # player 2 is the AND player aka the minimizing player
        
    #     player_type = "OR" if isPlayer1 else "AND"
        
    #     proof = None
    #     disproof = None
        
    #     # if self.game.get_legal_moves():
    #     children = self.game.get_legal_moves()
    #     if len(children) > 0:
    #         print("Legal moves exist")
    #         if player_type == "AND":
    #             print("AND player")
    #         else: # OR player
    #             print("OR player")
    #             # inf
    #             proof = float('inf')                
    #             disproof = 0
    #             for child in children:
    #                 self.game.make_move(child)
                    
        
        
    #     # print("temp")
    #     # pass