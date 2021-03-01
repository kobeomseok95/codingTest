from sys import stdin
read = lambda: stdin.readline().strip()


def dfs(k, sums, y, x, max_maps_val, visit):
    global answer, drc, n, m, maps

    if sums + max_maps_val * (3 - k) <= answer:
        return
    if k == 3:
        answer = max(answer, sums)
        return

    for dy, dx in drc:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and not visit[ny][nx]:
            if k == 1:
                visit[ny][nx] = True
                dfs(k + 1, sums + maps[ny][nx], y, x, max_maps_val, visit)
                visit[ny][nx] = False

            visit[ny][nx] = True
            dfs(k + 1, sums + maps[ny][nx], ny, nx, max_maps_val, visit)
            visit[ny][nx] = False


n, m = map(int, read().split())
maps = [list(map(int, read().split())) for _ in range(n)]
max_maps_val = max(max(maps))

visit = [[False for _ in range(m)] for _ in range(n)]
answer = 0
drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(0, maps[i][j], i, j, max_maps_val, visit)
        visit[i][j] = False
print(answer)