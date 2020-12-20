from sys import stdin
from itertools import combinations
from collections import deque
from copy import deepcopy
read = lambda : stdin.readline().strip()

def get_safety(new_maps):
    count = 0
    for i in range(n):
        for j in range(m):
            if new_maps[i][j] == 0:
                count += 1
    return count


def spread_virus(new_maps, virus):
    q = deque(virus)
    while q:
        vy, vx = q.popleft()

        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if new_maps[ny][nx] == 0:
                    new_maps[ny][nx] = 2
                    q.append((ny, nx))
                elif new_maps[ny][nx] == 1:
                    continue


dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
n, m = map(int, read().split())
maps, installable, virus = [], [], []
for i in range(n):
    maps.append(list(map(int, read().split())))
    for j in range(m):
        if maps[i][j] == 0:
            installable.append((i, j))
        elif maps[i][j] == 2:
            virus.append((i, j))

answer = -1
for com in combinations(installable, 3):
    new_maps = deepcopy(maps)
    for install_y, install_x in com:
        new_maps[install_y][install_x] = 1

    spread_virus(new_maps, virus)

    answer = max(answer, get_safety(new_maps))

print(answer)