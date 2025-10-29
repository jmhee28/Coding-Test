import sys
from collections import deque
input = sys.stdin.readline

dx = (1,-1,0,0)
dy = (0,0,1,-1)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 1) 1들의 연결 컴포넌트를 라벨링: comp_id[x][y] = k (k는 1..K)
comp_id = [[0]*M for _ in range(N)]
sizes = [0]  # sizes[k] = 컴포넌트 k의 크기, 0번은 더미
cid = 0

def bfs_label(sx, sy, cid):
    q = deque([(sx, sy)])
    comp_id[sx][sy] = cid
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and comp_id[nx][ny] == 0:
                    comp_id[nx][ny] = cid
                    cnt += 1
                    q.append((nx, ny))
    return cnt

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and comp_id[i][j] == 0:
            cid += 1
            sizes.append(bfs_label(i, j, cid))

# 2) 각 0칸을 1로 바꾼다고 가정하고, 인접한 서로 다른 컴포넌트 크기 합 + 1
ans = 0
any_zero = False
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            any_zero = True
            neigh = set()
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 1:
                    neigh.add(comp_id[ni][nj])
            # 자기 자신(뒤집는 0) + 인접한 서로 다른 컴포넌트 크기 합
            cand = 1
            for k in neigh:
                cand += sizes[k]
            if cand > ans:
                ans = cand

# 전부 1인 경우 대비(문제에 따라 필요 없을 수도 있지만 안전)
if not any_zero:
    ans = max(sizes) if sizes else 0

print(ans)
