from collections import deque


def solution(n, path, order):
    adj = {i: [] for i in range(n)}
    for s, e in path:
        adj[s].append(e)
        adj[e].append(s)

    precedeA = {}   # 선행 조건 A -> B
    precedeB = {}   # 선행 조건의 확인

    for a, b in order:
        precedeA[a] = b
        precedeB[b] = a
        if b == 0:
            return False
        if a == 0:
            precedeA[0] = 0

    visit = [0] * n
    visit[0] = 1

    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        if now == precedeA.get(precedeB.get(now)):
            visit[now] = 2
        else:
            for nxt in adj[now]:
                if visit[nxt] == 0:
                    q.append(nxt)
                    visit[nxt] = 1

                    if precedeA.get(nxt):
                        if visit[precedeA[nxt]] == 2:
                            q.append(precedeA[nxt])
                            visit[precedeA[nxt]] = 1
                        precedeA[nxt] = 0

    for i in visit:
        if i == 0:
            return False
    return True