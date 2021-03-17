from sys import stdin
read = lambda : stdin.readline().strip()

if __name__ == "__main__":
    one = read()
    two = read()
    m = len(one)
    n = len(two)

    maps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 서로 공통의 부분 문자열이 증가하기 때문에
            # [i - 1][j - 1] 에서 + 1 해줌
            if one[j - 1] == two[i - 1]:
                maps[i][j] = maps[i - 1][j - 1] + 1
            # 서로 공통의 부분 문자열이 증가하지 않기 때문에
            # [i-1][j]와 [i][j-1] 중 최댓값을 그대로 가져간다.
            else:
                maps[i][j] = max(maps[i-1][j], maps[i][j-1])

    print(maps[n][m])