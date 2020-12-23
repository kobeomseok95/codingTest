from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, read().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

print(max(dp[n - 1]))