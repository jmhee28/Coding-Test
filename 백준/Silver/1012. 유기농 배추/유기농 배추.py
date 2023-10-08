import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


T = int(input())

def bfs(n, m, x, y, board, visited):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny <m and visited[nx][ny] == 0 and board[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                
for i in range(T):
    answer = 0
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        y, x = map(int, input().split())
        board[x][y] = 1
    
    for a in range(N):
        for b in range(M):
            if board[a][b] == 1 and visited[a][b] == 0:
                answer += 1
                bfs(N, M, a, b, board, visited)
    print(answer)
