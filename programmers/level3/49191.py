def solution(n, results):
    # wins[i] = i번째 선수에게 진 사람들
    # loses[i] = i번째 선수를 이긴 사람들
    wins, loses = {}, {}
    for i in range(1, n + 1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n + 1):
        for winner, loser in results:
            if i == winner:
                wins[i].add(loser)
            if i == loser:
                loses[i].add(winner)

        # A는 B를 무조건 이길 수 있는 결과 반영
        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])

    answer = 0
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1
    return answer