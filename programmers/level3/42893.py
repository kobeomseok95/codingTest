import re


def solution(word, pages):
    url_to_idx = {}
    url_to_score = {}
    url_to_exlink = {}

    word = word.lower()
    for i in range(len(pages)):
        # 문자열 전부 소문자로 변환
        lower_page = pages[i].lower()
        url = re.search(r'<meta property="og:url" content="https://([\S]*)"/>', lower_page).group(1)
        url_to_idx[url] = i

        word_count = 0
        for find in re.findall(r'[a-zA-Z]+', lower_page):
            if word == find:
                word_count += 1

        s = set()
        for e in re.findall(r'<a href="https://[\S]*">', lower_page):
            s.add(re.search(r'"https://([\S]*)"', e).group(1))
        s = list(s)
        url_to_score[url] = list()
        url_to_score[url].append(word_count)
        url_to_score[url].append(len(s))

        for e in s:
            if e not in url_to_exlink.keys():
                url_to_exlink[e] = list()
            url_to_exlink[e].append(url)

    result = []
    for k, v in url_to_score.items():
        score = v[0]
        if k in url_to_exlink.keys():
            for u in url_to_exlink[k]:
                score += url_to_score[u][0] / url_to_score[u][1]
        result.append([score, url_to_idx[k]])
    return sorted(result, key=lambda x:(-x[0], x[1]))[0][1]