class Trie:
    def __init__(self):
        self.count = 0
        self.children = {}

    def insert(self, string):
        # Top 부분
        cur = self
        for s in string:
            # 해당 글자에 몇번 접근하는지 저장
            cur.count += 1

            # 딕셔너리로 다음 단어 글자 표현하기
            if s not in cur.children:
                cur.children[s] = Trie()
            cur = cur.children[s]

        # 마지막 글자도 몇번 접근하는지 저장
        cur.count += 1

    def find(self, string):
        cur = self
        for s in string:
            if s not in cur.children:
                return False
            cur = cur.children[s]

        if cur.count > 1:
            return False
        else:
            return True


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        find = False
        for i in range(1, len(word) + 1):
            if trie.find(word[:i]):
                answer += len(word[:i])
                find = True
                break

        if not find:
            answer += len(word)

    return answer