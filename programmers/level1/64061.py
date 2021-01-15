def get_doll(board, idx):
    for i in range(len(board)):
        if board[i][idx] != 0:
            doll = board[i][idx]
            board[i][idx] = 0
            return doll
    return 0


def solution(board, moves):
    answer = 0
    bucket = []
    for m in moves:
        doll = get_doll(board, m - 1)

        if doll != 0:
            if not bucket or bucket[-1] != doll:
                bucket.append(doll)

            elif bucket[-1] == doll:
                bucket.pop()
                answer += 2

    return answer