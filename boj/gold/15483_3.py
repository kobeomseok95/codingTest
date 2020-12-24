from sys import stdin
read = lambda : stdin.readline().strip()

s1 = read()
s2 = read()
l1 = len(s1)
l2 = len(s2)

dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

for j in range(l2 + 1):
    dp[0][j] = j

for i in range(l1 + 1):
    dp[i][0] = i

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if s1[i - 1] != s2[j - 1]:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        else:
            dp[i][j] = dp[i-1][j-1]

print(dp[l1][l2])