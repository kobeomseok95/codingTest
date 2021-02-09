# 내가 생각한 시간복잡도 : n + n + n * log(n)
# for로 [a[i], index] 재정의 : n
# sort : n * log(n)
# 2 ~ len(balloon) : n

# heapq를 이용해 풀어보기
def get_balloon_count(balloon):
    answer = 0
    first = min(balloon[0][1], balloon[1][1])
    second = max(balloon[0][1], balloon[1][1])
    for i in range(2, len(balloon)):
        current = balloon[i][1]
        if first < current < second:
            continue

        answer += 1
        first = min(first, current)
        second = max(second, current)

    return answer


def solution(a):
    if len(a) <= 2:
        return len(a)

    balloon = []
    for i in range(len(a)):
        balloon.append([a[i], i])
    balloon.sort(key=lambda x: x[0])
    answer = get_balloon_count(balloon)
    return answer + 2