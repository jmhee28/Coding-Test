from collections import deque

board = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sx, sy, ex, ey, lx, ly = 0, 0, 0, 0, 0, 0


def bfs(x, y, n, m, target):
    q = deque()
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 0
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if board[x][y] == target:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and board[nx][ny] != "X"
                and visited[nx][ny] == -1
            ):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    if target == "L":
        return visited[lx][ly]
    return visited[ex][ey]


def solution(maps):
    global sx, sy, ex, ey, lx, ly
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        board.append(list(maps[i]))
    for i in range(n):
        for j in range(m):
            if board[i][j] == "S":
                sx, sy = i, j
            if board[i][j] == "E":
                ex, ey = i, j
            if board[i][j] == "L":
                lx, ly = i, j
    toLever = bfs(sx, sy, n, m, "L")
    leverToExit = bfs(lx, ly,n, m, "E")
    if toLever == -1 or leverToExit == -1 :
        return -1
    else:
        return toLever+leverToExit
    


# solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])
