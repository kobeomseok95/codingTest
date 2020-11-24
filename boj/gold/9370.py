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
    return distance


test = int(READ())
for _ in range(test):
    n, m, t = map(int, READ().split())
    s, g, h = map(int, READ().split())

    graph = [[] for _ in range(n + 1)]
    candidate = []
    for _ in range(m):
        a, b, d = map(int, READ().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):
        candidate.append(int(READ()))

    result = []
    distances = dijkstra(s, n)
    distances_node1 = dijkstra(g, n)
    distances_node2 = dijkstra(h, n)
    gh = 0

    for x, d in graph[g]:
        if x == h:
            gh = d
            break

    for c in candidate:
        if distances[c] == distances[g] + gh + distances_node2[c] \
            or distances[c] == distances[h] + gh + distances_node1[c]:
            result.append(c)
    result.sort()
    for i in range(len(result)):
        print(result[i], end=' ')
    print()