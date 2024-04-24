# agents/__init__.py

# Import essential classes or functions from the package for easier access
from .random_agent import RandomAgent
from .minimax_agent import MinimaxAgent
from .pn_search_agent import PNS

# You might want to define what is accessible when importing * from this package
__all__ = ['RandomAgent', 'MinimaxAgent', 'PNS']
