from heapq import heappush, heappop


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heappush(q, (food_times[i], i + 1))

    times, previous, length = 0, 0, len(q)
    while times + ((q[0][0] - previous) * length) <= k :
        now = heappop(q)[0]
        times += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x:x[1])
    return result[(k - times) % length][1]