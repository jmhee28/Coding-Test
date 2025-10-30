import sys
from collections import deque
input = sys.stdin.readline

INF = 10**9

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
board = []
jpos = (0,0)
fpos = (0,0)
c = 0
fires = []
fireMap = [[INF] * M for _ in range(N)]
for i in range(N):
    line = input().strip()
    for j in range(M):
        if line[j] == 'J':
            jpos = (i, j)
            c += 1
        if line[j] == 'F':
            fires.append((i, j))
            c += 1       
    board.append(line)

def fire():
    global fireMap 
    queue = deque()
    for fx, fy in fires:      # <-- 멀티소스 초기화
        fireMap[fx][fy] = 0
        queue.append((fx, fy))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if fireMap[nx][ny] == INF and board[nx][ny] != '#':
                    queue.append((nx, ny))
                    fireMap[nx][ny] = fireMap[x][y] + 1
    
def dfs():
    queue = deque()
    queue.append(jpos)
    dist = [[-1] * M for _ in range(N)]
    dist[jpos[0]][jpos[1]] = 0
    while queue:
        x, y = queue.popleft()
        cur = dist[x][y]
        if x == 0 or y == 0 or x == ( N - 1 ) or y == ( M - 1):
            return cur
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if dist[nx][ny] != -1 or board[nx][ny] == '#':
                    continue
                arrive = cur + 1
                if fireMap[nx][ny] > arrive:
                    dist[nx][ny] = arrive
                    queue.append((nx, ny))
                       
    return -1

 
fire()
answer = dfs()
if answer == -1:
    print("IMPOSSIBLE")
else:
    print(answer + 1)