import re


def solution(word, pages):
    word = word.lower()

    page_url_index = {}
    page_url_score = {}
    page_exurl_url = {}
    page_url_exurl_count = {}

    for i in range(len(pages)):
        page_lower = pages[i].lower()

        # 해당 url의 index 설정
        url = re.search(r'<meta ([\S]*) content="([\S]*)"/>', page_lower).group(2)
        page_url_index[url] = i

        # 기본점수 구하기
        count = 0
        for split_word in re.split(r'[^a-zA-Z]', page_lower): # 알파벳을 제외한 모든 문자로 나눈다.
            if word == split_word:
                count += 1
        page_url_score[url] = count

        # 외부링크 구하기
        for exurl in re.findall(r'<a href="([\S]*)">', page_lower):
            if exurl not in page_exurl_url:
                page_exurl_url[exurl] = []
            page_exurl_url[exurl].append(url)
            #
            if url not in page_url_exurl_count:
                page_url_exurl_count[url] = 0
            page_url_exurl_count[url] += 1

    # 매칭 점수 계산하기, 링크 점수를 담을 임시 변수 생성
    page_url_exurl_score = {}
    for exurl, urls in page_exurl_url.items():
        if exurl in page_url_score:
            score = 0
            for url in urls:
                score += (page_url_score[url] / page_url_exurl_count[url])
            page_url_exurl_score[exurl] = score

    # 계산한 매칭점수를 page_url_score에 대입
    for url, score in page_url_exurl_score.items():
        page_url_score[url] += score
    
    # 기록한 score를 점수순으로 정렬, index 리턴
    answer = sorted(page_url_score.items(), key=lambda x: -x[1])
    return page_url_index[answer[0][0]]