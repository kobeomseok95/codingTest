from sys import stdin
READ = lambda : stdin.readline().strip()

n = int(READ())
score = []
for _ in range(n):
    name, kor, eng, mat = READ().split()
    score.append((-int(kor), int(eng), -int(mat), name))
score.sort()
for i in range(n):
    print(score[i][3])