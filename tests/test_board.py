import pytest
from game.board import Board

# def test_one():
#     assert 1 == 1

def test_make_move():
    board = Board()
    assert board.make_move(3, 1)  # Assume player 1 places on column 3
    assert board.board[5][3] == 1  # The bottom row, column 3 should have a 1

def test_undo_move():
    board = Board()
    board.make_move(3, 1)
    assert board.board[5][3] == 1
    board.undo_move()
    assert board.board[5][3] == 0  # The cell should be empty after undoing

def test_get_valid_moves():
    board = Board()
    # Fill up column 3
    for _ in range(board.rows):
        board.make_move(3, 1)
    valid_moves = board.get_valid_moves()
    assert 3 not in valid_moves  # Column 3 should be full
    assert len(valid_moves) == board.columns - 1  # All other columns should be available

def test_is_winner_vertical():
    board = Board()
    # Create a vertical win for player 1
    for _ in range(4):
        board.make_move(2, 1)
    assert board.is_winner(1)

def test_is_winner_horizontal():
    board = Board()
    # Create a horizontal win for player 1
    for i in range(4):
        board.make_move(i, 1)
    assert board.is_winner(1)

def test_player_2_horizontal_win():
    board = Board()
    # Create a horizontal win for player 2
    for i in range(4):
        board.make_move(i, -1)
    assert board.is_winner(-1)
    assert board.move_history == [(5, 0), (5, 1), (5, 2), (5, 3)], "Unexpected move history: " + str(board.move_history)

def test_is_winner_diagonal():
    board = Board()
    # Create a diagonal win for player 1
    board.make_move(0, 1)  # Column 0
    board.make_move(1, 2)  # Block
    board.make_move(1, 1)  # Column 1
    board.make_move(2, 2)  # Block
    board.make_move(2, 2)  # Block
    board.make_move(2, 1)  # Column 2
    board.make_move(3, 2)  # Block
    board.make_move(3, 2)  # Block
    board.make_move(3, 2)  # Block
    board.make_move(3, 1)  # Column 3
    assert board.is_winner(1)

def test_no_winner():
    board = Board()
    board.make_move(0, 1)
    board.make_move(1, 1)
    board.make_move(2, 1)
    # No fourth move in a line
    assert not board.is_winner(1)

@pytest.mark.parametrize("column, player", [
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
])
def test_make_move_on_full_column(column, player):
    board = Board()
    # Fill the column
    for _ in range(board.rows):
        assert board.make_move(column, player)
    # Try to place another token in the full column
    assert not board.make_move(column, player)

def test_player_two_win():
    board = Board()
    # Create a vertical win for player 2
    for _ in range(4):
        board.make_move(2, -1)
    assert board.is_winner(-1)

def test_no_winner_full_board_with_undo():
    board = Board()
    moves_made = 0
    player = 1  # Start with player 1
    last_valid_moves = []  # To store last valid move before a win check

    # Attempt to fill the board completely without resulting in a win
    while moves_made < board.rows * board.columns:
        move_made = False
        for column in range(board.columns):
            if column in board.get_valid_moves():
                board.make_move(column, player)
                if board.is_winner(player):
                    # Undo move if it results in a win
                    board.undo_move()
                else:
                    # Move was valid and did not result in a win
                    last_valid_moves.append((column, player))  # Keep track of the last valid move
                    moves_made += 1
                    move_made = True
                    player = 1 if player == -1 else -1  # Switch players
                    break  # Break to start the next move from column 0

        if not move_made:  # If no move was made, it means all columns were tried and should be full
            break

    # Assert the board is full and no valid moves are left
    assert not board.get_valid_moves(), "Board should be full now"

    # Reapply the last valid moves without a winner being declared
    for column, pl in last_valid_moves:
        board.make_move(column, pl)
        assert not board.is_winner(pl), f"Unexpected win detected after reapplying moves for player {pl}"

    # Check if the board is indeed full and results in a tie
    assert not board.get_valid_moves(), "There should be no valid moves left"
    assert not board.is_winner(1), "There should be no winner (Player 1)"
    assert not board.is_winner(-1), "There should be no winner (Player 2)"