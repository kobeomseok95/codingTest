### 괄호 변환

def balanced_index(string):
    tmp = list(string)
    left, right = 0, 0
    for i in range(len(tmp)):
        if tmp[i] == '(':
            left += 1
        elif tmp[i] == ')':
            right += 1

        if left > 0 and right > 0 and left == right:
            return i
    return len(string)


def proper_string(string):
    tmp = list(string)
    left, right = 0, 0
    for i in range(len(tmp)):
        if tmp[i] == '(':
            left += 1
        elif tmp[i] == ')':
            right += 1

        if right > left:
            return False
    return True



def solution(p):
    answer = ''
    if p == '':
        return ''

    index = balanced_index(p)
    u = p[: index + 1]
    v = p[index + 1 :]
    if proper_string(u):
        answer += u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            elif u[i] == ')':
                u[i] = '('
        answer += ''.join(u)
    return answer















########################################################################################################################
a = solution("(()())()")
print(a)
print(a == "(()())()")

b = solution(")(")
print(b)
print(b == "()")

c = solution("()))((()")
print(c)
print(c == "()(())()")