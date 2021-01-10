def solution(record):
    msg = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    nickname_dict = {}

    for r in record:
        command = r.split()
        if command[0] != 'Leave':
            nickname_dict[command[1]] = command[2]

    answer = []
    for r in record:
        command = r.split()
        if command[0] != 'Change':
            answer.append(nickname_dict[command[1]] + msg[command[0]])

    return answer