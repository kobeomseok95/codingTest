from itertools import combinations


def solution(orders, course):
    answer = []

    for count in course:
        menu_dict = {}
        for order in orders:
            for com in list(combinations(order, count)):
                com = list(com)
                com.sort()
                menu = ''.join(com)
                if menu not in menu_dict:
                    menu_dict[menu] = 0
                menu_dict[menu] += 1

        if not menu_dict:
            continue

        menu = sorted(menu_dict.items(), key=lambda x: x[1], reverse=True)
        max_val = menu[0][1]
        if max_val <= 1:
            continue
        for m in menu:
            if m[1] == max_val:
                answer.append(m[0])
            else:
                break

    return sorted(answer)