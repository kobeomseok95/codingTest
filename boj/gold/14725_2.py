from sys import stdin
read = lambda: stdin.readline().strip()

def main():
    ants = []
    for i in range(int(read())):
        ants.append(read().split()[1:])

    tmp = []
    for ant in sorted(ants):
        count = 0
        for j in range(len(tmp)):
            if tmp[j] == ant[j]:
                count += 1
            else:
                break
        c = count
        for j in range(count, len(ant)):
            print("--" * c + ant[j])
            c += 1
        tmp = ant


if __name__ == "__main__":
    main()