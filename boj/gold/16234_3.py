from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()


def bfs(i, j, count):
    summary = maps[i][j]
    united[i][j] = count
    locate = [(i, j)]
    q = deque()
    q.append((i, j))
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and united[ny][nx] == -1:
                if L <= abs(maps[y][x] - maps[ny][nx]) <= R:
                    united[ny][nx] = count
                    summary += maps[ny][nx]
                    locate.append((ny, nx))
                    q.append((ny, nx))
    for ly, lx in locate:
        maps[ly][lx] = summary // len(locate)


n, L, R = map(int, read().split())
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
maps = []
for _ in range(n):
    maps.append(list(map(int, read().split())))

answer = 0
while True:
    count = 0
    united = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if united[i][j] == -1:
                bfs(i, j, count)
                count += 1

    if count >= n * n:
        break
    answer += 1

print(answer)