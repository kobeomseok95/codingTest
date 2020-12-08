from sys import stdin
READ = lambda : stdin.readline().strip()


def count_by_value(array, x):
    n = len(array)
    a = first(array, x, 0, n - 1)
    if a == None:
        return 0
    b = last(array, x, 0, n - 1)

    return b - a + 1


def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)


n, x = map(int, READ().split())
array = list(map(int, READ().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)
"""
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
"""