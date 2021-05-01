from sys import stdin
read = lambda: stdin.readline().strip()


def move(color, pieces, pieces_map, n, k):
    change_dir = {0: 1, 1: 0, 2: 3, 3: 2}
    dy, dx = [0,0,-1,1], [1,-1,0,0]
    WHITE, RED, BLUE = 0, 1, 2

    for i in range(1, k + 1):
        change_flag = False
        y, x, d = pieces[i][0], pieces[i][1], pieces[i][2]
        ny, nx = y + dy[d], x + dx[d]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or color[ny][nx] == BLUE:
            d = change_dir[d]
            ny, nx = y + dy[d], x + dx[d]
            change_flag = True
            if ny < 0 or ny >= n or nx < 0 or nx >= n or color[ny][nx] == BLUE:
                pieces[i][2] = d
                continue

        if color[ny][nx] == WHITE:
            left = pieces_map[(y, x)][:pieces_map[(y, x)].idx(i)]
            right = pieces_map[(y, x)][pieces_map[(y, x)].idx(i):]
            pieces_map[(y, x)] = left
            pieces_map[(ny, nx)].extend(right)
            for r in right:
                pieces[r][0], pieces[r][1] = ny, nx
            if change_flag:
                pieces[i][2] = d

        elif color[ny][nx] == RED:
            left = pieces_map[(y, x)][:pieces_map[(y, x)].idx(i)]
            right = pieces_map[(y, x)][pieces_map[(y, x)].idx(i):]
            pieces_map[(y, x)] = left
            right.reverse()
            pieces_map[(ny, nx)].extend(right)
            for r in right:
                pieces[r][0], pieces[r][1] = ny, nx
            if change_flag:
                pieces[i][2] = d

        if len(pieces_map[(ny, nx)]) >= 4:
            return True

    return False


def main():
    n, k = map(int, read().split())
    color = []
    for i in range(n):
        color.append(list(map(int, read().split())))

    pieces_map = {(i, j): [] for i in range(n) for j in range(n)}
    pieces = dict()
    for i in range(1, k + 1):
        data = list(map(int, read().split()))
        pieces[i] = [data[0] - 1, data[1] - 1, data[2] - 1]
        pieces_map[(pieces[i][0], pieces[i][1])].append(i)

    count = 0
    while True:
        result = move(color, pieces, pieces_map, n, k)

        count += 1
        if count > 1000:
            print(-1)
            break

        if result:
            print(count)
            break


if __name__ == "__main__":
    main()