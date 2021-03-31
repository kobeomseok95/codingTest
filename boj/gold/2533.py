import sys
sys.setrecursionlimit(10**6)
read = lambda: sys.stdin.readline().strip()


def dfs(cur):
    visit[cur] = True
    for child in edge[cur]:
        if not visit[child]:
            dfs(child)
            # 얼리어답터가 아닌 경우, 자식들이 얼리어답터여야한다.
            dp[cur][0] += dp[child][1]
            # 얼리어답터인 경우, 최솟값만 만족하면 된다.
            dp[cur][1] += min(dp[child])


if __name__ == "__main__":
    n = int(read())
    visit = [False] * (n + 1)
    edge = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, read().split())
        edge[a].append(b)
        edge[b].append(a)
    dp = [[0, 1] for _ in range(n + 1)]
    dfs(1)
    print(min(dp[1]))