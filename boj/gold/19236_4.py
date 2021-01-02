from sys import stdin
from copy import deepcopy

read = lambda: stdin.readline().strip()


def rotate(direction):
    return (direction + 1) % 8


def find_fish(maps, idx):
    for i in range(4):
        for j in range(4):
            if maps[i][j][0] == idx:
                return i, j
    return None


def move_fish(sy, sx, maps):
    for idx in range(1, 17):
        fish = find_fish(maps, idx)
        if fish is not None:
            y, x = fish
            direction = maps[y][x][1]

            for r in range(8):
                ny, nx = y + dy[direction], x + dx[direction]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    if not (ny == sy and nx == sx):
                        maps[y][x][1] = direction
                        maps[ny][nx], maps[y][x] = maps[y][x], maps[ny][nx]
                        break
                direction = rotate(direction)


def get_next_eat(y, x, maps):
    arr = []
    direction = maps[y][x][1]
    for i in range(4):
        y += dy[direction]
        x += dx[direction]
        if 0 <= y < 4 and 0 <= x < 4 and maps[y][x][0] > 0:
            arr.append((y, x))

    return arr


def dfs(y, x, count, maps):
    global answer
    new_maps = deepcopy(maps)
    count += new_maps[y][x][0]
    new_maps[y][x][0] = -1

    move_fish(y, x, new_maps)

    fishes = get_next_eat(y, x, new_maps)
    if not fishes:
        answer = max(answer, count)
        return

    for fy, fx in fishes:
        dfs(fy, fx, count, new_maps)


dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
maps = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, read().split()))
    for j in range(4):
        maps[i].append([data[2 * j], data[2 * j + 1] - 1])

answer = 0
dfs(0, 0, 0, maps)
print(answer)