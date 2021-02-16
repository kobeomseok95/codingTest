def solution(A, B):
    n = len(A)
    a = sorted(A)
    b = sorted(B)
    check = [False for _ in range(n)]

    answer = 0
    for i in range(n):
        if a[i] < b[i] and not check[i]:
            check[i] = True
            answer += 1
        elif a[i] >= b[i] or check[i]:
            for j in range(i, n):
                if a[i] < b[j] and not check[j]:
                    check[j] = True
                    answer += 1
                    break

    return answer



































########################################################################################
def main():
    a = solution([5, 1, 3, 7], [2, 2, 6, 8])
    print(a == 3, a)
    a = solution([2, 2, 2, 2], [1, 1, 1, 1])
    print(a == 0, a)


if __name__ == "__main__":
    main()