from sys import stdin
read = lambda: stdin.readline().strip()


def counting(n, L, maps):
    count = 0
    chk = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        j = 0
        flag = True
        while j < n - 1:
            if maps[i][j] == maps[i][j + 1]:
                j += 1
                continue
            elif maps[i][j] - maps[i][j + 1] == 1:
                if maps[i][j + 1: j + 1 + L].count(maps[i][j + 1]) == L:
                    chk[i][j + 1: j + 1 + L] = [True] * L
                    j += L
                    continue
                else:
                    flag = False
                    break
            elif maps[i][j] - maps[i][j + 1] == -1:
                if maps[i][j - L + 1: j + 1].count(maps[i][j]) == L and True not in chk[i][j - L + 1: j + 1]:
                    chk[i][j - L + 1: j + 1] = [True] * L
                    j += 1
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            count += 1
    return count


if __name__ == "__main__":
    n, l = map(int, read().split())
    maps = []
    answer = 0
    for i in range(n):
        maps.append(list(map(int, read().split())))
    zip_maps = list(map(list, list(zip(*maps))))

    count1 = counting(n, l, maps)
    count2 = counting(n, l, zip_maps)
    print(count1 + count2)