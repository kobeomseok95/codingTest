# 매개변수의 조건을 검증하는 메서드
def assert_condition(condition, arguments_list):
    # 아무것도 주어지지 않은 경우
    if condition == "":
        return False

    # 문자열 확인하기, list 크기가 1 초과이거나 비었거나, 알파벳이 아닌 경우
    elif condition == "STRING":
        if len(arguments_list) > 1 or not arguments_list or not arguments_list[0].isalpha():
            return False
        return True

    # 문자열 리스트 확인하기, 리스트의 argument 중 하나라도 isalpha를 만족하지 못하면 false 반환
    elif condition == "STRINGS":
        for a in arguments_list:
            if not a.isalpha():
                return False
        return True

    # 숫자 확인하기, list 크기가 1 초과이거나 비었거나, 숫자가 아닌 경우
    elif condition == "NUMBER":
        if len(arguments_list) > 1 or not arguments_list or not arguments_list[0].isdigit():
            return False
        return True

    # 숫자 리스트 확인하기, 만약 argument중 하나라도 isdigit을 만족하지 못하면 false 반환
    elif condition == "NUMBERS":
        for a in arguments_list:
            if not a.isdigit():
                return False
        return True

    # null일 경우 argument_list가 없어야한다.
    else:
        return True if arguments_list else False


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
        names_idx, arguments_idx = 0, 0
        while names_idx < len(flags):
            # 명령어가 rules에 담겨있는지 조회
            if flags[names_idx][0] == "-":

                # rules에 담겨있지 않으면 break
                if flags[names_idx] not in rules.keys():
                    assert_flag = False
                    break

                # 있을 경우 arguments_idx를 통해 검사하기,
                else:
                    arguments_idx = names_idx + 1
                    # 다음 flags 중 -가 없는 경우까지 인덱스 조회
                    while arguments_idx < len(flags):
                        if flags[arguments_idx][0] == "-":
                            break
                        arguments_idx += 1

                    # 검증되지 않은 경우 반복문 탈출
                    if not assert_condition(rules[flags[names_idx]], flags[names_idx + 1: arguments_idx]):
                        assert_flag = False
                        break
                    # 검증된 경우 names_idx에 매개변수 위치를 가리킨 arguments_idx를 더해준다.
                    else:
                        names_idx += arguments_idx

            # 처음부터 flag_name 규칙에 위반되므로 break
            else:
                assert_flag = False
                break

        # 모든 조건을 만족한 경우
        if assert_flag:
            answer[i] = True

    return answer





if __name__ == "__main__":
    a = solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"],
                 ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"])
    print(a == [True, False], a)
    a = solution("trip", ["-days NUMBERS", "-dest STRING"],
                 ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"])
    print(a == [False, True], a)