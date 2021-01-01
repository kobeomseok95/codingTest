from sys import stdin
read = lambda : stdin.readline().strip()

inf = int(1e9)
n, m = map(int, read().split())

maps = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    maps[i][i] = 0

for i in range(m):
    a, b = map(int, read().split())
    maps[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            maps[a][b] = min(maps[a][k] + maps[k][b], maps[a][b])

answer = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if maps[i][j] != inf or maps[j][i] != inf:
            count += 1
    if count == n:
        answer += 1

print(answer)