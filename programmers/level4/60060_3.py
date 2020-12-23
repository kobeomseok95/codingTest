from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []
    words_length = [[] for _ in range(10001)]
    reversed_words_length = [[] for _ in range(10001)]
    for w in words:
        words_length[len(w)].append(w)
        reversed_words_length[len(w)].append(w[::-1])

    for i in range(10001):
        words_length[i].sort()
        reversed_words_length[i].sort()

    for q in queries:
        if q[0] == '?':
            words_list = reversed_words_length[len(q)]
            left = bisect_left(words_list, q[::-1].replace("?", "a"))
            right = bisect_right(words_list, q[::-1].replace("?", "z"))
            answer.append(right - left)

        elif q[0] != '?':
            words_list = words_length[len(q)]
            left = bisect_left(words_list, q.replace("?", "a"))
            right = bisect_right(words_list, q.replace("?", "z"))
            answer.append(right - left)

    return answer















######################################################################
a = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
             ["fro??", "????o", "fr???", "fro???", "pro?"])
print(a, a == [3, 2, 4, 1, 0])