def possible(stones, k, mid):
    count = 0
    for stone in stones:
        # 음수인 경우는 건너지 못한 경우이므로 이 구간마다 count += 1 해주기
        if stone - mid < 0:
            count += 1
            # 연속된 음수가 k개인 경우 바로 False를 리턴한다.
            if count >= k:
                return False
        # 연속되지 않은 경우이므로 count = 0으로 초기화
        else:
            count = 0
    return True


def solution(stones, k):
    answer = 0
    # 초기값 설정
    start, end = 1, max(stones)
    while start <= end:
        mid = (start + end) // 2

        # 해당 인원이 징검다리를 건널 수 있는지 체크
        if possible(stones, k, mid):
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer