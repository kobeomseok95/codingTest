from sys import stdin
read = lambda: stdin.readline().strip()


n = int(read())
stack = []
answer = 0
for _ in range(n):
    height = int(read())

    while stack and stack[-1][0] < height:
        answer += stack.pop()[1]

    if stack and stack[-1][0] == height:
        count = stack.pop()[1]
        answer += count
        if stack:
            answer += 1
        stack.append((height, count + 1))

    else:
        if stack:
            answer += 1
        stack.append((height, 1))
print(answer)