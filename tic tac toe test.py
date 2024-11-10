import sys
x = int(input('run times: '))
for d in range(x):
    board = []
    for i in range(3):
        board.append(sys.stdin.readline().strip().split())
    winner = None
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            winner = board[i][0]
            break
    if not winner:
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
                winner = board[0][i]
                break
    if not winner:
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
            winner = board[0][0]
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
            winner = board[0][2]
    if winner:
        print(winner + ' win')
    else:
        print('draw')