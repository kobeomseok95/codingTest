from collections import deque


def get_next_points(board, point):
    n = len(board)
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    result = []
    point = list(point)
    p1y, p1x, p2y, p2x = point[0][0], point[0][1], point[1][0], point[1][1]

    # 상하좌우 이동의 경우
    for i in range(4):
        next_p1y, next_p1x, next_p2y, next_p2x = p1y + dy[i], p1x + dx[i], p2y + dy[i], p2x + dx[i]
        if 0 <= next_p1y < n and 0 <= next_p1x < n and 0 <= next_p2y < n and 0 <= next_p2x < n:
            if board[next_p1y][next_p1x] != 1 and board[next_p2y][next_p2x] != 1:
                next_point = {(next_p1y, next_p1x), (next_p2y, next_p2x)}
                result.append(next_point)
    # 가로에서 회전
    if p1y == p2y:
        for idx in [-1, 1]:
            if board[p1y + idx][p1x] == 0 and board[p2y + idx][p2x] == 0:
                result.append({(p1y, p1x), (p1y + idx, p1x)})
                result.append({(p2y, p2x), (p2y + idx, p2x)})
    # 세로에서 회전
    if p1x == p2x:
        for idx in [-1, 1]:
            if board[p1y][p1x + idx] == 0 and board[p2y][p2x + idx] == 0:
                result.append({(p1y, p1x), (p1y, p1x + idx)})
                result.append({(p2y, p2x), (p2y, p2x + idx)})

    return result


def solution(board):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    n = len(board)
    new_board = [[1 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    visit = []
    start = {(1,1), (1,2)}
    visit.append(start)
    count = 0
    q = deque()
    q.append((start, count))
    while q:
        point, count = q.popleft()
        if (n, n) in point:
            return count

        nexts = get_next_points(new_board, point)
        for nxt in nexts:
            if nxt not in visit:
                visit.append(nxt)
                q.append((nxt, count + 1))
























#####################################################################################
a = solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
print(a == 7, a)