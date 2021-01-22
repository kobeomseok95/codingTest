from collections import deque


def solution(n, path, order):
    wait, check = [False] * (n + 1), [0] * (n + 1)
    path_dict = dict()

    for x, y in path:
        if x in path_dict:
            path_dict[x].append(y)
        else:
            path_dict[x] = [y]
        if y in path_dict:
            path_dict[y].append(x)
        else:
            path_dict[y] = [x]

    before = {y: x for x, y in order}
    after = {x: y for x, y in order}

    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        if now in before and check[before[now]] == 0 and not wait[now]:
            wait[now] = True
            continue

        if now in after:
            if wait[after[now]]:
                q.append(after[now])

        for nx in path_dict[now]:
            if check[nx] == 0:
                q.append(nx)
        check[now] = 1

    return True if sum(check) == n else False