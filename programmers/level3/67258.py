def solution(gems):
    size = len(set(gems))
    answer = [0, len(gems) - 1]
    maps = {gems[0]: 1}

    start, end = 0, 0
    while start < len(gems) and end < len(gems):
        if len(maps) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            if maps[gems[start]] == 1:
                del maps[gems[start]]
            else:
                maps[gems[start]] -= 1
            start += 1

        else:
            end += 1
            if end == len(gems):
                break

            if gems[end] in maps.keys():
                maps[gems[end]] += 1
            else:
                maps[gems[end]] = 1

    return [answer[0] + 1, answer[1] + 1]























########################################################################################
a = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
print(a == [3, 7], a)
b = solution(["AA", "AB", "AC", "AA", "AC"])
print(b == [1, 3], b)
c = solution(["XYZ", "XYZ", "XYZ"])
print(c == [1, 1], c)
d = solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
print(d == [1, 5], d)