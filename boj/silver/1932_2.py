from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, read().split())))

dp = [[0 for j in range(i + 1)] for i in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    length = len(triangle[i])
    for j in range(length):
        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == length - 1:
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[n-1]))