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

"""
### bisect를 사용하기
from bisect import bisect_left
from sys import stdin
READ = lambda : stdin.readline().strip()


def LIS(arr):
    best = []
    for i in arr:
        idx = bisect_left(best, i)
        if len(best) <= idx:
            best.append(i)
        else:
            best[idx] = i
    return len(best)


n = int(READ())
soldier = list(map(int, READ().split()))[::-1]
print(n - LIS(soldier))
"""