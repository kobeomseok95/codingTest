from sys import stdin
READ = lambda : stdin.readline().strip()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


test = int(READ())
for _ in range(test):
    n, m = map(int, READ().split())
    parent = [i for i in range(n + 1)]

    graph = []
    for _ in range(m):
        a, b = map(int, READ().split())
        graph.append((a, b))

    answer = 0
    for start, end in graph:
        if find_parent(parent, start) != find_parent(parent, end):
            union_parent(parent, start, end)
            answer += 1
    print(answer)