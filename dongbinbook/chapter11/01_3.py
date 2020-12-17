from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
data = list(map(int, read().split()))
data.sort()

team, count = 0, 0
for i in range(n):
    count += 1
    if count == data[i]:
        team += 1
        count = 0


print(team)