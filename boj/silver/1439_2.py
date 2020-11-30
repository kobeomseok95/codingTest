from sys import stdin
read = lambda : stdin.readline().strip()

s = read()
standard = s[0]

answer = 0
for i in range(1, len(s)):
    if standard != s[i]:
        standard = s[i]
        if standard == s[0]:
            continue
        else:
            answer += 1
print(answer)