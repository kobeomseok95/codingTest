from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()

for _ in range(int(read())):
    n = int(read())
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    data = list(map(int, read().split()))
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    for _ in range(int(read())):
        a, b = map(int, read().split())
        # 순위가 a > b 일 경우
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        #순위가 a < b 일 경우
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)
        for i in range(1, n + 1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()