import sys
import copy
from collections import deque
input = sys.stdin.readline
dx = [0, 1]
dy = [1, 0]
n, m = map(int, input().split())
board = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    board.append(list(map(int, input().split())))
cboard = copy.deepcopy(board)
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                cboard[nx][ny] += cboard[x][y]
                visited[nx][ny] = 1
                q.append((nx, ny))
            else:
                cboard[nx][ny] = max(cboard[nx][ny], board[nx][ny]+ cboard[x][y])
        
            
            
print(cboard[n-1][m-1])