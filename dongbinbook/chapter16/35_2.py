# 오답코드 입니다.

from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
ugly = [1 for _ in range(n)]

idx2, idx3, idx5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5

for idx in range(1, n):
    ugly[idx] = min(next2, next3, next5)

    if ugly[idx] == next2:
        idx2 = idx
        next2 = ugly[idx2] + 2

    if ugly[idx] == next3:
        idx3 = idx
        next3 = ugly[idx3] + 3

    if ugly[idx] == next5:
        idx5 = idx
        next5 = ugly[idx5] + 5

print(ugly[n-1])


# n = int(read())
# ugly = set()
# ugly.add(1)
#
# num = 2
# while len(ugly) < n:
#     if num % 2 == 0:
#         ugly.add(num)
#
#     if num % 3 == 0:
#         ugly.add(num)
#
#     if num % 5 == 0:
#         ugly.add(num)
#     num += 1
#
# ans = list(ugly)
# ans.sort()
# print(ans[n-1])
