from copy import deepcopy
from sys import stdin
READ = lambda : stdin.readline().strip()
dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]

arr = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, READ().split()))
    for j in range(4):
        arr[i].append([data[2 * j], data[2 * j + 1] - 1])


def rotate_direction(direction):
    return (direction + 1) % 8


def find_fishes(arr, idx):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == idx:
                return (i, j)
    return None


def move_all_fishes(arr, shark_y, shark_x):
    for idx in range(1, 17):
        fish_pos = find_fishes(arr, idx)

        if fish_pos != None:
            fish_y, fish_x = fish_pos[0], fish_pos[1]
            direction = arr[fish_y][fish_x][1]

            for i in range(8):
                ny, nx = fish_y + dy[direction], fish_x + dx[direction]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    if not (ny == shark_y and nx == shark_x):
                        arr[fish_y][fish_x][1] = direction
                        arr[fish_y][fish_x], arr[ny][nx] = arr[ny][nx], arr[fish_y][fish_x]
                        break

                direction = rotate_direction(direction)


def shark_possible_position(arr, now_y, now_x):
    pos = []
    direct = arr[now_y][now_x][1]
    for i in range(4):
        now_y += dy[direct]
        now_x += dx[direct]
        if 0 <= now_y < 4 and 0 <= now_x < 4:
            if arr[now_y][now_x][0] != -1:
                pos.append((now_y, now_x))
    return pos


def dfs(arr, shark_y, shark_x, total):
    global result
    arr = deepcopy(arr)
    total += arr[shark_y][shark_x][0]
    arr[shark_y][shark_x][0] = -1

    move_all_fishes(arr, shark_y, shark_x)

    pos = shark_possible_position(arr, shark_y, shark_x)
    if len(pos) == 0:
        result = max(result, total)
        return
    for p in pos:
        dfs(arr, p[0], p[1], total)


result = 0
dfs(arr, 0, 0, 0)
print(result)