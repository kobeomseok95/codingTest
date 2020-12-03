from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answer, direction = 0, 0

n = int(read())
k = int(read())

board = [[0 for _ in range(n)] for _ in range(n)]
body = deque([(0, 0)])
for _ in range(k):
    y, x = map(int, read().split())
    board[y - 1][x - 1] = 2

l = int(read())
directions = deque()
for _ in range(l):
    x, c = map(str, read().split())
    directions.append((int(x), c))


y, x = 0, 0
while True:
    answer += 1
    y, x = y + dy[direction], x + dx[direction]
    if 0 <= y < n and 0 <= x < n:
        if (y, x) in body:
            break

        if board[y][x] == 2:
            board[y][x] = 0
            body.append((y, x))
        else :
            body.popleft()
            body.append((y, x))
    else:
        break

    if directions and directions[0][0] == answer:
        times, d = directions.popleft()
        if d == 'D':
            direction = (direction + 1) % 4
        elif d == 'L':
            direction = (direction - 1) % 4

print(answer)