from collections import deque
n,k = map(int, input().split())
grid = []
q = deque()
depth = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] != 0:
            q.append((i,j))
    grid.append(lst)
s, x, y = map(int, input().split())

while q:
    r, c  = q.popleft()
    now = grid[r][c]
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if 0 <= nr < n and 0 <= nc < n and  depth[r][c] + 1 <= s:
            if grid[nr][nc] == 0:
                grid[nr][nc] = now
                depth[nr][nc] = depth[r][c] + 1
                q.append((nr, nc))
            elif now < grid[nr][nc] and depth[nr][nc] == depth[r][c]+1:
                grid[nr][nc] = now
                depth[nr][nc] = depth[r][c] + 1
                q.append((nr, nc))
print(grid[x-1][y-1])





