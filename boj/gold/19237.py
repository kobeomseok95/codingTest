from sys import stdin
read = lambda : stdin.readline().strip()
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m, k = map(int, read().split())
maps = []
for i in range(n):
    maps.append(list(map(int, read().split())))

directions = list(map(int, read().split()))
priorities = [[] for _ in range(m)]
smell = [[[0,0] for _ in range(n)] for _ in range(n)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, read().split())))


def smell_check():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if maps[i][j] != 0:
                smell[i][j] = [maps[i][j], k]


def move():
    new_maps = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            # 움직일 상어 찾음
            if maps[y][x] != 0:
                #방향
                direction = directions[maps[y][x] - 1]
                found = False
                for idx in range(4):
                    ny = y + dy[priorities[maps[y][x] - 1][direction - 1][idx] - 1]
                    nx = x + dx[priorities[maps[y][x] - 1][direction - 1][idx] - 1]
                    if 0 <= ny < n and 0 <= nx < n:
                        # 이동할 곳에 냄새가 없다면
                        if smell[ny][nx][1] == 0:
                            directions[maps[y][x] - 1] = priorities[maps[y][x] - 1][direction - 1][idx]
                            if new_maps[ny][nx] == 0:
                                new_maps[ny][nx] = maps[y][x]
                            else:
                                new_maps[ny][nx] = min(new_maps[ny][nx], maps[y][x])
                            found = True
                            break
                if found:
                    continue
                # 이동할 곳이 없다면 내 냄새로 가자
                for idx in range(4):
                    ny = y + dy[priorities[maps[y][x] - 1][direction - 1][idx] - 1]
                    nx = x + dx[priorities[maps[y][x] - 1][direction - 1][idx] - 1]
                    if 0 <= ny < n and 0 <= nx < n:
                        if smell[ny][nx][0] == maps[y][x]:
                            directions[maps[y][x] - 1] = priorities[maps[y][x] - 1][direction - 1][idx]
                            new_maps[ny][nx] = maps[y][x]
                            break
    return new_maps



time = 0
while True:
    smell_check()
    new_maps = move()
    maps = new_maps
    time += 1

    # 1번 상어 이외의 다른 상어 체크
    chk = True
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 1:
                chk = False
    if chk:
        print(time)
        break

    if time >= 1000:
        print("-1")
        break