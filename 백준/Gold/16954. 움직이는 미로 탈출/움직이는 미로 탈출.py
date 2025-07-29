from collections import deque

N = 8
board = [list(input()) for _ in range(N)]

# 방향: 제자리 + 8방향
dx = [0, 1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 0, 1, -1, 1, -1, 1, -1]

# 시간에 따른 board 상태를 미리 저장
def get_boards():
    boards = [board]
    for t in range(1, 9):  # 최대 8초
        new_board = [['.' for _ in range(N)] for _ in range(N)]
        for i in range(N - 1):
            for j in range(N):
                if boards[t - 1][i][j] == '#':
                    new_board[i + 1][j] = '#'
        boards.append(new_board)
    return boards

boards = get_boards()

def bfs():
    q = deque()
    q.append((7, 0, 0))  # (x, y, time)
    visited = [[[False] * N for _ in range(N)] for _ in range(9)]

    while q:
        x, y, t = q.popleft()
        if (x, y) == (0, 7):
            return 1
        if boards[t][x][y] == '#':
            continue
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            nt = min(t + 1, 8)
            if 0 <= nx < N and 0 <= ny < N:
                if boards[t][nx][ny] == '.' and boards[nt][nx][ny] == '.' and not visited[nt][nx][ny]:
                    visited[nt][nx][ny] = True
                    q.append((nx, ny, nt))
    return 0

print(bfs())
