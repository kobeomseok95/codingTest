from sys import stdin
READ = lambda : stdin.readline().strip()

n, m = map(int, READ().split())
ball = list(map(int, READ().split()))
weight = [0] * (m + 1)
for i in ball:
    weight[i] += 1

ans = 0
for i in range(1, m + 1):
    n -= weight[i]
    ans += weight[i] * n

print(ans)