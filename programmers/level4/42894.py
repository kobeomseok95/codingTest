def solution(board):
    answer = 0
    remove_count = -1
    while remove_count != 0:
        remove_count = get_remove_count(board)
        answer += remove_count

    return answer


def get_remove_count(board):
    n = len(board)
    count = 0
    for i in range(n):
        for j in range(n):
            if remove_possible(n, board, i, j, 2, 3):
                remove_block(board, i, j, 2, 3)
                count += 1

            if remove_possible(n, board, i, j, 3, 2):
                remove_block(board, i, j, 3, 2)
                count += 1

    return count


def remove_possible(n, board, y, x, height, weight):
    if y + height > n or x + weight > n:
        return False

    block_count = 0
    before_number = -1

    for i in range(y, y + height):
        for j in range(x, x + weight):
            if empty(board, i, j):
                if not empty_top(board, i, j):
                    return False

                block_count += 1
                if block_count > 2:
                    return False

            else:
                if check_other_block(board, i, j, before_number):
                    return False
                before_number = board[i][j]

    return True


def check_other_block(board, y, x, before_number):
    return True if before_number != -1 and board[y][x] != before_number else False


def empty_top(board, y, x):
    for i in range(y):
        if board[i][x] != 0:
            return False
    return True


def remove_block(board, y, x, height, weight):
    for i in range(y, y + height):
        for j in range(x, x + weight):
            board[i][j] = 0


def empty(board, i, j):
    return True if board[i][j] == 0 else False