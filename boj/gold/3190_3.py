from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 0
rotate_list = deque()
snake_body = deque()

n = int(read())
maps = [[0 for _ in range(n)] for _ in range(n)]
snake_body.append((0, 0))

k = int(read())
for i in range(k):
    y, x = map(int, read().split())
    maps[y-1][x-1] = 2

l = int(read())
for i in range(l):
    second, rotate = map(str, read().split())
    rotate_list.append((int(second), rotate))

answer = 0
while True:
    answer += 1
    head_y, head_x = snake_body[-1][0], snake_body[-1][1]
    ny, nx = head_y + dy[direction], head_x + dx[direction]
    if 0 <= ny < n and 0 <= nx < n:
        if maps[ny][nx] == 0:
            if (ny, nx) in snake_body:
                break
            snake_body.popleft()
        elif maps[ny][nx] == 2:
            maps[ny][nx] = 0
        snake_body.append((ny, nx))

    else:   # 벽을 부딪힐 경우
        break

    if len(rotate_list) > 0 and rotate_list[0][0] == answer:
        d = rotate_list.popleft()[1]
        if d == 'D':
            direction = (direction + 1) % 4
        elif d == 'L':
            direction = (direction - 1) % 4

print(answer)




"""
8
5
6 1
7 3
3 5
5 7
5 6
12
2 D
8 D
10 D
12 D
18 L
20 L
22 L
24 L
25 L
28 L
32 D
33 L
"""