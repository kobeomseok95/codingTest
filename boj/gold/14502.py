### PyPy3 으로 제출
from sys import stdin
READ = lambda: stdin.readline().strip()

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
n, m = map(int, READ().split())
graph = [list(map(int, READ().split())) for _ in range(n)]
tmp = [[0] * m for _ in range(n)]
result = 0


def virus(y, x):
    for i in range(4):
        nexty, nextx = y + dy[i], x + dx[i]
        if 0 <= nexty < n and 0 <= nextx < m:
            if tmp[nexty][nextx] == 0:
                tmp[nexty][nextx] = 2
                virus(nexty, nextx)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1


dfs(0)
print(result)