from sys import stdin
read = lambda: stdin.readline().strip()


def get_nemo_scores(n, m, scores):
    answer = 0
    for i in range(n - 1):
        for j in range(m - 1):
            answer = max(answer, scores[i][j] + scores[i][j + 1] + scores[i + 1][j] + scores[i + 1][j + 1])
    return answer


def get_ilja_scores(n, m, scores):
    answer = 0
    for i in range(n):
        for j in range(m - 3):
            answer = max(answer, scores[i][j] + scores[i][j + 1] + scores[i][j + 2] + scores[i][j + 3])

    for i in range(n - 3):
        for j in range(m):
            answer = max(answer, scores[i][j] + scores[i + 1][j] + scores[i + 2][j] + scores[i + 3][j])

    return answer


def get_thunder_scores(n, m, scores):
    answer = 0
    for i in range(n - 2):
        for j in range(m - 1):
            answer = max(answer, scores[i][j] + scores[i + 1][j] + scores[i + 1][j + 1] + scores[i + 2][j + 1])
            answer = max(answer, scores[i][j + 1] + scores[i + 1][j + 1] + scores[i + 1][j] + scores[i + 2][j])

    for i in range(n - 1):
        for j in range(m - 2):
            answer = max(answer, scores[i + 1][j] + scores[i + 1][j + 1] + scores[i][j + 1] + scores[i][j + 2])
            answer = max(answer, scores[i][j] + scores[i][j + 1] + scores[i + 1][j + 1] + scores[i + 1][j + 2])

    return answer


def get_nieun_scores(n, m, scores):
    answer = 0
    for i in range(n - 2):
        for j in range(m - 1):
            answer = max(answer, scores[i][j] + scores[i + 1][j] + scores[i + 2][j] + scores[i + 2][j + 1])
            answer = max(answer, scores[i][j] + scores[i][j + 1] + scores[i + 1][j + 1] + scores[i + 2][j + 1])
            answer = max(answer, scores[i + 2][j] + scores[i + 2][j + 1] + scores[i + 1][j + 1] + scores[i][j + 1])
            answer = max(answer, scores[i][j] + scores[i][j + 1] + scores[i + 1][j] + scores[i + 2][j])

    for i in range(n - 1):
        for j in range(m - 2):
            answer = max(answer, scores[i][j] + scores[i + 1][j] + scores[i + 1][j + 1] + scores[i + 1][j + 2])
            answer = max(answer, scores[i + 1][j] + scores[i + 1][j + 1] + scores[i + 1][j + 2] + scores[i][j + 2])
            answer = max(answer, scores[i][j] + scores[i][j + 1] + scores[i][j + 2] + scores[i + 1][j])
            answer = max(answer, scores[i][j] + scores[i][j + 1] + scores[i][j + 2] + scores[i + 1][j + 2])

    return answer


def get_fuckyou_scores(n, m, scores):
    answer = 0
    for i in range(n - 2):
        for j in range(m - 1):
            answer = max(answer, scores[i][j] + scores[i + 1][j] + scores[i + 2][j] + scores[i + 1][j + 1])
            answer = max(answer, scores[i][j + 1] + scores[i + 1][j] + scores[i + 1][j + 1] + scores[i + 2][j + 1])

    for i in range(n - 1):
        for j in range(m - 2):
            answer = max(answer, scores[i][j + 1] + scores[i + 1][j] + scores[i + 1][j + 1] + scores[i + 1][j + 2])
            answer = max(answer, scores[i][j] + scores[i][j + 1] + scores[i][j + 2] + scores[i + 1][j + 1])

    return answer


def solve():
    n, m = map(int, read().split())
    scores = []
    for i in range(n):
        scores.append(list(map(int, read().split())))
    answer = 0
    answer = max(answer, get_nemo_scores(n, m, scores))
    answer = max(answer, get_ilja_scores(n, m, scores))
    answer = max(answer, get_thunder_scores(n, m, scores))
    answer = max(answer, get_nieun_scores(n, m, scores))
    answer = max(answer, get_fuckyou_scores(n, m, scores))
    print(answer)


if __name__ == "__main__":
    solve()