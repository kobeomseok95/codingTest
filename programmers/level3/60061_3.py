def possible(answer):
    for x, y, structure in answer:
        if structure == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif structure == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        if frame[3] == 0:
            answer.remove([frame[0], frame[1], frame[2]])
            if not possible(answer):
                answer.append([frame[0], frame[1], frame[2]])

        elif frame[3] == 1:
            answer.append([frame[0], frame[1], frame[2]])
            if not possible(answer):
                answer.remove([frame[0], frame[1], frame[2]])

    return sorted(answer, key=lambda x:(x[0], x[1], x[2]))