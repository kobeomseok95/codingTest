from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
dp = [1 for _ in range(n)]

i2, i3, i5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5
dp = [1 for _ in range(n)]
for i in range(1, n):
    dp[i] = min(next2, next3, next5)

    if dp[i] % 2 == 0:
        i2 += 1
        next2 = dp[i2] * 2

    if dp[i] % 3 == 0:
        i3 += 1
        next3 = dp[i3] * 3

    if dp[i] % 5 == 0:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[n-1])