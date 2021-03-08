import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = lambda: sys.stdin.readline().strip()


def throw(height, order):
    # 왼쪽에서 오른쪽
    if order % 2 == 0:
        j = 0
        while j < c and maps[r - height][j] == '.':
            j += 1
        if 0 <= j < c:
            maps[r - height][j] = '.'

    # 오른쪽에서 왼쪽
    else:
        j = c - 1
        while j >= 0 and maps[r - height][j] == '.':
            j -= 1
        if 0 <= j < c:
            maps[r - height][j] = '.'


def bfs(visit, y, x, count, clusters):
    drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque()
    q.append((y, x))
    visit[y][x] = True
    while q:
        now_y, now_x = q.popleft()

        # 군집 표시
        maps[now_y][now_x] = count

        # 해당 군집의 위치 넣어주기
        if count not in clusters:
            clusters[count] = []
        clusters[count].append([now_y, now_x])

        # 탐색하기
        for i in range(4):
            next_y, next_x = now_y + drc[i][0], now_x + drc[i][1]
            if 0 <= next_y < r and 0 <= next_x < c and not visit[next_y][next_x] and maps[next_y][next_x] != '.':
                visit[next_y][next_x] = True
                bfs(visit, next_y, next_x, count, clusters)


# 클러스터들을 내릴 수 있는지 체크하는 함수
def check_down_cluster(number, location):
    for y, x in location:
        if y + 1 >= r or (maps[y + 1][x] != '.' and maps[y + 1][x] != number):
            return False
    return True


def down_cluster(number):
    # 위치들을 .으로 고친 다음, y값을 + 1 해주기
    for i in range(len(clusters[number])):
        maps[clusters[number][i][0]][clusters[number][i][1]] = '.'
        clusters[number][i][0] += 1
    # y + 1 해준 값들을 맵에 군집표시 해주기
    for i in range(len(clusters[number])):
        maps[clusters[number][i][0]][clusters[number][i][1]] = number


if __name__ == "__main__":
    r, c = map(int, read().split())
    maps = []
    for i in range(r):
        maps.append(list(read()))
        for j in range(c):
            if maps[i][j] == 'x':
                maps[i][j] = 0

    n = int(read())
    height = list(map(int, read().split()))
    for i in range(n):
        # 막대 던지기
        throw(height[i], i)

        # 클러스터 체크
        clusters = {}
        visit = [[False for _ in range(c)] for _ in range(r)]
        count = 0
        for y in range(r):
            for x in range(c):
                if not visit[y][x] and maps[y][x] != '.':
                    bfs(visit, y, x, count, clusters)
                    count += 1

        # 클러스터 내려주기
        for key in clusters:
            for j in range(r):
                if check_down_cluster(key, clusters[key]):
                    down_cluster(key)
                else:
                    break

    for i in range(r):
        for j in range(c):
            print('x' if maps[i][j] != '.' else maps[i][j], end='')
        print()