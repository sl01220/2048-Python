import sys
x=int(input('run times : '))
for d in range (x):
    list = []
    for i in range(3):
        list.append(sys.stdin.readline().strip().split())
    if list[0][0] == list[1][0] == list[2][0]:
        print(list[0][0] + ' win')
    if list[0][1] == list[1][1] == list[2][1]:
        print(list[0][1] + ' win')
    if list[0][2] == list[1][2] == list[2][2]:
        print(list[0][2] + ' win')
    if list[0][0] == list[1][0] == list[0][2]:
        print(list[0][0] + ' win')
    if list[1][0] == list[1][1] == list[2][2]:
        print(list[1][0] + ' win')
    if list[2][0] == list[2][1] == list[2][2]:
        print(list[2][0] + ' win')
    if list[0][0] == list[1][1] == list[2][2]:
        print(list[0][0] + ' win')
    if list[0][2] == list[1][1] == list[2][0]:
        print(list[0][2] + ' win')
    else:
        print('draw')