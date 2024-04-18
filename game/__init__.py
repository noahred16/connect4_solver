# game/__init__.py

# Import essential classes or functions from the package for easier access
from .board import Board
from .game import Game
from .game_v2 import GameV2
from .mocker_v2 import MockerV2

# You might want to define what is accessible when importing * from this package
__all__ = ['Board', 'Game', 'Mocker', 'GameV2', 'MockerV2']
