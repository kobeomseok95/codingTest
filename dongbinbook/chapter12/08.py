from sys import stdin
READ = lambda: stdin.readline().strip()

s = list(map(str, READ()))
s.sort(reverse=True)

num = 0
while s and s[-1].isdigit():
    num += int(s.pop())

num = str(num)
ans = ''
for i in reversed(s):
    ans += i
if num != '0':
    for i in num:
        ans += i
print(ans)