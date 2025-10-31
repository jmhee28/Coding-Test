import sys
input = sys.stdin.readline
board = []
N, M = map(int, input().split())
INF = 10 ** 9
dx = [1, 1, 1]
dy = [-1, 0, 1]

for i in range(N):
    board.append(list(map(int, input().split())))
    
costs = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

for i in range(M):
    for j in range(3):
        costs[0][i][j] = board[0][i]
for m in range(M):
    for j in range(3):
        if j == 0:
            if m < (M - 1):
                costs[1][m][j] = board[0][m + 1] + board[1][m]
        elif j == 1:
            costs[1][m][j] = board[0][m] + board[1][m]
        elif j == 2:
            if m > 0:
                costs[1][m][j] = board[0][m - 1] + board[1][m]
            
for i in range(2, N):
    for j in range(M):
        for d in range(3):
            t1 = INF
            t2 = INF
            # costs[i][j][d] # d: 이전에 선택한 방향
            if d == 0: # 왼쪽 아래
                if j >= M-1:
                    continue
                t1 = costs[i - 1][j + 1][1]
                t2 = costs[i - 1][j + 1][2]
                costs[i][j][d] = min(t1, t2)
            elif d == 1: # 아래
                t1 = costs[i - 1][j][0]
                t2 = costs[i - 1][j][2]
                costs[i][j][d] = min(t1, t2)
            elif d == 2: # 오른쪽 아래
                if j == 0:
                    continue
                t1 = costs[i - 1][j - 1][1]
                t2 = costs[i - 1][j - 1][0]
                costs[i][j][d] = min(t1, t2)
            costs[i][j][d] += board[i][j]
answer = INF

for j in range(M):
    answer = min(answer, min(costs[N-1][j]))
print(answer)