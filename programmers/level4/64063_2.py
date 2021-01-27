import sys
sys.setrecursionlimit(10**6)


def get_empty_room(number, room_dict):
    if number not in room_dict:
        room_dict[number] = number + 1
        return number

    room = get_empty_room(room_dict[number], room_dict)
    room_dict[number] = room + 1
    return room


def solution(k, room_number):
    answer = []
    room_dict = dict()

    for number in room_number:
        answer.append(get_empty_room(number, room_dict))
    return answer
