from sys import stdin
from math import ceil, log2
read = lambda: stdin.readline().strip()


def min_tree_init(arr, min_tree, node, left, right):
    if left == right:
        min_tree[node] = arr[left]
        return

    mid = (left + right) // 2
    min_tree_init(arr, min_tree, node * 2, left, mid)
    min_tree_init(arr, min_tree, node * 2 + 1, mid + 1, right)
    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
    
    
def max_tree_init(arr, max_tree, node, left, right):
    if left == right:
        max_tree[node] = arr[left]
        return

    mid = (left + right) // 2
    max_tree_init(arr, max_tree, node * 2, left, mid)
    max_tree_init(arr, max_tree, node * 2 + 1, mid + 1, right)
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])


def max_find(tree, node, left, right, start, end):
    if start > right or end < left:
        return 0

    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2
    return max(max_find(tree, node, left, mid, start, end), max_find(tree, node, mid + 1, right, start, end))


def min_find(tree, node, left, right, start, end):
    if start > right or end < left:
        return 1000000001

    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2
    return min(min_find(tree, node, left, mid, start, end), min_find(tree, node, mid + 1, right, start, end))


if __name__ == "__main__":
    n, m = map(int, read().split())
    arr = [int(read()) for _ in range(n)]
    pairs = []
    for _ in range(m):
        a, b = map(int, read().split())
        pairs.append((a - 1, b - 1))

    h = int(ceil(log2(n)))
    size = 1 << (h + 1)

    max_tree, min_tree = [0] * size, [0] * size
    max_tree_init(arr, max_tree, 1, 0, n - 1)
    min_tree_init(arr, min_tree, 1, 0, n - 1)

    for p1, p2 in pairs:
        min_val = min_find(min_tree, 1, 0, n - 1, p1, p2)
        max_val = max_find(max_tree, 1, 0, n - 1, p1, p2)
        print(min_val, max_val)

"""
구간 문제! 구간을 나눌때 세그먼트 트리로 어떻게 표현?
10 1
75
30
100
38
50
51
52
20
81
5
3 5
# 6 9
# 8 10
"""