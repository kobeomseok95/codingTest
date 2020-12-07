from sys import stdin
read = lambda : stdin.readline().strip()

n = int(read())
students = []
for i in range(n):
    name, kor, eng, mat = map(str, read().split())
    students.append((-int(kor), int(eng), -int(mat), name))

students.sort()
for i in range(n):
    print(students[i][3])