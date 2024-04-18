# agents/__init__.py

# Import essential classes or functions from the package for easier access
from .random_agent import RandomAgent
from .minimax_agent import MinimaxAgent
from .minimax_agent_v2 import MinimaxAgentV2

# You might want to define what is accessible when importing * from this package
__all__ = ['RandomAgent']
