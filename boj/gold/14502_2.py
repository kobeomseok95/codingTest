### 다시 풀어보기
from sys import stdin
from itertools import combinations
read = lambda : stdin.readline().strip()
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def spread_virus(y, x):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                spread_virus(ny, nx)

def check_save_zone():
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                count += 1
    return count


n, m = map(int, read().split())
maps, safety = [], []
answer = 0
tmp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    maps.append(list(map(int, read().split())))
    for j in range(m):
        if maps[i][j] == 0:
            safety.append((i, j))

# 안전지대중 3곳을 조합으로 뽑는다.
for save_zone in combinations(safety, 3):
    # tmp에 일단 다 넣어주고
    for i in range(n):
        for j in range(m):
            tmp[i][j] = maps[i][j]

    # save_zone을 벽으로 설정하기
    for y, x in save_zone:
        tmp[y][x] = 1

    # 바이러스 퍼트리기
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                spread_virus(i, j)

    safe = check_save_zone()
    answer = max(answer, safe)

print(answer)