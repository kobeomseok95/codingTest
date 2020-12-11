from sys import stdin
from heapq import heappush, heappop
read = lambda : stdin.readline().strip()


dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
INF = int(1e9)
for _ in range(int(read())):
    n = int(read())
    maps = []
    for _ in range(n):
        maps.append(list(map(int, read().split())))

    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = maps[0][0]
    q = [(maps[0][0], 0, 0)]
    while q:
        cost, y, x = heappop(q)
        if distance[y][x] < cost:
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if distance[ny][nx] > cost + maps[ny][nx]:
                    distance[ny][nx] = cost + maps[ny][nx]
                    heappush(q, (cost + maps[ny][nx], ny, nx))

    print(distance[n-1][n-1])