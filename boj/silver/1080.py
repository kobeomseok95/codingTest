from sys import stdin
READ = lambda : stdin.readline().strip()

def check(a, b, n, m):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

def flip(a, i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            a[x][y] = int(not a[x][y])
    return a

def change(a, b, n, m):
    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if a[i][j] != b[i][j]:
                a = flip(a, i, j)
                count += 1
    if not check(a, b, n, m):
        return -1
    else:
        return count


if __name__ == "__main__":
    n, m = map(int, READ().split())
    a = [list(map(int, READ())) for _ in range(n)]
    b = [list(map(int, READ())) for _ in range(n)]
    print(change(a, b, n, m))