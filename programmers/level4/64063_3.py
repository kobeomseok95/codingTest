def solution(k, room_number):
    answer = []
    room = dict()

    for number in room_number:
        n = number
        visit = [n]
        while n in room.keys():
            n = room[n]
            visit.append(n)

        answer.append(n)
        for v in visit:
            room[v] = n + 1

    return answer