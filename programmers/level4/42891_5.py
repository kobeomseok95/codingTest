from heapq import heappush, heappop


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    length = len(food_times)
    heap = []
    for i in range(length):
        heappush(heap, (food_times[i], i + 1))

    sum_foods = 0
    previous = 0
    while ((heap[0][0] - previous) * length) <= k:
        food = heappop(heap)[0]
        sum_foods += (food - previous) * length
        k -= (food - previous) * length
        previous = food
        length -= 1

    answer = sorted(heap, key=lambda x: x[1])
    return answer[k % length][1]



















#############################################################################
food_times1=[4,2,3,6,7,1,5,8]
k1 = 16
a = solution(food_times1, k1)
print( a == 3, a )
food_times2=[4,2,3,6,7,1,5,8]
k2 = 27
b = solution(food_times2, k2)
print( b == 5, b )