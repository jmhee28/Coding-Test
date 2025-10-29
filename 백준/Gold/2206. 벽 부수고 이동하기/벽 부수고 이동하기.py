import sys
from collections import deque

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

N, M = map(int, input().split())
# 보드를 문자열로 저장 (메모리 절약)
board = [input().strip() for _ in range(N)]

# visited0: 벽 안 부순 상태 방문표시, visited1: 벽 1번 부순 상태 방문표시
visited0 = [bytearray(M) for _ in range(N)]
visited1 = [bytearray(M) for _ in range(N)]

q = deque()
q.append((0, 0, 0))          # (x, y, w)  w=0: 아직 안 부숨, w=1: 이미 한 번 부숨
visited0[0][0] = 1

dist = 1                     # 시작 칸을 1로 세는 관례
while q:
    for _ in range(len(q)):  # 레벨 BFS로 거리 관리(큐 튜플에 거리 안 넣음)
        x, y, w = q.popleft()
        if x == N - 1 and y == M - 1:
            print(dist)
            sys.exit(0)

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                cell = board[nx][ny]
                if cell == '0':
                    # 빈 칸: 현재 w 상태 그대로
                    if w == 0 and not visited0[nx][ny]:
                        visited0[nx][ny] = 1
                        q.append((nx, ny, 0))
                    elif w == 1 and not visited1[nx][ny]:
                        visited1[nx][ny] = 1
                        q.append((nx, ny, 1))
                else:  # cell == '1' (벽)
                    # 아직 안 부쉈으면 한 번 부수고 진행
                    if w == 0 and not visited1[nx][ny]:
                        visited1[nx][ny] = 1
                        q.append((nx, ny, 1))
    dist += 1

print(-1)
