from sys import stdin
read = lambda : stdin.readline().strip()


n = int(read())
arr = list(map(int, read().split()))
answer = -1

start, end = 0, n - 1
while start <= end:
    mid = (start + end) // 2

    if arr[mid] == mid:
        answer = mid
        break

    else:
        if mid < arr[mid]:
            end = mid - 1
        elif mid > arr[mid]:
            start = mid + 1

print(answer)