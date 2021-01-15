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






























######################################################################################
a = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
print(a == 3, a)