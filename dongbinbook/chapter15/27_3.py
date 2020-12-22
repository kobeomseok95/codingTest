# bisect를 활용하면 더 빨리 구할 수 있다.
from sys import stdin
read = lambda : stdin.readline().strip()


def get_left(arr, x, idx):
    for i in range(idx, 0, -1):
        if arr[i - 1] != x:
            return i
    return 0


def get_right(arr, x, idx):
    for i in range(idx, len(arr) - 1):
        if arr[i + 1] != x:
            return i
    return len(arr)


def binary_search_left(x, arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        elif arr[mid] == x:
            left = get_left(arr, x, mid)
            right = get_right(arr, x, mid)
            return abs(left - right) + 1

    return -1


n, x = map(int, read().split())
arr = list(map(int, read().split()))

print(binary_search_left(x, arr))