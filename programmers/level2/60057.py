### 문자열 압축

def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1
        tmp_str = s[: cut]
        for i in range(cut, len(s), cut):
            if tmp_str == s[i: i + cut]:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tmp_str
                tmp_str = s[i: i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tmp_str
        length.append(len(result))
        result = ""

    return min(length)