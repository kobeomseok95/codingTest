from sys import stdin
read = lambda : stdin.readline().strip()

INF = int(1e9)
n = int(read())
maps = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    maps[i][i] = 0

m = int(read())
for _ in range(m):
    a, b, c = map(int, read().split())
    maps[a-1][b-1] = min(maps[a-1][b-1], c)

for k in range(n):
    for a in range(n):
        for b in range(n):
            maps[a][b] = min(maps[a][b], maps[a][k] + maps[k][b])

for i in range(n):
    for j in range(n):
        if maps[i][j] >= INF:
            print("0", end=' ')
        else:
            print(maps[i][j], end=' ')
    print()