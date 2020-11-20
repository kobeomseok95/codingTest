from sys import stdin
READ = lambda : stdin.readline().strip()

n = int(READ())
soldier = list(map(int, READ().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if soldier[i] < soldier[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))