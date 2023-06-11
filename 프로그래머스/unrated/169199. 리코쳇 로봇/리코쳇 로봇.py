from collections import deque
nboard = []
dx = [1,-1,0,0]
dy = [0,0, -1, 1]
n = 0
m = 0
def go(dir, x, y):
    global n, m, nboard
    nx = x
    ny = y
    while 1:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and nboard[nx][ny] != 'D':
            x = nx
            y = ny
        else: 
            break
    return (x, y)

def solution(board):
    global n, m, nboard
    answer = -1
    n = len(board)
    m = len(board[0])
    rx, ry  = 0,0
    gx, gy = 0,0
    for i in range(n):
        lst = list(board[i])
        nboard.append(lst)
        for j in range(m):
            if lst[j] == 'R':
                rx, ry = i, j
            if lst[j] == 'G':
                gx, gy = i, j
                
    q = deque()
    q.append((rx, ry, 0))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[rx][ry] = 1
    while(q):
        x, y, c = q.popleft()
        if x == gx and y == gy:
            answer = c
            break
        for i in range(4):
            aftergo = go(i, x, y)
            nx,ny = aftergo
            if (nx != x or ny != y) and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, c+1))
    return answer