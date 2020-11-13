from sys import stdin
from collections import deque
READ = lambda : stdin.readline().strip()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def change(d, c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


def start():
    direction = 1
    time = 1
    y, x = 0, 0
    visited = deque([[y, x]])
    arr[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if arr[y][x] != 1:
                tmp_y, tmp_x = visited.popleft()
                arr[tmp_y][tmp_x] = 0
            arr[y][x] = 2
            visited.append([y, x])

            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else:
            return time


if __name__ == "__main__":
    N = int(READ())
    K = int(READ())
    arr = [[0] * N for _ in range(N)]
    for _ in range(K):
        a, b = map(int, READ().split())
        arr[a - 1][b - 1] = 1    #apple
    L = int(READ())
    times = {}
    for i in range(L):
        X, C = READ().split()
        times[int(X)] = C
    print(start())

"""
35
28
21 2
22 23
3 5
34 30
29 31
3 28
20 12
27 26
31 7
5 10
21 10
19 2
15 23
4 23
3 19
3 35
13 30
30 30
23 27
32 17
22 24
8 27
4 8
30 18
15 28
22 29
28 5
16 33
20
27 D
61 L
68 L
100 L
133 L
160 L
165 D
168 D
170 D
182 D
206 D
207 D
214 D
215 D
216 L
237 D
240 D
241 L
251 D
252 D

답 : 237
"""











