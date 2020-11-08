from sys import stdin
READ = lambda : stdin.readline().strip()

N = int(READ())
adventurer = list(map(int, READ().split()))
adventurer.sort()

count, answer = 0, 0
for i in adventurer:
    count += 1
    if count >= i:
        answer += 1
        count = 0

print(answer)