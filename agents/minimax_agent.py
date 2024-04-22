import numpy as np
from game.game import Game

class MinimaxAgent:
    def __init__(self, game: Game, depth=100):
        self.game = game
        self.depth = depth
        self.debug = False
        self.debug_depth = 0

    def make_move(self):
        move = self.best_move()
        self.game.make_move(move)
        return move

    def best_move(self):
        """
        Determine the best move by running the maximizer from the root.
        """
        # max_eval = float('-inf')
        # min_eval = float('inf')
        # best_col = None
        # alpha = float('-inf')
        # beta = float('inf')

        # for move in self.game.get_legal_moves():
        #     isPlayer1 = self.game.current_player == 1
        #     self.game.make_move(move)

        #     if move == 5: 
        #         self.debug = True
        #     else:
        #         self.debug = False

        #     if isPlayer1:
        #         eval = self.max_value(0, alpha, beta)
        #         print(f"Move {move} with eval {eval}")
        #         if eval > max_eval:
        #             max_eval = eval
        #             best_col = move
        #         alpha = max(alpha, eval)
        #     else:
        #         eval = self.min_value(0, alpha, beta)
        #         if eval < min_eval:
        #             min_eval = eval
        #             best_col = move
        #         beta = min(beta, eval)

        #     self.game.undo_move()
        isPlayer1 = self.game.current_player == 1
        
        best_move = None
        if isPlayer1:
            best_eval = float('-inf')    
            for move in self.game.get_legal_moves():
                self.game.make_move(move)
                value = self.min_value(0, float('-inf'), float('inf'))
                self.game.undo_move()
                if value > best_eval:
                    best_eval = value
                    best_move = move
        else:
            best_eval = float('inf')
            for move in self.game.get_legal_moves():
                self.game.make_move(move)
                value = self.max_value(0, float('-inf'), float('inf'))
                self.game.undo_move()
                if value < best_eval:
                    best_eval = value
                    best_move = move
        if best_move is None:
            ValueError("No move found")
            # return np.random.choice(self.game.get_legal_moves())            
        
        return best_move
            
        
        
        # if self.game.current_player == 1:
        #     print("Player 1")
        #     best_col = self.max_value(0, float('-inf'), float('inf'))
        # else:
        #     best_col = self.min_value(0, float('-inf'), float('inf'))
        
        # print("Best move: ", best_col)
        # return best_col

    def max_value(self, depth, alpha, beta):
        """
        Maximizing layer of the minimax algorithm with alpha-beta pruning.
        """
        result = self.game.evaluate_board()
        if depth == self.depth:
            return 0 # we assume everything is a tie
        elif result is not None:
            return result

        max_eval = float('-inf')
        for move in self.game.get_legal_moves():
            # if depth == 0:
            #     print(f"Move {move}, Alpha: {alpha}, Beta: {beta}")
            self.game.make_move(move)
            eval = self.min_value(depth + 1, alpha, beta)
            self.game.undo_move()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        # if self.debug and depth <= self.debug_depth:
        # if depth <= self.debug_depth:
        #     print(" " * depth + f"Max-Value: {max_eval} For depth {depth} and move {move}")
        return max_eval

    def min_value(self, depth, alpha, beta):
        """
        Minimizing layer of the minimax algorithm with alpha-beta pruning.
        """
        result = self.game.evaluate_board()
        if depth == self.depth:
            return 0 # we assume everything is a tie
        elif result is not None:
            return result

        min_eval = float('inf')
        for move in self.game.get_legal_moves():
            self.game.make_move(move)
            eval = self.max_value(depth + 1, alpha, beta)
            # if depth == 1:
            #     print(f"Sub-move: {move} with eval {eval}")
            self.game.undo_move()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        # if self.debug and depth <= self.debug_depth:
        # if depth <= self.debug_depth:
            # print(f"Min-Value: {min_eval} For depth {depth} and move {move}")
            # print(" " * depth + f"Min-Value: {min_eval} For depth {depth} and move {move}")
        return min_eval

# Usage example:
# Assuming you have an instance of Game called game_instance
# minimax = MinimaxAB(game_instance)
# print("Best move:", minimax.best_move())
