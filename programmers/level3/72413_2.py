### 플로이드 워셜
### 효율성 테스트
# 테스트 1 〉	통과 (137.44ms, 10.4MB)
# 테스트 2 〉	통과 (466.89ms, 11.1MB)
# 테스트 3 〉	통과 (1099.93ms, 11.4MB)
# 테스트 4 〉	통과 (1101.13ms, 11.5MB)
# 테스트 5 〉	통과 (1093.21ms, 11.5MB)
# 테스트 6 〉	통과 (1098.41ms, 11.5MB)
# 테스트 7 〉	통과 (1181.10ms, 13.9MB)
# 테스트 8 〉	통과 (1145.24ms, 14.2MB)
# 테스트 9 〉	통과 (1452.35ms, 13MB)
# 테스트 10 〉	통과 (1389.87ms, 13MB)
# 테스트 11 〉	통과 (1456.60ms, 12.9MB)
# 테스트 12 〉	통과 (1223.21ms, 12.8MB)
# 테스트 13 〉	통과 (1118.91ms, 12.9MB)
# 테스트 14 〉	통과 (1199.04ms, 12.9MB)
# 테스트 15 〉	통과 (1206.15ms, 12.6MB)
# 테스트 16 〉	통과 (1072.84ms, 11.4MB)
# 테스트 17 〉	통과 (1089.67ms, 11.5MB)
# 테스트 18 〉	통과 (1071.29ms, 11.2MB)
# 테스트 19 〉	통과 (1132.35ms, 11.6MB)
# 테스트 20 〉	통과 (1086.12ms, 11.8MB)
# 테스트 21 〉	통과 (1142.98ms, 11.7MB)
# 테스트 22 〉	통과 (1198.61ms, 12.8MB)
# 테스트 23 〉	통과 (1239.63ms, 12.8MB)
# 테스트 24 〉	통과 (1112.08ms, 12.8MB)
# 테스트 25 〉	통과 (1079.03ms, 11.1MB)
# 테스트 26 〉	통과 (1073.30ms, 10.9MB)
# 테스트 27 〉	통과 (1012.13ms, 10.5MB)
# 테스트 28 〉	통과 (1004.07ms, 10.3MB)
# 테스트 29 〉	통과 (136.11ms, 10.3MB)
# 테스트 30 〉	통과 (136.66ms, 10.4MB)
def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0

    for y, x, fare in fares:
        graph[y][x] = fare
        graph[x][y] = fare

    for k in range(1, n + 1):
        for y in range(1, n + 1):
            for x in range(1, n + 1):
                value = graph[y][k] + graph[k][x]
                if graph[y][x] > value:
                    graph[y][x] = value

    answer = graph[s][a] + graph[s][b]
    for i in range(1, n + 1):
        if i != s:
            value = graph[s][i] + graph[i][a] + graph[i][b]
            if answer > value:
                answer = value
    return answer