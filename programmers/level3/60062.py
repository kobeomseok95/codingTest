### 외벽 점검

from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(n + weak[i])

    answer = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]

            for idx in range(start, start + length):
                if position < weak[idx]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[idx] + friends[count - 1]
            answer = min(answer, count)

    return -1 if answer > len(dist) else answer










########################################################################################################################
print("첫번째 예제 결과 :", 2 == solution(12, [1,5,6,10], [1,2,3,4]))
print("두번째 예제 결과 :", 1 == solution(12, [1,3,4,9,10], [3,5,7]))