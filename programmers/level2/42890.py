from itertools import combinations


def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    canditate = []
    for i in range(1, n_col + 1):
        canditate.extend(combinations(range(n_col), i))

    uniqueness = []
    for c in canditate:
        tmp = [tuple(row[x] for x in c) for row in relation]
        if len(set(tmp)) == n_row:
            uniqueness.append(c)

    minimality = set(uniqueness)

    for i in range(len(uniqueness)):
        for j in range(i + 1, len(uniqueness)):
            if len(uniqueness[i]) == len(set(uniqueness[i]).intersection(set(uniqueness[j]))):
                minimality.discard(uniqueness[j])

    return len(minimality)