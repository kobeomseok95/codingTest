from sys import stdin
read = lambda : stdin.readline().strip()

n, m = map(int, read().split())
maps = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, read().split())
    maps[a].append(b)
    maps[b].append(a)

visit = [False for _ in range(n + 1)]
visit[1] = True
before = [1]
dist = 0
while True:
    after = []
    for i in before:
        for nxt in maps[i]:
            if not visit[nxt]:
                visit[nxt] = True
                after.append(nxt)

    if not after:
        break

    dist += 1
    before = after

print(min(before), dist, len(before))

















