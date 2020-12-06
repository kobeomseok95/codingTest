from sys import stdin
from collections import deque
READ = lambda: stdin.readline().strip()

n, l, r = map(int, READ().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, READ().split())))

dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
result = 0

def process(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary // count
    return count


total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)

"""
from collections import deque
from sys import stdin
READ = lambda : stdin.readline().strip()
nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(x, y):
    t = [(x, y)]
    tq = deque([(x, y)])
    s = m[x][y]
    v[x][y] = 1
    while tq:
        x, y = tq.popleft()
        for _x, _y in nm:
            tx = x + _x
            ty = y + _y
            if 0 <= tx < n and 0 <= ty < n and not v[tx][ty]:
                diff = abs(m[tx][ty] - m[x][y])
                if l <= diff <= r:
                    v[tx][ty] = 1
                    s += m[tx][ty]
                    tq.append((tx,ty))
                    t.append((tx, ty))
    if (size := len(t)) > 1:
        num = s // size
        for i in range(size):
            x, y = t[i]
            m[x][y] = num
            q.append((x, y))
        return 0
    else:
        return 1


def c(x, y):    # borderline open 여부
    for _x, _y in nm:
        tx = x + _x
        ty = y + _y
        if 0 <= tx < n and 0 <= ty < n:
            diff = abs(m[tx][ty] - m[x][y])
            if l <= diff <= r:
                return 0
    return 1


n, l, r = map(int, READ().split())
m = [[] for _ in range(n)]
cnt = 0
q = deque()
for i in range(n):
    m[i] = list(map(int, READ().split()))
    for j in range(n):
        q.append((i, j))
f = 0
while not f:
    v = [[0] * n for _ in range(n)]
    f = 1
    sz = len(q)
    for _ in range(sz):
        x, y = q.popleft()
        if v[x][y] or c(x, y):
            continue
        if not bfs(x, y):
            f = 0
    if not f:
        cnt += 1
print(cnt)
"""