def solution(money):
    n = len(money)
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0], dp[0][1] = money[0], money[0]    # 첫번째를 먹은 경우
    dp[1][1] = money[1]                         # 두번째를 먹은 경우
    for i in range(2, n):
        # 마지막에 인덱스가 짝수(집의 갯수가 홀수)일 경우 첫번째를 먹었다면
        # 먹지 말아야 한다.
        if i == n - 1:
            dp[0][i] = dp[0][i-1]
            dp[1][i] = max(dp[1][i-2] + money[i], dp[1][i-1])
        else:
            dp[0][i] = max(dp[0][i-2] + money[i], dp[0][i-1])
            dp[1][i] = max(dp[1][i-2] + money[i], dp[1][i-1])

    return max(dp[0][n-1], dp[1][n-1])