from itertools import permutations


def is_match(per, banned_id):
    for i in range(len(banned_id)):
        if len(per[i]) != len(banned_id[i]):
            return False
        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != per[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    for per in permutations(user_id, len(banned_id)):
        if is_match(per, banned_id):
            per = set(per)
            if per not in answer:
                answer.append(per)
    return len(answer)



























#######################################################################################
if __name__ == "__main__":
    # a = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
    # print(a)
    # a = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
    # print(a)
    a = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
    print(a)