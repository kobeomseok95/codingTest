from sys import stdin
from heapq import heappush, heappop
READ = lambda : stdin.readline().strip()

INF = int(1e9)
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
answers = []
test = int(READ())
for _ in range(test):
    n = int(READ())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, READ().split())))

    distance = [[INF] * n for _ in range(n)]
    y, x = 0, 0
    dist = graph[y][x]
    q = [(dist, y, x)]

    while q:
        dist, y, x = heappop(q)

        if distance[y][x] < dist:
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                cost = dist + graph[ny][nx]
                if distance[ny][nx] > cost :
                    distance[ny][nx] = cost
                    heappush(q, (cost, ny, nx))

    answers.append(distance[n - 1][n - 1])

for i in range(test):
    print(answers[i])