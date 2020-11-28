from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
m = int(read())
if m != 0:
    broken = list(map(str, read().split()))

result = abs(n - 100)
for i in range(1000001):
    can = True
    for s in str(i):
        if s in broken:
            can = False
            break

    if can:
        result = min(result, len(str(i)) + abs(n - i))
print(result)










"""
5457
3
6 7 8
"""











