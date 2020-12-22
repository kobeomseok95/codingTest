from sys import stdin
from heapq import heappush, heappop
read = lambda : stdin.readline().strip()

n = int(read())
card = []
for i in range(n):
    heappush(card, int(read()))

answer = 0
while card:
    c1 = heappop(card)
    if not card:
        break

    c2 = heappop(card)
    answer += c1 + c2
    heappush(card, c1 + c2)

print(answer)