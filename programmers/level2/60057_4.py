def solution(s):
    length = len(s)
    answer = length

    for i in range(1, (length // 2) + 1):
        count = 1
        string = ""
        tmp = ""
        for j in range(i, length, i):
            front = s[j - i: j]
            back = s[j: j + i]
            if front == back:
                count += 1
            else:
                if count != 1:
                    string += str(count) + front
                else:
                    string += front
                count = 1
            tmp = back

        if count > 1:
            string += str(count) + tmp
        elif count == 1:
            string += tmp
        answer = min(answer, len(string))
    return answer