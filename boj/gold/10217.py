from sys import stdin
READ = lambda : stdin.readline().strip()
INF = int(1e9)

test = int(READ())
for _ in range(test):
    n, m, k = map(int, READ().split())
    airport = [[] for _ in range(n + 1)]

    for _ in range(k):
        u, v, c, d = map(int, READ().split())
        airport[u].append((v, c, d))

    #행 : 도착지, 열 : 비용, dp[행][열] : 거리
    dp = [[INF for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][0] = 0

    for c in range(m + 1):
        for d in range(1, n + 1):
            if dp[d][c] == INF :
                continue
            t = dp[d][c]
            for nv, nc, nd in airport[d]:
                if nc + c > m :
                    continue
                dp[nv][nc + c] = min(dp[nv][nc + c], t + nd)
    answer = min(dp[n])
    print(answer if answer < INF else "Poor KCM")