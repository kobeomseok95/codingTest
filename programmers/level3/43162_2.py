def dfs(start, visit, computers):
    visit[start] = True
    for j in range(len(computers[start])):
        if computers[start][j] == 1 and not visit[j]:
            dfs(j, visit, computers)


def solution(n, computers):
    answer = 0
    visit = [False for _ in range(n)]
    for i in range(n):
        if not visit[i]:
            dfs(i, visit, computers)
            answer += 1
    return answer