import copy
T = int(input())
board = []
n = 0
# def nclock():
def getDiag():
    ret = []
    for i in range(n):
        ret.append(board[i][i])
    return ret

def getSubDiag():
    ret = []
    for i in range(n):
        ret.append(board[i][n - i -1])
    return ret

def clock(midCol, midRow, diag, subDiag):
    for i in range(n):
        board[n//2][i] = subDiag[n-i-1]
        board[i][n//2] = diag[i]
        board[i][i] = midRow[i]
        board[i][n-i -1] = midCol[i]
def noclock(midCol, midRow, diag, subDiag):
    board[n//2] = diag
    for i in range(n):
        board[i][n//2] = subDiag[i]
        board[i][i] = midCol[i]
        board[n - i - 1][i] = midRow[i]

for t in range(T):
    board = []
    n, d = map(int, input().split())

    for i in range(n):
        board.append(list(map(int, input().split())))
    
    if d > 0:
        d = d % 360
        cnt = d // 45
        for i in range(cnt):
            midCol = [j[n//2] for j in board]
            midRow = copy.deepcopy(board[n//2])
            diag = getDiag()
            subDiag = getSubDiag()
            clock(midCol, midRow, diag, subDiag)
    elif d < 0:
        d = (-1 * d) % 360
        cnt = d //45
        for i in range(cnt):
            midCol = [j[n//2] for j in board]
            midRow = copy.deepcopy(board[n//2])
            diag = getDiag()
            subDiag = getSubDiag()
            noclock(midCol, midRow, diag, subDiag)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
