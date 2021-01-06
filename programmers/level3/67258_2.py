def solution(gems):
    size = len(set(gems))
    start, end = 0, 0
    gems_dict = {gems[0]: 1}
    answer = [0, len(gems) - 1]

    while start < len(gems) and end < len(gems):
        if len(gems_dict) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            if gems_dict[gems[start]] == 1:
                del gems_dict[gems[start]]
            else:
                gems_dict[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break

            if gems[end] in gems_dict.keys():
                gems_dict[gems[end]] += 1
            else:
                gems_dict[gems[end]] = 1

    return [answer[0] + 1, answer[1] + 1]