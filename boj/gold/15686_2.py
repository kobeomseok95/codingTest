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

answer = int(1e9)
for chicken in combinations(chickens, m):
    total = 0
    for h in house:
        house_chicken = int(1e9)
        for c in chicken:
            house_chicken = min(abs(h[0] - c[0]) + abs(h[1] - c[1]), house_chicken)
        total += house_chicken
    answer = min(answer, total)

print(answer)