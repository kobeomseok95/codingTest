from sys import stdin
read = lambda: stdin.readline().strip()


def clean(y, x, direction):
    answer = 1
    maps[y][x] = 2

    # 뒤가 벽인지 확인하기
    back_is_wall = False
    while not back_is_wall:
        # 청소했는지 확인
        is_clean = False
        # 왼쪽부터 방향 전환
        for i in range(4):
            # 시계 반대방향으로 회전
            direction = (direction - 1) % 4

            # 만약 돌린 방향이 청소하지 않은 곳이라면
            if maps[y + drc[direction][0]][x + drc[direction][1]] == 0:
                y, x = y + drc[direction][0], x + drc[direction][1]
                maps[y][x] = 2
                answer += 1
                is_clean = True
                break

        # 청소를 했으면 다시 while문 반복하게 continue 쳐주기
        if is_clean:
            continue

        # 후진했는데, 벽이라면 whlie문 끝내기
        if maps[y + drc[(direction - 2) % 4][0]][x + drc[(direction - 2) % 4][1]] == 1:
            back_is_wall = True
        # 후진했는데, 벽이 아닌 경우
        else:
            y = y + drc[(direction - 2) % 4][0]
            x = x + drc[(direction - 2) % 4][1]

    return answer


if __name__ == "__main__":
    drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n, m = map(int, read().split())
    r, c, d = map(int, read().split())

    maps = []
    for i in range(n):
        maps.append(list(map(int, read().split())))

    print(clean(r, c, d))