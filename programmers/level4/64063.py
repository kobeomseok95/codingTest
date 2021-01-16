import sys
sys.setrecursionlimit(10**6)


def find_empty_room(number, rooms):
    if number not in rooms.keys():
        rooms[number] = number + 1
        return number

    empty = find_empty_room(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty


def solution(k, room_number):
    answer = []
    rooms = {}
    for number in room_number:
        answer.append(find_empty_room(number, rooms))
    return answer