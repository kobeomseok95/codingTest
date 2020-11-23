from sys import stdin
READ = lambda : stdin.readline().strip()
INF = int(1e9)

n, m = map(int, READ().split())
maps = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            maps[i][j] = 0

for _ in range(m):
    a, b = map(int, READ().split())
    maps[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            maps[a][b] = min(maps[a][b], maps[a][k] + maps[k][b])

answer = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if maps[i][j] != INF or maps[j][i] != INF:
            count += 1
    if count == n:
        answer += 1
print(answer)

















"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""