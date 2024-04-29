import pytest
from game.mocker import Mocker
from game.game import Game
from agents.pn_search_agent import PNS

def test_end_game():
    mocker = Mocker()
    end_game: Game = mocker.game_states[-4]
    end_game.print_pretty()
    pns = PNS(end_game.board)
    move = pns.make_move()
    
    assert move == 0
    
def test_end_game_v2():
    mocker = Mocker()
    end_game: Game = mocker.game_states[-3]
    end_game.print_pretty()
    pns = PNS(end_game.board)
    move = pns.make_move()
    
    assert move == 6
    
def test_end_game_v3():
    mocker = Mocker()
    end_game: Game = mocker.game_states[-2]
    end_game.print_pretty()
    pns = PNS(end_game.board)
    move = pns.make_move()
    
    assert move == 6
    
def test_end_game_v4():
    mocker = Mocker()
    end_game: Game = mocker.game_states[-5]
    end_game.print_pretty()
    pns = PNS(end_game.board)
    move = pns.make_move()
    
    assert move == 0
    
def test_mid_game_mock1():
    mocker = Mocker()
    mid_game: Game = mocker.game_states[-14]

    agent = PNS(mid_game.board)
    move = agent.make_move()
    assert move == 5
    
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
        # assert game.evaluate_board() == None
        # assert game.result == None
        # assert game.current_player == 1 if i % 2 == 0 else -1
        
        agent = PNS(game.board)
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
            
# yellow who cares
# def test_mid_game_mock2():
#     mocker = Mocker()
#     mid_game: Game = mocker.game_states[-15]
#     mid_game.print_pretty()
    
#     agent = PNS(mid_game.board)
#     move = agent.make_move()
#     assert move == 1


def test_mid_game_mock3():
    mocker = Mocker()
    mid_game: Game = mocker.game_states[-16]
    mid_game.print_pretty()
    
    assert len(mocker.game_states) == 42
    assert mid_game.current_player == 1
    assert mid_game.move_count == 26
    assert mid_game.evaluate_board() == None
    assert mid_game.result == None
    
    agent = PNS(mid_game.board)
    move = agent.make_move()
    assert move == 1

# timeout after 2 secs 
# finishes in less than 15 secs. Pretty good!
@pytest.mark.timeout(20)
def test_start_game():
    mocker = Mocker()
    start_game: Game = mocker.game_states[-22]
    start_game.print_pretty()
    start_game.print_url()
    assert start_game.current_player == 1
    # assert start_game.move_count == 0
    assert start_game.evaluate_board() == None
    assert start_game.result == None
    
    agent = PNS(start_game.board,10)
    move = agent.make_move()
    assert move == 5
    
# timeout after 2 secs
# @pytest.mark.timeout(10)
def test_start_game_w_depth_limit():
    mocker = Mocker()
    start_game: Game = mocker.game_states[-26]
    start_game.print_pretty()
    start_game.print_url()
    assert start_game.current_player == 1
    # assert start_game.move_count == 0
    assert start_game.evaluate_board() == None
    assert start_game.result == None
    
    agent = PNS(start_game.board, 5)
    move = agent.make_move()
    assert move == 4
    
    
def test_start_game_w_depth_limit():
    mocker = Mocker()
    start_game: Game = mocker.game_states[0]
    start_game.print_pretty()
    start_game.print_url()
    assert start_game.current_player == 1
    # assert start_game.move_count == 0
    assert start_game.evaluate_board() == None
    assert start_game.result == None
    
    agent = PNS(start_game.board, 3)
    move = agent.make_move()
    assert move == 3