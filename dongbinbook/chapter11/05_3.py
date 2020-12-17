from sys import stdin
read = lambda : stdin.readline().strip()

n, m = map(int, read().split())
data = list(map(int, read().split()))

balls = []
for i in range(n):
    balls.append((data[i], i + 1))

balls.sort()

result = set()
for i in range(n):
    weight, ball_no = balls[i][0], balls[i][1]
    for j in range(i + 1, n):
        if weight != balls[j][0]:
            result.add((ball_no, balls[j][1]))

print(len(result))