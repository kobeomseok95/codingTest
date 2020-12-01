def rotate_key(key):
    list_of_tuples = zip(*key[::-1])
    return [list(elem) for elem in list_of_tuples]


def insert_key(y, x, key, expand, length_key):
    for i in range(0, length_key):
        for j in range(0, length_key):
            expand[i + y][j + x] += key[i][j]

    return expand


def take_out_key(y, x, key, expand, length_key):
    for i in range(0, length_key):
        for j in range(0, length_key):
            expand[i + y][j + x] -= key[i][j]

    return expand


def solve(expand, length_key, length_lock):
    for i in range(length_key, length_key + length_lock):
        for j in range(length_key, length_key + length_lock):
            if expand[i][j] == 2 or expand[i][j] == 0:
                return False
    return True


def solution(key, lock):
    length_key = len(key)
    length_lock = len(lock)
    expand_size = 2 * length_key + length_lock
    expand = [[0 for _ in range(expand_size)] for _ in range(expand_size)]
    for i in range(length_lock):
        for j in range(length_lock):
            expand[i + length_key][j + length_key] = lock[i][j]

    for i in range(1, length_key + length_lock):
        for j in range(1, length_key + length_lock):
            for rotate in range(4):
                key = rotate_key(key)
                expand = insert_key(i, j, key, expand, length_key)

                if solve(expand, length_key, length_lock):
                    return True

                expand = take_out_key(i, j, key, expand, length_key)
    return False