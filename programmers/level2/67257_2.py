def get_result(n, priority, expression):
    if n == 2:
        return str(eval(expression))

    if priority[n] == '*':
        result = eval('*'.join([get_result(n + 1, priority, e) for e in expression.split('*')]))
    if priority[n] == '+':
        result = eval('+'.join([get_result(n + 1, priority, e) for e in expression.split('+')]))
    if priority[n] == '-':
        result = eval('-'.join([get_result(n + 1, priority, e) for e in expression.split('-')]))

    return str(result)


def solution(expression):
    answer = 0
    priorities = [
        ('*', '+', '-'),
        ('*', '-', '+'),
        ('+', '-', '*'),
        ('+', '*', '-'),
        ('-', '+', '*'),
        ('-', '*', '+')
    ]

    for priority in priorities:
        result = get_result(0, priority, expression)
        answer = max(answer, abs(int(result)))
    return answer