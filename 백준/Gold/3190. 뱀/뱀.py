import sys
from collections import deque
dir = [0,1,2,3] # right, down, left, up
dx = [0,1,0, -1]
dy = [1,0, -1, 0]
cnt = 0
N = int(input())
K = int(input()) #사과갯수
m = [[0 for i in range(N+1)] for i in range(N+1)]


snake ={}
for i in range(K):
    r, c = map(int, input().split())
    m[r-1][c-1] = 1 #사과 체크

L = int(input())
for i in range(L):
    t, C = input().split()
    t = int(t)
    snake[t] = C

spos = deque()
spos.append((0,0))
curdir = 0
time = 0
x, y = 0, 0
m[x][y] = 2 #뱀체크
slen = 1

while 1:
    nx = x + dx[curdir]
    ny = y + dy[curdir]
    time+=1
    if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
        print(time)
        sys.exit()

    if m[nx][ny] == 2:
        print(time)
        sys.exit()
    
    else:
        if m[nx][ny] == 1: #사과가 있으면
            spos.append((nx,ny))
            m[nx][ny] = 2
            slen += 1
        else:
            px, py = spos.popleft()
            spos.append((nx,ny))
            m[px][py] = 0
            m[nx][ny] = 2
        x = nx
        y = ny
    if time in snake:
        C = snake[time]
        if C =='D': # 오른쪽으로 
            curdir = curdir + 1
            if curdir > 3:
                curdir = 0
        else:
            curdir = curdir -1
            if curdir == -1:
                curdir = 3