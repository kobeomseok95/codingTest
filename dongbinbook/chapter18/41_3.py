from sys import stdin
read = lambda : stdin.readline().strip()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, read().split())
parent = [i for i in range(n + 1)]

for i in range(n):
    data = list(map(int, read().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(i + 1, j + 1)

route = list(map(int, read().split()))
answer = True
for i in range(m - 1):
    if find_parent(parent, route[i]) != find_parent(parent, route[i + 1]):
        answer = False
        break

print("YES" if answer else "NO")