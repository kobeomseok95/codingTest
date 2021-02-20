def solution(n, number):
    if n == number:
        return 1

    case_list = [0, {n}]
    for i in range(2, 9):
        case_set = {int(str(n) * i)}
        for half in range(1, i // 2 + 1):
            for a in case_list[half]:
                for b in case_list[i - half]:
                    case_set.add(a + b)
                    case_set.add(a - b)
                    case_set.add(b - a)
                    case_set.add(a * b)
                    if b != 0:
                        case_set.add(a // b)
                    if a != 0:
                        case_set.add(b // a)
        if number in case_set:
            return i
        case_list.append(case_set)
    return -1

#######
a = solution(5, 12)
# a = solution(2, 11)
