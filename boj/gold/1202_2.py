from sys import stdin
from heapq import heappush, heappop
READ = lambda : stdin.readline().strip()

def solution(jewels: list, bags: list) -> int:
    price = 0
    hq_list = []

    for bag in bags:
        while jewels and bag >= jewels[-1][0]:
            heappush(hq_list, -jewels.pop()[1])

        if hq_list:
            price -= heappop(hq_list)
        elif not jewels:
            break
    return price


if __name__ == "__main__":
    n, k = map(int, READ().split())

    jewels = [list(map(int, READ().split())) for _ in range(n)]
    jewels.sort(key=lambda x: -x[0])

    bags = [int(READ()) for _ in range(k)]
    bags.sort()

    print(solution(jewels, bags))