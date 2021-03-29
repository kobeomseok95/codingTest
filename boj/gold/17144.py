from sys import stdin
read = lambda: stdin.readline().strip()


def get_cleaner_position():
    for i in range(r):
        if maps[i][0] == -1:
            return [i, 0], [i + 1, 0]


def spread():
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    tmp = [[0] * c for _ in range(r)]

    for y in range(r):
        for x in range(c):
            spread_value = 0
            if maps[y][x] >= 5:
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < r and 0 <= nx < c and not maps[ny][nx] == -1:
                        tmp[ny][nx] += maps[y][x] // 5
                        spread_value += maps[y][x] // 5
            tmp[y][x] += maps[y][x] - spread_value
    for y in range(r):
        for x in range(c):
            maps[y][x] = tmp[y][x]


def clean():
    # 위 청소
    ## 아래
    tmp1_1 = maps[top_cleaner[0]][c - 1]
    for i in range(c - 1, 1, -1):
        maps[top_cleaner[0]][i] = maps[top_cleaner[0]][i - 1]
    maps[top_cleaner[0]][1] = 0

    ## 오른쪽
    tmp1_2 = maps[0][c - 1]
    for i in range(top_cleaner[0] - 1):
        maps[i][c - 1] = maps[i + 1][c - 1]
    maps[top_cleaner[0] - 1][c - 1] = tmp1_1

    ## 위
    tmp1_3 = maps[0][0]
    for i in range(c - 2):
        maps[0][i] = maps[0][i + 1]
    maps[0][c - 2] = tmp1_2

    ## 왼쪽
    for i in range(top_cleaner[0] - 1, 1, -1):
        maps[i][0] = maps[i - 1][0]
    maps[1][0] = tmp1_3

    # 아래청소
    ## 위
    tmp2_1 = maps[bottom_cleaner[0]][c - 1]
    for i in range(c - 1, 1, -1):
        maps[bottom_cleaner[0]][i] = maps[bottom_cleaner[0]][i - 1]
    maps[bottom_cleaner[0]][1] = 0

    ## 오른쪽
    tmp2_2 = maps[r - 1][c - 1]
    for i in range(r - 1, bottom_cleaner[0] + 1, -1):
        maps[i][c - 1] = maps[i - 1][c - 1]
    maps[bottom_cleaner[0] + 1][c - 1] = tmp2_1

    ## 아래
    tmp2_3 = maps[r - 1][0]
    for i in range(c - 2):
        maps[r - 1][i] = maps[r - 1][i + 1]
    maps[r - 1][c - 2] = tmp2_2

    ## 왼쪽
    for i in range(bottom_cleaner[0] + 1, r - 1):
        maps[i][0] = maps[i + 1][0]
    maps[r - 2][0] = tmp2_3


if __name__ == "__main__":
    r, c, t = map(int, read().split())
    maps = [list(map(int, read().split())) for _ in range(r)]

    top_cleaner, bottom_cleaner = get_cleaner_position()

    for _ in range(t):
        spread()
        clean()

    total = 0
    for i in range(r):
        for j in range(c):
            if maps[i][j] > 0:
                total += maps[i][j]
    print(total)