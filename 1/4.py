class Doll:
    def __init__(self, keyword=None):
        self.parent = None
        self.children = {}
        self.keyword = keyword


def solution(data, word):
    doll = Doll()

    for d in data:
        cid, string, pid = d.split(" ")
        if pid == 0:
            doll.keyword = string
            doll.children[cid] = Doll()
        else:



if __name__ == "__main__":
    a = solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"],
                 "BROWN")
    print(a == ["CONY/DOLL/BROWN-CONY", "BROWN/DOLL/LARGE-BROWN", "BROWN/DOLL/SMALL-BROWN"], a)