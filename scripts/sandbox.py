from game.board import Board

board = Board()
# Fill the board
for i in range(6):
    for j in range(7):
        if j == 3:
            continue
        board.make_move(j, 1 if (i + j) % 2 == 0 else 2)
for i in range(6):
    board.make_move(3, 1 if i % 2 == 0 else 2)
    
board.show()
board.showPrettyBoard()

# print("Winner is player 1: ", board.is_winner(1))


# countB = self.count_in_direction(last_row, last_column, -dr, -dc, player)
input = (0, 3, 1, 1, 1)
result = board.count_in_direction(*input)
print(result)

temp = board.getBoard()

# print 0,0
print(temp[0][0])

