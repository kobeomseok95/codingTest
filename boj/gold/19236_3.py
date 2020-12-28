from sys import stdin
from copy import deepcopy
read = lambda : stdin.readline().strip()


def rotate_direction(direction):
    return (direction + 1) % 8


def find_fish_no(maps, no):
    for i in range(4):
        for j in range(4):
            if maps[i][j][0] == no:
                return i, j
    return None


def move_fishes(maps, now_y, now_x):
    for i in range(1, 17):
        fish_no = find_fish_no(maps, i)
        if fish_no is not None:
            y, x = fish_no[0], fish_no[1]
            direction = maps[y][x][1]
            for d in range(8):
                ny, nx = y + dy[direction], x + dx[direction]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    if not (ny == now_y and nx == now_x):
                        maps[y][x][1] = direction
                        maps[ny][nx], maps[y][x] = maps[y][x], maps[ny][nx]
                        break
                direction = rotate_direction(direction)


def find_eat_fish(maps, y, x):
    fishes = []
    direction = maps[y][x][1]
    for i in range(4):
        y += dy[direction]
        x += dx[direction]
        if 0 <= y < 4 and 0 <= x < 4 and maps[y][x][0] > 0:
            fishes.append([y, x])

    return fishes


def dfs(maps, shark_y, shark_x, count):
    global answer
    maps = deepcopy(maps)
    count += maps[shark_y][shark_x][0]
    maps[shark_y][shark_x][0] = -1

    move_fishes(maps, shark_y, shark_x)
    eat_fishes = find_eat_fish(maps, shark_y, shark_x)
    if not eat_fishes:
        answer = max(answer, count)
        return
    for fish in eat_fishes:
        dfs(maps, fish[0], fish[1], count)


dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
maps = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, read().split()))
    for j in range(4):
        maps[i].append([data[j * 2], data[j * 2 + 1] - 1])

answer = 0
dfs(maps, 0, 0, 0)
print(answer)