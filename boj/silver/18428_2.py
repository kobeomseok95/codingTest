from sys import stdin
from itertools import combinations
read = lambda : stdin.readline().strip()


def find_student(y, x, direction):
    if direction == 0:      #상
        while 0 <= y < n and 0 <= x < n:
            if maps[y][x] == 'O':
                break
            elif maps[y][x] == 'X' or maps[y][x] == 'T':
                y -= 1
            elif maps[y][x] == 'S':
                return True

    if direction == 1:    #하
        while 0 <= y < n and 0 <= x < n:
            if maps[y][x] == 'O':
                break
            elif maps[y][x] == 'X' or maps[y][x] == 'T':
                y += 1
            elif maps[y][x] == 'S':
                return True

    if direction == 2:    #좌
        while 0 <= y < n and 0 <= x < n:
            if maps[y][x] == 'O':
                break
            elif maps[y][x] == 'X' or maps[y][x] == 'T':
                x -= 1
            elif maps[y][x] == 'S':
                return True

    if direction == 3:    #우
        while 0 <= y < n and 0 <= x < n:
            if maps[y][x] == 'O':
                break
            elif maps[y][x] == 'X' or maps[y][x] == 'T':
                x += 1
            elif maps[y][x] == 'S':
                return True

    return False


def process():
    for d in range(4):
        for ty, tx in teacher:
            if find_student(ty, tx, d):
                return False
    return True


n = int(read())
maps = []
teacher, obstacle = [], []
for i in range(n):
    maps.append(list(map(str, read().split())))
    for j in range(n):
        if maps[i][j] == 'X':
            obstacle.append((i, j))
        elif maps[i][j] == 'T':
            teacher.append((i, j))

avoid = False
for combi_obs in combinations(obstacle, 3):
    for obs_y, obs_x in combi_obs:
        maps[obs_y][obs_x] = 'O'

    if process():
        avoid = True
        break

    for obs_y, obs_x in combi_obs:
        maps[obs_y][obs_x] = 'X'

print("YES" if avoid else "NO")