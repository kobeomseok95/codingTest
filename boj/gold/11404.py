from sys import stdin
READ = lambda : stdin.readline().strip()
INF = int(1e9)

n = int(READ())
m = int(READ())

cities = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            cities[a][b] = 0

for _ in range(m):
    a, b, c = map(int, READ().split())
    cities[a][b] = min(cities[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            cities[a][b] = min(cities[a][b], cities[a][k] + cities[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cities[i][j] >= INF:
            print("0", end = ' ')
        else:
            print(cities[i][j], end=' ')
    print()

"""
from sys import stdin
READ = lambda : stdin.readline().strip()
INF = int(1e9)

n = int(READ())
m = int(READ())

maps = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            maps[i][j] = 0

for _ in range(m):
    a, b, c = map(int, READ().split())
    maps[a][b] = min(maps[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            maps[a][b] = min(maps[a][b], maps[a][k] + maps[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if maps[i][j] >= INF:
            print("0", end=' ')
        else:
            print(maps[i][j], end=' ')
    print()
"""