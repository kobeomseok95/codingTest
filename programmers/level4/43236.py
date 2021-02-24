def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2

        tmp, count = 0, 0
        for i in range(len(rocks)):
            if rocks[i] - tmp >= mid:
                tmp = rocks[i]
            else:
                count += 1
                if count > n:
                    break

        if count > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer