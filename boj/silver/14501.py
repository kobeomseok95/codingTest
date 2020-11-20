from sys import stdin
READ = lambda : stdin.readline().strip()

n = int(READ())
t, p = [], []
dp = [0] * (n + 1)
for _ in range(n):
    ti, pi = map(int, READ().split())
    t.append(ti)
    p.append(pi)

max_val = 0
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val)