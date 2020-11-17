### 실패율
def solution(n, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, n + 1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x:result[x], reverse=True)