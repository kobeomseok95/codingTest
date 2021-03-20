def possible_two(string):
    char = ["~", "!", "@", "#", "$", "%", "^", "&", "*"]
    for s in string:
        if s.isalpha():
            continue
        elif s.isdigit():
            continue
        elif s in char:
            continue
        else:
            return False
    return True


def possible_three(string):
    condition = [False, False, False, False]
    char = ["~", "!", "@", "#", "$", "%", "^", "&", "*"]

    for s in string:
        if s.isdigit():
            condition[0] = True
        if s.isupper():
            condition[1] = True
        if s.islower():
            condition[2] = True
        if s in char:
            condition[3] = True

    return True if condition.count(True) >= 3 else False


def possible_four(string):
    prev = ''
    count = 0
    for s in string:
        if prev != s:
            prev = s
            count = 1
        else:
            count += 1

        if count >= 4:
            return False
    return True


def possible_five(string):
    same_char = {}
    for s in string:
        if s not in same_char.keys():
            same_char[s] = 0
        same_char[s] += 1

        if same_char[s] >= 5:
            return False
    return True


def solution(inp_str):
    answer = []

    if not 8 <= len(inp_str) <= 15:
        answer.append(1)

    if not possible_two(inp_str):
        answer.append(2)

    if not possible_three(inp_str):
        answer.append(3)

    if not possible_four(inp_str):
        answer.append(4)

    if not possible_five(inp_str):
        answer.append(5)

    return answer if answer else [0]


if __name__ == "__main__":
    a = solution("AaTa+!12-3")
    print(a == [2], a)

    a = solution("aaaaZZZZ)")
    print(a == [2, 3, 4], a)

    a = solution("CaCbCgCdC888834A")
    print(a == [1, 4, 5], a)

    a = solution("UUUUU")
    print(a == [1, 3, 4, 5], a)

    a = solution("ZzZz9Z824")
    print(a == [0], a)