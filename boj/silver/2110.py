from sys import stdin
READ = lambda : stdin.readline().strip()

n, c = map(int, READ().split())
house = []
for _ in range(n):
    house.append(int(READ()))

house.sort()
result = 0
start, end = house[1] - house[0], house[-1] - house[0]
while start <= end:
    mid = (start + end) // 2
    tmp = house[0]
    count = 1
    for i in range(1, n):
        if house[i] - tmp >= mid:
            tmp = house[i]
            count += 1
    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)