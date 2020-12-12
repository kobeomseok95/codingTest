from sys import stdin
read = lambda : stdin.readline().strip()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


g = int(read())
p = int(read())

parent = [0 for _ in range(g + 1)]

for i in range(1, g + 1):
    parent[i] = i

count = 0
for _ in range(p):
    find_parent_no = find_parent(parent, int(read()))
    if find_parent_no != 0:
        count += 1
        union_parent(parent, find_parent_no, find_parent_no - 1)
    else:
        break

print(count)