from sys import stdin
from bisect import bisect_left
read = lambda : stdin.readline().strip()

n = int(read())
arr = list(map(int, read().split()))[::-1]
result = []

for i in arr:
    idx = bisect_left(result, i)
    if idx == len(result):
        result.append(i)
    elif idx < len(result):
        result[idx] = i

print(len(arr) - len(result))