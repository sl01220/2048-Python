R, C = map(int, input().split())
Map = []
for i in range(R):
    row = list(map(int, input().split()))
    Map.append(row)
detected=0
undetected =0
for i in range(R):
    for j in range(C):
        if Map[i][j] >= 5:
            for n in range(i-1, i+2):
                for m in range(j-1, j+2):
                    if n >= 0 and n < R and m >= 0 and m < C and not (n == i and m == j):
                        if Map[n][m] >= 5:
                            Map[i][j] = 6
                            Map[n][m] = 6
        if Map[i][j]==5:
            for n in range(i - 1, i + 2):
                for m in range(j - 1, j + 2):
                    if n >= 0 and n < R and m >= 0 and m < C and not (n == i and m == j):
                        if Map[n][m]==1:
                            detected+=1
                            Map[n][m]=0
for i in range(R):
    for j in range(C):
        if Map[i][j]==1:
            undetected+=1
print(detected,undetected)



