from sys import stdin
from itertools import combinations
from copy import deepcopy
read = lambda: stdin.readline().strip()


def get_distance(arc_pos, maps, d):
    possible_shot = []
    for arc in arc_pos:
        possible = []
        for y in range(len(maps)):
            for x in range(len(maps[0])):
                if abs(arc[0] - y) + abs(arc[1] - x) <= d:
                    possible.append((abs(arc[0] - y) + abs(arc[1] - x), y, x))
        possible_shot.append(possible)
    return possible_shot


def get_nearest(arc_shot_position, enemy_position):
    arc_shot_position.sort(key=lambda x: (x[0], x[2]))
    for dist, y, x in arc_shot_position:
        if (y, x) in enemy_position:
            return y, x
    return None


def go_forward(enemy_position):
    return set((y + 1, x) for y, x in enemy_position if y + 1 < n)


if __name__ == "__main__":
    n, m, d = map(int, read().split())

    enemy_position = set()
    for i in range(n):
        arr = list(map(int, read().split()))
        for j in range(m):
            if arr[j] == 1:
                enemy_position.add((i, j))

    answer = 0
    maps = [[0 for _ in range(m)] for _ in range(n)]
    archer_combi = combinations([(n, i) for i in range(m)], 3)
    # 궁수들이 자리잡은 위치별로 쓰러트릴 수 있는 최대 적 수 계산하기
    for archer_positions in archer_combi:
        count = 0
        # 각 궁수들이 쏠 수 있는 위치들
        copy_enemy = deepcopy(enemy_position)
        possible_shot_list = get_distance(archer_positions, maps, d)
        while enemy_position:
            # 죽은 적들 위치
            tmp = set()
            for arc_shot_position in possible_shot_list:
                # 궁수가 죽일 수 있는 적들 중, 가깝고 왼쪽에 위치한 적 위치 반환
                shot_pos = get_nearest(arc_shot_position, enemy_position)
                if shot_pos is not None:
                    tmp.add(shot_pos)

            # count 추가, 죽은 적 지워주기, 한칸 이동
            count += len(tmp)
            enemy_position -= tmp
            enemy_position = go_forward(enemy_position)

        # 계산 이후 적들의 위치 초기화
        enemy_position = copy_enemy
        answer = max(answer, count)
    print(answer)