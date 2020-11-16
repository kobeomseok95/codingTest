from itertools import combinations
from sys import stdin
READ = lambda : stdin.readline().strip()

def monitor(x, y, direction):
    if direction == 0:
        while x < n:
            if maps[x][y] == 'S':
                return True
            if maps[x][y] == 'O':
                return False
            x += 1

    if direction == 1:
        while x >= 0:
            if maps[x][y] == 'S':
                return True
            if maps[x][y] == 'O':
                return False
            x -= 1

    if direction == 2:
        while y < n:
            if maps[x][y] == 'S':
                return True
            if maps[x][y] == 'O':
                return False
            y += 1

    if direction == 3:
        while y >= 0:
            if maps[x][y] == 'S':
                return True
            if maps[x][y] == 'O':
                return False
            y -= 1
    return False


def process():  #False = 선생님께 안잡힌 경우, True = 선생님께 잡힌 경우
    for x, y in teachers:
        for i in range(4):
            if monitor(x, y, i):
                return True
    return False


n = int(READ())
teachers, empty, maps = [], [], []
for i in range(n):
    maps.append(list(READ().split(' ')))
    for j in range(n):
        if maps[i][j] == 'T':
            teachers.append((i, j))
        if maps[i][j] == 'X':
            empty.append((i, j))

find = False
for data in combinations(empty, 3):
    for x, y in data:
        maps[x][y] = 'O'
    if not process():
        find = True
        break
    for x, y in data:
        maps[x][y] = 'X'

print("NO" if not find else "YES")