import sys
for s in sys.stdin:
    S = int(s.strip())
    x = int((2 * S) ** 0.5) + 1
    noS = True
    for n in range(x, 1, -1):
        if (2 * S) % n == 0:
            if ((2 * S) / n - n + 1) % 2 == 0:
                a1 = (((2 * S) / n) - n + 1) // 2
                if a1>0:
                    an = a1 + n - 1
                    print(int(a1), int(an), sep='-')
                    noS = False
    if noS == True:
        print('No Solution...')