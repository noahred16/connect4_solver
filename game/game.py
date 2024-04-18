from .board import Board

class Game:
    def __init__(self, board: Board):
        self.board = board
        self.current_player = 1
        self.move_count = 0
        self.result = None

    def print_current_player(self):
        if self.current_player == 1:
            print("Current player: Player 1")
        elif self.current_player == -1:
            print("Current player: Player 2")
        else:
            print("Current player: " + str(self.current_player))

    def make_move(self, column, player):
        """
        Make a move in the game.
        """
        self.board.make_move(column, player)
        # if self.board.make_move(column, player):
        #     self.move_count += 1
        #     if self.board.is_winner(player):
        #         self.result = player
        #         return player * self.move_count
        #     elif not self.board.get_valid_moves():
        #         self.result = 0
        #         return 0
        #     self.current_player = 1 - player
    
    def evaluate_move(self, column):
        """
        Evaluate a move in the game.
        """
        # player = self.current_player + 1
        player = self.current_player
        # if self.board.make_move(column, player):
        self.move_count += 1
        if self.board.is_winner(player):
            self.result = player
            return player * self.move_count
        elif not self.board.get_valid_moves():
            self.result = 0
            return 0
            # self.current_player = 1 - self.current_player  # Switch player

    def make_move_and_evaluate(self, column):
        """
        Make a move and return the outcome:
        - 1 for a win,
        - -1 for a loss,
        - 0 for a tie,
        - None if the game is still ongoing.
        """
        # player = self.current_player + 1
        player = self.current_player
        if self.board.make_move(column, player):
            self.move_count += 1
            if self.board.is_winner(player):
                self.result = player
                return player * self.move_count  # Winner
            elif not self.board.get_valid_moves():
                self.result = 0
                return 0  # Tie
            # self.current_player = 1 - self.current_player  # Switch player
            self.switchPlayers()
            return None  # Game still ongoing
        return None  # Move was not successful, game still ongoing

    def undo_move(self):
        """
        Undo the last move made in the game.
        """
        if self.board.undo_move():
            self.move_count -= 1
            self.result = None
            # self.current_player = 1 - self.current_player  # Switch back to the previous player
            # self.switchPlayers()
            return True
        return False

    def is_game_over(self):
        """
        Determine if the game is over.
        """
        return self.board.is_winner(1) or self.board.is_winner(-1) or not self.board.get_valid_moves()

    def reset(self):
        """
        Reset the game to start anew.
        """
        move_count = self.move_count
        result = self.result
        self.board = Board()
        self.current_player = 1
        self.move_count = 0
        return move_count, result

    def switchPlayers(self):
        self.current_player *= -1