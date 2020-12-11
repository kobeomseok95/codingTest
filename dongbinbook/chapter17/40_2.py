from sys import stdin
from heapq import heappush, heappop
read = lambda : stdin.readline().strip()
INF = int(1e9)

n, m = map(int, read().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF for _ in range(n + 1)]
distance[1] = 0
q = []
heappush(q, (0, 1))

max_val = 0
while q:
    cost, barn = heappop(q)
    if distance[barn] < cost:
        continue

    for nxt_barn in graph[barn]:
        dist = cost + 1
        if distance[nxt_barn] > dist:
            distance[nxt_barn] = dist
            heappush(q, (dist, nxt_barn))

            max_val = max(max_val, dist)

max_count = distance.count(max_val)
min_barn = INF
for i in range(n):
    if distance[i] == max_val:
        min_barn = i
        break

print(min_barn, max_val, max_count)