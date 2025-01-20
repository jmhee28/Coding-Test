from collections import deque

m,n,k = map(int, input().split())
board = [[0] * (n+1) for _ in range(m + 1)]
visited = [[0] * (n+1) for _ in range(m + 1)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    x , y, x1, y1 = map(int, input().split())
    nx = m - y
    ny = x
    nx1 = m - y1
    ny1 = x1
    for i in range(nx1, nx):
        for j in range(ny, ny1):
            board[i][j] = 1
areas = []

def bfs(x, y):
    global visited
    q = deque()
    visited[x][y] = 1
    q.append((x, y))
    ret = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] != 1:
                q.append((nx, ny))
                visited[nx][ny] = 1
                ret += 1
    return ret

num = 1
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and board[i][j] != 1:
            temp = bfs(i,j)
            areas.append(temp)


print(len(areas))
areas.sort()
for i in range(len(areas)):
    print(areas[i], end=" ")
