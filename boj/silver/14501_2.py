from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
time, price = [], []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    t, p = map(int, read().split())
    time.append(t)
    price.append(p)

max_value = 0
for i in range(n-1, -1, -1):
    cur_time = time[i] + i
    if cur_time <= n:
        dp[i] = max(max_value, dp[cur_time] + price[i])
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)