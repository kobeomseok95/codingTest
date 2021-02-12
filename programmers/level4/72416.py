### 나중에 풀어보기


import sys
sys.setrecursionlimit(10**6)


def dfs(sales_dict, leader_team_no, team_no_members, check, answer, count, idx):
    if False not in check and idx == len(team_no_members) + 1:
        answer = min(answer, count)

    for i in range(len(team_no_members[idx])):
        count += sales_dict[team_no_members[idx][i]]
        check[idx] = True
        if team_no_members[idx][i] in leader_team_no:
            check[leader_team_no[team_no_members[idx][i]]] = True

        dfs(sales_dict, leader_team_no, team_no_members, check, answer, count, idx + 1)

        count -= sales_dict[team_no_members[idx][i]]
        check[idx] = False


def solution(sales, links):
    answer = int(1e9)
    # 사원번호: 매출액
    sales_dict = {i + 1: sales[i] for i in range(len(sales))}

    links.sort(key=lambda x: (x[0], x[1]))
    # 팀장사번, 팀번호
    leader_team_no = {}
    idx = 0
    for link in links:
        if link[0] not in leader_team_no:
            leader_team_no[link[0]] = idx
            idx += 1

    # 팀번호(인덱스), 속한 팀원 및 팀장
    team_no_members = {}
    for leader, member in links:
        if leader_team_no[leader] not in team_no_members:
            team_no_members[leader_team_no[leader]] = [leader]
        team_no_members[leader_team_no[leader]].append(member)

    # 팀 방문 체크
    team_check = [False for _ in range(len(leader_team_no))]
    dfs(sales_dict, leader_team_no, team_no_members, team_check, answer, 0, 0)
    return answer



# leader_team_no =
# {1: 0, 5: 1, 9: 2, 10: 3}
# team_no_members =
# {0: [1, 3, 5, 9], 1: [5, 4, 10], 2: [9, 7], 3: [10, 2, 6, 8]}






























###########################################################################
if __name__ == "__main__":
    a = solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])
    print(a == 44, a)
    # a = solution([5, 6, 5, 3, 4],[[2,3], [1,4], [2,5], [1,2]])
    # print(a == 6, a)
    # a = solution([5, 6, 5, 1, 4],[[2,3], [1,4], [2,5], [1,2]])
    # print(a == 5, a)
    # a = solution([10, 10, 1, 1],[[3,2], [4,3], [1,4]])
    # print(a == 2, a)