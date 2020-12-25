from sys import stdin
read = lambda : stdin.readline().strip()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(read())
parent = [i for i in range(n + 1)]

x, y, z = [], [], []
for i in range(1, n + 1):
    data = list(map(int, read().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n - 1):
    # 이전과 다음의 거리, 이전좌표, 다음좌표
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()
answer = 0
for edge in edges:
    cost, now, nxt = edge
    if find_parent(parent, now) != find_parent(parent, nxt):
        union_parent(parent, now, nxt)
        answer += cost

print(answer)