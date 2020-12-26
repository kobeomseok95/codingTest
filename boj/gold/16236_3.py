from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()


def find_fish():
    visit = [[False for _ in range(n)] for _ in range(n)]
    fishes = []
    q = deque()
    q.append((0, shark[0], shark[1]))
    visit[shark[0]][shark[1]] = True
    while q:
        dist, y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visit[ny][nx]:
                cost = dist + 1
                if maps[ny][nx] <= size:
                    visit[ny][nx] = True
                    q.append((cost, ny, nx))
                    if 0 < maps[ny][nx] <= size - 1:
                        fishes.append((cost, ny, nx))
    if not fishes:
        return None

    fishes.sort()
    return fishes[0]


n = int(read())
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
maps = []
shark, size = None, 2
for i in range(n):
    maps.append(list(map(int, read().split())))
    for j in range(n):
        if maps[i][j] == 9:
            shark = (i, j)

answer, count = 0, 0
while True:
    eat = find_fish()
    if eat == None:
        break

    distance, fy, fx = eat
    answer += distance
    maps[shark[0]][shark[1]] = 0
    maps[fy][fx] = 9
    shark = (fy, fx)
    count += 1

    if count == size:
        size += 1
        count = 0

print(answer)