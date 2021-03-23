from sys import stdin
from itertools import combinations
from copy import deepcopy
read = lambda: stdin.readline().strip()


# 궁수의 row보다 -1한 값부터 0까지 거꾸로 돌면서 궁수가 적을 죽일 수 있는지 체크한다.
def kill(copy_maps, archer_y, archer_x):
    for y in range(archer_y - 1, -1, -1):
        for x in range(m):
            # 궁수는 적 한명만 죽일 수 있으므로 죽인 다음 바로 True를 리턴한다.
            if copy_maps[y][x] == 1 and abs(archer_y - y) + abs(archer_x - x) <= d:
                kill_set.add((y, x))
                return


def delete_enemies(copy_maps, kill_set):
    for y, x in kill_set:
        copy_maps[y][x] = 0


if __name__ == "__main__":
    n, m, d = map(int, read().split())
    maps = [list(map(int, read().split())) for _ in range(n)]

    # 궁수가 위치할 자리를 조합으로 설정하고 위치마다
    # 적을 제거하는 최댓값 비교
    answer = 0
    for archer_positions in map(list, combinations([i for i in range(m)], 3)):
        count = 0
        copy_maps = deepcopy(maps)

        # 궁수들은 maps_row 보다 + 1에 위치해 있으므로
        # n부터 1까지 검사한다.
        for archer_y in range(n, 0, -1):
            # 같은 적이 여러 궁수에게 죽을 수 있다를 처리하기 위해
            # 죽은 적 열 위치를 담을 리스트 생성
            kill_set = set()
            for archer_x in archer_positions:
                kill(copy_maps, archer_y, archer_x)

            count += len(kill_set)
            delete_enemies(copy_maps, kill_set)

        answer = max(answer, count)
    print(answer)

"""
4 4 3
0 1 1 0
0 0 1 1
1 0 1 0
1 1 1 0 
8
2 7 2
0 0 1 0 1 0 1
1 0 1 0 1 0 0
5
"""