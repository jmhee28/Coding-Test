import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
board = []
fires = []
jpos = (-1, -1)

for i in range(N):
    line = list(input().strip())
    for j, ch in enumerate(line):
        if ch == 'J':
            jpos = (i, j)
        elif ch == 'F':
            fires.append((i, j))
    board.append(line)

INF = 10**9
fire_time = [[INF]*M for _ in range(N)]

# 1) 불의 도착 시간: 멀티 소스 BFS
fq = deque()
for fx, fy in fires:
    fire_time[fx][fy] = 0
    fq.append((fx, fy))

while fq:
    x, y = fq.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] != '#' and fire_time[nx][ny] == INF:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fq.append((nx, ny))

# 2) 지훈이 탈출 BFS
jx, jy = jpos
# 시작이 가장자리면 한 번에 탈출
if jx == 0 or jy == 0 or jx == N-1 or jy == M-1:
    print(1)
    sys.exit(0)

dist = [[-1]*M for _ in range(N)]
q = deque()
q.append((jx, jy))
dist[jx][jy] = 0

while q:
    x, y = q.popleft()
    cur = dist[x][y]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == '#' or dist[nx][ny] != -1:
                continue
            arrive = cur + 1
            # 불이 오지 않거나, 불이 지훈이 도착 이후에 와야 함 (동시 도착 불가)
            if fire_time[nx][ny] > arrive:
                dist[nx][ny] = arrive
                # 가장자리 도달하면 탈출
                if nx == 0 or ny == 0 or nx == N-1 or ny == M-1:
                    print(arrive + 1)  # 칸을 나가는 데 +1
                    sys.exit(0)
                q.append((nx, ny))

print("IMPOSSIBLE")
