from heapq import heappush, heappop
from sys import stdin
READ = lambda : stdin.readline().strip()

n = int(READ())
heap = []
for i in range(n):
    heappush(heap, int(READ()))

answer = 0
while len(heap) > 1:
    x = heappop(heap)
    sum_value = x + heappop(heap)
    answer += sum_value
    heappush(heap, sum_value)
print(answer)