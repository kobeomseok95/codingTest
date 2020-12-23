from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
time, price = [], []
for _ in range(n):
    x, y = map(int, read().split())
    time.append(x)
    price.append(y)

dp = [0 for _ in range(n + 1)]
max_val = 0
for day in range(n - 1, -1, -1):
    if day + time[day] <= n:
        dp[day] = max(max_val, price[day] + dp[day + time[day]])
        max_val = dp[day]
    else:
        dp[day] = max_val

print(max(dp))




















# print("time =", time)
# print("price =", price)
# print("=======================================")
# print(dp)