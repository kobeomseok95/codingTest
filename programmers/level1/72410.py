def step2(string):
    ret = ""
    for i in range(len(string)):
        if string[i].isalpha() or string[i].isdigit() or string[i] == "-" or string[i] == "_" or string[i] == ".":
            ret += string[i]
    return ret


def step3(string):
    ret = string[0]
    for i in range(1, len(string)):
        if ret[-1] == "." and string[i] == ".":
            continue
        ret += string[i]
    return ret


def step4(string):
    ret = ""
    if string[0] != ".":
        ret += string[0]
    ret += string[1:-1]
    if string[-1] != ".":
        ret += string[-1]
    return ret


def step6(string):
    if len(string) < 16:
        return string
    ret = ""
    if string[:15][-1] != ".":
        ret = string[:15]
    else:
        ret = string[:14]
    return ret


def step7(string):
    if len(string) > 2:
        return string
    while len(string) < 3:
        string += string[-1]
    return string


def solution(new_id):
    new_id = new_id.lower()
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    if new_id == "":
        new_id += "a"
    new_id = step6(new_id)
    new_id = step7(new_id)

    return new_id



































################
a = solution("...!@BaT#*..y.abcdefghijklm")
print(a == "bat.y.abcdefghi", a)
a = solution("z-+.^.")
print(a == "z--", a)
a = solution("=.=")
print(a == "aaa", a)
a = solution("123_.def")
print(a == "123_.def", a)
a = solution("abcdefghijklmn.p")
print(a == "abcdefghijklmn", a)