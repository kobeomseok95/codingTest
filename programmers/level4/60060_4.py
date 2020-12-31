from bisect import bisect_left, bisect_right


def solution(words, queries):
    len_words = [[] for _ in range(10001)]
    reverse_len_words = [[] for _ in range(10001)]
    for w in words:
        len_words[len(w)].append(w)
        reverse_len_words[len(w)].append(w[::-1])

    for i in range(1, 10001):
        len_words[i].sort()
        reverse_len_words[i].sort()

    answer = []
    for query in queries:
        if query[0] != '?':
            a = bisect_left(len_words[len(query)], query.replace("?", "a"))
            b = bisect_right(len_words[len(query)], query.replace("?", "z"))
            answer.append(b - a)
        elif query[0] == '?':
            a = bisect_left(reverse_len_words[len(query)], query[::-1].replace("?", "a"))
            b = bisect_right(reverse_len_words[len(query)], query[::-1].replace("?", "z"))
            answer.append(b - a)
    return answer























################################################################################
a = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
             ["fro??", "????o", "fr???", "fro???", "pro?"])
print(a == [3, 2, 4, 1, 0], a)