from collections import deque

n, m = map(int, input().split())
pos = 1
ladders = []
snakes = []
board = [0] * 101
# 1 : ladder
# 2 : snake

for i in range(n):
    x, y = map(int, input().split())
    ladders.append((x, y))
    board[x] = y


for i in range(m):
    u, v = map(int, input().split())
    board[u] = v
    snakes.append((u, v))

def bfs(start):
    q = deque()
    q.append((start, 0)) # pos, 주사위 카운트
    visited = [0] * 101
    visited[start] = 1
    
    while q:
        pos, count = q.popleft()
        if pos == 100:
            return count
        
        for i in range(1, 7):
            npos = i + pos
            if npos <= 100 and visited[npos] == 0:
                if board[npos] != 0:
                    npos = board[npos]
                visited[npos] = 1
                q.append((npos, count + 1))

answer = bfs(pos)
print(answer)