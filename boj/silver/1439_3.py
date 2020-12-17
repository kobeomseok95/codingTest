from sys import stdin
read = lambda : stdin.readline().strip()

s = read()
initial, standard, count = s[0], s[0], 0
for i in range(1, len(s)):
    if standard != s[i] and initial != s[i]:
        count += 1
    standard = s[i]
print(count)