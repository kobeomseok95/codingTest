from sys import stdin
read = lambda : stdin.readline().strip()

n, m = map(int, read().split())
ball = list(map(int, read().split()))
ball.sort()

answer = 0
for i in range(n):
    for j in range(i + 1, n):
        if ball[i] != ball[j]:
            answer += 1
print(answer)