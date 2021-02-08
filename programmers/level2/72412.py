from bisect import bisect_left
from itertools import combinations


def solution(info, query):
    answer = []
    info_dict = {}

    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        for j in range(5):
            for combi in list(combinations(range(4), j)):
                copy_conditions = conditions.copy()
                for c in combi:
                    copy_conditions[c] = '-'
                changed = '/'.join(copy_conditions)
                if changed in info_dict:
                    info_dict[changed].append(score)
                else:
                    info_dict[changed] = [score]

    for value in info_dict.values():
        value.sort()

    for q in query:
        q_condition = [c for c in q.split() if c != "and"]
        q_score = int(q_condition[-1])
        q_condi = '/'.join(q_condition[:-1])

        if q_condi in info_dict:
            if len(info_dict[q_condi]) > 0:
                answer.append(len(info_dict[q_condi]) - bisect_left(info_dict[q_condi], q_score))
        else:
            answer.append(0)

    return answer