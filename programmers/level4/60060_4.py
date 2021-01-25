from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []
    len_words = [[] for _ in range(10001)]
    reverse_len_words = [[] for _ in range(10001)]
    for w in words:
        len_words[len(w)].append(w)
        reverse_len_words[len(w)].append(w[::-1])

    for i in range(10001):
        len_words[i].sort()
        reverse_len_words[i].sort()

    for i in range(len(queries)):
        n = len(queries[i])
        if queries[i][0] != "?":
            find_left_index_query = queries[i].replace("?", "a")
            find_right_index_query = queries[i].replace("?", "z")
            answer.append(
                bisect_right(len_words[n], find_right_index_query)
                - bisect_left(len_words[n], find_left_index_query)
            )
        else:
            find_left_index_query = queries[i][::-1].replace("?", "a")
            find_right_index_query = queries[i][::-1].replace("?", "z")
            answer.append(
                bisect_right(reverse_len_words[n], find_right_index_query)
                - bisect_left(reverse_len_words[n], find_left_index_query)
            )

    return answer