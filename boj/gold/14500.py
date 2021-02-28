from sys import stdin
read = lambda: stdin.readline().strip()


def get_nemo_list(n, m):
    nemo_list = []
    for i in range(n - 1):
        for j in range(m - 1):
            nemo_list.append([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])
    return nemo_list


def get_ilja_list(n, m):
    ilja_list = []
    for i in range(n):
        for j in range(m - 3):
            ilja_list.append([(i, j), (i, j + 1), (i, j + 2), (i, j + 3)])

    for i in range(n - 3):
        for j in range(m):
            ilja_list.append([(i, j), (i + 1, j), (i + 2, j), (i + 3, j)])

    return ilja_list


def get_thunder_list(n, m):
    thunder_list = []
    for i in range(n - 2):
        for j in range(m - 1):
            thunder_list.append([(i, j), (i + 1, j), (i + 1, j + 1), (i + 2, j + 1)])

    for i in range(n - 1):
        for j in range(m - 2):
            thunder_list.append([(i + 1, j), (i + 1, j + 1), (i, j + 1), (i, j + 2)])

    return thunder_list


def get_nieun_list(n, m):
    nieun_list = []
    for i in range(n - 2):
        for j in range(m - 1):
            nieun_list.append([(i, j), (i + 1, j), (i + 2, j), (i + 2, j + 1)])
            nieun_list.append([(i, j), (i, j + 1), (i + 1, j + 1), (i + 2, j + 1)])

    for i in range(n - 1):
        for j in range(m - 2):
            nieun_list.append([(i, j), (i + 1, j), (i, j + 1), (i, j + 2)])
            nieun_list.append([(i + 1, j), (i + 1, j + 1), (i + 1, j + 2), (i, j + 2)])

    return nieun_list


def get_fuckyou_list(n, m):
    fuckyou_list = []
    for i in range(n - 2):
        for j in range(m - 1):
            fuckyou_list.append([(i, j), (i + 1, j), (i + 2, j), (i + 1, j + 1)])
            fuckyou_list.append([(i, j + 1), (i + 1, j), (i + 1, j + 1), (i + 2, j + 1)])

    for i in range(n - 1):
        for j in range(m - 2):
            fuckyou_list.append([(i, j + 1), (i + 1, j), (i + 1, j + 1), (i + 1, j + 2)])
            fuckyou_list.append([(i, j), (i, j + 1), (i, j + 2), (i + 1, j + 1)])

    return fuckyou_list


def get_score(scores, location):
    score = 0
    for y, x in location:
        score += scores[y][x]
    return score


def solve():
    n, m = map(int, read().split())
    scores = []
    for i in range(n):
        scores.append(list(map(int, read().split())))

    nemo_list = get_nemo_list(n, m)
    ilja_list = get_ilja_list(n, m)
    thunder_list = get_thunder_list(n, m)
    nieun_list = get_nieun_list(n, m)
    fuckyou_list = get_fuckyou_list(n, m)
    shape_list = [nemo_list, ilja_list, thunder_list, nieun_list, fuckyou_list]
    
    answer = 0
    for shape in shape_list:
        for location in shape:
            answer = max(answer, get_score(scores, location))
    print(answer)


if __name__ == "__main__":
    solve()