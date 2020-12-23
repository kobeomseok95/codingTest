### 가사 검색 이진탐색 적용
from bisect import bisect_left, bisect_right

def count_by_range(arr, left_val, right_val):
    right_idx = bisect_right(arr, right_val)
    left_idx = bisect_left(arr, left_val)

    return right_idx - left_idx


array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for query in queries:
        if query[0] != '?':
            res = count_by_range(array[len(query)],
                                 query.replace('?', 'a'),
                                 query.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(query)],
                                 query[::-1].replace('?', 'a'),
                                 query[::-1].replace('?', 'z'))

        answer.append(res)

    return answer
"""
from bisect import bisect_left, bisect_right


def count_by_range(arr, left_val, right_val):
    l = bisect_left(arr, left_val)
    r = bisect_right(arr, right_val)

    return r - l


def solution(words, queries):
    answer = []

    sorted_words = [[] for _ in range(10001)]
    reversed_sorted_words = [[] for _ in range(10001)]
    for word in words:
        sorted_words[len(word)].append(word)
        reversed_sorted_words[len(word)].append(word[::-1])

    for i in range(10001):
        sorted_words[i].sort()
        reversed_sorted_words[i].sort()

    for query in queries:
        if query[0] == '?':
            res = count_by_range(reversed_sorted_words[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        else:
            res = count_by_range(sorted_words[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))

        answer.append(res)
    return answer

a = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
             ["fro??", "????o", "fr???", "fro???", "pro?"])
print([3, 2, 4, 1, 0] == a)
print(a)
"""