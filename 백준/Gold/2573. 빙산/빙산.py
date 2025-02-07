from collections import deque
import copy
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))
 
def melt():
    global board
    newBoard = [arr[:] for arr in board]
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                meltCnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == 0:
                            meltCnt += 1
                newBoard[i][j] -= meltCnt
                if newBoard[i][j] < 0: newBoard[i][j] = 0         
    board = [arr[:] for arr in newBoard]                      

                
def bfs(visited, x, y):
    q = deque()
    q.appendleft((x, y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] > 0 and visited[nx][ny] == 0:
                    visited[nx][ny]  = 1
                    q.append((nx, ny))
    
def getChunkCount():
    visited = [[0] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and visited[i][j] == 0:
                count += 1
                bfs(visited, i, j)
    return count

def isAllZero():
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                return False
    return True


answer = 0
while getChunkCount() < 2:
    if isAllZero():
        answer = 0
        break
    melt()
    answer += 1
    
print(answer)