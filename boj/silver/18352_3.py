from sys import stdin
from heapq import heappush, heappop
read = lambda : stdin.readline().strip()

n, m, k, x = map(int, read().split())
visit = [False for _ in range(n + 1)]
maps = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, read().split())
    maps[a].append((b, 1))

answer = []
q = []
heappush(q, (0, x))
visit[x] = True
while q:
    dist, now = heappop(q)
    if dist > k:
        break
    elif dist == k:
        answer.append(now)

    for m in maps[now]:
        nxt, cost = m[0], m[1]
        if not visit[nxt]:
            heappush(q, (cost + dist, nxt))
            visit[nxt] = True

if not answer:
    print("-1")
else:
    answer.sort()
    for a in answer:
        print(a)