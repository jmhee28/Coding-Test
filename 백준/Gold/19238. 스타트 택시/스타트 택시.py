import sys
from collections import deque
import heapq
 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
input = sys.stdin.readline

N,M,Fuel = map(int, input().split())
# 1: wall 2: 승객 3: taxi
board = []

for i in range(N):
    board.append(list(map(int, input().split())))
#taxi start
sx, sy = map(int, input().split()) 
taxi = (sx-1, sy-1)
# 손님 정보
customer = {}
for i in range(M):
    x, y, fx, fy = map(int, input().split())
    
    customer[(x-1, y-1)] = (fx-1, fy-1)
    board[x-1][y-1] = 2

def bfs(taxi):
    heap =[]
    x, y = taxi
    q = deque()
    q.append((x, y))
    visited = [[-1 for i in range(N)] for i in range(N)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        if board[x][y] == 2:
            heapq.heappush(heap, (visited[x][y], x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return heap

def calbfs(start, target):
    x, y = start
    q = deque()
    q.append((x, y))
    visited = [[-1 for i in range(N)] for i in range(N)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        if target == (x, y):
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return visited[target[0]][target[1]]     
           
cnt = 0
while 1:
    vheap = bfs(taxi)
    if len(vheap) == 0:
        break
    #distance = 택시와 손님사이의 거리
    distance, x, y = heapq.heappop(vheap)
    fx, fy = customer[(x, y)]
    distance2 = calbfs((x, y),customer[(x, y)])
    if distance2 == -1:
        Fuel = -1
        break
    totalDis = distance + distance2
   
    if(Fuel < distance):
        Fuel = -1
        break
    else:
        Fuel -= distance
        if Fuel < distance2:
            Fuel = -1
            break
        else:
            Fuel = Fuel + distance2    
    board[x][y] = 0
    taxi = (fx,fy)
    cnt += 1
if cnt < M:
    print(-1)
else:
    print(Fuel)

