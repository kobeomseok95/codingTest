from sys import stdin
from heapq import heappush, heappop
READ = lambda : stdin.readline().strip()
INF = int(1e9)

def dijkstra(start, end):
    q = []
    distance = [INF] * (n + 1)
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        for nxt, weight in graph[now]:
            cost = weight + dist
            if distance[nxt] > cost:
                distance[nxt] = cost
                heappush(q, (cost, nxt))
    return distance[end]


n, e = map(int, READ().split())
start = 1

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, READ().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, READ().split())

one = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
two = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
if one + two >= INF:
    print("-1")
else:
    print(min(one, two))