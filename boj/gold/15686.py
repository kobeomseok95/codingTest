from itertools import combinations
from sys import stdin
READ = lambda : stdin.readline().strip()

n, m = map(int, READ().split())
board = [list(map(int, READ().split())) for _ in range(n)]

house, chicken = [], []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

min_distance = int(1e9)
for c in combinations(chicken, m):
    sum_distance = 0
    for h in house:
        sum_distance += min( [abs(h[0] - cy) + abs(h[1] - cx) for cy, cx in c] )

    min_distance = min(min_distance, sum_distance)
print(min_distance)