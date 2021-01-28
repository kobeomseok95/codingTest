def get_new_lock(len_key, len_lock, lock):
    new_lock = [[0 for _ in range(2 * len_key + len_lock)] for _ in range(2 * len_key + len_lock)]
    for i in range(len_lock):
        for j in range(len_lock):
            new_lock[i + len_key][j + len_key] = lock[i][j]
    return new_lock


def insert_key(key, lock, y, x):
    for i in range(len(key)):
        for j in range(len(key)):
            lock[y + i][x + j] += key[i][j]


def delete_key(key, lock, y, x):
    for i in range(len(key)):
        for j in range(len(key)):
            lock[y + i][x + j] -= key[i][j]


def is_open(new_lock, len_key, len_lock):
    for i in range(len_key, len_key + len_lock):
        for j in range(len_key, len_key + len_lock):
            if new_lock[i][j] != 1:
                return False
    return True


def rotate_key(key):
    return list(zip(*key[::-1]))


def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    new_lock = get_new_lock(len_key, len_lock, lock)
    for i in range(len_lock + len_key):
        for j in range(len_lock + len_key):
            for k in range(4):
                insert_key(key, new_lock, i, j)
                if is_open(new_lock, len_key, len_lock):
                    return True
                delete_key(key, new_lock, i, j)
                key = rotate_key(key)
    return False