import sys
input = sys.stdin.readline
# →, ←, ↑, ↓
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
sd = ["", "R", "L", "U", "D"]
N, K = map(int, input().split())

# 흰색: 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 올림
    # A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동
# 빨간색: 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다
# 파란색: A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 
# 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
# 체스판을 벗어나는 경우에는 파란색과 같은 경우
board = []
# id, direction
entities = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    # 0은 흰색, 1은 빨간색, 2는 파란색
    line = list(map(int, input().split()))
    board.append(line)
entityInfos = [(0, 0, 0)]  

for i in range(1, K+1):
    x, y, d = map(int, input().split())
    x = x - 1
    y = y - 1
    entities[x][y].append((i, d))
    entityInfos.append((x, y, d))
    
def oppositeDirection(direction):
    if direction == 1:
        return 2
    if direction == 2:
        return 1
    if direction == 3:
        return 4
    if direction == 4:
        return 3
    
# entities 에서 방향 그대로 옳김
def move(eid, nx, ny, toggle):
    global entityInfos, entities
    x, y, d = entityInfos[eid] # 이전
    idx = 0
    for i in range(len(entities[x][y])):   # 스택 길이만큼만 순회
        if entities[x][y][i][0] == eid:
            idx = i
            break
        
    # blue, 격자 벗어났을 때 
    entities[x][y][idx] = (eid, d)
    
    for j in range(idx, len(entities[x][y])):
        cid, d = entities[x][y][j]
        entityInfos[cid] = (nx, ny, d)
        
    if not toggle:
        entities[nx][ny] += entities[x][y][idx:]
    else:
        for k in range(len(entities[x][y]) - 1, idx - 1, -1):
            entities[nx][ny].append(entities[x][y][k])
            
    entities[x][y] = entities[x][y][:idx]
    if len(entities[nx][ny]) >= 4:
        return True
    return False

def blue(eid, x, y, d):
    global entityInfos
    nd = oppositeDirection(d)
    for i in range(len(entities[x][y])):       # range(N) 아님!
        if entities[x][y][i][0] == eid:
            entities[x][y][i] = (eid, nd)
            break
    nx = x + dx[nd]
    ny = y + dy[nd]
    entityInfos[eid] = (x, y, nd)
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
        return False

    # 도착 칸 색에 따라 이동
    if board[nx][ny] == 0:   # 흰
        return move(eid, nx, ny, False)
    else:                    # 빨강 
        return move(eid, nx, ny, True)


        
def printArr(arr):
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) == 0:
                print("X", end=" ")
            else:
                for k in range(len(arr[i][j])):
                    s = str(arr[i][j][k][0]) + sd[arr[i][j][k][1]] 
                    print(s, end = " ")
        print()
    
def solve():
    T = 0   
    while T < 1000:
        T += 1
        for eid in range(1, K + 1):
            x, y, d = entityInfos[eid]
            nx = x + dx[d]
            ny = y + dy[d]
            ret = False
            # blue
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                ret = blue(eid, x, y, d)
            else:
                if board[nx][ny] == 2:   # blue                       
                    ret = blue(eid, x, y, d)
                if board[nx][ny] == 0: # 흰색
                    ret = move(eid, nx, ny, False)
                if board[nx][ny] == 1: # 빨간색
                    ret = move(eid, nx, ny, True)
            if ret : 
                return T 
        
    return -1

answer = solve()
print(answer)