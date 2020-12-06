from collections import deque
from sys import stdin
read = lambda : stdin.readline().strip()

n, l, r = map(int, read().split())
graph = []
dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
for _ in range(n):
    graph.append(list(map(int, read().split())))


def process(y, x, index):
    union[y][x] = index
    summary = graph[y][x]
    count = 1
    united = [(y, x)]
    q = deque()
    q.append((y, x))

    while q:
        uy, ux = q.popleft()
        for i in range(4):
            ny, nx = uy + dy[i], ux + dx[i]
            if 0 <= ny < n and 0 <= nx < n and union[ny][nx] == -1:
                if l <= abs(graph[ny][nx] - graph[uy][ux]) <= r:
                    union[ny][nx] = index
                    summary += graph[ny][nx]
                    count += 1
                    united.append((ny, nx))
                    q.append((ny, nx))

    for i, j in united:
        graph[i][j] = summary // count


result = 0
while True:
    union = [[-1 for _ in range(n)] for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1

    if index == n * n:
        break
    result += 1

print(result)