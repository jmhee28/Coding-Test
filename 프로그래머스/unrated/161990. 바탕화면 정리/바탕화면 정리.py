def solution(wallpaper):
    board = []
    n = len(wallpaper)
    m = len(wallpaper[0])
    for i in range(n):
        board.append(list(wallpaper[i]))
    lx = n
    ly = m
    rx = 0
    ry = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "#":
                lx = min(lx, i)
                ly = min(ly, j)
                rx = max(rx, i + 1)
                ry = max(ry, j + 1)
    answer = [lx, ly, rx, ry]
    return answer