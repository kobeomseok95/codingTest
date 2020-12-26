from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()

for _ in range(int(read())):
    n = int(read())
    indegree = [0 for i in range(n + 1)]
    rank = list(map(int, read().split()))
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            indegree[rank[j]] += 1
            graph[rank[i]][rank[j]] = True

    m = int(read())
    for _ in range(m):
        a, b = map(int, read().split())
        if graph[a][b]:
            indegree[a] += 1
            indegree[b] -= 1
            graph[a][b] = False
            graph[b][a] = True
        else:
            indegree[a] -= 1
            indegree[b] += 1
            graph[a][b] = True
            graph[b][a] = False

    q = deque()
    answer = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    impossible, certain = False, True
    for i in range(n):
        if len(q) == 0:
            impossible = True
            break
        elif len(q) >= 2:
            certain = False
            break

        top = q.popleft()
        answer.append(top)
        for j in range(1, n + 1):
            if graph[top][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if impossible:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in range(len(answer)):
            print(answer[i], end=' ')
        print()














