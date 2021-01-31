### 다익스트라
### 효율성 테스트
# 테스트 1 〉	통과 (56.36ms, 10.3MB)
# 테스트 2 〉	통과 (283.77ms, 10.7MB)
# 테스트 3 〉	통과 (107.28ms, 10.2MB)
# 테스트 4 〉	통과 (107.79ms, 10.3MB)
# 테스트 5 〉	통과 (105.55ms, 10.3MB)
# 테스트 6 〉	통과 (109.58ms, 10.3MB)
# 테스트 7 〉	통과 (3610.94ms, 16.2MB)
# 테스트 8 〉	통과 (3512.71ms, 16.1MB)
# 테스트 9 〉	통과 (3123.69ms, 16.1MB)
# 테스트 10 〉	통과 (2990.56ms, 16.1MB)
# 테스트 11 〉	통과 (3411.43ms, 16MB)
# 테스트 12 〉	통과 (1687.74ms, 13.1MB)
# 테스트 13 〉	통과 (1669.31ms, 13.3MB)
# 테스트 14 〉	통과 (1654.34ms, 13.3MB)
# 테스트 15 〉	통과 (1660.87ms, 13.2MB)
# 테스트 16 〉	통과 (95.17ms, 10.3MB)
# 테스트 17 〉	통과 (95.71ms, 10.1MB)
# 테스트 18 〉	통과 (92.19ms, 10.3MB)
# 테스트 19 〉	통과 (242.06ms, 10.6MB)
# 테스트 20 〉	통과 (392.48ms, 10.7MB)
# 테스트 21 〉	통과 (392.59ms, 10.7MB)
# 테스트 22 〉	통과 (1909.67ms, 13.3MB)
# 테스트 23 〉	통과 (1661.88ms, 13.3MB)
# 테스트 24 〉	통과 (1647.83ms, 13.2MB)
# 테스트 25 〉	통과 (65.52ms, 10.3MB)
# 테스트 26 〉	통과 (64.55ms, 10.3MB)
# 테스트 27 〉	통과 (348.24ms, 10.8MB)
# 테스트 28 〉	통과 (355.42ms, 10.8MB)
# 테스트 29 〉	통과 (35.25ms, 10.3MB)
# 테스트 30 〉	통과 (35.67ms, 10.3MB)
from heapq import heappush, heappop


def dijkstra(graph, start, destination):
    INF = int(1e9)
    distance = [INF for _ in range(len(graph))]
    distance[start] = 0
    heap = [[0, start]]
    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue

        for cost, next_point in graph[now]:
            next_dist = cost + dist
            if distance[next_point] > next_dist:
                distance[next_point] = next_dist
                heappush(heap, [next_dist, next_point])

    return distance[destination]


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for p1, p2, fare in fares:
        graph[p1].append([fare, p2])
        graph[p2].append([fare, p1])

    # 우선 각자 갈 경우
    answer = dijkstra(graph, s, a) + dijkstra(graph, s, b)

    # start를 제외하고 한 point까지 무지와 어피치가 같이가는 경우
    for i in range(1, n + 1):
        if i != s:
            answer = min(answer, dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i, b))

    return answer