import pytest
from game.board import Board
from game.game import Game

def test_make_move_and_evaluate():
    board = Board()
    game = Game(board)

    # Make a valid move
    result = game.make_move_and_evaluate(0)
    assert result is None, "Game should continue with no winner or tie yet"

    # Fill the board to force a win or a tie
    # This is simplified; you'd typically loop and fill the board considering valid moves
    for i in range(1, 7):
        game.make_move_and_evaluate(i)

    # Assuming a setup that would result in a win for player 2
    game.make_move_and_evaluate(0)
    game.make_move_and_evaluate(1)
    
    game.make_move_and_evaluate(0)
    game.make_move_and_evaluate(1)
    
    game.make_move_and_evaluate(0)
    game.make_move_and_evaluate(1)
    
    result = game.make_move_and_evaluate(0)
    assert result == -14, "Player 2 should win with 4 tokens in a row"

def test_undo_move():
    board = Board()
    game = Game(board)

    # check current player
    assert game.current_player == 1, "Player 1 should start the game"
    game.make_move_and_evaluate(0)
    assert game.current_player == -1, "Player should switch after a move"
    game.make_move_and_evaluate(1)
    assert game.current_player == 1, "Player should switch after a move"

    assert game.undo_move(), "Should be able to undo the last move"
    assert game.current_player == -1, "Player should switch back after undo"
    assert game.move_count == 1, "Move count should decrement after undo"

def test_reset():
    board = Board()
    game = Game(board)
    
    # Make some moves
    for _ in range(3):
        game.make_move_and_evaluate(0)

    game.reset()

    assert game.move_count == 0, "Move count should be reset to 0"
    assert game.current_player == 1, "Current player should reset to 0"
    assert len(game.board.get_valid_moves()) == 7, "All columns should be available after reset"
    assert all(game.board.board.flatten() == 0), "Board should be empty after reset"

