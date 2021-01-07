import sys
sys.setrecursionlimit(10**6)


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(node, _list, dic):
    _list.append(dic[tuple(node.data)])

    if node.left:
        preorder(node.left, _list, dic)
    if node.right:
        preorder(node.right, _list, dic)


def postorder(node, _list, dic):
    if node.left:
        postorder(node.left, _list, dic)
    if node.right:
        postorder(node.right, _list, dic)

    _list.append(dic[tuple(node.data)])


def solution(nodeinfo):
    dic = {tuple(nodeinfo[i]): i + 1 for i in range(len(nodeinfo))}
    print(dic)

    sorted_nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    root = None
    for node in sorted_nodeinfo:
        if root is None:
            root = Tree(node)
        else:
            current = root
            while True:
                if node[0] < current.data[0]:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(node)
                        break
                elif node[0] > current.data[0]:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break

    preorder_list = []
    postorder_list = []
    preorder(root, preorder_list, dic)
    postorder(root, postorder_list, dic)
    return [preorder_list, postorder_list]
