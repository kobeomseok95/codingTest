import sys
read = lambda : sys.stdin.readline().strip()


def calculator(front, back, op_idx):
    result = 0
    if op_idx == 0:
        return front + back
    elif op_idx == 1:
        return front - back
    elif op_idx == 2:
        return front * back
    elif op_idx == 3:
        if front < 0:
            return -(-front // back)
        else:
            return front // back


def dfs(count, idx, result):
    if count == 0:
        global max_answer, min_answer
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
    else:
        for i in range(4):
            if operator[i] > 0:
                r = calculator(result, numbers[idx + 1], i)
                operator[i] -= 1
                dfs(count - 1, idx + 1, r)
                operator[i] += 1
            else:
                continue


n = int(read())
numbers = list(map(int, read().split()))
operator = list(map(int, read().split()))
max_answer, min_answer = -sys.maxsize, sys.maxsize
dfs(sum(operator), 0, numbers[0])
print(max_answer)
print(min_answer)