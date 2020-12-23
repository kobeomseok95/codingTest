from sys import stdin
read = lambda : stdin.readline().strip()

for _ in range(int(read())):
    n, m = map(int, read().split())
    maps = []
    data = list(map(int, read().split()))
    for i in range(n):
        maps.append(data[m * i: m * i + m])

    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = maps[i][0]

    for j in range(1, m):
        for i in range(1, n):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + maps[i][j]
            elif i == n - 1:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + maps[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + maps[i][j]

    answer = -1
    for i in range(n):
        answer = max(answer, dp[i][m - 1])
    print(answer)
