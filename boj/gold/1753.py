from sys import stdin
from heapq import heappush, heappop
READ = lambda : stdin.readline().strip()
INF = int(1e9)

def dijkstra(start):
    q = []
    distance[start] = 0
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue

        for nxt, cost in graph[now]:
            nxt_cost = cost + dist
            if distance[nxt] > nxt_cost:
                distance[nxt] = nxt_cost
                heappush(q, (nxt_cost, nxt))


v, e = map(int, READ().split())
start = int(READ())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for _ in range(e):
    a, b, e = map(int, READ().split())
    graph[a].append((b, e))

dijkstra(start)
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])








