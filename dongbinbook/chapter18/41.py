from sys import stdin
READ = lambda : stdin.readline().strip()


def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, READ().split())

parent = [i for i in range(n + 1)]
for i in range(n):
    data = list(map(int, READ().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)

result = True
tour = list(map(int, READ().split()))
for i in range(m - 1):
    if find_parent(parent, tour[i]) != find_parent(parent, tour[i + 1]):
        result = False
        break

print("YES" if result else "NO")