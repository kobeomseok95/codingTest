from math import sqrt


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
        else:
            sqrt_no = int(sqrt(i))
            chk = False
            for j in range(2, sqrt_no + 1):
                quotient = i // j
                if quotient > 10 ** 7:
                    continue
                if i % j == 0:
                    chk = True
                    answer.append(i // j)
                    break
            if not chk:
                answer.append(1)

    return answer