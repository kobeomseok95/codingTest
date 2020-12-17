from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
data = list(map(int, read().split()))
data.sort()

target = 1
for i in range(n):
    if target < data[i]:
        break
    target += data[i]

print(target)