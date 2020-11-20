from sys import stdin
READ = lambda : stdin.readline().strip()

n = int(READ())
dp = [0] * n
dp[0] = 1

i2, i3, i5 = 0, 0, 0
nx2, nx3, nx5 = 2, 3, 5
for i in range(1, n):
    dp[i] = min(nx2, nx3, nx5)

    if dp[i] == nx2:
        i2 += 1
        nx2 = dp[i2] * 2

    if dp[i] == nx3:
        i3 += 1
        nx3 = dp[i3] * 3

    if dp[i] == nx5:
        i5 += 1
        nx5 = dp[i5] * 5

print(dp[n-1])