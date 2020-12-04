### 다시 풀어보기
from sys import stdin
read = lambda : stdin.readline().strip()

n, m = map(int, read().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, read().split())))

tmp = [[0 for _ in range(m)] for _ in range(n)]

dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
result = 0


def get_score():
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                count += 1
    return count


def virus(y, x):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                virus(ny, nx)


def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = maps[i][j]

        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                count += 1
                maps[i][j] = 1
                dfs(count)
                count -= 1
                maps[i][j] = 0


dfs(0)
print(result)