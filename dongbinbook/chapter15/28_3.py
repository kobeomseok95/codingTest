from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
arr = list(map(int, read().split()))

answer = -1
start, end = 0, len(arr) - 1
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == mid:
        answer = mid
        break
    elif arr[mid] < mid:
        start = mid + 1
    elif arr[mid] > mid:
        end = mid - 1

print(-1 if answer == -1 else answer)