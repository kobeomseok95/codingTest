def solution(s):
    length = len(s)
    compression = length // 2
    answer = length

    for c in range(1, compression + 1):
        count = 1
        compression_str = ""
        tmp = ""

        for idx in range(c, length, c):
            front = s[idx - c: idx]
            back = s[idx: idx + c]
            if front == back:
                count += 1

            else:
                if count != 1:
                    compression_str += str(count)
                    count = 1
                compression_str += front

            tmp = back

        if count != 1:
            compression_str += str(count)
        compression_str += tmp

        answer = min(answer, len(compression_str))

    return answer