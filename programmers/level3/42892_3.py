import sys
sys.setrecursionlimit(10**6)


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(tree, node_index, preorder_list):
    preorder_list.append(node_index[tuple(tree.data)])
    if tree.left:
        preorder(tree.left, node_index, preorder_list)
    if tree.right:
        preorder(tree.right, node_index, preorder_list)


def postorder(tree, node_index, postorder_list):
    if tree.left:
        postorder(tree.left, node_index, postorder_list)
    if tree.right:
        postorder(tree.right, node_index, postorder_list)
    postorder_list.append(node_index[tuple(tree.data)])


def solution(nodeinfo):
    node_index = {tuple(nodeinfo[i]): i + 1 for i in range(len(nodeinfo))}
    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    tree = None
    for node in nodeinfo:
        if tree is None:
            tree = Tree(node)
        else:
            point = tree
            while True:
                if point.data[1] > node[1] and point.data[0] > node[0]:
                    if point.left is None:
                        point.left = Tree(node)
                        break
                    else:
                        point = point.left
                elif point.data[1] > node[1] and point.data[0] < node[0]:
                    if point.right is None:
                        point.right = Tree(node)
                        break
                    else:
                        point = point.right
    preorder_list = []
    postorder_list = []
    preorder(tree, node_index, preorder_list)
    postorder(tree, node_index, postorder_list)
    return [preorder_list, postorder_list]