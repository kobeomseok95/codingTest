# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.2MB)
# 테스트 4 〉	통과 (0.06ms, 10.2MB)
# 테스트 5 〉	통과 (1.04ms, 10.5MB)
# 테스트 6 〉	통과 (0.90ms, 10.5MB)
# 테스트 7 〉	통과 (0.73ms, 10.5MB)
# 테스트 8 〉	통과 (0.88ms, 10.6MB)
# 테스트 9 〉	통과 (0.98ms, 10.6MB)
# 테스트 10 〉	통과 (0.83ms, 10.6MB)
# 테스트 11 〉	통과 (0.55ms, 10.3MB)
# 테스트 12 〉	통과 (0.51ms, 10.3MB)
# 테스트 13 〉	통과 (0.90ms, 10.5MB)
# 테스트 14 〉	통과 (1.02ms, 10.5MB)
# 테스트 15 〉	통과 (0.02ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.09ms, 10.1MB)
# 테스트 18 〉	통과 (0.08ms, 10.3MB)
# 테스트 19 〉	통과 (0.89ms, 10.6MB)
# 테스트 20 〉	통과 (0.83ms, 10.5MB)
# 테스트 21 〉	통과 (0.80ms, 10.4MB)
# 테스트 22 〉	통과 (0.82ms, 10.2MB)
# 테스트 23 〉	통과 (0.94ms, 10.6MB)
# 테스트 24 〉	통과 (0.93ms, 10.7MB)
# 테스트 25 〉	통과 (81.66ms, 55.7MB)
# 테스트 26 〉	통과 (99.07ms, 60.4MB)
# 테스트 27 〉	통과 (104.29ms, 63.3MB)
# 테스트 28 〉	통과 (105.29ms, 65.7MB)
# 테스트 29 〉	통과 (111.59ms, 65.5MB)
# 테스트 30 〉	통과 (67.05ms, 51.3MB)
# 테스트 31 〉	통과 (78.70ms, 63.6MB)
# 테스트 32 〉	통과 (59.92ms, 55.7MB)
def solution(record):
    answer = []
    ids = {}
    for r in record:
        command = r.split()
        if command[0] == "Enter":
            ids[command[1]] = command[2]
            answer.append([command[1], True])
        elif command[0] == "Leave":
            answer.append([command[1], False])
        elif command[0] == "Change":
            ids[command[1]] = command[2]

    for i in range(len(answer)):
        user_id, status = answer[i]
        if status:
            answer[i] = ids[user_id] + "님이 들어왔습니다."
        else:
            answer[i] = ids[user_id] + "님이 나갔습니다."

    return answer