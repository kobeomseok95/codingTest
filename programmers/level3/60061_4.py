def build_possible(answer):
    for build in answer:
        x, y, a = build
        if a == 0:  #기둥
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        else:       #보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:
            answer.remove([x, y, a])
            if not build_possible(answer):
                answer.append([x, y, a])
        else:
            answer.append([x, y, a])
            if not build_possible(answer):
                answer.remove([x, y, a])
    answer.sort()
    return answer






















####################################################################################
a = solution(5, [[1,0,0,1],
                 [1,1,1,1],
                 [2,1,0,1],
                 [2,2,1,1],
                 [5,0,0,1],
                 [5,1,0,1],
                 [4,2,1,1],
                 [3,2,1,1]])
print(a, a == [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]])

b = solution(5, 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
print(b, b == [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]])