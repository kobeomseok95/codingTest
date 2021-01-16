def possible(stones, mid, k):
    count = 0
    for stone in stones:
        if stone - mid < 0:
            count += 1
            if count >= k:
                return False
        else:
            count = 0
    return True


def solution(stones, k):
    answer = 0
    start, end = 1, max(stones)
    while start <= end:
        mid = (start + end) // 2
        if possible(stones, mid, k):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer