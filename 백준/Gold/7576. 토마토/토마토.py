from collections import deque
m,n = map(int, input().split())
size = n * m
info = []
q = deque()
dx = [1, -1, 0, 0]
dy = [0,0, 1,-1]
initom = 0
day = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            q.append((i, j, 0))
        elif temp[j] == 0:
            initom += 1
    info.append(temp)
day = [[0 for _ in range(m)] for _ in range(n)]

if initom == 0:
    print(0)
else:
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if info[nx][ny] == 0:
                   info[nx][ny] = 1
                   day[nx][ny] = d + 1  
                   q.append((nx, ny, d+1))
    ans = -1
    flag = 0
    for i in range(n):
        for j in range(m):
            if info[i][j] == 0:
                ans = -1
                flag = 1
                break
            ans = max(ans, day[i][j])
        if flag == 1:
            break
    print(ans)