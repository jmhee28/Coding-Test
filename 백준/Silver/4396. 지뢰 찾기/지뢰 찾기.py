n = int(input())
board = []
user = []
ans = [['.' for _ in range(n)] for _ in range(n)]

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

for i in range(n):
    board.append(list(input()))
for i in range(n):
    user.append(list( input()))

flag = False
bombpos = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '*':
            bombpos.append((i, j))
        if user[i][j] == 'x':
            if board[i][j] == '*':
                flag = True
                continue
            bomb = 0
            for d in range(8):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == '*':
                        bomb += 1
            ans[i][j] = bomb
if flag == True:
    for i in range(len(bombpos)):
        x, y = bombpos[i]
        ans[x][y] = '*'
for i in range(n):
    for j in range(n):
        print(ans[i][j], end = '')
    print()