from sys import stdin
read = lambda : stdin.readline().strip()

INF = int(1e9)
n, m = map(int, read().split())
maps = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    maps[i][i] = 0

for _ in range(m):
    a, b = map(int, read().split())
    maps[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            maps[a][b] = min(maps[a][b], maps[a][k] + maps[k][b])

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(maps[i][j], end = ' ')
#     print()

result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if maps[i][j] != INF or maps[j][i] != INF:
            count += 1

    if count == n:
        result += 1
print(result)