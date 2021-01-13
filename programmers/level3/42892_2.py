import sys
sys.setrecursionlimit(10 ** 6)


def get_preorder(root, nodeinfo, preorder):
    preorder.append(nodeinfo.index(root.data) + 1)

    if root.left:
        get_preorder(root.left, nodeinfo, preorder)
    if root.right:
        get_preorder(root.right, nodeinfo, preorder)


def get_postorder(root, nodeinfo, postorder):
    if root.left:
        get_postorder(root.left, nodeinfo, postorder)
    if root.right:
        get_postorder(root.right, nodeinfo, postorder)

    postorder.append(nodeinfo.index(root.data) + 1)


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def solution(nodeinfo):
    sorted_node_info = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    root = None
    for node in sorted_node_info:
        if not root:
            root = Tree(node)
        else:
            current = root
            while True:
                if current.data[0] > node[0]:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(node)
                        break
                else:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break

    answer = []
    preorder = []
    postorder = []

    get_preorder(root, nodeinfo, preorder)
    get_postorder(root, nodeinfo, postorder)

    answer.append(preorder)
    answer.append(postorder)
    return answer