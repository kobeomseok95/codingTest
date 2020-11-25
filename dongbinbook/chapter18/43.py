from sys import stdin
READ = lambda : stdin.readline().strip()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x > y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, READ().split())
parent = [i for i in range(n)]
load = []
for _ in range(m):
    x, y, z = map(int, READ().split())
    load.append((z, x, y))

load.sort()
result, total = 0, 0
for l in load:
    cost, x, y = l
    total += cost

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(total - result)