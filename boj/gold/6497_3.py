from sys import stdin
read = lambda: stdin.readline().strip()


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


while True:
    m, n = map(int, read().split())
    if m == 0 and n == 0:
        break

    parent = [i for i in range(m)]
    edges = []
    for _ in range(n):
        a, b, c = map(int, read().split())
        edges.append((c, a, b))

    edges.sort()
    result, total = 0, 0
    for edge in edges:
        cost, a, b = edge
        total += cost

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(total - result)