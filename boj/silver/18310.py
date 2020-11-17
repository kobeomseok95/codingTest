from sys import stdin
READ = lambda : stdin.readline().strip()

n = int(READ())
antenna = list(map(int, READ().split()))
antenna.sort()
print(antenna[(n - 1) // 2])