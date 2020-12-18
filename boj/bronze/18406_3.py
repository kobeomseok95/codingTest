from sys import stdin
read = lambda : stdin.readline().strip()

n = list(map(int, read()))
s1, s2 = sum(n[:len(n) // 2]), sum(n[len(n) // 2:])

if s1 == s2:
    print("LUCKY")
else:
    print("READY")