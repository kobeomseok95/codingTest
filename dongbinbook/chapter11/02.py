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
"""
또 다른 풀이
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
"""