from sys import stdin
import copy
read = lambda : stdin.readline().strip()

dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
array = [[False for _ in range(4)] for _ in range(4)]
for i in range(4):
    data = list(map(int, read().split()))
    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]


def turn_left(direction):
    return (direction + 1) % 8


def find_fishes(array, idx):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == idx:
                return i, j
    return None


def move_all_fishes(array, now_y, now_x):
    for i in range(1, 17):
        position = find_fishes(array, i)
        if position is not None:
            y, x = position[0], position[1]
            direction = array[y][x][1]

            for _ in range(8):
                ny, nx = y + dy[direction], x + dx[direction]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    if not (ny == now_y and nx == now_x):
                        array[y][x][1] = direction
                        array[y][x], array[ny][nx] = array[ny][nx], array[y][x]
                        break

                direction = turn_left(direction)


def get_eatable_fishes(array, now_y, now_x):
    arr = []
    direction = array[now_y][now_x][1]
    for i in range(4):
        now_y += dy[direction]
        now_x += dx[direction]
        if 0 <= now_y < 4 and 0 <= now_x < 4:
            if array[now_y][now_x][0] != -1:
                arr.append((now_y, now_x))
    return arr


def dfs(array, now_y, now_x, total):
    global result
    array = copy.deepcopy(array)
    total += array[now_y][now_x][0]
    array[now_y][now_x][0] = -1

    move_all_fishes(array, now_y, now_x)

    eatable_fishes = get_eatable_fishes(array, now_y, now_x)
    if len(eatable_fishes) == 0:
        result = max(result, total)
        return

    for ny, nx, in eatable_fishes:
        dfs(array, ny, nx, total)


result = 0
dfs(array, 0, 0, 0)
print(result)