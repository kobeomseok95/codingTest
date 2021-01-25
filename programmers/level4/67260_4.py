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
        # before[now] = now를 방문하기 전에 방문해야할 방
        # wait[now] = now가 먼저 방문해야 하는 방을 위해 대기중인지 체크
        # now를 대기중인 상태로 놓고 큐를 돌린다.
        if now in before and check[before[now]] == 0 and not wait[now]:
            wait[now] = True
            continue
        # now가 먼저 방문해야하는 방인지 체크한다
        # after[now] = now를 방문한 후 다음방
        # after[now]가 대기중이라면 큐에 먼저 넣어주기
        if now in after and wait[after[now]]:
            q.append(after[now])

        for nx in path_dict[now]:
            if check[nx] == 0:
                q.append(nx)
        check[now] = 1

    return True if sum(check) == n else False