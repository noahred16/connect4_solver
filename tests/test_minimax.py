import pytest
from game.mocker import Mocker
from agents.minimax_agent import MinimaxAgent
from game.game import Game


def test_game_make_move():
    game = Game()
    game.make_move(3)
    game.make_move(3)
    game.print_pretty()
    assert len(game.move_history) == 2
    

def test_mocker():
    mocker = Mocker()
    fresh_game: Game = mocker.game_states[0]
    fresh_game.print_pretty()
    assert fresh_game.current_player == 1
    assert fresh_game.move_count == 0

def test_early_game_mock():
    mocker = Mocker()
    early_game: Game = mocker.game_states[1]
    early_game.print_pretty()
    assert early_game.current_player == -1
    assert early_game.move_count == 1
    assert early_game.evaluate_board() == None
    assert early_game.result == None

def test_last_game_mock():
    mocker = Mocker()
    last_game: Game = mocker.game_states[-1]
    last_game.print_pretty()
    # assert last_game.current_player == 1
    assert last_game.move_count == 41
    assert last_game.evaluate_board() == 43 - 41
    assert last_game.result == 1

def test_end_game_mocks():
    mocker = Mocker()
    excepted_results = [
        6,6,0,0,
        # 0,0,0,0,
        # 0,0,0,0
        ]
    n = len(excepted_results)
    total = len(mocker.game_states)
    
    for i in range(n):
        # if i != 3:
        #     continue
        game: Game = mocker.game_states[-2-i]
        assert game.evaluate_board() == None
        assert game.result == None
        assert game.current_player == 1 if i % 2 == 0 else -1
        
        agent = MinimaxAgent(game)
        move = agent.make_move()
        if move != excepted_results[i]:
            game.undo_move()
            game.print_pretty()
            print("Expected: " + str(excepted_results[i]))
            print("Got: " + str(move))
            print("Player turn: " + str(game.current_player))
            # print("Failed on move num: " + str(game.move_count))
            print("i: " + str(i)) 
            assert False
        
# This one takes a few secs
def test_mid_game_mock1():
    mocker = Mocker()
    mid_game: Game = mocker.game_states[-14]
    mid_game.print_pretty()
    assert mid_game.current_player == 1
    assert mid_game.move_count == 28
    assert mid_game.evaluate_board() == None
    assert mid_game.result == None
    
    agent = MinimaxAgent(mid_game)
    move = agent.make_move()
    assert move == 5

# Even longer 
# def test_mid_game_mock2():
#     mocker = Mocker()
#     mid_game: Game = mocker.game_states[-15]
#     mid_game.print_pretty()
#     assert mid_game.current_player == -1
#     assert mid_game.move_count == 27
#     assert mid_game.evaluate_board() == None
#     assert mid_game.result == None
    
#     agent = MinimaxAgent(mid_game)
#     move = agent.make_move()
#     assert move == 1

# def test_mid_game_mock3():
#     mocker = Mocker()
#     mid_game: Game = mocker.game_states[-16]
#     mid_game.print_pretty()
#     assert mid_game.current_player == 1
#     assert mid_game.move_count == 26
#     assert mid_game.evaluate_board() == None
#     assert mid_game.result == None
    
#     agent = MinimaxAgent(mid_game)
#     move = agent.make_move()
#     assert move == 1

# def test_mid_game_mock4():
#     mocker = Mocker()
#     mid_game: Game = mocker.game_states[-17]
#     mid_game.print_pretty()
#     assert mid_game.current_player == -1
#     assert mid_game.move_count == 25
#     assert mid_game.evaluate_board() == None
#     assert mid_game.result == None
    
#     agent = MinimaxAgent(mid_game)
#     move = agent.make_move()
#     assert move == 0

# @pytest.mark.timeout(10)
# def test_custom_end_game():
#     moves = [
#         3, 3, 3, 3, 3, 3,
#         4, 5, 1, 2, 2, 2, 
#         2, 2, 4, 5, 4, 4, 
#         4, 5, 5, 1, 0, 1, 
#         0, 0, 0, 0, 1, 1,
#         2, 1, 6, 6, 6, 0,
#         6, 4
#     ]
    
#     mocker = Mocker(moves)
#     last_game: Game = mocker.game_states[-1]
#     last_game.print_pretty()
#     assert last_game.current_player == 1
#     assert last_game.move_count == 38
    
#     agent = MinimaxAgent(last_game)
#     move = agent.make_move()
#     assert move == 6
#     assert last_game.evaluate_board() == None
    
# timeout after 3
@pytest.mark.timeout(3)
def test_start_game():
    game = Game()
    assert game.current_player == 1
    agent = MinimaxAgent(game, 5) # 10 is the depth
    move = agent.make_move()
    assert move >= 0
    
    
    
# moved over old tests ~~~~~~~~~~~~

# def test_next_move_win():
#     game = Mocker().player_1_next_move_win()
#     # agent = MinimaxAgent(game)
#     assert game.evaluate_board() == None
#     # move = agent.make_move()
    
#     # assert game.result == None
#     # assert move == 4, f"Move: {move}"
#     # assert move == 4

# def test_end_game_situation():
#     game = Mocker().mock_end_game_situation()
#     agent = MinimaxAgent(game)
#     move = agent.make_move()
#     # assert move == 5
    
    
# def test_end_game_situation_3_moves():
#     game = Mocker().mock_end_game_situation_3_moves()
#     agent = MinimaxAgent(game)
#     move = agent.make_move()
#     assert move == 5
    
# def test_end_game_situation_4_moves():
#     game = Mocker().mock_end_game_situation_4_moves()
#     agent = MinimaxAgent(game)
#     move = agent.make_move()
#     assert move == 4
    
# def test_end_game_situation_5_moves():
#     game = Mocker().mock_end_game_situation_5_moves()
#     agent = MinimaxAgent(game)
#     move = agent.make_move()
#     assert move == 5
    
# def test_end_game_situation_6_moves():
#     game = Mocker().mock_end_game_situation_6_moves()
#     agent = MinimaxAgent(game)
#     move = agent.make_move()
#     assert move == 6
