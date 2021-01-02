from sys import stdin
from copy import deepcopy
from collections import deque
read = lambda : stdin.readline().strip()


def find_shark(maps):
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 9:
                return i, j


def find_eat_fish():
    eatable = []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    visit = [[False for _ in range(n)] for _ in range(n)]

    q = deque()
    q.append((shark[0], shark[1], 0))
    visit[shark[0]][shark[1]] = True
    while q:
        y, x, dist = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visit[ny][nx]:
                visit[ny][nx] = True
                if 0 < maps[ny][nx] <= size - 1:
                    eatable.append((dist + 1, ny, nx))
                elif maps[ny][nx] == 0 or maps[ny][nx] == size:
                    q.append((ny, nx, dist + 1))

    if not eatable:
        return None

    eatable.sort()
    return eatable[0]


n = int(read())
maps = []
for i in range(n):
    maps.append(list(map(int, read().split())))

size, eat_count, answer = 2, 0, 0
while True:
    shark = find_shark(maps)
    nxt = find_eat_fish()
    if nxt is None:
        break

    dist, fish_y, fish_x = nxt
    answer += dist
    eat_count += 1
    if size <= eat_count:
        eat_count = 0
        size += 1

    maps[shark[0]][shark[1]] = 0
    maps[fish_y][fish_x] = 9
    maps = deepcopy(maps)

print(answer)