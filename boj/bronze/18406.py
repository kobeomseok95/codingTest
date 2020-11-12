from sys import stdin
READ = lambda : stdin.readline().strip()

N = str(READ())
length = len(N)
left, right = 0, 0
for i in range(length // 2):
    left += int(N[i])

for i in range(length // 2, length):
    right += int(N[i])

if right == left:
    print("LUCKY")
else:
    print("READY")