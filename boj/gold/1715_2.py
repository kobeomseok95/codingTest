from sys import stdin
from heapq import heappush, heappop
read = lambda : stdin.readline().strip()

heap = []
answer = 0
for i in range(int(read())):
    heappush(heap, int(read()))

while True:
    p1 = heappop(heap)

    if not heap:
        break

    p2 = heappop(heap)
    x = p1 + p2
    answer += x
    heappush(heap, x)

print(answer)