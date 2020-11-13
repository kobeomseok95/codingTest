### 자물쇠와 열쇠
def attach(board, key, x, y, m):
    for i in range(m):
        for j in range(m):
            board[x + i][y + j] += key[i][j]
    return board


def detach(board, key, x, y, m):
    for i in range(m):
        for j in range(m):
            board[x + i][y + j] -= key[i][j]
    return board


def chk(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[m + i][m + j] != 1:
                return False
    return True


def rotate_90(arr):
    return list(zip(*arr[::-1]))


def solution(key, lock):
    m, n = len(key), len(lock)
    board = [[0 for _ in range(2 * m + n)] for _ in range(2 * m + n)]
    for i in range(n):
        for j in range(n):
            board[m + i][m + j] = lock[i][j]

    rotated_key = key
    for _ in range(4):
        rotated_key = rotate_90(rotated_key)

        for x in range(1, m + n):
            for y in range(1, m + n):
                board = attach(board, rotated_key, x, y, m)

                if chk(board, m, n):
                    return True
                board = detach(board, rotated_key, x, y, m)
    return False