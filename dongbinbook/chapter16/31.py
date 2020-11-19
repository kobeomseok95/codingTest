from sys import stdin
READ = lambda : stdin.readline().strip()

test = int(READ())
for _ in range(test):
    m, n = map(int, READ().split())
    maps = [[0] * m for _ in range(n)]
    inputs = list(map(int, READ().split()))
    for i in range(m):
        for j in range(n):
            maps[j][i] = inputs[i * n + j]

    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = maps[i][j]
            else:
                if j == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1]) + maps[i][j]
                elif j == m - 1 :
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + maps[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + maps[i][j]

    print(max(dp[n - 1]))