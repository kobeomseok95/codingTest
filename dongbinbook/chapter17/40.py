from sys import stdin
from heapq import heappop, heappush
READ = lambda : stdin.readline().strip()
INF = int(1e9)

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))


n, m = map(int, READ().split())

distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, READ().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

start = 1
dijkstra(start)

max_node, max_distance = 0, 0
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_distance = distance[i]
        max_node = i
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
print(max_node, max_distance, len(result))