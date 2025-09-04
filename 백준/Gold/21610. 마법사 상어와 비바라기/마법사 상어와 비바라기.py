# A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양
# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다
# 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 

# 1.모든 구름이 di 방향으로 si칸 이동한다.

# 2.각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.

# 3.구름이 모두 사라진다.

# 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 

# 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    # 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    # 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.

# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.

# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.

import sys
input = sys.stdin.readline
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
ddx = [-1, -1, 1, 1]
ddy = [ -1, 1, 1, -1]

N, M = map(int, input().split())
board = []
clouds = []
commands = []
def init():
    global board, clouds, commands
    
    for _ in range(N):
        arr = list(map(int, input().split()))
        board.append(arr)

    for _ in range(M):
        commands.append(list(map(int, input().split())))
    clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]


def rain(d, s):
    global clouds, board
    newClouds = []
    for cloud in clouds:
        nx = (cloud[0] + (dx[d] * s)) % N
        ny = (cloud[1] + (dy[d] * s)) % N
            
        board[nx][ny] += 1
        newClouds.append((nx, ny))
    return newClouds
 
def waterCopyBug(newClouds):
    global board  
    for pos in newClouds:
        x, y = pos
        cnt = 0
        for d in range(4):
            nx = x + ddx[d]
            ny = y + ddy[d]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
                cnt += 1
        board[x][y] += cnt
        
def makeClouds(newClouds):
    global board         
    finalClouds = []
    cloudCheck = [[0] * N for _ in range(N)]
    for c in newClouds:
        x, y = c
        cloudCheck[x][y] = 1
        
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i, j) and cloudCheck[i][j] != 1:
                   board[i][j] -= 2
                   finalClouds.append((i, j))
    return finalClouds                   
init()

for command in commands:
    d, s = command
    newClouds = rain(d, s)
    waterCopyBug(newClouds)
    clouds = makeClouds(newClouds)

answer = 0
for b in board:
    answer += sum(b)
print(answer)