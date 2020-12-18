from sys import stdin
read = lambda : stdin.readline().strip()

string = list(map(str, read()))
string.sort(reverse=True)

sums = 0
while string[-1].isdigit():
    sums += int(string[-1])
    string.pop()

answer = ''.join(string[::-1]) + str(sums)
print(answer)