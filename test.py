board = [' ' for x in range(3)]

board1 = board

board2 = board[:]

print(board)
print(board1)
print(board2)

board.append('y')
board2.pop()

print(board)
print(board1)
print(board2)