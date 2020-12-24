from sys import stdin
from heapq import heappush, heappop
read = lambda : stdin.readline().strip()

INF = int(1e9)
n, m = map(int, read().split())
maps = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, read().split())
    maps[a].append(b)
    maps[b].append(a)

distance = [INF for _ in range(n + 1)]
distance[1] = 0
q = []
heappush(q, (0, 1))

while q:
    dist, now = heappop(q)
    if distance[now] < dist:
        continue

    for nxt in maps[now]:
        cost = dist + 1
        if distance[nxt] > cost:
            distance[nxt] = cost
            heappush(q, (cost, nxt))

max_val = 0
barn = []
for i in range(1, n + 1):
    max_val = max(max_val, distance[i])

for i in range(1, n + 1):
    if max_val == distance[i]:
        barn.append(i)
print(barn[0], max_val, len(barn))

# 다른 풀이
# n, m = map(int, read().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, read().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visit = [False for _ in range(n + 1)]
# visit[1] = True
# before = [1]
# dist = 0
# while True:
#     after = []
#     for i in before:
#         for nxt in graph[i]:
#             if not visit[nxt]:
#                 visit[nxt] = True
#                 after.append(nxt)
#
#     if not after:
#         break
#     before = after
#     dist += 1
#
# print(min(before), dist, len(before))
















