from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1
    for idx in range(length):
        for friends in permutations(dist, len(dist)):
            count = 1
            start = weak[idx] + friends[count - 1]
            for w in range(idx, idx + length):
                if start < weak[w]:
                    count += 1
                    if count > len(dist):
                        break
                    start = weak[w] + friends[count - 1]
            answer = min(answer, count)

    return answer if answer <= len(dist) else -1























######################################################################################
# a = solution(12, [1,5,6,10], [1,2,3,4])
# print(a, a == 2)
# b = solution(12, [1,3,4,9,10], [3,5,7])
# print(b, b == 1)