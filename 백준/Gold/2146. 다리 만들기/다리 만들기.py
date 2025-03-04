import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

INF = sys.maxsize
answer = INF 
        
def bfs(x, y, idx, visited, boardIdx):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    boardIdx[x][y] = idx
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and board[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                boardIdx[nx][ny] = idx
                
def getDistances(island, boardIdx):
    global answer
    q = deque()
    distances =[[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if boardIdx[i][j] == island:
                q.append((i, j))
                distances[i][j] == 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if boardIdx[nx][ny] == 0 and distances[nx][ny] == -1:
                        distances[nx][ny] = distances[x][y] + 1
                        q.append((nx, ny))
                
                if boardIdx[nx][ny] != island and boardIdx[nx][ny] != 0: 
                        return distances[x][y]
                    

for i in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)

visited = [[False for _ in range(n)] for _ in range(n)]
boardIdx = [[0] * n for _ in range(n)]
idx = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visited[i][j] == False:
            bfs(i, j, idx, visited, boardIdx)
            idx += 1
            
for island in range(1, idx):
    ret = getDistances(island, boardIdx)
    answer = min(ret, answer)
print(answer + 1)