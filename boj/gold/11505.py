from sys import stdin
from math import ceil, log2
read = lambda: stdin.readline().strip()


def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    init(arr, tree, node * 2, start, mid)
    init(arr, tree, node * 2 + 1, mid + 1, end)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD


def update(tree, node, start, end, idx, val):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = val
        return

    mid = (start + end) // 2
    update(tree, node * 2, start, mid, idx, val)
    update(tree, node * 2 + 1, mid + 1, end, idx, val)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD


def query(tree, node, start, end, left, right):
    if start > right or end < left:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return (query(tree, node * 2, start, mid, left, right) * query(tree, node * 2 + 1, mid + 1, end, left, right)) % MOD


if __name__ == "__main__":
    MOD = 1000000007
    n, m, k = map(int, read().split())
    h = int(ceil(log2(n)))
    size = 1 << (h + 1)

    tree = [0] * size
    arr = [int(read()) for _ in range(n)]
    init(arr, tree, 1, 0, n - 1)

    for _ in range(m + k):
        a, b, c = map(int, read().split())
        if a == 1:
            arr[b - 1] = c
            update(tree, 1, 0, n - 1, b - 1, c)
        elif a == 2:
            print(query(tree, 1, 0, n - 1, b - 1, c - 1))