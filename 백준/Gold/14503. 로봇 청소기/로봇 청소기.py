N, M  = map(int, input().split())
r,c,d  = map(int, input().split())
dx = [-1, 0, 1, 0] #북, 동, 남, 서 # 위, 오, 아, 왼
dy = [0, 1, 0, -1]

loc =[]
answer = 1
for i in range(N):
    loc.append(list(map(int, input().split())))

loc[r][c] = 2
while 1:    
    cnt = 0
    flag = 0
    inid = d
    for i in range(4):
        cnt += 1
        d = d - 1
        if d == -1:
            d = 3
        nr = r +dx[d]
        nc = c + dy[d]
        if 1 <= nr < N-1 and 1 <= nc < M-1:
            if loc[nr][nc] == 0:                
                loc[nr][nc] = 2
                answer += 1
                r = nr
                c = nc
                flag = 1
                break
    if cnt == 4 and flag == 0:
        nr = r - dx[inid]
        nc = c - dy[inid]
        d = inid
        if 1 <= nr < N -1 and 1 <= nc < M-1:
            if loc[nr][nc] == 1:  
                break
            else:
                r = nr
                c = nc
        else:
            break
print(answer)