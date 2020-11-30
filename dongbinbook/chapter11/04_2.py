from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
coin = list(map(int, read().split()))
target = 1
for c in coin:
    if target < c:
        break
    target += c

print(target)