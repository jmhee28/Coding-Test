import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sky = [list(map(int, input().split())) for _ in range(N)]

NEG_INF = -10**18

# up[i][j]: (N-1,0)에서 시작해 위/오른쪽만 써서 (i,j)까지 얻을 수 있는 최대 합
up = [[NEG_INF]*M for _ in range(N)]
# down[i][j]: (i,j)에서 시작해 아래/오른쪽만 써서 (N-1,M-1)까지 얻을 수 있는 최대 합
down = [[NEG_INF]*M for _ in range(N)]

# 상승 DP: 아래왼쪽 -> 위오른쪽으로 채우기
up[N-1][0] = sky[N-1][0]
for i in range(N-1, -1, -1):
    for j in range(0, M):
        if i+1 < N and up[i+1][j] != NEG_INF:
            up[i][j] = max(up[i][j], up[i+1][j] + sky[i][j])
        if j-1 >= 0 and up[i][j-1] != NEG_INF:
            up[i][j] = max(up[i][j], up[i][j-1] + sky[i][j])

# 하강 DP: 오른쪽아래 -> 왼쪽위로 채우기
down[N-1][M-1] = sky[N-1][M-1]
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if i+1 < N and down[i+1][j] != NEG_INF:
            down[i][j] = max(down[i][j], down[i+1][j] + sky[i][j])
        if j+1 < M and down[i][j+1] != NEG_INF:
            down[i][j] = max(down[i][j], down[i][j+1] + sky[i][j])

# 스위치 지점 (i,j)에서의 총점 최댓값
ans = NEG_INF
for i in range(N):
    for j in range(M):
        if up[i][j] != NEG_INF and down[i][j] != NEG_INF:
            ans = max(ans, up[i][j] + down[i][j])

print(ans)
