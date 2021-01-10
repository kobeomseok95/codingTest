from itertools import combinations


def solution(relation):
    n = len(relation)

    uniqueness = []
    # 유일성 체크
    for i in range(len(relation[0])):
        for unique in combinations([x for x in range(len(relation[0]))], i + 1):
            row = [tuple(r[u] for u in unique) for r in relation]
            row = set(row)
            if len(row) == n:
                uniqueness.append(unique)

    # 최소성 체크
    minimality = set(uniqueness)
    for i in range(len(uniqueness)):
        for j in range(i + 1, len(uniqueness)):
            if set(uniqueness[i]).intersection(set(uniqueness[j])) == set(uniqueness[i]):
                minimality.discard(uniqueness[j])

    return len(minimality)
























##################################################################################
a = solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
print(a == 2, a)