from sys import stdin
read = lambda : stdin.readline().strip()

n = read()
mid = len(n) // 2
front = list(map(int, n[:mid]))
back = list(map(int, n[mid:]))

if sum(front) == sum(back):
    print("LUCKY")
else:
    print("READY")