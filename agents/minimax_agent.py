from game.board import Board
from game.game import Game

# Relevant functions 
# get_valid_moves
# make_move
# evaluate_move
# undo_move

# MaxValue and MinValue are used to determine the best move for the agent
# Each takes a state, a, b, max_depth. 
class MinimaxAgent:
    def __init__(self, game: Game, player=1, depth=7000):
        self.game = game
        self.player = player
        self.depth = depth

    def make_move(self):
        """Determines the best move using the minimax algorithm with alpha-beta pruning."""
        best_score = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        board = self.game.board
        for move in board.get_valid_moves():
            # print(f"Move: {move}")
            self.game.make_move(move, self.player)
            score = self.min_value(move, self.depth - 1, alpha, beta)
            # print(f"Board: {board.board}")
            # board.showPrettyBoard()
            self.game.undo_move()
            print(f"Move: {move} with score {score}")
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, score)  # Update alpha for alpha-beta pruning
            break
        print(f"Best Move: {best_move} with score {best_score}")
        return best_move

    def max_value(self, move, depth, alpha, beta):
        """Evaluate the max value of the minimax function with alpha-beta pruning."""
        result = self.game.evaluate_move(move)
        if depth == 0 or result is not None:
            return result

        max_eval = float('-inf')
        for move in self.game.board.get_valid_moves():
            self.game.make_move(move, self.player)
            eval = self.min_value(move, depth - 1, alpha, beta)
            self.game.undo_move()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval

    def min_value(self, move, depth, alpha, beta):
        """Evaluate the min value of the minimax function with alpha-beta pruning."""
        result = self.game.evaluate_move(move)
        # print(f"Min-Value: {result}")
        # print(f"Board: {self.game.board.board}")
        if depth == 0 or result is not None:
            return result
        # print(f"Min-Move: {move}")

        min_eval = float('inf')
        for move in self.game.board.get_valid_moves():
            self.game.make_move(move, -self.player)
            print(f"sub-move {move} with eval")
            temp_result = self.game.evaluate_move(move)
            if temp_result is not None:
                print(f"winner sub-move {move} with eval {temp_result}")
                self.game.board.showPrettyBoard()
                return temp_result
            eval = self.max_value(move, depth - 1, alpha, beta)
            self.game.undo_move()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval