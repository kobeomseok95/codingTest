from collections import deque


def solution(board):
    n = len(board)
    answer = int(1e9)

    dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
    q = deque()
    q.append((0, 0, -1, 0))
    visit = {(0, 0, 0): 0, (0, 0, 1): 0, (0, 0, 2): 0, (0, 0, 3): 0}

    while q:
        y, x, direction, cost = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                new_cost = cost

                if direction == - 1:
                    new_cost += 100
                elif (direction - i) % 2 == 0:
                    new_cost += 100
                elif (direction - i) % 2 != 0:
                    new_cost += 600

                if ny == n - 1 and nx == n - 1:
                    answer = min(answer, new_cost)

                if visit.get((ny, nx, i)) is None or visit.get((ny, nx, i)) > new_cost:
                    visit[(ny, nx, i)] = new_cost
                    q.append((ny, nx, i, new_cost))
    return answer





















########################################################################################
a = solution([[0,0,0],[0,0,0],[0,0,0]])
print(a, a == 900)
b = solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
print(b, b == 3800)
c = solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
print(c, c == 2100)
i = solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])
print(i, i == 3200)
