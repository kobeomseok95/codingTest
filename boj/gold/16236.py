from sys import stdin
from collections import deque
READ = lambda : stdin.readline().strip()
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
INF = int(1e9)

n = int(READ())
arr = []
for _ in range(n):
    arr.append(list(map(int, READ().split())))

now_size, now_y, now_x = 2, 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            now_y, now_x = i, j
            arr[now_y][now_x] = 0


def bfs():
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque([(now_y, now_x)])
    dist[now_y][now_x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if dist[ny][nx] == -1 and arr[ny][nx] <= now_size:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
    return dist


def find(dist):
    min_dist = INF
    y, x = 0, 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= arr[i][j] < now_size:
                if min_dist > dist[i][j]:
                    min_dist = dist[i][j]
                    y, x = i, j
    if min_dist == INF:
        return None
    else:
        return y, x, min_dist


result, ate = 0, 0
while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_y, now_x = value[0], value[1]
        result += value[2]
        arr[now_y][now_x] = 0
        ate += 1

        if now_size <= ate:
            ate = 0
            now_size += 1