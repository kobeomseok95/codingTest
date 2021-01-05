import sys
sys.setrecursionlimit(10**6)


def check_cycle(direct_graph, i, visit):
    if visit[i]:
        if visit[i] == -1:
            return True
        return False

    visit[i] = -1
    for nxt in direct_graph[i]:
        if check_cycle(direct_graph, nxt, visit):
            return True
    visit[i] = 1
    return False


def make_direct_graph(node, parent, adj, direct_graph):
    for nxt in adj[node]:
        if nxt != parent:
            direct_graph[nxt].append(node)
            make_direct_graph(nxt, node, adj, direct_graph)


def solution(n, path, order):
    adj, direct_graph, visit = [[] for _ in range(n)], [[] for _ in range(n)], [0] * n
    for node, parent in path:
        adj[node].append(parent)
        adj[parent].append(node)

    make_direct_graph(0, -1, adj, direct_graph)
    for parent, node in order:
        direct_graph[node].append(parent)

    for i in range(n):
        if check_cycle(direct_graph, i, visit):
            return False
    return True