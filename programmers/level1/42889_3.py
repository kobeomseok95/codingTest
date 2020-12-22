def solution(n, stages):
    users_stages = [0 for _ in range(n + 1)]
    for i in range(len(stages)):
        if stages[i] > n:
            continue
        users_stages[stages[i]] += 1

    users = len(stages)
    result, answer = [], []
    for i in range(1, n + 1):
        if users <= 0:
            result.append((0, i))
        else:
            result.append((users_stages[i] / users, i))
            users -= users_stages[i]

    result.sort(key=lambda x : (-x[0], x[1]))
    for r in result:
        answer.append(r[1])
    return answer