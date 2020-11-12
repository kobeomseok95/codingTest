from sys import stdin
from heapq import heappush, heappop
READ = lambda : stdin.readline().strip()

n, k = map(int, READ().split())
diamonds, bags = [], []
for _ in range(n):
    ins = list(map(int, READ().split()))
    diamonds.append(ins)
for _ in range(k):
    bags.append(int(READ()))

diamonds.sort()
bags.sort()

ans, chk, max_heap = 0, 0, []
for i in range(k):
    while chk < n and bags[i] >= diamonds[chk][0]:
        heappush(max_heap, -diamonds[chk][1])
        chk += 1

    if max_heap:
        ans += abs(heappop(max_heap))

print(ans)
# chk < n의 이유 : 가방의 담을수 있는 무게가 낮아 다이아몬드를 담을 수 없는 상황을 고려하여 chk 인자를 주었다.
# 가방을 담을수있는 무게순으로 정렬했기 때문에 정렬순으로 선형 탐색할 경우
# 무게를 담을 수 없다면 아예 다이아몬드를 가져올 수 없기때문이다.