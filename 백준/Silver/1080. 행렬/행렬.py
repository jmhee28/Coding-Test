import sys

N, M = map(int, input().split())
rc = []
target = []
cnt = 0
def flip(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            if rc[i][j] == 0:
                rc[i][j] = 1
            else:
                rc[i][j] = 0

rc = [list(map(int, input())) for _ in range(N)]

target = [list(map(int, input())) for _ in range(N)]

for i in range(0, N-2):
    for j in range(0, M-2):
        if rc[i][j] != target[i][j]:
            flip(i,j)
            cnt += 1

flag = 0
for i in range(0, N):
    for j in range(0, M):
        if rc[i][j] != target[i][j]:
            flag = 1
            break
        
if flag == 1 :
    print(-1)
else :
    print(cnt)