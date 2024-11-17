import sys


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    return None


x = int(input('run times: '))
for _ in range(x):
    board = []
    for _ in range(3):
        board.append(sys.stdin.readline().strip().split())

    winner = check_winner(board)
    if winner:
        print(winner + ' win')
    else:
        print('draw')