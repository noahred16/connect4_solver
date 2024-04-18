import numpy as np

class Board:
    def __init__(self, rows=6, columns=7, board=None):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((rows, columns), dtype=int)
        if board is not None:
            self.board = board
        self.move_history = []  # to track move history for undo

    def make_move(self, column, player):
        """Place a token in the given column for the player if possible."""
        for row in reversed(range(self.rows)):
            if self.board[row][column] == 0:
                self.board[row][column] = player
                self.move_history.append((row, column))  # save move to history
                return True
        return False

    def undo_move(self):
        """Remove the last token placed on the board."""
        if self.move_history:
            last_row, last_column = self.move_history.pop()
            self.board[last_row][last_column] = 0
            return True
        return False

    def get_valid_moves(self):
        """Returns a list of columns that can accept more tokens."""
        return [col for col in range(self.columns) if self.board[0][col] == 0]

    def is_winner(self, player):
        """Check for a win from the last placed token."""
        if not self.move_history:
            return False
        
        last_row, last_column = self.move_history[-1]
        
        # Directions as (row_increment, column_increment)
        directions = [
            (0, 1),  # Horizontal right
            (1, 0),  # Vertical down
            (1, 1),  # Diagonal down-right
            (1, -1)  # Diagonal down-left
        ]
        
        for dr, dc in directions:
            count = 1  # Include the last placed token in the count
            # Check in one direction
            count += self.count_in_direction(last_row, last_column, dr, dc, player)
            # Check in the opposite direction
            count += self.count_in_direction(last_row, last_column, -dr, -dc, player)
            
            if count >= 4:
                self.result = player
                return True
        
        return False

    def count_in_direction(self, start_row, start_col, row_inc, col_inc, player):
        """Count how many tokens of the same player are in a given direction."""
        row, col = start_row + row_inc, start_col + col_inc
        count = 0
        while 0 <= row < self.rows and 0 <= col < self.columns and self.board[row][col] == player:
            count += 1
            row += row_inc
            col += col_inc
        return count

    def show(self):
        """Print the board."""
        print('\n'.join(' '.join(map(str, row)) for row in self.board))
        print('-' * self.columns*2)
        print(' '.join(map(str, range(self.columns))))
        
    def showPrettyBoard(self):
        """Print the board but use X and O for players."""
        print('Player 1: X  Player 2: O')
        for row in self.board:
            pretty_row = []
            for cell in row:
                if cell == 1:
                    pretty_row.append('X')
                elif cell == -1:
                    pretty_row.append('O')
                else:
                    pretty_row.append(' ')
            print('| ' + ' | '.join(pretty_row) + ' |')
            print('-' * self.columns * 4)
        print('  ' + '   '.join(map(str, range(self.columns))) + '  ')
        
    def getBoard(self):
        return self.board