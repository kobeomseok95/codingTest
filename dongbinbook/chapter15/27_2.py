from sys import stdin
from bisect import bisect_left, bisect_right
read = lambda : stdin.readline().strip()


def find_idx(arr, left_value, right_value):
    left_idx = bisect_left(arr, left_value)
    right_idx = bisect_right(arr, right_value)
    return right_idx - left_idx

n, x = map(int, read().split())
arr = list(map(int, read().split()))

count = find_idx(arr, x, x)
print("-1" if count == 0 else count)

# def find_first(arr, find_number, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] > find_number:
#             end = mid - 1
#         elif arr[mid] < find_number:
#             start = mid + 1
#         elif arr[mid] == find_number:
#             for i in range(mid - 1, -1, -1):
#                 if arr[i] != find_number:
#                     return i + 1
#
#     return None
#
#
# def find_last(arr, find_number, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] > find_number:
#             end = mid - 1
#         elif arr[mid] < find_number:
#             start = mid + 1
#         elif arr[mid] == find_number:
#             for i in range(mid + 1, len(arr)):
#                 if arr[i] != find_number:
#                     return i - 1
#
#     return None
#
#
# def count_by_value(arr, target):
#     length = len(arr)
#     a = find_first(arr, target, 0, length - 1)
#
#     if a == None:
#         return 0
#
#     b = find_last(arr, target, 0, length - 1)
#
#     return b - a + 1
#
#
# n, x = map(int, read().split())
# arr = list(map(int, read().split()))
#
# count = count_by_value(arr, x)
# if count == 0:
#     print("-1")
# else:
#     print(count)