#### 2회독째
from sys import stdin

read = lambda: stdin.readline().strip()

n = int(read())
fear = list(map(int, read().split()))

fear.sort()
group, member = 0, 0
for i in range(n):
    member += 1
    if fear[i] == member:
        group += 1
        member = 0

print(group)