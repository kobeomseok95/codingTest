from sys import stdin
read = lambda : stdin.readline().strip()


def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if maps[i][j] != 0:
                smell[i][j] = [maps[i][j], k]


def move():
    new_array = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if maps[y][x] != 0:
                direction = directions[maps[y][x] - 1]
                found = False

                for index in range(4):
                    nx = x + dx[priority[maps[y][x] - 1][direction - 1][index] - 1]
                    ny = y + dy[priority[maps[y][x] - 1][direction - 1][index] - 1]

                    if 0 <= ny < n and 0 <= nx < n:
                        if smell[ny][nx][1] == 0:
                            directions[maps[y][x] - 1] = priority[maps[y][x] - 1][direction - 1][index]
                            if new_array[ny][nx] == 0:
                                new_array[ny][nx] = maps[y][x]
                            else:
                                new_array[ny][nx] = min(maps[y][x], new_array[ny][nx])
                            found = True
                            break
                if found:
                    continue

                for index in range(4):
                    nx = x + dx[priority[maps[y][x] - 1][direction - 1][index] - 1]
                    ny = y + dy[priority[maps[y][x] - 1][direction - 1][index] - 1]
                    if 0 <= ny < n and 0 <= nx < n:
                        if smell[ny][nx][0] == maps[y][x]:
                            directions[maps[y][x] - 1] = priority[maps[y][x] - 1][direction - 1][index]
                            new_array[ny][nx] = maps[y][x]
                            break
    return new_array


# 1, 2, 3, 4 : 위 아래 왼 오른
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m, k = map(int, read().split())
maps = []
for i in range(n):
    maps.append(list(map(int, read().split())))

# 상어의 방향 순서대로 입력
directions = list(map(int, read().split()))

smell = [[[0, 0]] * n for _ in range(n)]

# 우선순위
priority = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priority[i].append(list(map(int, read().split())))

time = 0
while True:
    update_smell()
    new_array = move()
    maps = new_array
    time += 1

    chk = True
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 1:
                chk = False

    if chk:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break