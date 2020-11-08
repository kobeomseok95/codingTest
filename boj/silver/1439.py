from sys import stdin
READ = lambda : stdin.readline().strip()

S = READ()
prev, count = 'X', 0
for i in S:
    if i != prev:
        count += 1
        prev = i

print(count // 2)