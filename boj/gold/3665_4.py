from sys import stdin
read = lambda : stdin.readline().strip()

for _ in range(int(read())):
    n = int(read())
    team = list(map(int, read().split()))

    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            graph[team[i]][team[j]] = True
            indegree[team[j]] += 1

    m = int(read())
    for _ in range(m):
        a, b = map(int, read().split())

        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q, answer = [], []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    cycle, certain = False, True
    for i in range(n):
        if len(q) == 0:
            certain = False
            break
        elif len(q) >= 2:
            cycle = True
            break

        now = q.pop()
        answer.append(now)
        for j in range(1, n + 1):
            if graph[now][j]:
                graph[now][j] = False
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("?")
    elif not certain:
        print("IMPOSSIBLE")
    else:
        for a in answer:
            print(a, end=' ')
        print()