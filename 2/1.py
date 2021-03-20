# 매개변수의 조건을 검증하는 메서드
def assert_condition(condition, flag_argument):
    # 아무것도 주어지지 않은 경우
    if condition == "":
        return False
    # 문자열 확인하기
    elif condition == "STRING":
        return flag_argument.isalpha()
    # 숫자인지 확인하기
    elif condition == "NUMBER":
        return flag_argument.isdigit()
    # null일 경우
    else:
        return len(flag_argument) > 0


def solution(program, flag_rules, commands):
    answer = [False] * len(commands)

    # flag_name을 key, 매개변수 타입(string)을 value로 하는 딕셔너리
    rules = {}
    for fr in flag_rules:
        flag_name, flag_argument_type = fr.split(" ")
        rules[flag_name] = flag_argument_type

    # commands를 하나씩 검사합니다.
    for i in range(len(commands)):
        com = commands[i].split(" ")

        # 프로그램명과 명령어들을 분할
        program_name = com[0]
        flags = com[1:]

        # 프로그램명을 검사하고 만족하지 못할 경우, 바로 다음 반복문으로 넘어갑니다.
        if program_name != program:
            continue

        # flag들을 만족하는지 검사한다.
        assert_flag = True
        j = 0
        condition = ""
        while j < len(flags):
            # flag_name 검증
            if flags[j][0] == "-":

                # flag_name이 rules의 key에 없는 경우는
                # while문을 바로 나옵니다.
                if flags[j] not in rules:
                    assert_flag = False
                    break

                # 있을 경우는 condition에 저장합니다.
                condition = rules[flags[j]]

            # flag_argument 검사, 기존에 저장한 condition에 맞게 확인합니다.
            else:
                # 검증되지 못했을 경우 while문을 바로 나옵니다.
                if not assert_condition(condition, flags[j]):
                    assert_flag = False
                    break
            j += 1

        # 모든 조건을 만족한 경우
        if assert_flag:
            answer[i] = True

    return answer



































if __name__ == "__main__":
    a = solution("line", ["-s STRING", "-n NUMBER", "-e NULL"],
                 ["line -n 100 -s hi -e", "lien -s Bye"])
    print(a == [True, False], a)
    a = solution("line", ["-s STRING", "-n NUMBER", "-e NULL"],
                 ["line -s 123 -n HI", "line fun"])
    print(a == [False, False], a)