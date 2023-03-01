from itertools import combinations
from collections import deque
import copy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n ,m  = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
zeros=[]
twos = []
zerocnt = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            zeros.append((i, j))
            zerocnt += 1
        if grid[i][j] == 2:
            twos.append((i, j))
lst = []
for i in range(zerocnt):
    lst.append(i)
combs = list(combinations(lst, 3))

ans = 0
for comb in combs:
    ones = 0
    ngrid = copy.deepcopy(grid)
    ngrid[zeros[comb[0]][0]][zeros[comb[0]][1]] = 1
    ngrid[zeros[comb[1]][0]][zeros[comb[1]][1]] = 1
    ngrid[zeros[comb[2]][0]][zeros[comb[2]][1]] = 1
    
    q = deque(twos)
    visited = [[0 for _ in range(m) ] for _ in range(n)]
    visited[twos[0][0]][twos[0][1]] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < n and 0 <= ny < m:
                if ngrid[nx][ny] == 0 and visited[nx][ny] == 0:
                    ngrid[nx][ny] = 2
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    for i in range(n):
        for j in range(m):               
            if ngrid[i][j] == 0:
                ones += 1
    ans = max(ans, ones)
print(ans)