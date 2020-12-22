from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
arr = []
for _ in range(n):
    data = list(map(str, read().split()))
    name, kor, eng, math = data[0], -int(data[1]), int(data[2]), -int(data[3]),
    arr.append([kor, eng, math, name])

arr.sort()
for i in range(n):
    print(arr[i][3])