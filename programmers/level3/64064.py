from itertools import permutations


def is_match(user_set, banned_set):
    for i in range(len(user_set)):
        if len(user_set[i]) != len(banned_set[i]):
            return False
        for j in range(len(user_set[i])):
            if banned_set[i][j] == '*':
                continue
            if banned_set[i][j] != user_set[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    for com_set in permutations(user_id, len(banned_id)):
        if is_match(com_set, banned_id):
            com_set = set(com_set)
            if com_set not in answer:
                answer.append(com_set)

    return len(answer)