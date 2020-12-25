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


g = int(read())
p = int(read())
parent = [i for i in range(g + 1)]

count = 0
for _ in range(p):
    air = int(read())
    if find_parent(parent, air) != 0:
        union_parent(parent, parent[air], parent[air] - 1)
        count += 1
    else:
        break

print(count)