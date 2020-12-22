from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
arr = list(map(int, read().split()))
arr.sort()
print(arr[(n - 1) // 2])