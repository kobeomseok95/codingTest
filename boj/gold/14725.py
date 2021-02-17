from sys import stdin
read = lambda: stdin.readline().strip()


class Trie:
    def __init__(self, me, parent=None):
        self.me = me
        self.parent = parent
        self.children = {}


def get_answer(trie, count):
    print(("--" * count) + trie.me)

    trie.children = dict(sorted(trie.children.items(), key=lambda x: x[0]))
    for k in trie.children.keys():
        get_answer(trie.children[k], count + 1)


def main():
    trie_dict = {}
    for i in range(int(read())):
        data = read().split()
        if data[1] not in trie_dict:
            trie_dict[data[1]] = Trie(data[1])

        cur = trie_dict[data[1]]
        for j in range(2, len(data)):
            # cur에 같은 데이터가 없을 경우
            if data[j] not in cur.children:
                cur.children[data[j]] = Trie(data[j])
            cur = cur.children[data[j]]

    trie_dict = dict(sorted(trie_dict.items(), key=lambda x: x[0]))
    for k in trie_dict.keys():
        get_answer(trie_dict[k], 0)


if __name__ == "__main__":
    main()