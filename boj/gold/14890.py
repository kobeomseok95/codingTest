from sys import stdin
read = lambda: stdin.readline().strip()


def counting(n, L, maps):
    count = 0
    slope = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        flag = True
        j = 0
        while j < n - 1:
            if maps[i][j] == maps[i][j + 1]:
                j += 1
                continue
            # 감소의 경우
            elif maps[i][j] - maps[i][j + 1] == 1:
                # 같은 경사의 숫자 체크
                if maps[i][j+1 : j+1+L].count(maps[i][j+1]) >= L:
                    slope[i][j+1 : j+1+L] = [True] * L
                    j += L
                    continue
                else:
                    flag = False
                    break
            # 증가의 경우
            elif maps[i][j] - maps[i][j + 1] == -1:
                # 경사를 만들기 충분한지, 이전 인덱스를 조절하기에 이전 경사가 설정되어있는지 체크
                if maps[i][j-L+1 : j+1].count(maps[i][j]) >= L and True not in slope[i][j-L+1 : j+1]:
                    slope[i][j - L + 1: j + 1] = [True] * L
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