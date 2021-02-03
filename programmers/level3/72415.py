from collections import deque
from itertools import permutations


def ctrl(board, y0, x0, dir_y, dir_x):
    for i in range(1, 4):
        if 0 <= (y1 := y0 + dir_y * i) < 4 and 0 <= (x1 := x0 + dir_x * i) < 4:
            if board[y1][x1] != 0:
                return (y1, x1)
            l = i
    return (y0 + dir_y * l, x0 + dir_x * l)


def move(board, start, end):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    dist = [[6 for _ in range(4)] for _ in range(4)]
    q = deque([(start, 0)])
    while q:
        [y, x], d = q.popleft()
        # 큐에서 나온 좌표가 최소 거리인 상황에 이어서 최단 경로를 구해주어야 한다.
        # if절에서 최단 경로가 아니라면 거리를 구할 이유가 없다. 최단 경로가 아니기 때문이다.
        if dist[y][x] > d:
            dist[y][x] = d
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    q.append(((ny, nx), d + 1))
                    q.append((ctrl(board, y, x, dy[i], dx[i]), d + 1))

    return dist[end[0]][end[1]]


def solution(board, r, c):
    location = {k: [] for k in range(1, 7)}
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                location[board[i][j]].append((i, j))

    answer = int(1e9)
    for per in permutations(filter(lambda v: v, location.values())):
        dist = 0
        cursors = [(r, c)]
        stage = [[v for v in w] for w in board]
        for xy1, xy2 in per:
            # 해당 그림까지의 거리, 목적지
            vs = [(move(stage, cursor, xy1) + move(stage, xy1, xy2), xy2) for cursor in cursors] + \
                 [(move(stage, cursor, xy2) + move(stage, xy2, xy1), xy1) for cursor in cursors]

            # 이동처리
            stage[xy1[0]][xy1[1]] = stage[xy2[0]][xy2[1]] = 0
            dist += 2 + (mvn := min(vs)[0])

            # 커서가 될 수 있는 위치, 최소 거리여야 한다.
            cursors = [pos for d, pos in vs if d == mvn]
        answer = min(answer, dist)
    return answer



















if __name__ == "__main__":
    a = solution([[1,0,0,3],
                  [2,0,0,0],
                  [0,0,0,2],
                  [3,0,1,0]], 1, 0)
    print(a == 14, a)
    # a = solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1)
    # print(a == 16, a)