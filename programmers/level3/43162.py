from collections import deque


def bfs(start, visit, computers):
    q = deque([start])
    while q:
        now = q.popleft()
        visit[now] = True
        for j in range(len(computers[now])):
            if computers[now][j] == 1 and not visit[j]:
                q.append(j)


def solution(n, computers):
    answer = 0
    visit = [False for _ in range(n)]
    for i in range(n):
        if not visit[i]:
            bfs(i, visit, computers)
            answer += 1
    return answer