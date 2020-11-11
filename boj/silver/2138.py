from sys import stdin
READ = lambda : stdin.readline().strip()

def change(arr, idx):
    if idx != N - 1:
        arr[idx - 1] = 1 - arr[idx - 1]
        arr[idx] = 1 - arr[idx]
        arr[idx + 1] = 1 - arr[idx + 1]
    else:
        arr[idx - 1] = 1 - arr[idx - 1]
        arr[idx] = 1 - arr[idx]
    return arr

def count_change(arr):
    count = 0
    for i in range(1, N):
        if arr[i - 1] != to[i - 1]:
            arr = change(arr, i)
            count += 1
    if arr != to:
        return -1
    else:
        return count

N = int(READ())
zero_off = list(map(int, READ()))
to = list(map(int, READ()))
zero_on = [1 - zero_off[0], 1 - zero_off[1]]
zero_on.extend(zero_off[2:])

a1 = count_change(zero_off)
a2 = count_change(zero_on)

if a1 == -1 and a2 != -1:
    print(a2 + 1)
elif a1 != -1 and a2 == -1:
    print(a1)
else:
    print(min(a1, a2+1))