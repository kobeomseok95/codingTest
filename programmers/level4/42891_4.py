from heapq import heappush, heappop


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    length = len(food_times)
    heap = []
    for i in range(length):
        heappush(heap, [food_times[i], i + 1])

    sum_value, previous = 0, 0
    while sum_value + ((heap[0][0] - previous) * length) <= k:
        now = heappop(heap)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(heap, key=lambda x : x[1])
    return result[(k - sum_value) % length][1]























################################################################################
a = solution([3,1,2], 5)
print(a, a == 1)
b = solution([4,2,3,6,7,1,5,8], 27)
print(b, b == 5)