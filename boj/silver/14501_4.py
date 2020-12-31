from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
time, price = [], []
for i in range(n):
    t, p = map(int, read().split())
    time.append(t)
    price.append(p)

dp = [0 for i in range(n + 1)]
max_val = 0
for i in range(n - 1, -1, -1):
    if time[i] + i <= n:
        dp[i] = max(max_val, price[i] + dp[time[i] + i])
        max_val = dp[i]
    else:
        dp[i] = max_val

print(dp[0])