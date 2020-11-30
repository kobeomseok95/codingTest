from sys import stdin
read = lambda : stdin.readline().strip()

s = list(map(str, read()))
s.sort()

nums, string = 0, ""
for i in range(len(s)):
    if s[i].isdigit():
        nums += int(s[i])
    else:
        string += s[i]

string += str(nums)
print(string)