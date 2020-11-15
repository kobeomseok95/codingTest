from collections import deque
from sys import stdin
READ = lambda : stdin.readline().strip()

n, k = map(int, READ().split())
graph = []
virus = []
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

for i in range(n):
    graph.append(list(map(int, READ().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

ts, tx, ty = map(int, READ().split())

virus.sort()
q = deque(virus)
while q:
    virus_no, sec, x, y = q.popleft()
    if sec == ts:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus_no
                q.append((virus_no, sec + 1, nx, ny))

print(graph[tx - 1][ty - 1])