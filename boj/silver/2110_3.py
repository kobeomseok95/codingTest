from sys import stdin
read = lambda : stdin.readline().strip()

n, c = map(int, read().split())
house = [int(read()) for _ in range(n)]
house.sort()

answer = 0
start, end = 1, house[-1] - house[0]
while start <= end:
    mid = (start + end) // 2
    router = house[0] + mid
    count = 1
    for h in house:
        if h >= router:
            count += 1
            router = h + mid

    if count < c:
        end = mid - 1
    elif count >= c:
        start = mid + 1
        answer = mid

print(answer)