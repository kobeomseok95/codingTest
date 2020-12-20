def divide(p):
    u, v = "", ""
    for i in range(len(p)):
        u += p[i]
        if u.count('(') == u.count(')'):
            v += p[i + 1:]
            break
    return u, v


def proper(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        elif p[i] == ')':
            right += 1

        if left < right:
            return False
    return True


def reverse_string(str):
    string = ""
    for i in range(len(str)):
        if str[i] == '(':
            string += ')'
        elif str[i] == ')':
            string += '('
    return string


def solution(p):
    if p == '':
        return p

    u, v = divide(p)
    if not proper(u):
        return "(" + solution(v) + ")" + reverse_string(u[1:-1])
    else:
        return u + solution(v)



















######################################################################
a = solution("(()())()")
print(a, a == "(()())()")
b = solution(")(")
print(b, b == "()")
c = solution("()))((()")
print(c, c == "()(())()")