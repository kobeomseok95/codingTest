from bisect import bisect_left, bisect_right
from sys import stdin
READ = lambda : stdin.readline().strip()


def count_by_range(arr, left, right):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx

n, x = map(int, READ().split())
arr = list(map(int, READ().split()))

count = count_by_range(arr, x, x)

if count == 0:
    print(-1)
else:
    print(count)