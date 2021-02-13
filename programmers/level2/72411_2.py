from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for size in course:
        count = []
        for order in orders:
            count += combinations(sorted(order), size)
        most_count = Counter(count).most_common()
        answer += [k for k, v in most_count if v > 1 and v == most_count[0][1]]

    return sorted(''.join(k) for k in answer)