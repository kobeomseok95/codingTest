from sys import stdin
from collections import deque
READ = lambda : stdin.readline().strip()

for _ in range(int(READ())):
    n = int(READ())
    indegree = [0] * (n + 1)
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    data = list(map(int, READ().split()))

    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(READ())
    for i in range(m):
        a, b = map(int, READ().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1

    result = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    cycle = False
    certain = True

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in range(n):
            print(result[i], end=' ')
        print()








"""
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
"""