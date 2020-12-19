from sys import stdin
from itertools import combinations
read = lambda : stdin.readline().strip()

n, m = map(int, read().split())
maps, house, chicken = [], [], []
for i in range(n):
    maps.append(list(map(int, read().split())))
    for j in range(n):
        if maps[i][j] == 1:
            house.append((i, j))
        elif maps[i][j] == 2:
            chicken.append((i, j))

answer = int(1e9)
for com in combinations(chicken, m):
    tmp = 0
    for h in house:
        min_length = int(1e9)
        for c in com:
            min_length = min(min_length, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        tmp += min_length

    answer = min(answer, tmp)

print(answer)