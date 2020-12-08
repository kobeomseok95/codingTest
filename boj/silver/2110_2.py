from sys import stdin
read = lambda : stdin.readline().strip()

n, c = map(int, read().split())
house = [int(read()) for _ in range(n)]
house.sort()

start, end = house[1] - house[0], house[-1] - house[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    t = house[0] + mid

    for h in house:
        if t <= h:
            t = h + mid
            count += 1
        if count == c:
            break

    if count < c:
        end = mid - 1

    elif count >= c:
        start = mid + 1
        answer = max(answer, mid)

print(answer)