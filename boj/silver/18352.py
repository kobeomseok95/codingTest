from sys import stdin
from collections import deque
READ = lambda : stdin.readline().strip()

n, m, k, x = map(int, READ().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, READ().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0

q = deque()
q.append(x)
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

chk = False
for i in range(1, n + 1):
    if dist[i] == k:
        chk = True
        print(i)
if not chk:
    print(-1)