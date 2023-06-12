from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
board = []
n, m = 0, 0
def bfs(x, y, visited):
    ret = 0
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        ret += int(board[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and board[nx][ny] != 'X':
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return ret
                    
                
def solution(maps):
    global n, m
    answer = []
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        board.append(list(maps[i]))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] != 'X':
                days = bfs(i, j, visited)
                answer.append(days)
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer