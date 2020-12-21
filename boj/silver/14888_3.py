from sys import stdin
read = lambda : stdin.readline().strip()


def dfs(count, result):
    global max_val, min_val, add, sub, mul, div

    if count == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)

    if add > 0:
        add -= 1
        dfs(count + 1, result + numbers[count])
        add += 1

    if sub > 0:
        sub -= 1
        dfs(count + 1, result - numbers[count])
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(count + 1, result * numbers[count])
        mul += 1

    if div > 0:
        div -= 1
        if result < 0:
            dfs(count + 1, -(-result // numbers[count]))
        else:
            dfs(count + 1, result // numbers[count])
        div += 1


max_val, min_val = -int(1e9) - 1, int(1e9) + 1
n = int(read())
numbers = list(map(int, read().split()))
add, sub, mul, div = map(int, read().split())

dfs(1, numbers[0])
print(max_val)
print(min_val)