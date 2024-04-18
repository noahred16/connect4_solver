# Connect 4 Solver - Noah Smith
## NEU CS 5100: Foundations of Artificial Intelligence (Spring 2024)

### Files structure plan:
```
connect4_solver/
│
├── agents/                # Agents implementing different strategies
│   ├── __init__.py        # Makes agents a Python module
│   ├── random_agent.py    # Random play agent
│   ├── minimax_agent.py   # Minimax with alpha-beta pruning agent
│   └── advanced_agent.py  # More complicated algorithm (e.g., reinforcement learning)
│
├── game/                  # Core game implementation and utilities
│   ├── __init__.py        # Makes game a Python module
│   ├── board.py           # Definitions related to the game board
│   └── game.py            # Game logic and management
│
├── tests/                 # Pytest tests for all modules
│   ├── __init__.py
│   ├── test_random_agent.py
│   ├── test_minimax_agent.py
│   ├── test_advanced_agent.py
│   ├── test_board.py
│   └── test_game.py
│
├── experiments/           # Scripts or notebooks for comparing agents
│   ├── __init__.py
│   ├── random_agent_performance.py # Script to measure randome agent performance. 
│   ├── compare_agents.py  # Script to run and compare agents
│   └── analysis.ipynb     # Jupyter notebook for detailed analysis and charts
│
├── requirements.txt       # Project dependencies
└── README.md              # Project overview and instructions

```

## Board design considerations
- NumPy - simple and efficient data structure
- function for get all possible valid moves
- Make and Undo Moves
    - Undoing moves is useful for backtracking algorithms like Minimax with alpha-beta pruning.
- Check Win Conditions 
    - optimized using directional checking from the last placed token rather than scanning the whole board.

## Game design considerations
- Game State Management: whos turn and win/lose/tie
- 


# Comparative Algorithm: Alpha-Beta Pruning
Compare my program against a less efficient version. We expect the same decisions to be made but, one will be much more efficient.

## Define Test Scenarios
Variety of Board States: Select or generate a wide range of board states that might occur in typical games. Include early, mid, and late-game scenarios to fully test both algorithms under various conditions.  
Edge Cases: Include board configurations that are rare or involve complex winning paths to truly test the depth and efficiency of each algorithm.

## Measure Performance Metrics
Decision Time  
Optimality of Decisions  
Resource Usage (CPU and memory usage)

## Analysis
Statistical Analysis - This might include t-tests or other statistical tests to compare the performance metrics between the two algorithms  
Performance Graphs: Plot the results in graphs to visually present the comparison, such as decision time versus game complexity or resource usage over time.

## Interpretation and Reporting
Draw Conclusions: Based on the results, provide a reasoned analysis of how well your program performs compared to the alpha-beta pruning algorithm. Discuss any observed strengths and weaknesses.  
Discuss Algorithm Efficiency: Reflect on how the complexity of your algorithm compares to alpha-beta pruning in terms of both speed and accuracy of decision-making.  
Future Work: Suggest improvements or further research opportunities based on your findings.  




<!-- break -->


# Method 2: Compare against random agent
Makes random valid moves

## Define Evaluation Metrics
Win Rate. Test both as player 1 and as player 2. I imagine that the random may somehow force a tie or maybe win. Highly unlikely though. 
Game Length. 



# Potential evaluation function for ab pruning and my solution
Win: return float('inf') - depth  
This ensures that earlier wins (smaller depths) have a higher score than later wins.  
Loss: return float('-inf') + depth  
This ensures that later losses (larger depths) have a less negative score than earlier losses.  
Draw: Typically remains 0 since draws are neutral and the timing typically doesn’t matter as much.  





<!--  -->
# Description of Victor Allis's work
```
In 1988, Victor Allis devised a groundbreaking solution for the game of Connect Four. His work demonstrated that, with perfect play by both players:

First Player Advantage: If the first player begins by playing in the middle column, they can always win.
Second Player Draw: If the first player chooses any other column initially, the second player can always force a draw123.
Victor Allis’s approach involved a knowledge-based strategy implemented in a program called VICTOR. This program utilized nine strategic rules, each proven to be correct. Some of these rules include:

Useless Threats: Identifying and avoiding futile threats.
Control of Zugzwang: Managing the game state to maintain an advantageous position.
Baseinverse, Claimeven, and other specialized rules.
By combining these rules and employing techniques like conspiracy-number search, search tables, and depth-first search, VICTOR demonstrated that White could indeed win on the standard 7 × 6 Connect Four board. In fact, using a database of approximately half a million positions, VICTOR could play in real time against opponents on the same board, consistently winning with White4.

Victor Allis’s work not only solved Connect Four but also showcased the power of strategic reasoning and computational methods in game theory.
```


## Notes from professor.

The basic idea is fine but there are some issues. Feel free to continue but take these things into account. 


The problem definition
- The problem definition should be more formal to make it clear exactly what the states, actions, etc. are. 

Incorporate Additional Algorithms for Comparison
- You want to use other algorithms (such as alpha-beta) to compare to. 

Evaluation Functions
- You'll need evaluation functions as well. 

Experimental Results
- You'll want extensive experimental results against different opponents (e.g., starting with a fixed, simple opponent).


# Future work? 
- different board sizes maybe. Our game class does take rows=6, columns=7 in constructor. 

## Helpful commands
Update list of all installed packages in your current environment  
`pip freeze > requirements.txt`  



## Resources
https://connect4.gamesolver.org/