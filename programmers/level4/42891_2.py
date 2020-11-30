from heapq import heappush, heappop
def solution(food_times, k):
    ### 방송이 중단되기 전에 다 먹을 경우
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        ### (음식, 회전판 번호)
        heappush(q, (food_times[i], i + 1))

    length = len(q)
    sum_value = 0
    previous = 0

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]



    
    
    
    
    







# print(solution([3,1,2], 5))
# print(solution([1,1,2,7], 7))
print(solution([2,6,1,1,3], 7))
