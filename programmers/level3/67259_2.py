from collections import deque


def solution(board):
    answer = int(1e9)

    n = len(board)
    dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
    visit = {(0, 0, 0): 0, (0, 0, 1): 0, (0, 0, 2): 0, (0, 0, 3): 0}
    q = deque()
    q.append((0, 0, 0, -1))

    while q:
        y, x, cost, direction = q.popleft()

        if y == n - 1 and x == n - 1:
            answer = min(answer, cost)

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                nxt_cost = cost
                if direction == -1:
                    nxt_cost += 100
                elif (direction - d) % 2 == 0:
                    nxt_cost += 100
                else:
                    nxt_cost += 600

                if (ny, nx, d) not in visit:
                    visit[(ny, nx, d)] = nxt_cost
                    q.append((ny, nx, nxt_cost, d))
                else:
                    if visit[(ny, nx, d)] > nxt_cost:
                        visit[(ny, nx, d)] = nxt_cost
                        q.append((ny, nx, nxt_cost, d))

    return answer