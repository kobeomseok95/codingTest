def solution(A, B):
    A.sort()
    B.sort()

    answer = 0
    j = 0
    for i in range(len(B)):
        if B[i] > A[j]:
            answer += 1
            j += 1

    return answer