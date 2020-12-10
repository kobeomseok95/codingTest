from sys import stdin
read = lambda : stdin.readline().strip()
from bisect import bisect_left

n = int(read())
arr = list(map(int, read().split()))[::-1]
result = []

for i in arr:
    idx = bisect_left(result, i)
    if len(result) <= idx:
        result.append(i)
    else:
        result[idx] = i

print(n - len(result))

# 기존의 방법대로 풀이
# n = int(read())
# arr = list(map(int, read().split()))
# arr.reverse()
#
# dp = [1 for _ in range(n)]
# for i in range(1, n):
#     for j in range(0, i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(n - max(dp))