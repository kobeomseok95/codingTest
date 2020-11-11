### 무지의 먹방 라이브
import heapq
def solution(food_times, k):
    food = [(time, idx) for idx, time in enumerate(food_times, 1)]
    heapq.heapify(food)

    smallest = food[0][0]
    prev = 0
    while k - ((smallest - prev) * len(food)) >= 0:
        k -= (smallest - prev) * len(food)
        prev, idx = heapq.heappop(food)

        if not food:
            return -1

        smallest = food[0][0]

    food = sorted(food, key=lambda x:x[1])
    return food[k % len(food)][1]