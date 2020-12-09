from sys import stdin
read = lambda : stdin.readline().strip()

test = int(read())
for _ in range(test):
    n, m = map(int, read().split())
    maps = [[0 for _ in range(m)] for _ in range(n)]

    data = list(map(int, read().split()))
    for i in range(n):
        for j in range(m):
            maps[i][j] = data[m * i + j]

    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = maps[i][0]

    for col in range(1, m):
        for row in range(n):
            if row == 0:
                dp[row][col] = maps[row][col] + max(dp[row][col - 1], dp[row + 1][col - 1])
            elif row == n-1:
                dp[row][col] = maps[row][col] + max(dp[row][col - 1], dp[row - 1][col - 1])
            else:
                dp[row][col] = maps[row][col] + max(dp[row + 1][col - 1], dp[row][col - 1], dp[row - 1][col - 1])
    answer = -1
    for i in range(n):
        answer = max(dp[i][m-1], answer)
    print(answer)