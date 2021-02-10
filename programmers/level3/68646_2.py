# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.28ms, 10.2MB)
# 테스트 4 〉	통과 (18.84ms, 15.2MB)
# 테스트 5 〉	통과 (99.68ms, 36.8MB)
# 테스트 6 〉	통과 (144.56ms, 47.8MB)
# 테스트 7 〉	통과 (198.04ms, 63.4MB)
# 테스트 8 〉	통과 (217.69ms, 60.1MB)
# 테스트 9 〉	통과 (193.04ms, 60.2MB)
# 테스트 10 〉	통과 (197.42ms, 60MB)
# 테스트 11 〉	통과 (405.29ms, 60.1MB)
# 테스트 12 〉	통과 (348.16ms, 60.1MB)
# 테스트 13 〉	통과 (299.91ms, 60.1MB)
# 테스트 14 〉	통과 (384.77ms, 60MB)
# 테스트 15 〉	통과 (403.34ms, 60MB)
import heapq


def solution(a):
    answer = 0
    heap = []

    idx = a.index(min(a))
    left = a[:idx]
    right = reversed(a[idx+1:])

    for l in left:
        heapq.heappush(heap, l)
        if heap[0] == l:
            answer += 1

    heap = []
    for r in right:
        heapq.heappush(heap, r)
        if heap[0] == r:
            answer += 1

    return answer + 1