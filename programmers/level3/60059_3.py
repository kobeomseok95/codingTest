def make_new_lock(lock, m):
    n = len(lock)
    arr = [[0 for _ in range(2 * m + n)] for _ in range(2 * m + n)]

    for i in range(n):
        for j in range(n):
            arr[i + m][j + m] = lock[i][j]

    return arr


def rotate_key(key):
    return list(zip(*key[::-1]))


def try_unlock(key, new_lock, i, j):
    m = len(key)
    for y in range(m):
        for x in range(m):
            new_lock[i + y][j + x] += key[y][x]
    return new_lock


def fail(key, new_lock, i, j):
    m = len(key)
    for y in range(m):
        for x in range(m):
            new_lock[i + y][j + x] -= key[y][x]
    return new_lock


def check_unlock(new_lock, m, n):
    for i in range(n):
        for j in range(n):
            if new_lock[i + m][j + m] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = make_new_lock(lock, m)

    for i in range(1, len(new_lock) - m):
        for j in range(1, len(new_lock) - m):
            for _ in range(4):
                key = rotate_key(key)
                new_lock = try_unlock(key, new_lock, i, j)

                if check_unlock(new_lock, m, n):
                    return True

                new_lock = fail(key, new_lock, i, j)

    return False



























######################################################################
a = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	)
print(a)