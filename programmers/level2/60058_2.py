def change_bracket(string):
    return_string = ''
    for i in range(len(string)):
        if string[i] == '(':
            return_string += ')'
        else:
            return_string += '('
    return return_string


def proper(string):
    for i in range(len(string)):
        tmp = string[:i + 1]
        if tmp.count('(') < tmp.count(')'):
            return False
    return True


def find_idx(string):
    for idx in range(len(string)):
        tmp = string[:idx + 1]

        if tmp.count('(') == tmp.count(')'):
            return idx + 1


def solution(p):
    answer = ''
    if p == '' or proper(p):
        return p

    divide_idx = find_idx(p)
    u, v = p[: divide_idx], p[divide_idx:]

    # u가 올바르다면
    if proper(u):
        answer = u + solution(v) # 해당 문자열이 올바르게
    # u가 올바르지 않다면
    else:
        tmp_v = '(' + solution(v) + ')'
        tmp_u = change_bracket(u[1:-1])
        return tmp_v + tmp_u

    return answer

























##############################################################################
a = solution("(()())()")
print(a)
print(a == "(()())()")
b = solution(")(")
print(b)
print(b == "()")
c = solution("()))((()")
print(c)
print(c == "()(())()")