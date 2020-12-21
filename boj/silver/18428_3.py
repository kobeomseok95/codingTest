from sys import stdin
read = lambda : stdin.readline().strip()


def monitor(maps, teacher):
    for ty, tx in teacher:
        up_y, down_y, right_x, left_x = ty, ty, tx, tx
        while up_y >= 0:
            if maps[up_y][tx] == 'S':
                return True
            elif maps[up_y][tx] == 'O':
                break
            up_y -= 1

        while down_y < n:
            if maps[down_y][tx] == 'S':
                return True
            elif maps[down_y][tx] == 'O':
                break
            down_y += 1

        while right_x < n:
            if maps[ty][right_x] == 'S':
                return True
            elif maps[ty][right_x] == 'O':
                break
            right_x += 1

        while left_x >= 0:
            if maps[ty][left_x] == 'S':
                return True
            elif maps[ty][left_x] == 'O':
                break
            left_x -= 1

    return False


def dfs(count, maps):
    global result

    if count == 3:
        if not monitor(maps, teacher):  #학생들 모두 걸리지 않았다.
            result = True
            return

    elif count < 3 and not result:
        for i in range(n):
            for j in range(n):
                if maps[i][j] == 'X':
                    maps[i][j] = 'O'
                    dfs(count + 1, maps)
                    maps[i][j] = 'X'


n = int(read())
maps, teacher = [], []
for i in range(n):
    maps.append(list(map(str, read().split())))
    for j in range(n):
        if maps[i][j] == 'T':
            teacher.append((i, j))

result = False
dfs(0, maps)
print("NO" if not result else "YES")