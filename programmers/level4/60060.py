### 가사 검색
### 정확성 모두 통과, 효율성 5개중 2개 통과
def get_word_count(query, word):
    if len(query) != len(word):
        return False

    for i in range(len(query)):
        if query[i] != '?' and query[i] != word[i] :
            return False

    return True


def solution(words, queries):
    lw = len(words)
    lq = len(queries)
    answer = [0] * lq

    for i in range(lq):
        for j in range(lw):
            result = get_word_count(queries[i], words[j])
            if result:
                answer[i] += 1

    return answer