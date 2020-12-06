"""
노력의 흔적이라 남겨둠
from collections import deque

def solution(board):
    n = len(board)
    dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
    q = deque()
    q.append([0, (0, 0), (0, 1)])

    while q:
        # 0:움직인횟수, 1:첫번째 로봇 몸 좌표, 2:두번째 로봇 몸 좌표
        robot = q.popleft()
        if (n - 1, n - 1) in robot:
            return robot[0]

        # 로봇 본체를 상하좌우 이동시키는 경우
        for i in range(4):
            next_robots = [(robot[1][0] + dy[i], robot[1][1] + dx[i]), (robot[2][0] + dy[i], robot[2][1] + dx[i])]

            if 0 <= next_robots[0][0] < n and 0 <= next_robots[0][1] < n \
                    and 0 <= next_robots[1][0] < n and 0 <= next_robots[1][1] < n:
                if board[next_robots[0][0]][next_robots[0][1]] == 0 \
                        and board[next_robots[1][0]][next_robots[1][0]] == 0:
                    q.append([robot[0] + 1, (next_robots[0][0], next_robots[0][1]), (next_robots[1][0], next_robots[1][1])])

        # 로봇을 회전시키는 경우, 세로와 가로의 경우를 다 파악해야 한다.
        # 가로일 경우
        if robot[1][0] == robot[2][0] and robot[1][1] != robot[2][1]:
            # 왼쪽을 중심으로 위로 회전할 경우
            if 0 <= robot[2][0] - 1 < n and 0 <= robot[2][1] < n and board[robot[2][0] - 1][robot[2][1]] == 0:
                q.append([robot[0] + 1, (robot[1][0], robot[1][1]), (robot[2][0] - 1, robot[2][1] - 1)])

            # 아래로 회전할 경우
            if 0 <= robot[2][0] + 1 < n and 0 <= robot[2][1] < n and board[robot[2][0] + 1][robot[2][1]] == 0:
                q.append([robot[0] + 1, (robot[1][0], robot[1][1]), (robot[2][0] + 1, robot[2][1] - 1)])

            # 오른쪽을 중심으로 위로 회전할 경우
            if 0 <= robot[1][0] - 1 < n and 0 <= robot[1][1] < n and board[robot[1][0] - 1][robot[1][1]] == 0:
                q.append([robot[0] + 1, (robot[1][0] - 1, robot[1][1] + 1), (robot[2][0], robot[2][1])])

            # 아래로 회전할 경우
            if 0 <= robot[1][0] + 1 < n and 0 <= robot[1][1] < n and board[robot[1][0] + 1][robot[1][1]] == 0:
                q.append([robot[0] + 1, (robot[1][0] + 1, robot[1][1] + 1), (robot[2][0], robot[2][1])])

        # 세로일 경우
        if robot[1][0] != robot[2][0] and robot[1][1] == robot[2][1]:
            # 위를 중심으로 좌로 회전할 경우
            if 0 <= robot[2][0] < n and 0 <= robot[2][1] - 1 < n and board[robot[2][0]][robot[2][1] - 1] == 0:
                q.append([robot[0] + 1, (robot[1][0], robot[1][1]), (robot[2][0] - 1, robot[2][1] - 1)])

            # 위를 중심으로 좌로 회전할 경우
            if 0 <= robot[2][0] < n and 0 <= robot[2][1] + 1 < n and board[robot[2][0]][robot[2][1] + 1] == 0:
                q.append([robot[0] + 1, (robot[1][0], robot[1][1]), (robot[2][0] - 1, robot[2][1] + 1)])

            # 아래를 중심으로 좌로 회전할 경우
            if 0 <= robot[1][0] < n and 0 <= robot[1][1] - 1 < n and board[robot[1][0]][robot[1][1] - 1] == 0:
                q.append([robot[0] + 1, (robot[1][0] + 1, robot[1][1] - 1), (robot[2][0], robot[2][1])])

            # 아래를 중심으로 우로 회전할 경우
            if 0 <= robot[1][0] < n and 0 <= robot[1][1] + 1 < n and board[robot[1][0]][robot[1][1] + 1] == 0:
                q.append([robot[0] + 1, (robot[1][0] + 1, robot[1][1] + 1), (robot[2][0], robot[2][1])])
"""
from collections import deque


def get_next_pos(pos, board):
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 상하좌우의 경우
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y \
            = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 회전의 경우
    if pos1_x == pos2_x:    # 가로로 놓인 경우
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    elif pos1_y == pos2_y:  # 세로로 놓인 경우
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost

        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0