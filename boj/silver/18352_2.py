from sys import stdin
from heapq import heappush, heappop
read = lambda : stdin.readline().strip()

n, m, k, x = map(int, read().split())
graph = [[] for _ in range(n + 1)]
answer = []
for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)

visited = [False for _ in range(n + 1)]
q = []
heappush(q, (0, x))
visited[x] = True

while q:
    dist, now = heappop(q)
    if dist == k:
        answer.append(now)
    elif dist > k:
        break

    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            heappush(q, (dist + 1, nxt))

if not answer:
    print("-1")
else:
    for a in sorted(answer):
        print(a)