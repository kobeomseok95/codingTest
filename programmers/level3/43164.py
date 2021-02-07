from collections import defaultdict


def solution(tickets):
    answer = []
    route = defaultdict(list)

    # 딕셔너리로 해당 루트들 표현
    for a, b in tickets:
        route[a].append(b)

    for key in route.keys():
        route[key].sort(reverse=True)


    stack = ["ICN"]
    while stack:
        top = stack[-1]
        # 해당 지점에 티켓이 없는 경우
        if len(route[top]) == 0 or top not in route:
            answer.append(stack.pop())
        # 티켓이 있는 경우
        else:
            stack.append(route[top].pop())

    return answer[::-1]