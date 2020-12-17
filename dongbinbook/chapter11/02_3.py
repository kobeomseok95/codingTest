from sys import stdin
read = lambda : stdin.readline().strip()

data = list(map(int, read()))
result = 0

for i in data:
    if result == 0 or i == 0:
        result += i
    else:
        result *= i
print(result)