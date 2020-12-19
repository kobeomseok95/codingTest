from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            distance = weak[start] + friends[count - 1]

            for index in range(start, start + length):
                if distance < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    distance = weak[index] + friends[count - 1]
            answer = min(answer, count)

    return -1 if answer > len(dist) else answer