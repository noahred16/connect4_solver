import numpy as np
import hashlib

# Helpful connect 4 functions

def board_hash(state):
    return hashlib.sha256(str(state).encode()).hexdigest()

def get_legal_moves(board: np.ndarray) -> list:
    """
    Get the legal moves for the current board state
    """
    # return [i for i in range(7) if board[0][i] == 0]
    legal_moves = []
    search_order = [0, 1, 2, 3, 4, 5, 6]
    # search_order = [3, 2, 4, 1, 5, 0, 6]
    for column in search_order:
        if board[0][column] == 0:
            legal_moves.append(column)
    return legal_moves

def evaluate_board(board: np.ndarray, move: tuple) -> int:
    """
    Evaluate the board for the current player, using last move made and last player
    """
    row, column = move
    player = board[row][column]
    
    directions = [
        (0, 1),  # Horizontal right
        (1, 0),  # Vertical down
        (1, 1),  # Diagonal down-right
        (1, -1)  # Diagonal down-left
    ]
    
    for direction in directions:
        count = 1
        for sign in [-1, 1]:
            for i in range(1, 4):
                new_row = row + sign * i * direction[0]
                new_column = column + sign * i * direction[1]
                if (
                    0 <= new_row < 6
                    and 0 <= new_column < 7
                    and board[new_row][new_column] == player
                ):
                    count += 1
                else:
                    break
        if count >= 4:
            return player
    # check top row for full board
    if np.all(board[0]):
        return 0
    return None

def make_move(board: np.ndarray, column: int, player: int) -> tuple:
    """
    Make a move on the board
    """
    new_board = np.copy(board)
    for row in reversed(range(6)):
        if new_board[row][column] == 0:
            new_board[row][column] = player
            return new_board, (row, column)
    raise ValueError("Invalid move")

def undo_move(board: np.ndarray, move: tuple) -> np.ndarray:
    """
    Undo the last move made on the board
    """
    row, column = move
    board[row][column] = 0
    return board

def print_pretty(board: np.ndarray, indent=''):
    """
    Print the board in a pretty way
    """
    print("\n")
    for row in range(6):
        print(indent, "|", end="")
        for col in range(7):
            if board[row][col] == 1:
                print("X|", end="")
            elif board[row][col] == -1:
                print("O|", end="")
            else:
                print(" |", end="")
        print(indent, "\n")
    print(indent, "---------------")
    print(indent, " 0 1 2 3 4 5 6")
    # print("\n")
    