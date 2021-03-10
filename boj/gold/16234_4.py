from sys import stdin
from collections import deque
read = lambda: stdin.readline().strip()


def bfs(y, x, number):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append((y, x))
    locate = [(y, x)]
    population = maps[y][x]
    union[y][x] = number

    while q:
        now_y, now_x = q.popleft()

        for i in range(4):
            next_y, next_x = now_y + dy[i], now_x + dx[i]
            if 0 <= next_y < n and 0 <= next_x < n:

                # 두 나라의 인구 차이가 L명 이상, R명 이하라면
                # 연합국에 속해있지 않은 나라라면
                if l <= abs(maps[now_y][now_x] - maps[next_y][next_x]) <= r and union[next_y][next_x] == 0:
                    q.append((next_y, next_x))
                    union[next_y][next_x] = number
                    locate.append((next_y, next_x))
                    population += maps[next_y][next_x]

    move(locate, population)


def move(locate, population):
    for y, x in locate:
        maps[y][x] = population // len(locate)


if __name__ == "__main__":
    n, l, r = map(int, read().split())
    maps = []
    for _ in range(n):
        maps.append(list(map(int, read().split())))

    count = 0
    while True:
        # 연합 체크
        union = [[0 for _ in range(n)] for _ in range(n)]
        union_count = 1
        for i in range(n):
            for j in range(n):
                if union[i][j] == 0:
                    bfs(i, j, union_count)
                    union_count += 1

        # 연합 수 체크, union_count를 1부터 시작했기 때문에 n ** 2 + 1 이상이어야
        # 연합을 맺은 나라가 없다고 간주한다.
        if union_count >= n * n + 1:
            print(count)
            break

        count += 1