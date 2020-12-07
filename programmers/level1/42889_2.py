def solution(n, stages):
    answer = []
    user = len(stages)

    for i in range(1, n + 1):
        challenger = stages.count(i)

        if challenger == 0:
            fail = 0
        else:
            fail = challenger / user

        answer.append((i, fail))
        user -= challenger

    answer.sort(key=lambda x : x[1], reverse=True)
    answer = [answer[i][0] for i in range(n)]
    return answer



















################################################################################
a = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
print(a == [3,4,2,1,5])
print(a)

b = solution(4, [4,4,4,4,4])
print(b == [4,1,2,3])
print(b)