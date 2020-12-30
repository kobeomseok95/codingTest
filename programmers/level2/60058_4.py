def reverse_str(string):
    r = ''
    for i in range(len(string)):
        if string[i] == '(':
            r += ')'
        else:
            r += '('
    return r


def proper(string):
    left, right = 0, 0
    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        else:
            right += 1

        if left < right:
            return False

    return True


def divide(string):
    left, right = 0, 0
    u, v = '', ''
    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = string[:i + 1]
            v = string[i + 1:]
            break

    return u, v


def solution(p):
    if len(p) == 0 or p == '':
        return p

    u, v = divide(p)
    if proper(u):
        return u + solution(v)
    else:
        reverse = reverse_str(u[1:-1])
        return '(' + solution(v) + ')' + reverse























####################################################################################
a = solution("(()())()")
print(a, a == "(()())()")
b = solution(")(")
print(b, b == "()")
c = solution("()))((()")
print(c, c == "()(())()")
