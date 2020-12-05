from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()


n, k = map(int, read().split())
dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
maps, data = [], []
for i in range(n):
    maps.append(list(map(int, read().split())))
    for j in range(n):
        if maps[i][j] != 0:
            # 바이러스 종류, 초, y, x
            data.append((maps[i][j], 0, i, j))

data.sort()
target_second, target_y, target_x = map(int, read().split())

q = deque(data)
tmp = 0
while q:
    virus, second, y, x, = q.popleft()
    if second == target_second:
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if maps[ny][nx] == 0:
                maps[ny][nx] = virus
                q.append((virus, second + 1, ny, nx))

print(maps[target_y - 1][target_x - 1])