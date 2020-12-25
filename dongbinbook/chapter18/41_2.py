## 오답

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


n, m = map(int, read().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, read().split())))

plan = list(map(int, read().split()))

parent = [0 for _ in range(n + 1)]
for i in range(n + 1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if i != j and graph[i][j] == graph[j][i]:
            union_parent(parent, i + 1, j + 1)

possible = True
for i in range(1, n + 1):
    if parent[i] != 1:  # 1이 아닐수도있다.
        possible = False
        break

print("YES" if possible else "NO")