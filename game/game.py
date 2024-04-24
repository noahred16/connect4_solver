import numpy as np

class Game:
    def __init__(self, board=None, current_player=1):
        if board is not None:
            self.board = board
        else:
            self.board = np.zeros((6, 7), dtype=int)
        self.result = None
        self.move_count = 0
        self.current_player = current_player
        self.move_history = []  # to track move history for undo

    def reset(self):
        self.board = np.zeros((6, 7), dtype=int)
        self.result = None
        self.move_count = 0
        self.current_player = 1
        self.move_history = []

    def get_legal_moves(self):
        return [i for i in range(7) if self.board[0][i] == 0]

    def make_move(self, column):
        for row in reversed(range(6)):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                self.move_count += 1
                self.move_history.append((row, column))  # save move to history
                self.current_player = -self.current_player
                return
        raise ValueError("Invalid move")

    def undo_move(self):
        """Remove the last token placed on the board."""
        if self.move_history:
            last_row, last_column = self.move_history.pop()
            self.board[last_row][last_column] = 0
            self.move_count -= 1
            self.current_player = -self.current_player
            self.result = None
        else:
            raise ValueError("No moves to undo")

    # result is not set unless we evaluate. thats fine.
    def evaluate_board(self):
        """
        Evaluate the board for the current player, using last move made and last player
        """
        if self.move_count == 0:
            return None
            # raise ValueError("No moves made")
        row, column = self.move_history[-1]
        player = self.board[row][column]
        
        directions = [
            (0, 1),  # Horizontal right
            (1, 0),  # Vertical down
            (1, 1),  # Diagonal down-right
            (1, -1)  # Diagonal down-left
        ]
        
        for dr, dc in directions:
            count = 1
            count += self.count_in_direction(row, column, dr, dc, player)
            count += self.count_in_direction(row, column, -dr, -dc, player)
            if count >= 4:
                self.result = player
                return player * (43-self.move_count)
                # return player * self.move_count
        # if board is full or has no more moves
        # if self.board.all():
        if self.move_count == 42:
            # print("TIE")
            self.result = 0
            return 0
        return None

    def count_in_direction(self, row, column, dr, dc, player):
        count = 0
        r, c = row + dr, column + dc
        while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == player:
            # print("r: ", r, "c: ", c, "player: ", player, "board: ", self.board[r][c])
            count += 1
            r += dr
            c += dc
        return count

    def print_pretty(self):
        # use X for player 1 and O for player -1 and empty for 0
        print("\n")
        for row in range(6):
            print("|", end="")
            for col in range(7):
                if self.board[row][col] == 1:
                    print("X|", end="")
                elif self.board[row][col] == -1:
                    print("O|", end="")
                else:
                    print(" |", end="")
            print("\n")
        print("---------------")
        print(" 0 1 2 3 4 5 6")
        print("\n")
        
    def print_url(self):
        # https://connect4.gamesolver.org/?pos=44444456233333565556621211
        url = "https://connect4.gamesolver.org/?pos="
        # loop through history
        for row, column in self.move_history:
            url += str(column+1)
        print(url)
    
    def ugly_print(self):
        print(self.board)