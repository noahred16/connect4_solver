# game/__init__.py

# Import essential classes or functions from the package for easier access
from .game import Game
from .mocker import Mocker
from .util import get_legal_moves, evaluate_board, make_move, undo_move

# You might want to define what is accessible when importing * from this package
__all__ = ['Game', 'Mocker', 'get_legal_moves', 'evaluate_board', 'make_move', 'undo_move']
