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
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update(tree, node, left, right, idx, val):
    if idx < left or idx > right:
        return
    if left == right:
        tree[node] = val
        return

    mid = (left + right) // 2
    update(tree, node * 2, left, mid, idx, val)
    update(tree, node * 2 + 1, mid + 1, right, idx, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(tree, node, left, right, start, end):
    if end < left or start > right:
        return 0
    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2
    return query(tree, node * 2, left, mid, start, end) + query(tree, node * 2 + 1, mid + 1, right, start, end)


if __name__ == "__main__":
    n, m, k = map(int, read().split())

    h = int(ceil(log2(n)))
    size = 1 << (h + 1)
    tree = [0] * size
    arr = [int(read()) for _ in range(n)]

    init(arr, tree, 1, 0, n - 1)

    for _ in range(m + k):
        a, b, c = map(int, read().split())
        if a == 1:
            update(tree, 1, 0, n - 1, b - 1, c)
        elif a == 2:
            print(query(tree, 1, 0, n - 1, b - 1, c - 1))