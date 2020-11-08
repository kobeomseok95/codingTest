from sys import stdin
READ = lambda : stdin.readline().strip()

S = READ()
answer = 0
for i in range(len(S)):
    if S[i] == '0' or S[i] == '1' or answer == 0:
        answer += int(S[i])
    else:
        answer *= int(S[i])

print(answer)