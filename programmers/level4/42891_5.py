from heapq import heappush, heappop


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = []
    length = len(food_times)
    for i in range(length):
        heappush(heap, [food_times[i], i + 1])

    # 이전에 먹은 음식양, 먹은 음식 총량
    previous = 0
    sumv = 0
    while (heap[0][0] - previous) * length <= k:
        food = heappop(heap)[0]
        sumv += (food - previous) * length
        k -= (food - previous) * length
        previous = food
        length -= 1

    answer = sorted(heap, key=lambda x: x[1])
    return answer[k % length][1]