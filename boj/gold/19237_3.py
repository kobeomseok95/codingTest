from sys import stdin
read = lambda : stdin.readline().strip()


def find_shark(no):
    for i in range(n):
        for j in range(n):
            if maps[i][j] == no:
                return i, j
    return None


def move():
    new_maps = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if maps[y][x] != 0:
                direction = now_direction[maps[y][x] - 1]
                found = False

                for idx in range(4):
                    ny = y + dy[priorities[maps[y][x] - 1][direction - 1][idx] - 1]
                    nx = x + dx[priorities[maps[y][x] - 1][direction - 1][idx] - 1]
                    if 0 <= ny < n and 0 <= nx < n:
                        if smells[ny][nx][1] == 0:
                            now_direction[maps[y][x] - 1] = priorities[maps[y][x] - 1][direction - 1][idx]
                            if new_maps[ny][nx] == 0:
                                new_maps[ny][nx] = maps[y][x]
                            else:
                                new_maps[ny][nx] = min(new_maps[ny][nx], maps[y][x])
                            found = True
                            break
                if found:
                    continue
                for idx in range(4):
                    ny = y + dy[priorities[maps[y][x] - 1][direction - 1][idx] - 1]
                    nx = x + dx[priorities[maps[y][x] - 1][direction - 1][idx] - 1]
                    if 0 <= ny < n and 0 <= nx < n:
                        if smells[ny][nx][0] == maps[y][x]:
                            now_direction[maps[y][x] - 1] = priorities[maps[y][x] - 1][direction - 1][idx]
                            new_maps[ny][nx] = maps[y][x]
                            break
    return new_maps


def spread_smell():
    for i in range(n):
        for j in range(n):
            if smells[i][j][1] > 0:
                smells[i][j][1] -= 1

            if maps[i][j] != 0:
                smells[i][j] = [maps[i][j], k]


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m, k = map(int, read().split())
maps = []
smells = [[[0, 0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    maps.append(list(map(int, read().split())))

# 상어가 현재 바라보는 방향
now_direction = list(map(int, read().split()))

# 각 상어들의 바라보는 방향에 따른 우선순위
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, read().split())))

time = 0
while True:
    spread_smell()
    new_maps = move()
    maps = new_maps
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