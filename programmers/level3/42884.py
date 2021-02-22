def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    answer = 0
    camera = -30001

    for start, end in routes:
        if camera < start:
            answer += 1
            camera = end

    return answer