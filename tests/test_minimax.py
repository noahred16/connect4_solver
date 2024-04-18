import pytest
from game.board import Board
from game.game import Game
from game.mocker import Mocker
from agents.minimax_agent import MinimaxAgent

def test_next_move_win():
    game = Mocker().player_1_next_move_win()
    agent = MinimaxAgent(game)
    move = agent.make_move()
    assert move == 4

def test_end_game_situation():
    game = Mocker().mock_end_game_situation()
    agent = MinimaxAgent(game)
    move = agent.make_move()
    # assert move == 5
    
    
def test_end_game_situation_3_moves():
    game = Mocker().mock_end_game_situation_3_moves()
    agent = MinimaxAgent(game)
    move = agent.make_move()
    assert move == 5
    
def test_end_game_situation_4_moves():
    game = Mocker().mock_end_game_situation_4_moves()
    agent = MinimaxAgent(game)
    move = agent.make_move()
    assert move == 4
    
def test_end_game_situation_5_moves():
    game = Mocker().mock_end_game_situation_5_moves()
    agent = MinimaxAgent(game)
    move = agent.make_move()
    assert move == 5
    
def test_end_game_situation_6_moves():
    game = Mocker().mock_end_game_situation_6_moves()
    agent = MinimaxAgent(game)
    move = agent.make_move()
    assert move == 6

# set timeout to 5 seconds
# @pytest.mark.timeout(5)
# def test_empty_board():
#     board = Board()
#     game = Game(board)
#     agent = MinimaxAgent(game)
#     move = agent.make_move()
#     # assert move == 3
    
test_end_game_situation()