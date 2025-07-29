from collections import deque
import copy
N = 8
board = []
dx = [0, 1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 0, 1, -1, 1, -1, 1, -1]

# 옥지 위치
x = N-1
y = 0

target = (0, N-1)

for i in range(N):
    board.append(list(input()))
    
def get_boards():
    boards = [board]
    for t in range(1, 9):  # 최대 8초
        new_board = [['.' for _ in range(N)] for _ in range(N)]
        for i in range(N - 1):
            for j in range(N):
                if boards[t - 1][i][j] == '#':
                    new_board[i + 1][j] = '#'
        boards.append(new_board)
    return boards

boards = get_boards()
   

            
def bfs():
    q = deque()
    q.append([x, y, 0])
    visited = [[[False] * N for _ in range(N)] for _ in range(9)]
    
    
    while q:
        cx, cy, t = q.popleft()
        
        if (cx, cy) == target:
            return 1
        if boards[t][cx][cy] == '#':
            continue
        
        for i in range(9):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nt = min(t + 1, 8)
            if 0 <= nx < N and 0 <= ny < N :
                if boards[t][nx][ny] == '.' and boards[nt][nx][ny] == '.' and not visited[nt][nx][ny]:
                    q.append([nx, ny, nt])
                    visited[nt][nx][ny] = True    
            
    return 0

answer = bfs()
print(answer)