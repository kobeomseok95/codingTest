from sys import stdin
READ = lambda : stdin.readline().strip()

n = int(READ())
arr = list(map(int, READ().split()))

ans = -1
start, end = 0, n-1
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == mid:
       ans = mid
       break

    elif arr[mid] > mid:
        end = mid - 1

    elif arr[mid] < mid:
        start = mid + 1

print(ans)