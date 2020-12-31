from sys import stdin
read = lambda : stdin.readline().strip()

n, c = map(int, read().split())
house = [int(read()) for _ in range(n)]
house.sort()

start, end = 1, house[-1] - house[0]
answer = -1
while start <= end:
    mid = (start + end) // 2
    count = 1
    install = house[0]
    for i in range(1, n):
        if install + mid <= house[i]:
            count += 1
            install = house[i]
            if count == c:
                break

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)