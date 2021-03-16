from sys import stdin
read = lambda: stdin.readline().strip()


def possible():
    for i in range(n):
        goal = i
        for j in range(h):
            if ladders[j][goal]:
                goal += 1
            elif 0 < goal and ladders[j][goal-1]:
                goal -= 1

        if i != goal:
            return False
    return True


def dfs(count, height_index, add_horizontal_count):
    if count == add_horizontal_count:
        if possible():
            print(add_horizontal_count)
            exit(0)
        return

    for y in range(height_index, h):
        for x in range(n - 1):
            # 현재 가로선이 놓인 경우
            if ladders[y][x]:
                continue
            # 왼쪽에 가로선이 존재하는 경우
            elif 0 < x and ladders[y][x - 1]:
                continue
            # 오른쪽에 가로선이 존재하는 경우
            elif x < n - 1 and ladders[y][x + 1]:
                continue

            ladders[y][x] = True
            dfs(count + 1, y, add_horizontal_count)
            ladders[y][x] = False


if __name__ == "__main__":
    n, m, h = map(int, read().split())

    # 사다리 및 가로선 표현
    ladders = [[False for _ in range(n)] for _ in range(h)]
    for _ in range(m):
        a, b = map(int, read().split())
        ladders[a-1][b-1] = True

    # 0 ~ 3까지 브루트포스 시작
    for add_horizontal_count in range(0,4):
        dfs(0, 0, add_horizontal_count)

    print(-1)