from collections import deque
n,m,lt = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

q = deque()
q.append((0,0,0))
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
dx =[1, -1, 0, 0]
dy = [0,0,1,-1]
t = 0
gramt = 0
flag = 0
while q:
    x, y, now = q.popleft()
    if x == n-1 and y == m-1:
        t = now
        flag = 1
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, now + 1))
            if graph[nx][ny] == 2  and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, now + 1))
                flag = 1
                tx = n - 1 - nx
                ty = m -1 - ny
                gramt = now + 1 + tx + ty
            

if flag:
    if t == 0 and gramt == 0:
        print('Fail')
    elif t == 0 and gramt != 0:
        if gramt <= lt:
            print(gramt)
        else: print('Fail')
    elif t != 0 and gramt == 0:
        if t <= lt:
            print(t)
        else: print('Fail')
    else:
        ans = min(t, gramt)
        if ans <= lt:
            print(ans)
        else:
            print('Fail')
else: print('Fail')