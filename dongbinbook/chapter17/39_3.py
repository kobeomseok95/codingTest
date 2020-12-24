from sys import stdin
from heapq import heappush, heappop
read = lambda : stdin.readline().strip()

INF = int(1e9)
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def dijkstra(n, maps):
    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = maps[0][0]
    q = []
    heappush(q, (maps[0][0], 0, 0))

    while q:
        dist, now_y, now_x = heappop(q)
        if distance[now_y][now_x] < dist:
            continue

        for i in range(4):
            ny, nx = now_y + dy[i], now_x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                cost = dist + maps[ny][nx]
                if distance[ny][nx] > cost:
                    distance[ny][nx] = cost
                    heappush(q, (cost, ny, nx))

    return distance


for _ in range(int(read())):
    n = int(read())
    maps = [list(map(int, read().split())) for _ in range(n)]
    distance = dijkstra(n, maps)
    print(distance[n - 1][n - 1])