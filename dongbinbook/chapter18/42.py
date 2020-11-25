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


g = int(READ())
p = int(READ())
parent = [i for i in range(g + 1)]

result = 0
for _ in range(p):
    data = find_parent(parent, int(READ()))
    if data == 0:
        break
    union_parent(parent, data, data - 1)
    result += 1

print(result)