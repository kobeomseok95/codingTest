def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    check = []

    for i in range(len(routes)):
        exit = routes[i][1]
        if exit in check:
            continue
        for j in range(i, len(routes)):
            if routes[j][0] <= exit <= routes[j][1]:
                check.append(routes[j][1])
        answer += 1

        if len(check) == len(routes):
            break

    return answer


def main():
    a = solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])
    print(a, a == 2)


if __name__ == "__main__":
    main()