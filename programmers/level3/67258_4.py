def solution(gems):
    # 보석 종류 파악하기
    kinds = set(gems)

    # 종류가 gems의 크기와 같거나 종류가 한 가지인 경우
    answer = [1, len(gems)]
    if len(kinds) == len(gems):
        return answer
    if len(kinds) == 1:
        return [1, 1]

    # 보석을 담을 dict
    bucket = dict()

    # while문을 사용하기 위해 start, end 지정
    start, end = 0, 0
    while True:
        if len(bucket) == len(kinds):
            if answer[1] - answer[0] + 1 > end - start:
                answer = [start + 1, end]

            if bucket[gems[start]] == 1:
                del bucket[gems[start]]
            else:
                bucket[gems[start]] -= 1
            start += 1
        else:
            if end >= len(gems):
                break
            if gems[end] not in bucket.keys():
                bucket[gems[end]] = 1
            else:
                bucket[gems[end]] += 1
            end += 1

    return answer
