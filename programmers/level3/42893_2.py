import re


def solution(word, pages):
    page_index = {}
    page_score = {}
    page_link_count = {}
    page_to_exlink = {}

    word = word.lower()
    for i in range(len(pages)):
        lower_page = pages[i].lower()
        url = re.search(r'<meta property="og:url" content="https://([\S]*)"/>', lower_page).group(1)
        page_index[url] = i

        page_score[url] = 0
        for find in re.findall(r'[a-zA-Z]+', lower_page):
            if find == word:
                page_score[url] += 1

        exlink = re.findall(r'<a href="https://([\S]*)">', lower_page)
        page_link_count[url] = len(exlink)
        for e in exlink:
            if e in page_to_exlink.keys():
                page_to_exlink[e].append(url)
            else:
                page_to_exlink[e] = [url]

    score_dict = {}
    for k, v in page_to_exlink.items():
        score = 0
        if k in page_score.keys():
            for ex in v:
                score += page_score[ex] / page_link_count[ex]
            score_dict[k] = score
    for k, v in score_dict.items():
        page_score[k] += v

    answer = sorted(page_score.items(), key=lambda x: -x[1])
    return page_index[answer[0][0]]