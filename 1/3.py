def solution(enter, leave):
    answer = [0] * (len(enter) + 1)

    trace = set()
    prev_meet = [False for _ in range(len(enter) + 1)]
    enter_idx, leave_idx = 0, 0
    while True:
        if leave_idx >= len(leave):
            break

        if leave[leave_idx] not in trace:
            trace.add(enter[enter_idx])
            enter_idx += 1
        else:
            flag = False
            for t in trace:
                if not prev_meet[t]:
                    flag = True
                    break

            if flag:
                for no in trace:
                    prev_meet[no] = True
                    answer[no] += len(trace) - 1
            trace.remove(leave[leave_idx])
            prev_meet[leave[leave_idx]] = False
            leave_idx += 1

    return answer[1:]





























if __name__ == "__main__":
    a = solution([1, 3, 2], [1, 2, 3])
    print(a == [0, 1, 1], a)

    a = solution([1, 4, 2, 3], [2, 1, 3, 4])
    print(a == [2, 2, 1, 3], a)

    a = solution([3, 2, 1], [2, 1, 3])
    print(a == [1, 1, 2], a)

    a = solution([3, 2, 1], [1, 3, 2])
    print(a == [2, 2, 2], a)

    a = solution([1, 4, 2, 3], [2, 1, 4, 3])
    print(a == [2, 2, 0, 2], a)