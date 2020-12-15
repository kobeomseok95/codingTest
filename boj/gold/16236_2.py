from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n = int(read())
shark_direction = 0
maps = []
for i in range(n):
    maps.append(list(map(int, read().split())))
    for j in range(n):
        if maps[i][j] == 9:
            shark_direction = (i, j)


def find_fish(shark_direction):
    visit = [[False for _ in range(n)] for _ in range(n)]
    possible_fishes = []
    count = 0
    shark_y, shark_x = shark_direction[0], shark_direction[1]
    q = deque()
    q.append((count, shark_y, shark_x))
    visit[shark_y][shark_x] = True

    while q:
        c, y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visit[ny][nx]:
                if 0 < maps[ny][nx] < shark_size:
                    q.append((c + 1, ny, nx))
                    possible_fishes.append((c + 1, ny, nx))
                if maps[ny][nx] == shark_size or maps[ny][nx] == 0:
                    q.append((c + 1, ny, nx))

                visit[ny][nx] = True

    if not possible_fishes:
        return None
    possible_fishes = sorted(possible_fishes, key=lambda x:(x[0], x[1], x[2]))
    return possible_fishes[0][0], possible_fishes[0][1], possible_fishes[0][2]


shark_size = 2
ate_fish, move_count = 0, 0
while True:
    fish = find_fish(shark_direction)
    if fish is None:
        print(move_count)
        break

    move_count += fish[0]
    maps[shark_direction[0]][shark_direction[1]] = 0
    shark_direction = (fish[1], fish[2])
    maps[shark_direction[0]][shark_direction[1]] = 9
    ate_fish += 1

    if ate_fish >= shark_size:
        shark_size += 1
        ate_fish = 0