from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
coins = list(map(int, read().split()))
coins.sort()

target = 1
for i in range(n):
    if target < coins[i]:
        break
    target += coins[i]

print(target)