from sys import stdin
from collections import deque
read = lambda: stdin.readline().strip()


def move(y, x, dy, dx):
    length = 0
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        length += 1

    return y, x, length


def bfs():
    q = deque()
    q.append((ry, rx, by, bx, 1))
    visit[ry][rx][by][bx] = True

    while q:
        now_ry, now_rx, now_by, now_bx, count = q.popleft()

        if count > 10:
            print(-1)
            return

        for i in range(4):
            next_ry, next_rx, len_r = move(now_ry, now_rx, direction[i][0], direction[i][1])
            next_by, next_bx, len_b = move(now_by, now_bx, direction[i][0], direction[i][1])
            if board[next_by][next_bx] != 'O':
                if board[next_ry][next_rx] == 'O':
                    print(count)
                    return
                if next_ry == next_by and next_rx == next_bx:
                    if len_r > len_b:
                        next_ry -= direction[i][0]
                        next_rx -= direction[i][1]
                    else:
                        next_by -= direction[i][0]
                        next_bx -= direction[i][1]
                if not visit[next_ry][next_rx][next_by][next_bx]:
                    visit[next_ry][next_rx][next_by][next_bx] = True
                    q.append((next_ry, next_rx, next_by, next_bx, count + 1))
    print(-1)


if __name__ == "__main__":
    n, m = map(int, read().split())
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visit = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    board = []
    ry, rx, by, bx = 0, 0, 0, 0
    for i in range(n):
        board.append(list(read()))
        for j in range(m):
            if board[i][j] == 'R':
                ry, rx = i, j
            if board[i][j] == 'B':
                by, bx = i, j
    bfs()