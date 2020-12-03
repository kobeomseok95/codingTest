from sys import stdin
from itertools import combinations
read = lambda : stdin.readline().strip()

n, m = map(int, read().split())
maps, house, chickens = [], [], []
for i in range(n):
    maps.append(list(map(int, read().split())))
    for j in range(n):
        if maps[i][j] == 2:
            chickens.append((i, j))
        elif maps[i][j] == 1:
            house.append((i, j))

min_distance = int(1e9)
for c in combinations(chickens, m):
    sum_distance = 0
    for h in house:
        sum_distance += min([abs(h[0]-cy) + abs(h[1] - cx) for cy, cx in c])

    min_distance = min(min_distance, sum_distance)

print(min_distance)