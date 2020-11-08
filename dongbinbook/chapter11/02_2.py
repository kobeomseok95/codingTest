from sys import stdin
READ = lambda : stdin.readline().strip()

S = READ()
answer = int(S[0])
for i in range(1, len(S)):
    if answer <= 1:
        answer += int(S[i])
    else:
        answer *= int(S[i])

print(answer)