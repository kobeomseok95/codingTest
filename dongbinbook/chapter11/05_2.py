from sys import stdin
read = lambda : stdin.readline().strip()

n, m = map(int, read().split())
data = list(map(int, read().split()))

weight = [0 for _ in range(11)]
for d in data:
    weight[d] += 1

answer = 0
for i in range(1, m + 1):
    n -= weight[i]
    answer += n * weight[i]
print(answer)
#------#------#------#------#------#------#내가 작성한 코드------#------#------#------#------#------#------#------
# n, m = map(int, read().split())
# data = list(map(int, read().split()))
#
# pair = set()
# weight = [] #(공번호, 무게)
# for i in enumerate(data, start = 1):
#     weight.append(i)
#
# weight = sorted(weight, key = lambda x : (x[1], x[0]))
# for i in range(n):
#     for j in range(i + 1, n):
#         if weight[i][1] == weight[j][1]:
#             continue
#
#         num1, num2 = weight[i][0], weight[j][0]
#         if num1 > num2:
#             num1, num2 = num2, num1
#         pair.add((num1, num2))
# print(len(pair))

