def solution(board):
    answer = 0
    count = -1
    n = len(board)
    while count != 0:
        count = get_count(n, board)
        answer += count
    return answer


def get_count(n, board):
    count = 0
    for i in range(n):
        for j in range(n):
            if remove_check(n, board, i, j, 2, 3):
                remove_block(board, i, j, 2, 3)
                count += 1
            if remove_check(n, board, i, j, 3, 2):
                remove_block(board, i, j, 3, 2)
                count += 1

    return count


def remove_check(n, board, y, x, height, weight):
    if y + height > n or x + weight > n:
        return False

    black = 0
    before_block = -1
    for i in range(y, y + height):
        for j in range(x, x + weight):
            if board[i][j] == 0:
                if not top_check(i, j, board):
                    return False
                black += 1
                if black > 2:
                    return False
            else:
                if other_block_check(before_block, board[i][j]):
                    return False
                before_block = board[i][j]

    return True


def top_check(y, x, board):
    for i in range(y):
        if board[i][x] != 0:
            return False
    return True


def other_block_check(before_block, block):
    return False if before_block == -1 or before_block == block else True


def remove_block(board, y, x, weight, height):
    for i in range(y, y + weight):
        for j in range(x, x + height):
            board[i][j] = 0