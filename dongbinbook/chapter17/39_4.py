from sys import stdin
from heapq import heappush, heappop
read = lambda : stdin.readline().strip()


def get_distance(maps):
    n = len(maps)
    visit = [[False for _ in range(n)] for _ in range(n)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    q = []
    heappush(q, (maps[0][0], 0, 0))
    visit[0][0] = True
    while q:
        dist, y, x = heappop(q)
        if y == n - 1 and x == n - 1:
            return dist

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visit[ny][nx]:
                visit[ny][nx] = True
                heappush(q, (dist + maps[ny][nx], ny, nx))


for _ in range(int(read())):
    n = int(read())
    maps = []
    for _ in range(n):
        maps.append(list(map(int, read().split())))

    print(get_distance(maps))