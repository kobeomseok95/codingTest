from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    p1_y, p1_x, p2_y, p2_x = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    if p1_y == p2_y:
        for i in [-1, 1]:
            if board[p1_y + i][p1_x] == 0 and board[p2_y + i][p2_x] == 0:
                next_pos.append({(p1_y, p1_x), (p1_y + i, p1_x)})
                next_pos.append({(p2_y, p2_x), (p2_y + i, p2_x)})

    if p1_x == p2_x:
        for i in [-1, 1]:
            if board[p1_y][p1_x + i] == 0 and board[p2_y][p2_x + i] == 0:
                next_pos.append({(p1_y, p1_x), (p1_y, p1_x + i)})
                next_pos.append({(p2_y, p2_x), (p2_y, p2_x + i)})

    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        next_p1_y, next_p1_x, next_p2_y, next_p2_x = p1_y + dy[i], p1_x + dx[i], p2_y + dy[i], p2_x + dx[i]
        if board[next_p1_y][next_p1_x] == 0 and board[next_p2_y][next_p2_x] == 0:
            next_pos.append({(next_p1_y, next_p1_x), (next_p2_y, next_p2_x)})

    return next_pos


def solution(board):
    n = len(board)
    new_board = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    pos = {(1, 1), (1, 2)}
    q = deque()
    q.append((pos, 0))
    visit = [pos]
    while q:
        now, count = q.popleft()
        if (n, n) in now:
            return count

        for next_pos in get_next_pos(now, new_board):
            if next_pos not in visit:
                q.append((next_pos, count + 1))
                visit.append(next_pos)
    return 0