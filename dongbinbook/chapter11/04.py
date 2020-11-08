from sys import stdin
READ = lambda : stdin.readline().strip()

n = int(READ())
coin = list(map(int, READ().split()))
coin.sort()

target = 1
for i in coin:
    if target < i:
        break
    target += i
print(target)