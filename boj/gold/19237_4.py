from sys import stdin
read = lambda : stdin.readline().strip()


def move_shark():
    new_maps = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] != 0:
                y, x = i, j
                no = maps[i][j]
                direction = now_direction[no - 1]
                move_success = False

                for d in range(4):
                    ny = y + dy[directions[no - 1][direction - 1][d] - 1]
                    nx = x + dx[directions[no - 1][direction - 1][d] - 1]
                    if 0 <= ny < n and 0 <= nx < n:
                        # 해당방향에 냄새가 없을 경우
                        if smells[ny][nx][1] == 0:
                            now_direction[no - 1] = directions[no - 1][direction - 1][d]
                            # 상어가 있을 경우
                            if new_maps[ny][nx] != 0:
                                new_maps[ny][nx] = min(new_maps[ny][nx], maps[y][x])
                            # 상어가 없을 경우
                            elif new_maps[ny][nx] == 0:
                                new_maps[ny][nx] = maps[y][x]
                            move_success = True
                            break

                if not move_success:
                    for d in range(4):
                        ny = y + dy[directions[no - 1][direction - 1][d] - 1]
                        nx = x + dx[directions[no - 1][direction - 1][d] - 1]
                        if 0 <= ny < n and 0 <= nx < n:
                            if smells[ny][nx][0] == no:
                                now_direction[no - 1] = directions[no - 1][direction - 1][d]
                                new_maps[ny][nx] = no
                                break
    return new_maps


def spread_smells():
    for i in range(n):
        for j in range(n):
            if smells[i][j][1] > 0:
                smells[i][j][1] -= 1
            if maps[i][j] != 0:
                smells[i][j] = [maps[i][j], k]


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m, k = map(int, read().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, read().split())))

now_direction = list(map(int, read().split()))
directions = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        directions[i].append(list(map(int, read().split())))

smells = [[[0, 0] for _ in range(n)] for _ in range(n)]

count = 0
while True:
    spread_smells()
    new_maps = move_shark()
    maps = new_maps

    count += 1
    chk = True
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 1:
                chk = False

    if chk:
        print(count)
        break

    if count >= 1000:
        print(-1)
        break