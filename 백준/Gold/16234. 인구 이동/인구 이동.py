from collections import deque
N, L, R = map(int, input().split())
population = []

dx = [0, 0, 1, -1]
dy =[1, -1, 0, 0]
for i in range(0, N):
   population.append(list(map(int, input().split())))       
   
def bfs(x,y, num, visit):
    ret = False
    s = set()
    q = deque()
    q.append((x,y))
    visit[x][y] = num
    total = 0
    cnt = 0
    while q:
        x, y = q.popleft()
        s.add((x,y)) 
        total += population[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0: 
                if L <= abs(population[x][y] - population[nx][ny]) <= R:
                    visit[nx][ny] = num
                    q.append((nx, ny))
    if len(s) > 1:
        ret = True 
    p = total // cnt
    while s:
        x,y = s.pop()
        population[x][y] = p
    return ret
    # print(visit)
answer = 0
again = True
while again:
    flag = False
    num = 0
    visit = [[0 for _ in range(N)] for _ in range(N)] 
    for i in range(0, N):
        for j in range(0, N):
            if visit[i][j] == 0:
                num += 1
                repeat = bfs(i,j, num, visit)
                if repeat == True:
                    flag = True
    again = flag
    if flag == True:
        answer += 1
print(answer)
