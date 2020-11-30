#### 2회독째
from sys import stdin
read = lambda : stdin.readline().strip()

s = read()
answer = 0
for i in s:
    no = int(i)
    if no <= 1 or answer <= 1:
        answer += no
    else:
        answer *= no
print(answer)