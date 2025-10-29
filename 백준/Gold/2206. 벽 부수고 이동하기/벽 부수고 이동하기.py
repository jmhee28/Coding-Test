import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
board =[input().strip() for _ in range(N)]

visited0 = [bytearray(M) for _ in range(N)]
visited1 = [bytearray(M) for _ in range(N)]
visited0[0][0]= 1
# (x, y, wall)
answer = -1
def bfs():
    q = deque()
    q.append((0,0,0))
    dist = 1
    while q:
        for _ in range(len(q)): 
            x, y, w = q.popleft()
            if x == (N-1) and y == (M-1):
                return dist
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < M :
                    cell = board[nx][ny]
                    # 이동 가능
                    if cell == '0' :
                        if w == 0 and visited0[nx][ny] == 0:
                            q.append((nx, ny, 0))
                            visited0[nx][ny]= 1 # 벽안깸
                        elif w == 1 and visited1[nx][ny] == 0:
                            q.append((nx, ny, 1))
                            visited1[nx][ny]= 1 # 벽안깸
                    else:
                        if w == 0 and visited1[nx][ny] == 0:
                            q.append((nx, ny, 1))
                            visited1[nx][ny] = 1
        dist += 1
    return -1
answer = bfs()
print(answer)