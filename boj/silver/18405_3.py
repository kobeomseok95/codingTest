from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, k = map(int, read().split())
maps, virus = [], []
for i in range(n):
    maps.append(list(map(int, read().split())))
    for j in range(n):
        if maps[i][j] != 0:
            virus.append((maps[i][j], i, j, 0))

virus.sort()
s, y, x = map(int, read().split())

q = deque(virus)
while q:
    virus_no, vy, vx, second = q.popleft()
    if second == s:
        break

    for i in range(4):
        ny, nx = vy + dy[i], vx + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if maps[ny][nx] == 0:
                maps[ny][nx] = virus_no
                q.append((virus_no, ny, nx, second + 1))

print(maps[y-1][x-1])