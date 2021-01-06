import sys
from collections import deque
sys.setrecursionlimit(10**6)


def cycle(n, parents, visit, record_stack):  # 사이클 발생시 True 반환
    visit[n] = True

    record_stack[n] = True
    for child in parents[n]:
        if not visit[child]:
            if cycle(child, parents, visit, record_stack):
                return True
        elif record_stack[child]:
            return True
    record_stack[n] = False

    return False


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    parents = [[] for _ in range(n)]

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    q.append(0)
    visit = [False] * n
    visit[0] = True

    while q:
        node = q.popleft()

        for nxt in graph[node]:
            if not visit[nxt]:
                visit[nxt] = True
                parents[nxt].append(node)
                q.append(nxt)

    for parent, child in order:
        parents[child].append(parent)

    visit = [False] * n
    record_stack = [False] * n
    for i in range(n):
        if not visit[i]:
            if cycle(i, parents, visit, record_stack):
                return False
    return True