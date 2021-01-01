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


while True:
    n, m = map(int, read().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n)]

    heap = []
    for _ in range(m):
        x, y, z = map(int, read().split())
        heap.append((z, x, y))

    heap.sort()
    answer, onable = 0, 0
    for h in heap:
        cost, a, b = h
        answer += cost
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            onable += cost

    print(answer - onable)