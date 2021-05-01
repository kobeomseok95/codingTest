# 테스트 1 〉	통과 (0.01ms, 10MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.08ms, 10.2MB)
# 테스트 4 〉	통과 (6.49ms, 14.3MB)
# 테스트 5 〉	통과 (35.90ms, 33.1MB)
# 테스트 6 〉	통과 (47.71ms, 44.7MB)
# 테스트 7 〉	통과 (70.19ms, 56.2MB)
# 테스트 8 〉	통과 (63.53ms, 56.1MB)
# 테스트 9 〉	통과 (64.11ms, 56.2MB)
# 테스트 10 〉	통과 (84.10ms, 56.1MB)
# 테스트 11 〉	통과 (83.56ms, 56.2MB)
# 테스트 12 〉	통과 (81.78ms, 56.1MB)
# 테스트 13 〉	통과 (79.62ms, 56.1MB)
# 테스트 14 〉	통과 (83.16ms, 56.3MB)
# 테스트 15 〉	통과 (85.00ms, 56.1MB)
def solution(a):
    answer = 0
    min_idx = a.idx(min(a))
    left = a[:min_idx]
    right = reversed(a[min_idx + 1:])

    left_min = 1000000001
    right_min = 1000000001
    for l in left:
        if left_min > l:
            left_min = l
            answer += 1

    for r in right:
        if right_min > r:
            right_min = r
            answer += 1

    return answer + 1