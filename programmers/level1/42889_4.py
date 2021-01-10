def solution(n, stages):
    people = len(stages)
    non_clear = [0 for _ in range(n + 1)]
    for i in range(people):
        if stages[i] <= n:
            non_clear[stages[i]] += 1

    result = []
    for i in range(1, n + 1):
        if people <= 0:
            result.append([i, 0])
        else:
            result.append([i, non_clear[i] / people])
        people -= non_clear[i]

    result = sorted(result, key=lambda x: (-x[1], x[0]))
    return [i[0] for i in result]