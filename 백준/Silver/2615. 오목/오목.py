board = []
for i in range(19):
    board.append(list(map(int, input().split())))
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
color = 0
ax, ay = 20, 20


def bfs(x, y):
    global color, ax, ay

    cur = board[x][y]

    for i in range(4):
        cnt = 0
        while 1:
            nx = x + dx[i] * cnt
            ny = y + dy[i] * cnt
            if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == cur:
                cnt += 1
                if cnt == 5:
                    if (
                        0 <= x - dx[i] < 19
                        and 0 <= y - dy[i] < 19
                        and board[x - dx[i]][y - dy[i]] == cur
                    ):
                        break
                    if (
                        0 <= nx + dx[i] < 19
                        and 0 <= ny + dy[i] < 19
                        and board[nx + dx[i]][ny + dy[i]] == cur
                    ):
                        break
                    print(cur)
                    print(x + 1, y + 1)
                    exit(0)
            else:
                break


for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            bfs(i, j)
if color == 0:
    print(0)
else:
    print(color)
    print(ax + 1, ay + 1)
